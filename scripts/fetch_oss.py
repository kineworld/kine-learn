"""从 GitHub API 拉取开源资源的真实元数据。

为什么必须由脚本拉、不能手打：
  星数、许可证、最后提交时间每天都在变。手打的数字会在几周后骗人，
  而"骗人的数字"比"没有数字"更糟——读者无法分辨哪一行是实测、哪一行是印象。
  本组织 CONTRIBUTING.md 第 1 条就是这个意思：没有产物的主张不成立。

产出：data/oss-verified.json
  { fetched_at, source, entries: { "owner/name": {ok, full_name, stars, license,
    pushed_at, archived, size_kb, description, default_branch, code} } }

用法：
  python scripts/fetch_oss.py                 # 全量刷新
  python scripts/fetch_oss.py --only QGIS     # 只查名字里含 QGIS 的
  python scripts/fetch_oss.py --offline       # 不联网，只报告现有文件的状态

令牌：优先用环境变量 GITHUB_TOKEN / GH_TOKEN。匿名调用每小时 60 次，
本仓库约 55 条资源，赶上限流就会失败——所以匿名能跑通不代表下一次也能。
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _common  # noqa: E402
from _common import (  # noqa: E402
    load_oss, oss_verified, read_json, write_json,
)

# OSS_VERIFIED_FILE 不在导入列表里，见 build.py 顶部同一条注释：
# 导入时固化的路径会绕过 _common.set_root()。

API = "https://api.github.com/repos/"
TIMEOUT = 25


def token() -> str | None:
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(name)
        if value and value.strip():
            return value.strip()
    return None


def probe(repo: str, tok: str | None) -> dict:
    headers = {
        "User-Agent": "kine-learn-fetch-oss",
        "Accept": "application/vnd.github+json",
    }
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    request = urllib.request.Request(API + repo, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        return {"ok": False, "code": error.code}
    except Exception as error:  # 超时、DNS、代理问题都归到这里
        return {"ok": False, "code": str(error)}

    license_info = data.get("license") or {}
    return {
        "ok": True,
        "full_name": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "license": license_info.get("spdx_id"),
        "license_name": license_info.get("name"),
        "pushed_at": (data.get("pushed_at") or "")[:10],
        "created_at": (data.get("created_at") or "")[:10],
        "archived": bool(data.get("archived")),
        "size_kb": data.get("size"),
        "open_issues": data.get("open_issues_count"),
        "default_branch": data.get("default_branch"),
        "description": (data.get("description") or "").strip(),
        "html_url": data.get("html_url"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="刷新开源资源的 API 元数据")
    ap.add_argument("--only", default=None, help="只处理名字里含该子串的仓库")
    ap.add_argument("--offline", action="store_true", help="不联网，仅汇总已落盘数据")
    args = ap.parse_args()

    repos = [r["repo"] for r in load_oss()]
    if args.only:
        repos = [r for r in repos if args.only.lower() in r.lower()]
    if not repos:
        print("没有匹配的仓库")
        return 1

    previous = oss_verified()
    entries: dict[str, dict] = {}

    if args.offline:
        kept = 0
        for repo in repos:
            meta = previous.get(repo.lower())
            if meta:
                entries[repo] = meta
                kept += 1
        print(f"离线模式：沿用已落盘数据 {kept}/{len(repos)} 条")
    else:
        tok = token()
        if not tok:
            print("警告：未设置 GITHUB_TOKEN，使用匿名调用（每小时约 60 次限额）")
        for repo in repos:
            meta = probe(repo, tok)
            entries[repo] = meta
            if meta.get("ok"):
                lic = meta.get("license") or "NO-LICENSE"
                print(f"  ok  {meta['stars']:>7}★ {repo:45} {str(lic):14} "
                      f"push={meta['pushed_at']} arch={meta['archived']}")
            else:
                print(f"  MISS {repo:45} code={meta.get('code')}")

    payload = {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "GitHub REST API v3 · GET /repos/{owner}/{repo}",
        "count": len(entries),
        "entries": entries,
    }
    write_json(_common.OSS_VERIFIED_FILE, payload)

    missing = [r for r, m in entries.items() if not m.get("ok")]
    archived = [r for r, m in entries.items() if m.get("ok") and m.get("archived")]
    nolicense = [r for r, m in entries.items()
                 if m.get("ok") and not m.get("license")]
    print(f"\n写入 {_common.OSS_VERIFIED_FILE.name}："
          f"{len(entries)} 条，其中无许可证 {len(nolicense)} 条，已归档 {len(archived)} 条")
    if nolicense:
        print("  无许可证：" + "、".join(nolicense))
    if archived:
        print("  已归档：" + "、".join(archived))

    if missing:
        print(f"\n以下 {len(missing)} 个仓库 API 查不到，必须修掉（要么改名，要么从索引里删）：")
        for repo in missing:
            print(f"  - {repo} -> {entries[repo].get('code')}")
        return 1
    print("ok：所有仓库都能在 GitHub 上查到")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
