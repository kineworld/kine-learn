"""检查 data/links.yaml 里的外部链接是否活着。

这套检查的核心是一组**判别规则**，因为"链接检查"最容易做成假检查：

  1. 本机网络到不了 ≠ 链接已死。YouTube、BBC、剑桥词典在部分网络环境下
     一律超时或返回 000，如果把这种结果写成"失效"，报告就是在说谎，
     而且下次没人会看它。所以状态必须分开：dead（明确 404/410）与
     unreachable（本机到不了，需要换个网络复核）。
  2. 被墙/被 WAF 挡（403/429/5xx）也不是 dead。它只说明自动检查无效，
     不代表读者打不开。
  3. 只有 dead 会让退出码非零。把网络抖动当失败，CI 会变成"随机红"，
     随机红的检查等于没有检查。

产出：data/links-status.json，供 build.py 渲染成 docs/LINKS.md。
网络只发生在这一支，构建（build.py）永不上网。
"""

from __future__ import annotations

import argparse
import pathlib
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _common  # noqa: E402
from _common import (  # noqa: E402
    link_status, load_links, search_url, write_json,
)

# LINKS_STATUS_FILE 不在导入列表里，见 build.py 顶部同一条注释：
# 导入时固化的路径会绕过 _common.set_root()。

DEAD_CODES = {404, 410}
UA = "Mozilla/5.0 (compatible; kine-learn-linkcheck/1.0)"


def classify(code, error=None) -> str:
    """把一次探测结果归成四类。判据故意收得很窄，因为误判的代价不对称。

    - dead 是一次**指控**：说一条链接失效，就意味着有人得去修它。
      所以只有 404 / 410 这种"服务器明确说没有"才归 dead。
    - 其余一切都归 blocked / unreachable，含义是"这次没验成"，
      而不是"链接坏了"：连不上（本机网络到不了）、被 WAF 挡（403/429/5xx），
      以及任何没想到的状态码（400/405/451……）都算进来。

    把网络抖动或未预期状态码写成 dead，CI 就会变成随机红，
    而随机红的检查等于没有检查——这正是这个文件要防的事。
    """
    if error is not None:
        return "unreachable"
    if code is None:
        return "unreachable"
    if code in DEAD_CODES:
        return "dead"
    if 200 <= code < 400:
        return "verified"
    return "blocked"


def probe(url: str, timeout: float) -> dict:
    request = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    })
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"code": response.status, "final_url": response.geturl()}
    except urllib.error.HTTPError as error:
        return {"code": error.code, "final_url": None}
    except Exception as error:
        return {"code": None, "final_url": None, "error": type(error).__name__}


def main() -> int:
    ap = argparse.ArgumentParser(description="检查外部链接状态")
    ap.add_argument("--timeout", type=float, default=12.0)
    ap.add_argument("--only", default=None, help="只看 key 含该子串的条目")
    ap.add_argument("--sample-query", default="数学 入门",
                    help="给检索模板用的样例关键词")
    args = ap.parse_args()

    links = load_links()
    previous = link_status()
    entries: dict[str, dict] = {}

    targets = links["links"]
    if args.only:
        targets = [item for item in targets if args.only in item["key"]]

    print(f"检查 {len(targets)} 条登记链接（超时 {args.timeout}s，dead 判定为 404/410）")
    for item in targets:
        result = probe(item["url"], args.timeout)
        status = classify(result["code"], result.get("error"))
        entries[item["key"]] = {
            "url": item["url"],
            "title": item["title"],
            "status": status,
            "code": result["code"],
            "final_url": result.get("final_url"),
            "note": result.get("error"),
            "expect": item.get("expect"),
        }
        mark = ""
        if item.get("expect"):
            mark = (" ← 自查通过" if item["expect"] == status
                    else f" ← 自查失败（应为 {item['expect']}）")
        print(f"  {status:12} {str(result['code']):>5}  {item['key']:22} {item['url']}{mark}")

    print(f"\n检查 {len(links['search_templates'])} 个检索模板（拼上样例关键词后测通）")
    for tpl in links["search_templates"]:
        url = search_url(tpl["template"], args.sample_query)
        result = probe(url, args.timeout)
        status = classify(result["code"], result.get("error"))
        entries["template:" + tpl["key"]] = {
            "url": url,
            "title": tpl["title"],
            "status": status,
            "code": result["code"],
            "final_url": result.get("final_url"),
            "note": f"模板 {tpl['template']} 的样例查询",
        }
        print(f"  {status:12} {str(result['code']):>5}  {tpl['key']:22} {url}")

    for key, value in previous.items():
        entries.setdefault(key, value)

    write_json(_common.LINKS_STATUS_FILE, {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "note": ("unreachable / blocked 只表示本机网络到不了，不表示链接失效。"
                 "只有 dead（404/410）需要修。"),
        "sample_query": args.sample_query,
        "count": len(entries),
        "entries": entries,
    })

    dead = [k for k, v in entries.items() if v.get("status") == "dead"]
    unreachable = [k for k, v in entries.items() if v.get("status") == "unreachable"]
    blocked = [k for k, v in entries.items() if v.get("status") == "blocked"]
    verified = [k for k, v in entries.items() if v.get("status") == "verified"]

    # 自查条目是唯一会被预期为 dead 的东西。它反过来证明这个脚本不是永远说"通过"。
    selftest_failed = [k for k, v in entries.items()
                       if v.get("expect") and v["expect"] != v.get("status")]
    expected_dead = {k for k, v in entries.items() if v.get("expect") == "dead"}
    unexpected_dead = [k for k in dead if k not in expected_dead]

    print(f"\nverified={len(verified)} dead={len(dead)} "
          f"unreachable={len(unreachable)} blocked={len(blocked)}")
    if unreachable:
        print("  本机到不了（不是失效）：" + "、".join(sorted(unreachable)))
    if blocked:
        print("  被挡（不是失效）：" + "、".join(sorted(blocked)))
    if expected_dead:
        print("  预期失效（自查用）：" + "、".join(sorted(expected_dead)))

    if selftest_failed:
        print("\n自查失败，链接分类器可能坏了：")
        for key in selftest_failed:
            v = entries[key]
            print(f"  - {key} 期望 {v['expect']}，实际 {v.get('status')}（HTTP {v.get('code')}）")
        print("  修 check_links.py 的 classify() 之前，这份报告里的其它状态都不可信。")
        return 1

    if unexpected_dead:
        print("\n以下链接明确失效，必须修：")
        for key in unexpected_dead:
            print(f"  - {key} {entries[key]['url']} ({entries[key]['code']})")
        return 1

    print("ok：没有计划外的失效链接，且自查条目按预期被判为 dead")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
