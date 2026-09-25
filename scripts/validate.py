"""检查 curriculum/ 与 data/ 的内容是否自洽。

这个文件的存在理由：教材最常见的腐烂方式不是写错，是**目录和正文不一致**——
加了一个知识点却忘了在总表登记，改了一个 id 却没改引用它的前置条件。
人工核对会在第三次修改后失效，所以检查必须能脚本化、能失败。

    用法：python scripts/validate.py          # 有错就退出码 1
          python scripts/validate.py -v       # 打印每一条通过的检查

每条检查都要能失败。如果一个检查在任何输入下都通过，它就不是检查，
是装饰品（本组织 CONTRIBUTING.md 明写：无法让它变红的检查应当删除）。
"""

from __future__ import annotations

import argparse
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _common  # noqa: E402
from _common import (  # noqa: E402
    ALLOWED_KINDS, ALLOWED_LANGS, REPO_RE, REQUIRED_POINT_FIELDS,
    STAGE_PREFIX, iter_points, link_entries, load_index, load_links, load_oss,
    load_stages, oss_verified,
)

# ---------------------------------------------------------------- 措辞红线
#
# 本组织禁止无证据的能力与排名声明。这些不是风格偏好，是治理要求：
# 一旦允许"保证学会""全球第一"这类句子，整套材料就从教材退化成广告，
# 而读者无法区分哪一句有证据、哪一句没有。
#
# 注意这是**窄模式**：只拦具体的承诺句式，不拦"保证"二字本身
# （"不能保证"是合法且必要的表述）。
CLAIM_PATTERNS = [
    (r"保证[^。；\n]{0,8}(学会|掌握|提分|考上|达到|通过)", "保证性承诺"),
    (r"一定(能|会)[^。；\n]{0,6}(学会|掌握|考上|变成|达到)", "保证性承诺"),
    (r"必然(达到|成为|成为全球)", "保证性承诺"),
    (r"(全球|世界|全国|全网|全人类)(第一|最强|最好)", "排名或最强声明"),
    (r"最(权威|顶尖|先进)的(认知|水平|教材|课程)", "最高级断言"),
    (r"(百分百|100%)\s*(有效|正确|学会)", "保证性承诺"),
    (r"读(完|过)[^。；\n]{0,6}(就|即)[^。；\n]{0,6}(能|会)", "轻率承诺"),
    (r"包(过|学会)", "保证性承诺"),
]

# 允许出现"前 1%"的位置与条件：必须是目标语，且同一行里有明确的限定语。
#
# 限定语的写法要认**意图**，不是认某个固定句式。原先只认字面的"不是承诺"，
# 于是"是方向，不是它的承诺"被判违规——那句明明是在撇清，却被拦下。
# 被规矩逼着改措辞，而不是被规矩拦住错误，说明规矩写歪了。
#
# 反过来也不能放太松：把"方向"单列进白名单，等于只要提到"方向"就放行，
# 那这条检查就退化成"禁止提起前 1%"。所以只补"不是……承诺"这一族写法。
PCT_RE = re.compile(r"前\s*1\s*%")
PCT_SAFE_RE = re.compile(r"(目标|不是[^。\n]{0,6}承诺|不声称|自我检查|自检)")

# 红线只针对**承诺句**，否定形式恰好是诚实的那一半，必须放行。
# 「不能保证你掌握」和「保证你掌握」在正则眼里只差一个字，含义却相反，
# 所以命中后要回看前几个字有没有否定词。没有这道回看，整个正则写成
# `保证` 也能让"能变红"的用例通过，代价是所有诚实的限定句被一起干掉。
NEGATION_RE = re.compile(r"[不无难未别]")
NEGATION_LOOKBACK = 4

DOC_WORD_FIELDS = ("kid", "principle", "model", "exit", "why")
OSS_WORD_FIELDS = ("what", "how", "caution")


class Problems:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, where: str, msg: str) -> None:
        self.items.append(f"{where}: {msg}")

    def __bool__(self) -> bool:
        return bool(self.items)


