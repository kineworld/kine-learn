"""把 curriculum/ 与 data/ 渲染成 docs/*.md 与 site/index.html。

三条硬约束：

  1. **build.py 永不上网。** 它只读已经落盘的数据，所以断网可构建，
     也不会因为某个网站今天挂了而让 CI 变红。网络只在 check_links.py
     与 fetch_oss.py 里发生，且它们只写 data/。
  2. **文档里的每个数字都是现算的。** 页面上出现的"共 N 个知识点"由本脚本
     遍历源文件得出。手打的计数会与源文件漂移，漂移了还没人发现——
     这正是本仓库要防的那类缺陷。
  3. **生成物必须与源文件同步。** CI 会跑本脚本再 `git diff --exit-code`，
     源文件改了但没重新生成，CI 直接失败。

用法：python scripts/build.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _common  # noqa: E402
from _common import (  # noqa: E402
    iter_points, link_entries, link_status,
    link_status_meta, load_index, load_links, load_oss, load_stages,
    oss_verified, oss_verified_meta, search_url, write_text,
)

# DOCS_DIR / SITE_DIR / ROOT 刻意不写成 `from _common import ...`：
# 那样会把路径在导入时固化一份，而 _common.set_root() 之后改的是模块里的那份，
# 于是测试注入根目录时本脚本仍会往真实仓库写。路径一律在调用点取 _common.X。

CJK_RE = re.compile(r"[\u3400-\u9fff]")


# ---------------------------------------------------------------- 小工具
def money(n) -> str:
    return f"{n:,}" if isinstance(n, int) else "—"


def license_of(meta: dict) -> str:
    if not meta or not meta.get("ok"):
        return "未知"
    return meta.get("license") or "NO-LICENSE（未声明）"


def state_of(meta: dict) -> str:
    if not meta or not meta.get("ok"):
        return "⚠ API 查不到"
    bits = []
    if meta.get("archived"):
        bits.append("已归档")
    if not meta.get("license"):
        bits.append("未声明许可证")
    return "、".join(bits) if bits else "在用"


def video_links(point: dict) -> list[tuple[str, str]]:
    """按查询词的语言给出检索链接。

    中文查询给 B 站与国家平台的检索页，英文查询给 YouTube 的检索页。
    检索页是函数不是快照：它永远不会失效，且平台自己会把最新的好内容排前。
    具体某一条视频的地址会下架、会改名，写进教材就是在制造死链。
    """
    templates = {t["key"]: t["template"] for t in load_links()["search_templates"]}
    out: list[tuple[str, str]] = []
    for query in (point.get("video") or {}).get("q") or []:
        if CJK_RE.search(query):
            if "bilibili" in templates:
                out.append((f"B站：{query}", search_url(templates["bilibili"], query)))
            if "smartedu-search" in templates:
                out.append((f"官方微课：{query}", search_url(templates["smartedu-search"], query)))
        else:
            if "youtube" in templates:
                out.append((f"YouTube：{query}", search_url(templates["youtube"], query)))
            if "ocw-search" in templates:
                out.append((f"MIT OCW：{query}", search_url(templates["ocw-search"], query)))
    return out


def curated_links(point: dict) -> list[dict]:
    table = link_entries()
    return [table[k] for k in (point.get("video") or {}).get("c") or [] if k in table]


# ---------------------------------------------------------------- 反向索引
def resources_by_point() -> dict[str, list[dict]]:
    verified = oss_verified()
    out: dict[str, list[dict]] = {}
    for res in load_oss():
        meta = verified.get(res["repo"].lower()) or {}
        entry = {**res, "meta": meta}
        for pid in res.get("points") or []:
            out.setdefault(pid, []).append(entry)
    for entries in out.values():
        entries.sort(key=lambda e: -(e["meta"].get("stars") or 0))
    return out


def resource_row(res: dict) -> str:
    meta = res.get("meta") or {}
    stars = money(meta.get("stars")) if meta.get("ok") else "—"
    return (f"[{res['title']}](https://github.com/{meta.get('full_name') or res['repo']})"
            f" · ★{stars} · {license_of(meta)} · {state_of(meta)}")


# ---------------------------------------------------------------- 各文档渲染
def render_stage(stage: dict, resmap: dict) -> str:
    index = load_index()
    strands = {s["id"]: s for s in index["strands"]}
    points = [p for p in iter_points() if p["stage_id"] == stage["id"]]
    core = sum(1 for p in points if p.get("core"))
    lines = [
        f"# {stage['name']} · {stage['grades']}",
        "",
        f"[目录](CATALOG.md) · [主线视图](STRANDS.md) · [开源资源](RESOURCES.md) · "
        f"[覆盖情况](COVERAGE.md)",
        "",
        "> " + " ".join((stage.get("anchor") or "").split()),
        "",
        f"本学段共 **{len(points)}** 个知识点，其中主干 **{core}** 个；"
        f"覆盖 **{len(stage['units'])}** 个学科单元。"
        "「主干」= 缺了它后面的世界认知会断链的那些条目。",
        "",
    ]
    for unit in stage["units"]:
        upoints = unit.get("points") or []
        lines += [
            f"## {index['subjects'].get(unit['subject_id'], {}).get('name', unit['subject_id'])}"
            f"（{len(upoints)} 个知识点）",
            "",
            "> " + " ".join((unit.get("why") or "").split()),
            "",
        ]
        for point in upoints:
            lines += render_point(point, unit["subject_id"], strands, resmap)
    return "\n".join(lines)


def render_point(point: dict, subject_id: str, strands: dict, resmap: dict) -> list[str]:
    tags = [point.get("grade") or ""]
    if point.get("core"):
        tags.append("**主干**")
    if point.get("strand") in strands:
        tags.append("主线：" + strands[point["strand"]]["name"])
    lines = [
        f"### {point['id']} · {point['title']}",
        "",
        " · ".join(t for t in tags if t),
        "",
        f"- **一年级版**：{point['kid']}",
        f"- **第一性原理**：{' '.join(point['principle'].split())}",
        f"- **与世界模型的连接**：{' '.join(point['model'].split())}",
        f"- **出口标准**：{' '.join(point['exit'].split())}",
    ]
    if point.get("prereq"):
        lines.append("- **前置**：" + "、".join(f"`{p}`" for p in point["prereq"]))
    links = video_links(point)
    if links:
        lines.append("- **视频入口**：" + " · ".join(f"[{t}]({u})" for t, u in links))
    for item in curated_links(point):
        lines.append(f"- **整站资源**：[{item['title']}]({item['url']})（{item['platform']}）")
    for res in resmap.get(point["id"], []):
        lines.append(f"- **开源项目**：{resource_row(res)}")
        lines.append(f"  - 怎么用：{' '.join(res['how'].split())}")
    lines.append("")
    return lines


def render_catalog() -> str:
    index = load_index()
    stages = load_stages()
    points = iter_points()
    lines = [
        "# 知识点总目录",
        "",
        "[主线视图](STRANDS.md) · [开源资源](RESOURCES.md) · [覆盖情况](COVERAGE.md)",
        "",
        f"共 **{len(points)}** 个知识点，分布在 **{len(stages)}** 个学段、"
        f"**{sum(len(s['units']) for s in stages)}** 个学科单元。",
        "",
        "按学段读：[小学](primary.md) · [初中](middle.md) · [高中](high.md) · "
        "[大学基础](university.md) · [语言](language.md)",
        "",
    ]
    for stage in stages:
        lines += [
            f"## {stage['name']}（{stage['grades']}）— [完整内容]({stage['id']}.md)",
            "",
            "| id | 知识点 | 年级 | 学科 | 主干 | 主线 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        strands = {s["id"]: s["name"] for s in index["strands"]}
        for unit in stage["units"]:
            name = index["subjects"].get(unit["subject_id"], {}).get("name", unit["subject_id"])
            for point in unit.get("points") or []:
                lines.append(
                    f"| `{point['id']}` | {point['title']} | {point.get('grade', '')} | {name} | "
                    f"{'●' if point.get('core') else ''} | "
                    f"{strands.get(point.get('strand'), '')} |"
                )
        lines.append("")
    return "\n".join(lines)


def render_strands() -> str:
    index = load_index()
    points = iter_points()
    lines = [
        "# 按主线看：世界是怎么运作的",
        "",
        "学科是按人类分工切的，主线是按世界本身切的。同一个机制会在不同学科里反复出现，"
        "这一页的作用是把它揪出来——你在初中物理见过的「守恒」，和大学热力学的「熵」、"
        "编程里的「不可逆操作」，是同一件事的三件衣服。",
        "",
        f"共 {len(index['strands'])} 条主线。",
        "",
    ]
    for strand in index["strands"]:
        matched = [p for p in points if p.get("strand") == strand["id"]]
        lines += [
            f"## {strand['name']}（{len(matched)} 个知识点）",
            "",
            f"要回答的问题：{strand['question']}",
            "",
            "| 学段 | id | 知识点 | 主干 |",
            "| --- | --- | --- | --- |",
        ]
        for p in sorted(matched, key=lambda x: (x["stage_name"], x["id"])):
            lines.append(f"| {p['stage_name']} | `{p['id']}` | {p['title']} | "
                         f"{'●' if p.get('core') else ''} |")
        lines.append("")
    uncharted = [p for p in points if not p.get("strand")]
    lines += [
        f"## 未归入主线（{len(uncharted)} 个）",
        "",
        "这些条目支撑主线但本身不是某个机制的代表，因此不标主线。",
        "",
    ]
    for p in uncharted:
        lines.append(f"- `{p['id']}` {p['title']}（{p['stage_name']}·{p['subject_name']}）")
    lines.append("")
    return "\n".join(lines)


def render_resources() -> str:
    verified = oss_verified()
    meta = oss_verified_meta()
    resources = load_oss()
    points = {p["id"]: p for p in iter_points()}
    lines = [
        "# 开源资源索引",
        "",
        "这一页是全仓库**唯一**讲述第三方项目的地方。收进来的标准是：能用 API 查到、"
        "能对上某个知识点的出口标准、且能说清它的限制。",
        "",
        "**下面的星数与许可证不是手打的**，由 `scripts/fetch_oss.py` 从 GitHub API 拉取并落盘到 "
        "`data/oss-verified.json`；跑 `python scripts/fetch_oss.py` 即可刷新。"
        "最后一次拉取："
        + (meta.get("fetched_at") or "尚未拉取") + "。",
        "",
        "本仓库对这些项目**只做索引与使用说明**，不声称作者身份、不声称已经验证其正确性、"
        "不声称它们与勘境有关。作者、许可证与原始来源见 "
        "[ATTRIBUTION.md](../ATTRIBUTION.md)。",
        "",
        "## 一览",
        "",
        "| 项目 | 语言 | 类型 | 星数 | 许可证 | 状态 | 最后提交 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for res in sorted(resources, key=lambda r: -(verified.get(r["repo"].lower(), {}).get("stars") or 0)):
        m = verified.get(res["repo"].lower()) or {}
        url = f"https://github.com/{m.get('full_name') or res['repo']}"
        lines.append(
            f"| [{res['title']}]({url}) | {res['lang']} | {res['kind']} | "
            f"{money(m.get('stars')) if m.get('ok') else '—'} | {license_of(m)} | "
            f"{state_of(m)} | {m.get('pushed_at') or '—'} |"
        )
    lines += ["", "## 按知识点反查", "",
              "想知道某个知识点能用什么开源项目练，从这里查。", ""]
    resmap = resources_by_point()
    for pid in sorted(resmap):
        p = points.get(pid)
        head = f"`{pid}` {p['title']}" if p else pid
        lines.append(f"### {head}")
        lines.append("")
        for res in resmap[pid]:
            lines.append(f"- {resource_row(res)}")
            lines.append(f"  - 它是什么：{' '.join(res['what'].split())}")
            lines.append(f"  - 怎么用：{' '.join(res['how'].split())}")
            lines.append(f"  - 限制：{' '.join(res['caution'].split())}")
        lines.append("")
    lines += ["## 逐条说明", ""]
    for res in resources:
        m = verified.get(res["repo"].lower()) or {}
        url = f"https://github.com/{m.get('full_name') or res['repo']}"
        lines += [
            f"### {res['title']}（`{res['repo']}`）",
            "",
            f"[{url}]({url}) · {res['lang']} · {res['kind']} · ★"
            f"{money(m.get('stars')) if m.get('ok') else '—'} · {license_of(m)} · {state_of(m)}",
            "",
            f"- **是什么**：{' '.join(res['what'].split())}",
            f"- **怎么用**：{' '.join(res['how'].split())}",
            f"- **限制**：{' '.join(res['caution'].split())}",
            "",
        ]
    return "\n".join(lines)


def render_links() -> str:
    links = load_links()
    status = link_status()
    meta = link_status_meta()
    lines = [
        "# 外部链接与核验状态",
        "",
        "这个页面里的状态码是 `scripts/check_links.py` 实测的结果，不是人工判断。"
        "最后一次检查：" + (meta.get("checked_at") or "尚未检查") + "。",
        "",
        "**判据必须分清，否则报告会骗人**：",
        "",
        "| 状态 | 含义 | 要不要处理 |",
        "| --- | --- | --- |",
        "| verified | 本机实测有响应 | 不用 |",
        "| dead | 明确 404 / 410 | 必须修，CI 会失败 |",
        "| unreachable | 本机超时或连不上 | 换网络复核，**不代表失效** |",
        "| blocked | 401 / 403 / 429 / 5xx，被反爬或限额挡 | 人工打开确认，**不代表失效** |",
        "",
        "## 整站资源",
        "",
        "| key | 名称 | 平台 | 状态 | HTTP | 说明 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in links["links"]:
        s = status.get(item["key"]) or {}
        lines.append(
            f"| `{item['key']}` | [{item['title']}]({item['url']}) | {item['platform']} | "
            f"{s.get('status', '未检查')} | {s.get('code') or '—'} | "
            f"{' '.join(item['what'].split())} |"
        )
    lines += ["", "## 检索模板", "",
              "这些不是链接，是函数：给定关键词返回一个永远有效的检索页。"
              "每个知识点的具体视频都走这里，所以不存在「教材里的视频链接已下架」这个问题。", "",
              "| key | 平台 | 模板 | 状态 | 说明 |", "| --- | --- | --- | --- | --- |"]
    for tpl in links["search_templates"]:
        s = status.get("template:" + tpl["key"]) or {}
        lines.append(f"| `{tpl['key']}` | {tpl['title']} | `{tpl['template']}` | "
                     f"{s.get('status', '未检查')} | {' '.join(tpl['note'].split())} |")
    lines.append("")
    return "\n".join(lines)


def render_coverage() -> str:
    index = load_index()
    stages = load_stages()
    points = iter_points()
    resmap = resources_by_point()
    verified = oss_verified()
    meta = oss_verified_meta()

    per_stage = []
    for stage in stages:
        pts = [p for p in points if p["stage_id"] == stage["id"]]
        per_stage.append({
            "name": stage["name"],
            "subjects": len(stage["units"]),
            "points": len(pts),
            "core": sum(1 for p in pts if p.get("core")),
            "resources": sum(1 for p in pts if p["id"] in resmap),
        })
    total_core = sum(1 for p in points if p.get("core"))
    with_res = sum(1 for p in points if p["id"] in resmap)

    lines = [
        "# 覆盖情况与已知缺口",
        "",
        "每一行数字都由 `scripts/build.py` 现算。跑 `python scripts/validate.py -v` 也能看到同一张表。",
        "",
        "## 覆盖表",
        "",
        "| 学段 | 学科单元 | 知识点 | 其中主干 | 有开源项目可练 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in per_stage:
        lines.append(f"| {row['name']} | {row['subjects']} | {row['points']} | "
                     f"{row['core']} | {row['resources']} |")
    lines.append(f"| **合计** | {sum(r['subjects'] for r in per_stage)} | **{len(points)}** | "
                 f"{total_core} | {with_res} |")
    lines += [
        "",
        "## GitHub 在基础教育这一层是薄的：实测结论",
        "",
        "这不是猜测，是点名核验的结果。设计这个仓库时，先用 GitHub 搜索 API 找"
        "「小初高教材 / K-12 curriculum / 中文教材」，返回的主要是空壳 fork 与个人书单；"
        "再对一批相关仓库做逐个核验，下列思路在 GitHub 上**不存在**对应的真实仓库：",
        "",
        "| 我试过的方向 | API 结果 |",
        "| --- | --- |",
        "| `OpenSciEd/OpenSciEd`（开源 K-12 科学课程） | 404 |",
        "| `illustrative-mathematics/IllustrativeMathematics` | 404 |",
        "| `openstax/osbooks-calculus-volume-1` | 404（真实的是 `openstax/osbooks-calculus-bundle`） |",
        "| `openstax/osbooks-chemistry-2e` | 404 |",
        "| `openstax/unified` / `openstax/cnx-recipes` | 404 |",
        "| `teachyourselfcs/teachyourselfcs` | 404 |",
        "| `phetsims/phet`（PhET 主仓库） | 404（真实的是逐个子仿真仓库） |",
        "",
        "所以本仓库的取舍是：",
        "",
        "1. **小学到高中**：正文骨架自己写，外部资源走非 GitHub 的官方平台"
        "（国家中小学智慧教育平台、可汗学院中文、PhET 中文站）。",
        "2. **大学及以上**：大量索引真实存在的开源项目，因为这一层 GitHub 内容丰富且活跃。",
        "3. **实验与仿真**：索引 PhET 的逐个子仿真仓库，它们能对上中学物理化学的出口标准。",
        "",
        f"当前 {len(points)} 个知识点里有 {with_res} 个配到了开源项目"
        f"（{round(100 * with_res / len(points))}%），其余靠外部平台与检索入口支撑。",
        "",
        "## 已知缺口（诚实清单）",
        "",
        "- **视频是检索入口，不是精选视频。** 每个知识点给的是 B 站 / YouTube / 官方平台的"
        "检索页，不是某一条具体视频。原因写在 [LINKS.md](LINKS.md)：具体视频会下架、会改名，"
        "写进教材等于制造死链。代价是读者要多点一次，收益是链接永不失效且能拿到更新的内容。",
        "- **没有习题与答案。** 本仓库只给知识点、出口标准与练习方向，不提供题目。"
        "刷题请用 OpenStax、可汗学院、国家中小学智慧教育平台的题。",
        "- **没有教学进度表。** 「第几周学什么」取决于你每天能投入多久，本仓库不替你定。",
        "- **历史与思政两科的外部资源最薄。** 这两科高度依赖特定教材与语境，"
        "GitHub 上没有可用的开源对应物，只能靠官方平台。",
        "- **主线标注不完整。** 未标主线的条目见 [STRANDS.md](STRANDS.md) 结尾。",
        "",
        "## 外部数据的新鲜度",
        "",
        f"- 开源项目元数据（星数、许可证、最后提交）：{meta.get('fetched_at') or '尚未拉取'}"
        "，来源 " + (meta.get("source") or "—") + "。",
        "- 外部链接状态：见 [LINKS.md](LINKS.md) 顶部时间戳。",
        "",
        "这两类数字**必然**会过期。过期不是缺陷，假装不过期才是。"
        "看到某个项目已归档或换了许可证，请提 PR 更新 `data/` 下的源文件后重跑脚本。",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------- HTML 仪表盘
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KineLearn · 从第一性原理建立世界认知</title>
<style>
:root{
  --bg:#f7f8fa; --card:#ffffff; --ink:#1b1f24; --sub:#5b6673; --line:#e3e7ec;
  --accent:#1f6feb; --accent-soft:#eaf1ff; --warn:#a15c00; --warn-soft:#fff5e5;
  --ok:#1a7f37; --ok-soft:#e8f5ec; --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
header{background:#fff;border-bottom:1px solid var(--line);padding:28px 20px 20px}
.wrap{max-width:1180px;margin:0 auto}
h1{margin:0 0 6px;font-size:24px;letter-spacing:.2px}
.sub{color:var(--sub);font-size:13.5px;max-width:820px}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.stat{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:12.5px;color:var(--sub)}
.stat b{display:block;font-size:19px;color:var(--ink);font-weight:650;letter-spacing:.3px}
.controls{position:sticky;top:0;z-index:9;background:rgba(247,248,250,.94);
  backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 20px}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
input[type=search],select{font:inherit;font-size:13.5px;padding:7px 10px;border:1px solid var(--line);
  border-radius:7px;background:#fff;color:var(--ink)}
input[type=search]{flex:1;min-width:210px}
.chip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:5px 12px;font-size:13px;
  cursor:pointer;color:var(--sub);user-select:none}
.chip:hover{border-color:#c9d2dc}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fff}
.chip.core.on{background:#8a5a00;border-color:#8a5a00}
main{padding:18px 20px 60px}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));margin-top:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:14px 16px}
.card h3{margin:0 0 6px;font-size:16px;line-height:1.4}
.meta{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.tag{font-size:11.5px;padding:2px 8px;border-radius:999px;background:var(--bg);color:var(--sub);border:1px solid var(--line)}
.tag.core{background:#fff3d6;border-color:#f0d9a8;color:var(--warn)}
.tag.strand{background:var(--accent-soft);border-color:#cfe0ff;color:#14508c}
.tag.id{font-family:var(--mono);font-size:11px}
.f{margin:7px 0;font-size:13.6px}
.f .k{color:var(--sub);font-size:12px;display:block;margin-bottom:1px}
.f.kid{background:#fffdf5;border-left:3px solid #f0d9a8;padding:6px 10px;border-radius:0 6px 6px 0}
.f.model{color:#25436b}
.f.exit{background:var(--ok-soft);border-left:3px solid #a8d8b6;padding:6px 10px;border-radius:0 6px 6px 0}
.links{margin-top:10px;padding-top:9px;border-top:1px dashed var(--line);font-size:12.6px}
.links a{color:var(--accent);text-decoration:none;margin-right:10px;display:inline-block}
.links a:hover{text-decoration:underline}
.res{margin-top:6px;font-size:12.4px;color:var(--sub)}
.res a{color:var(--accent);text-decoration:none}
.empty{color:var(--sub);padding:30px 0;text-align:center}
footer{border-top:1px solid var(--line);background:#fff;padding:22px 20px;color:var(--sub);font-size:12.6px}
footer a{color:var(--accent)}
.note{background:var(--warn-soft);border:1px solid #f0d9a8;border-radius:8px;padding:10px 12px;margin-top:12px;font-size:12.8px;color:#6b4700}
@media (max-width:620px){.grid{grid-template-columns:1fr}h1{font-size:20px}}
</style>
</head>
<body>
<header><div class="wrap">
  <h1>KineLearn · 从第一性原理建立世界认知</h1>
  <p class="sub">小学到大学的学科骨架 + 真实存在的开源项目索引 + 永不失效的视频检索入口。
  每个知识点四件事：一年级小孩能听懂的说法、它背后的第一性原理、它与世界模型的连接、以及一个能失败的出口标准。</p>
  <div class="stats" id="stats"></div>
</div></header>

<div class="controls"><div class="wrap">
  <div class="row">
    <input type="search" id="q" placeholder="搜知识点、id、关键词（例如：守恒、导数、熵、uni-lin）">
    <select id="subject"><option value="">全部学科</option></select>
    <select id="strand"><option value="">全部主线</option></select>
    <span class="chip core" id="corechip">只看主干</span>
    <span class="chip" id="reset">清空</span>
  </div>
  <div class="row" id="stages" style="margin-top:8px"></div>
</div></div>

<main><div class="wrap">
  <div id="count" class="sub" style="font-size:13px"></div>
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" style="display:none">没有匹配的知识点。换个关键词试试。</div>
</div></main>

<footer><div class="wrap">
  <div id="gen"></div>
  <p><b>这不是能力声明。</b>本仓库是教育材料，不声称任何排名、水平或商业能力；
  「达到全球前 1% 认知」是读者可以自己检验的学习目标，不是本仓库的承诺——
  判断标准写在 <a href="https://github.com/kineworld/kine-learn/blob/main/ROADMAP.md">ROADMAP.md</a> 的出口检查里。</p>
  <p>其它入口：<a href="https://github.com/kineworld/kine-learn">仓库</a> ·
  <a href="https://github.com/kineworld/kine-learn/blob/main/docs/CATALOG.md">总目录</a> ·
  <a href="https://github.com/kineworld/kine-learn/blob/main/docs/STRANDS.md">按主线看</a> ·
  <a href="https://github.com/kineworld/kine-learn/blob/main/docs/RESOURCES.md">开源资源</a> ·
  <a href="https://github.com/kineworld/kine-learn/blob/main/docs/COVERAGE.md">覆盖与缺口</a> ·
  <a href="https://github.com/kineworld/kine-learn/blob/main/ATTRIBUTION.md">第三方归属</a></p>
  <div class="note">第三方项目与视频均指向各自的原站，版权归原作者所有。本仓库只做索引与使用说明，
  不镜像内容、不声称作者身份。外部资源的星数与许可证由脚本从 GitHub API 拉取，会过期——请以原站为准。</div>
</div></footer>

<script type="application/json" id="data">__DATA__</script>
<script>
(function(){
  var D = JSON.parse(document.getElementById('data').textContent);
  var S = {stage:"", subject:"", strand:"", core:false, q:""};

  var stats = document.getElementById('stats');
  D.stats.forEach(function(s){
    var d = document.createElement('div'); d.className='stat';
    d.innerHTML = '<b>'+s.v+'</b>'+s.k; stats.appendChild(d);
  });

  var stagesBox = document.getElementById('stages');
  D.stages.forEach(function(st){
    var c = document.createElement('span');
    c.className='chip'; c.textContent = st.name+'（'+st.n+'）'; c.dataset.id = st.id;
    c.onclick = function(){ pickStage(st.id, c); };
    stagesBox.appendChild(c);
  });
  function pickStage(id, el){
    S.stage = (S.stage === id) ? "" : id;
    Array.prototype.forEach.call(stagesBox.children, function(x){
      x.classList.toggle('on', x.dataset.id === S.stage);
    });
    render();
  }

  var subj = document.getElementById('subject');
  D.subjects.forEach(function(s){
    var o = document.createElement('option'); o.value=s.id; o.textContent=s.name+'（'+s.n+'）';
    subj.appendChild(o);
  });
  subj.onchange = function(){ S.subject = subj.value; render(); };

  var strand = document.getElementById('strand');
  D.strands.forEach(function(s){
    var o = document.createElement('option'); o.value=s.id; o.textContent=s.name+'（'+s.n+'）';
    strand.appendChild(o);
  });
  strand.onchange = function(){ S.strand = strand.value; render(); };

  var coreChip = document.getElementById('corechip');
  coreChip.onclick = function(){ S.core = !S.core; coreChip.classList.toggle('on', S.core); render(); };

  var qi = document.getElementById('q');
  qi.oninput = function(){ S.q = qi.value.trim().toLowerCase(); render(); };

  document.getElementById('reset').onclick = function(){
    S = {stage:"", subject:"", strand:"", core:false, q:""};
    qi.value=''; subj.value=''; strand.value='';
    coreChip.classList.remove('on');
    Array.prototype.forEach.call(stagesBox.children, function(x){ x.classList.remove('on'); });
    render();
  };

  var grid = document.getElementById('grid');
  var empty = document.getElementById('empty');
  var count = document.getElementById('count');

  function esc(t){
    return String(t).replace(/[&<>"]/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];
    });
  }

  function card(p){
    var h = '<h3>'+esc(p.title)+'</h3>';
    h += '<div class="meta">';
    h += '<span class="tag id">'+esc(p.id)+'</span>';
    h += '<span class="tag">'+esc(p.stage)+' · '+esc(p.subject)+'</span>';
    if(p.grade) h += '<span class="tag">'+esc(p.grade)+'</span>';
    if(p.core) h += '<span class="tag core">主干</span>';
    if(p.strand) h += '<span class="tag strand">'+esc(p.strand)+'</span>';
    h += '</div>';
    h += '<div class="f kid"><span class="k">一年级版</span>'+esc(p.kid)+'</div>';
    h += '<div class="f"><span class="k">第一性原理</span>'+esc(p.principle)+'</div>';
    h += '<div class="f model"><span class="k">与世界模型的连接</span>'+esc(p.model)+'</div>';
    h += '<div class="f exit"><span class="k">出口标准</span>'+esc(p.exit)+'</div>';
    if(p.prereq && p.prereq.length){
      h += '<div class="f"><span class="k">前置</span><code>'+p.prereq.map(esc).join('</code> <code>')+'</code></div>';
    }
    if(p.video && p.video.length){
      h += '<div class="links">视频：' + p.video.map(function(v){
        return '<a href="'+esc(v[1])+'" target="_blank" rel="noopener">'+esc(v[0])+'</a>';
      }).join('') + '</div>';
    }
    if(p.curated && p.curated.length){
      h += '<div class="links">整站：' + p.curated.map(function(v){
        return '<a href="'+esc(v[1])+'" target="_blank" rel="noopener">'+esc(v[0])+'</a>';
      }).join('') + '</div>';
    }
    if(p.res && p.res.length){
      h += '<div class="res">开源项目：' + p.res.map(function(v){
        return '<a href="'+esc(v[3])+'" target="_blank" rel="noopener">'+esc(v[0])+'</a>'
             + ' <span>★'+esc(v[1])+' · '+esc(v[2])+'</span>';
      }).join('<br>') + '</div>';
    }
    return '<div class="card">'+h+'</div>';
  }

  function render(){
    var out = D.points.filter(function(p){
      if(S.stage && p.stage_id !== S.stage) return false;
      if(S.subject && p.subject_id !== S.subject) return false;
      if(S.strand && p.strand_id !== S.strand) return false;
      if(S.core && !p.core) return false;
      if(S.q){
        var hay = (p.id+' '+p.title+' '+p.kid+' '+p.principle+' '+p.model+' '+p.exit+' '
                   +p.subject+' '+p.stage+' '+p.grade+' '+(p.strand||'')).toLowerCase();
        if(hay.indexOf(S.q) < 0) return false;
      }
      return true;
    });
    count.textContent = '显示 ' + out.length + ' / ' + D.points.length + ' 个知识点';
    empty.style.display = out.length ? 'none' : 'block';
    grid.innerHTML = out.map(card).join('');
  }

  document.getElementById('gen').textContent =
    '数据源 ' + D.sources + ' · 开源项目元数据更新于 ' + D.oss_fetched_at
    + ' · 链接状态检查于 ' + D.links_checked_at;
  render();
})();
</script>
</body>
</html>
"""


def build_html(resmap: dict) -> str:
    index = load_index()
    stages = load_stages()
    points = iter_points()
    verified = oss_verified()
    curated = link_entries()

    stage_counts: dict[str, int] = {}
    subject_counts: dict[str, int] = {}
    strand_counts: dict[str, int] = {}
    payload_points = []
    for p in points:
        stage_counts[p["stage_id"]] = stage_counts.get(p["stage_id"], 0) + 1
        subject_counts[p["subject_id"]] = subject_counts.get(p["subject_id"], 0) + 1
        if p.get("strand"):
            strand_counts[p["strand"]] = strand_counts.get(p["strand"], 0) + 1

        res = []
        for r in resmap.get(p["id"], []):
            meta = r.get("meta") or {}
            res.append([
                r["title"],
                money(meta.get("stars")) if meta.get("ok") else "—",
                license_of(meta),
                f"https://github.com/{meta.get('full_name') or r['repo']}",
            ])
        payload_points.append({
            "id": p["id"],
            "title": p["title"],
            "stage_id": p["stage_id"],
            "stage": p["stage_name"],
            "subject_id": p["subject_id"],
            "subject": p["subject_name"],
            "grade": p.get("grade") or "",
            "core": bool(p.get("core")),
            "strand_id": p.get("strand") or "",
            "strand": next((s["name"] for s in index["strands"] if s["id"] == p.get("strand")), ""),
            "kid": p["kid"],
            "principle": " ".join(p["principle"].split()),
            "model": " ".join(p["model"].split()),
            "exit": " ".join(p["exit"].split()),
            "prereq": p.get("prereq") or [],
            "video": video_links(p),
            "curated": [[c["title"], c["url"]] for c in curated_links(p)],
            "res": res,
        })

    total_core = sum(1 for p in points if p.get("core"))
    with_res = sum(1 for p in points if p["id"] in resmap)
    stats = [
        {"k": "知识点", "v": len(points)},
        {"k": "其中主干", "v": total_core},
        {"k": "学科单元", "v": sum(len(s["units"]) for s in stages)},
        {"k": "开源项目", "v": len(load_oss())},
        {"k": "配到开源项目的知识点", "v": with_res},
        {"k": "外部链接登记", "v": len(curated)},
    ]
    payload = {
        # 刻意不放"构建时间"。墙上时钟会让每次构建的产物都不同，
        # 于是 CI 里"生成物是否与源文件同步"的检查（git diff --exit-code）
        # 会永远为红，最后没人再看它。时间信息一律来自数据文件自身的戳。
        "sources": "curriculum/*.yaml + data/links.yaml + data/oss-resources.yaml",
        "oss_fetched_at": oss_verified_meta().get("fetched_at") or "尚未拉取",
        "links_checked_at": link_status_meta().get("checked_at") or "尚未检查",
        "stats": stats,
        "stages": [{"id": s["id"], "name": s["name"], "n": stage_counts.get(s["id"], 0)}
                   for s in stages],
        "subjects": [{"id": sid, "name": meta["name"], "n": subject_counts.get(sid, 0)}
                     for sid, meta in index["subjects"].items() if subject_counts.get(sid)],
        "strands": [{"id": s["id"], "name": s["name"], "n": strand_counts.get(s["id"], 0)}
                    for s in index["strands"]],
        "points": payload_points,
    }
    return HTML_TEMPLATE.replace("__DATA__", embed(payload))