def _nonempty(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


# ---------------------------------------------------------------- 逐项检查
def check_index(problems: Problems) -> dict:
    index = load_index()
    for field in ("version", "updated", "stages", "subjects", "strands"):
        if not _nonempty(index.get(field)):
            problems.add("curriculum/_index.yaml", f"缺少或为空：{field}")
    for stage in index.get("stages") or []:
        for field in ("id", "name", "file", "anchor"):
            if not _nonempty(stage.get(field)):
                problems.add(f"curriculum/_index.yaml 学段 {stage.get('id')}", f"缺少：{field}")
        if stage.get("id") not in STAGE_PREFIX:
            problems.add(f"curriculum/_index.yaml 学段 {stage.get('id')}",
                         f"未在 STAGE_PREFIX 登记，知识点 id 前缀无法校验")
    for s in index.get("strands") or []:
        for field in ("id", "name", "question"):
            if not _nonempty(s.get(field)):
                problems.add(f"curriculum/_index.yaml 主线 {s.get('id')}", f"缺少：{field}")
    return index


def check_stage_files(problems: Problems, index: dict) -> list[dict]:
    declared = {s["file"] for s in index["stages"]}
    actual = {p.name for p in (_common.ROOT / "curriculum").glob("*.yaml")} - {"_index.yaml"}
    for missing in sorted(declared - actual):
        problems.add("curriculum/", f"总表声明了 {missing}，文件不存在")
    for extra in sorted(actual - declared):
        problems.add(f"curriculum/{extra}", "文件存在但总表未登记")

    subjects = index["subjects"]
    strands = {s["id"] for s in index["strands"]}
    # 缺失的学段文件在上面的报告里已经点过名，这里跳过它的正文检查，
    # 而不是让 load_stages 抛 FileNotFoundError 把整份报告吃掉。
    stages = load_stages(skip_missing=True)
    used_subjects: set[str] = set()

    for stage in stages:
        where = f"curriculum/{stage['file']}"
        if stage["units"] == []:
            problems.add(where, "没有任何学科单元")
        seen_units = set()
        for unit in stage["units"]:
            sid = unit.get("subject_id")
            if sid not in subjects:
                problems.add(where, f"学科 id 未在总表登记：{sid}")
                continue
            if sid in seen_units:
                problems.add(where, f"同一学科出现两次：{sid}")
            seen_units.add(sid)
            used_subjects.add(sid)
            if not _nonempty(unit.get("why")):
                problems.add(f"{where} :: {sid}", "缺少 why（为什么学这一科）")
            if not unit.get("points"):
                problems.add(f"{where} :: {sid}", "没有任何知识点")
            for point in unit.get("points") or []:
                check_point(problems, where, stage, point, strands)
    return stages


def check_point(problems: Problems, where: str, stage: dict, point: dict, strands: set[str]) -> None:
    pid = point.get("id") or "<无 id>"
    loc = f"{where} :: {pid}"
    for field in REQUIRED_POINT_FIELDS:
        if not _nonempty(point.get(field)):
            problems.add(loc, f"缺少或为空：{field}")

    prefix = STAGE_PREFIX.get(stage["id"])
    if prefix and isinstance(pid, str) and not pid.startswith(prefix):
        problems.add(loc, f"id 前缀应为 {prefix}（当前学段是 {stage['name']}）")

    strand = point.get("strand")
    if strand is not None and strand not in strands:
        problems.add(loc, f"主线未登记：{strand}")

    if point.get("core") not in (True, False, None):
        problems.add(loc, "core 只能是 true/false")

    video = point.get("video") or {}
    if not video.get("q"):
        problems.add(loc, "缺少 video.q（检索关键词）——每个知识点都必须有视频入口")
    for key in video.get("c") or []:
        if key not in link_entries():
            problems.add(loc, f"video.c 引用了 data/links.yaml 里不存在的 key：{key}")


def check_against_registry(problems: Problems, stages: list[dict], index: dict) -> None:
    """跨文件的引用检查：id 唯一、前置存在、学科无孤儿定义。"""
    points = iter_points(skip_missing=True)
    ids = [p.get("id") for p in points]
    dupes = {i for i in ids if ids.count(i) > 1}
    for d in sorted(dupes):
        problems.add("curriculum/", f"知识点 id 重复：{d}")

    known = set(ids)
    for p in points:
        for pre in p.get("prereq") or []:
            if pre not in known:
                problems.add(f"curriculum/ :: {p.get('id')}", f"前置知识点不存在：{pre}")
            if pre == p.get("id"):
                problems.add(f"curriculum/ :: {p.get('id')}", "前置指向自己")

    used = {u["subject_id"] for s in stages for u in s["units"]}
    for sid in sorted(set(index["subjects"]) - used):
        problems.add("curriculum/_index.yaml", f"学科 {sid} 在总表登记但没有任何学段使用它")


def check_claims(problems: Problems) -> None:
    for stage in load_stages(skip_missing=True):
        where = f"curriculum/{stage['file']}"
        for unit in stage["units"]:
            for field in DOC_WORD_FIELDS:
                text = unit.get(field)
                if isinstance(text, str):
                    scan_claims(problems, f"{where} :: {unit['subject_id']}.{field}", text)
            for point in unit.get("points") or []:
                for field in DOC_WORD_FIELDS:
                    text = point.get(field)
                    if isinstance(text, str):
                        scan_claims(problems, f"{where} :: {point.get('id')}.{field}", text)
    for res in load_oss():
        for field in OSS_WORD_FIELDS:
            text = res.get(field)
            if isinstance(text, str):
                scan_claims(problems, f"data/oss-resources.yaml :: {res.get('repo')}.{field}", text)


def scan_claims(problems: Problems, where: str, text: str) -> None:
    for pattern, label in CLAIM_PATTERNS:
        for match in re.finditer(pattern, text):
            before = text[max(0, match.start() - NEGATION_LOOKBACK):match.start()]
            if NEGATION_RE.search(before):
                continue
            problems.add(where, f"命中措辞红线（{label}）：「{match.group(0)}」")
            break


def check_percent_wording(problems: Problems) -> None:
    """"前 1%"只能作为目标出现，不能作为承诺。

    这条是单列的，因为它是用户明确提出的目标措辞，也是最容易被后来的
    贡献者改成承诺句的地方。扫的是**仓库根部全部 Markdown**，不是只扫
    README——把范围写死成两个文件名，等于给"换个文件写承诺句"留了后门。
    """
    for path in sorted(_common.ROOT.glob("*.md")):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if PCT_RE.search(line) and not PCT_SAFE_RE.search(line):
                problems.add(f"{path.name}:{i}",
                             "出现「前 1%」但同句没有 目标/不是承诺 之类限定语")


def check_oss(problems: Problems) -> None:
    seen = {}
    verified = oss_verified()
    for res in load_oss():
        repo = res.get("repo") or ""
        where = f"data/oss-resources.yaml :: {repo or '<无 repo>'}"
        if not REPO_RE.match(repo):
            problems.add(where, "repo 必须是 owner/name 形式")
            continue
        if repo.lower() in seen:
            problems.add(where, f"与 {seen[repo.lower()]} 重复（GitHub 仓库名不区分大小写）")
        seen[repo.lower()] = repo

        for field in ("title", "lang", "kind", "what", "how", "caution"):
            if not _nonempty(res.get(field)):
                problems.add(where, f"缺少：{field}")
        if res.get("lang") not in ALLOWED_LANGS:
            problems.add(where, f"lang 不在允许集合内：{res.get('lang')}")
        if res.get("kind") not in ALLOWED_KINDS:
            problems.add(where, f"kind 不在允许集合内：{res.get('kind')}")
        if not isinstance(res.get("points", []), list):
            problems.add(where, "points 必须是列表（没有对应知识点时写 []）")

        meta = verified.get(repo.lower())
        if meta:
            canonical = meta.get("full_name")
            if canonical and canonical != repo:
                problems.add(where, f"大小写与 API 返回的 full_name 不一致，应为 {canonical}")
            if not meta.get("ok"):
                problems.add(where, f"API 查不到该仓库（HTTP {meta.get('code')}）")


def check_links_registry(problems: Problems) -> None:
    """检查 data/links.yaml 本身的字段完整性。"""
    allowed_status = {"verified", "dead", "unreachable", "blocked"}
    for item in load_links()["links"]:
        key = item.get("key") or "<无 key>"
        where = f"data/links.yaml :: {key}"
        for field in ("key", "title", "url", "platform", "lang", "what"):
            if not _nonempty(item.get(field)):
                problems.add(where, f"缺少：{field}")
        if not str(item.get("url", "")).startswith(("http://", "https://")):
            problems.add(where, "url 必须是 http(s) 绝对地址")
        expect = item.get("expect")
        if expect is not None and expect not in allowed_status:
            problems.add(where, f"expect 取值必须是 {sorted(allowed_status)} 之一，当前 {expect!r}")
    keys = [item.get("key") for item in load_links()["links"]]
    for key in sorted({k for k in keys if keys.count(k) > 1}):
        problems.add("data/links.yaml", f"key 重复：{key}")


def check_oss_points_exist(problems: Problems) -> None:
    known = {p["id"] for p in iter_points(skip_missing=True)}
    for res in load_oss():
        for pid in res.get("points") or []:
            if pid not in known:
                problems.add(f"data/oss-resources.yaml :: {res.get('repo')}",
                             f"points 引用了不存在的知识点：{pid}")


def coverage_report(stages: list[dict]) -> list[str]:
    """生成覆盖情况文本。数字全部现算，不写死。"""
    index = load_index()
    lines = ["| 学段 | 学科数 | 知识点 | 其中主干 | 有视频 | 有开源资源 |",
             "| --- | --- | --- | --- | --- | --- |"]
    oss_points = {pid for r in load_oss() for pid in (r.get("points") or [])}
    total = core = vid = withres = 0
    for stage in stages:
        n = core_n = vid_n = res_n = 0
        for unit in stage["units"]:
            for p in unit.get("points") or []:
                n += 1
                core_n += 1 if p.get("core") else 0
                vid_n += 1 if (p.get("video") or {}).get("q") else 0
                res_n += 1 if p["id"] in oss_points else 0
        lines.append(f"| {stage['name']} | {len(stage['units'])} | {n} | {core_n} | {vid_n} | {res_n} |")
        total += n; core += core_n; vid += vid_n; withres += res_n
    lines.append(f"| **合计** | {len(index['subjects'])} | **{total}** | {core} | {vid} | {withres} |")
    return lines


# 本模块里所有以 check_ 开头的检查函数，按调用顺序。
#
# 这个清单不是给人看的文档，是给 tests/test_every_check_can_fail.py 用的断言：
# 它比对清单与模块里真实的 check_ 函数集合，两边不等就红。理由是
# CONTRIBUTING.md 那条"加了检查就要能说明它为什么能变红"——
# 新加一个检查却忘了给它写一条能弄红它的用例，会在那里被拦下，
# 而不是等到某天这个检查默默失效、没人发现。
ALL_CHECKS = (
    "check_index",
    "check_stage_files",
    "check_point",
    "check_against_registry",
    "check_claims",
    "check_percent_wording",
    "check_links_registry",
    "check_oss",
    "check_oss_points_exist",
)


def run_all_checks() -> tuple[Problems, dict, list[dict]]:
    """跑完全部检查并返回结果，不打印、不退出。

    单独抽出来是为了让测试能对着任意一棵目录树跑同一套逻辑。
    调用顺序有依赖：check_stage_files 需要 check_index 的返回值，
    check_against_registry 需要两者的返回值。
    """
    problems = Problems()
    index = check_index(problems)
    stages = check_stage_files(problems, index)
    check_against_registry(problems, stages, index)
    check_claims(problems)
    check_percent_wording(problems)
    check_links_registry(problems)
    check_oss(problems)
    check_oss_points_exist(problems)
    return problems, index, stages


def main() -> int:
    ap = argparse.ArgumentParser(description="校验 kine-learn 内容自洽性")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    problems, _index, stages = run_all_checks()

    points = iter_points(skip_missing=True)
    print(f"学段 {len(stages)} 个 | 学科单元 {sum(len(s['units']) for s in stages)} 个 | "
          f"知识点 {len(points)} 个 | 开源资源 {len(load_oss())} 条 | "
          f"外部链接 {len(link_entries())} 条")

    if args.verbose:
        for line in coverage_report(stages):
            print(line)

    if problems:
        print(f"\n发现 {len(problems.items)} 个问题：")
        for item in problems.items:
            print(f"  - {item}")
        return 1
    print("ok：全部检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