def embed(payload: dict) -> str:
    """把数据载荷序列化成能安全塞进内联 script 的字符串。

    JSON 里任何一个 `</`（例如某段说明里出现了 `</script>`）都会提前闭合内联脚本，
    页面直接白屏——而且浏览器不报错，只留一片空白，排查起来毫无线索。
    所以 `</` 一律写成 `<\\/`，JSON 解析器看它仍是 `/`。

    单独抽成一个函数是为了能被直接测：这是整条渲染链上唯一一个"写错了会静默白屏"
    的地方，而静默失败最需要一条会变红的用例。
    """
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return raw.replace("</", "<\\/")


# ---------------------------------------------------------------- 入口
def main() -> int:
    resmap = resources_by_point()
    stages = load_stages()

    written = []
    for stage in stages:
        path = _common.DOCS_DIR / f"{stage['id']}.md"
        write_text(path, render_stage(stage, resmap))
        written.append(path)

    for name, renderer in (("CATALOG.md", render_catalog), ("STRANDS.md", render_strands),
                           ("RESOURCES.md", render_resources), ("LINKS.md", render_links),
                           ("COVERAGE.md", render_coverage)):
        path = _common.DOCS_DIR / name
        write_text(path, renderer())
        written.append(path)

    html_path = _common.SITE_DIR / "index.html"
    write_text(html_path, build_html(resmap))
    written.append(html_path)

    points = iter_points()
    total = len(points)
    core = sum(1 for p in points if p.get("core"))
    print(f"生成 {len(written)} 个文件：")
    for path in written:
        size = path.stat().st_size
        print(f"  {path.relative_to(_common.ROOT).as_posix():28} {size:>8,} 字节")
    print(f"\n知识点 {total} 个（主干 {core}）| 学科单元 "
          f"{sum(len(s['units']) for s in stages)} 个 | 开源资源 {len(load_oss())} 条 | "
          f"配到资源的知识点 {sum(1 for p in points if p['id'] in resmap)} 个")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
