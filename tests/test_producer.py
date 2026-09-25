"""生成侧的三条硬约束：不上网、可复现、写在被指定的地方。

docs/*.md 与 site/index.html 是**生成物**，但它们进了版本库。能这么做的唯一前提
是构建可复现：同一份源文件，任何机器上跑两次，产出逐字节相同。只要产物里混进一个
墙上时钟时间戳，"生成物是否与源文件同步"这条检查就会永远为红，
最后没人再看它——这是生成物进版本库最常见的死法。

另一条是 build.py 永不上网。它只读已落盘的数据，所以断网可构建，
也不会因为某个网站今天挂了而让 CI 变红。网络只发生在 check_links.py
与 fetch_oss.py 里，那两支只写 data/。这条边界用 ast 扫导入来钉住。
"""

from __future__ import annotations

import ast
import contextlib
import io
import pathlib
import re
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import _common  # noqa: E402
import build  # noqa: E402
import validate  # noqa: E402

REAL_ROOT = ROOT

# 会打开套接字或起子进程的模块。构建不应该碰其中任何一个。
NETWORK_OR_PROCESS = {
    "urllib", "http", "socket", "ssl", "requests", "httpx", "ftplib", "telnetlib",
    "smtplib", "subprocess", "asyncio",
}

GENERATED = ("primary.md", "middle.md", "high.md", "university.md", "language.md",
             "CATALOG.md", "STRANDS.md", "RESOURCES.md", "LINKS.md", "COVERAGE.md")

# 形如时间戳的字符串。产出里允许出现的时间戳，只允许是源数据里本来就有的
# （oss-verified.json 的 fetched_at、links-status.json 的 checked_at、
# 各仓库的 pushed_at / created_at）。多出来的只可能来自构建时刻。
TIMESTAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2})?")


def source_timestamps(root: pathlib.Path) -> set[str]:
    """收集源文件里出现过的时间戳字符串。"""
    found: set[str] = set()
    for base in ("curriculum", "data"):
        for path in (root / base).rglob("*"):
            if path.is_file():
                found.update(TIMESTAMP_RE.findall(path.read_text(encoding="utf-8")))
    return found


def imported_roots(source: str, filename: str) -> set[str]:
    """返回一份源码里出现的顶层模块名。"""
    roots: set[str] = set()
    for node in ast.walk(ast.parse(source, filename=filename)):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    return roots


class OfflineBoundaryTest(unittest.TestCase):
    def test_build_and_validate_never_reach_the_network(self):
        """把"构建永不上网"从注释变成一条会失败的检查。

        导入就有副作用，所以不需要真的调用什么——只要有人为了拿一个星数
        在 build.py 里写一行 urllib，这里就红。
        """
        for name in ("build.py", "validate.py"):
            source = (REAL_ROOT / "scripts" / name).read_text(encoding="utf-8")
            overlap = imported_roots(source, name) & NETWORK_OR_PROCESS
            self.assertEqual(
                overlap, set(),
                f"scripts/{name} 导入了 {sorted(overlap)}。构建与校验必须能断网跑完；"
                "需要联网的取数请放进 scripts/fetch_oss.py 或 scripts/check_links.py，"
                "它们只写 data/，不改正文。",
            )

    def test_network_lives_only_in_the_two_fetching_scripts(self):
        """反向确认边界还在：取数脚本该联网，构建脚本不该。"""
        for name in ("fetch_oss.py", "check_links.py"):
            source = (REAL_ROOT / "scripts" / name).read_text(encoding="utf-8")
            overlap = imported_roots(source, name) & NETWORK_OR_PROCESS
            self.assertTrue(
                overlap,
                f"scripts/{name} 不再导入任何联网模块。如果取数逻辑被搬走了，"
                "请一并更新本用例与 build.py 顶部的边界说明。",
            )


class BuildOutputTest(unittest.TestCase):
    """在临时目录里对**真实内容**构建，产出落在临时目录，真实仓库不动。"""

    def setUp(self):
        _common.set_root(REAL_ROOT)
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="kine-learn-build-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.addCleanup(_common.set_root, REAL_ROOT)
        for rel in ("curriculum", "data"):
            shutil.copytree(REAL_ROOT / rel, self.tmp / rel)
        _common.set_root(self.tmp)

    def build_quietly(self) -> str:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = build.main()
        self.assertEqual(code, 0, "build.main() 返回非零")
        return out.getvalue()

    def any_generated_file(self) -> pathlib.Path:
        self.build_quietly()
        return self.tmp / "site" / "index.html"

    def snapshot(self) -> dict[str, bytes]:
        files = {}
        for rel in ("docs", "site"):
            for path in sorted((self.tmp / rel).rglob("*")):
                if path.is_file():
                    files[path.relative_to(self.tmp).as_posix()] = path.read_bytes()
        return files

    # ---------------------------------------------------------------- 用例
    def test_two_runs_are_byte_identical(self):
        """可复现性。产物进版本库、CI 又要比对 diff，这条不成立整套就崩。"""
        self.build_quietly()
        first = self.snapshot()
        self.build_quietly()
        second = self.snapshot()

        self.assertEqual(sorted(first), sorted(second), "两次构建产生的文件列表不同")
        drifted = [k for k in first if first[k] != second[k]]
        self.assertEqual(
            drifted, [],
            "两次构建的产出不同：产物里混进了每次都变的内容（构建时间、随机序、"
            "字典遍历序）。生成物进版本库的前提就是它可复现。",
        )

    def test_no_timestamp_comes_from_the_build_clock(self):
        """产出里每个时间戳都必须能在源数据里找到出处。

        比"扫一遍 2026-xx-xx 就算违规"准确：数据自带的戳（fetched_at /
        checked_at / pushed_at）本来就该显示，而构建时刻不该。多出来的
        时间戳只可能来自构建时刻，那会让每次构建都产生 diff。
        """
        self.build_quietly()
        known = source_timestamps(self.tmp)
        self.assertTrue(known, "源数据里一个时间戳都没有，这条检查失去了比对基准")
        for rel, data in self.snapshot().items():
            unknown = sorted(set(TIMESTAMP_RE.findall(data.decode("utf-8"))) - known)
            self.assertEqual(
                unknown, [],
                f"{rel} 里出现了源数据中没有的时间戳：{unknown}。"
                "它只能来自构建时刻，也就是墙上时钟。要展示时间就展示数据文件"
                "自带的戳——它们是源的一部分，改一次才变一次。",
            )

    def test_html_payload_is_parseable_json(self):
        """载荷放在 <script type=\"application/json\"> 里，转义之后仍要是合法 JSON。

        这一条不只是测转义：它顺带把"载荷结构变了但页面没跟上"也一起拦住。
        """
        import json
        html = self.any_generated_file().read_text(encoding="utf-8")
        marker = 'id="data">'
        start = html.find(marker)
        self.assertGreater(start, 0, "页面里找不到数据载荷，模板结构可能变了")
        start += len(marker)
        payload = html[start:html.index("</script>", start)]
        self.assertNotIn("</", payload, "载荷里的 </ 没有转义，会提前闭合 script")
        data = json.loads(payload)
        self.assertIn("points", data)
        self.assertTrue(data["points"], "载荷里的知识点是空的")
        self.assertIn("kid", data["points"][0], "载荷里缺一年级版讲解")

    def test_embed_escapes_end_tags_without_corrupting_the_json(self):
        """直接测转义函数：写错了会静默白屏，这种失败最需要一条会变红的用例。"""
        import json
        risky = {"kid": "如果写成 </script> 就会白屏", "nested": ["a</b>c"]}
        embedded = build.embed(risky)
        self.assertNotIn("</", embedded)
        self.assertIn("<\\/script>", embedded)
        self.assertEqual(json.loads(embedded), risky,
                         "转义之后 JSON 必须还能解回原值")

    def test_generation_writes_into_the_injected_root_only(self):
        """set_root 若只改了一半路径，构建会静默改写真实仓库的产物。"""
        real_docs = (REAL_ROOT / "docs" / "primary.md").read_bytes()
        real_site = (REAL_ROOT / "site" / "index.html").read_bytes()

        self.build_quietly()

        for name in GENERATED:
            self.assertTrue((self.tmp / "docs" / name).exists(), f"docs/{name} 没生成")
        self.assertTrue((self.tmp / "site" / "index.html").exists())
        self.assertEqual((REAL_ROOT / "docs" / "primary.md").read_bytes(), real_docs,
                         "构建改写了真实仓库的 docs/primary.md，路径没有跟着 set_root 走")
        self.assertEqual((REAL_ROOT / "site" / "index.html").read_bytes(), real_site,
                         "构建改写了真实仓库的 site/index.html，路径没有跟着 set_root 走")

    def test_timestamps_shown_come_from_data_files_not_the_clock(self):
        """页面要显示时间，只允许显示数据文件自己的戳。

        这条与上面的"没有墙上时钟"互补：前者禁止构建时刻，后者保证
        展示的戳确实来自 data/，而不是随便一个字符串。
        """
        html = self.any_generated_file().read_text(encoding="utf-8")
        oss_meta = _common.oss_verified_meta().get("fetched_at")
        links_meta = _common.link_status_meta().get("checked_at")
        self.assertIsNotNone(oss_meta, "data/oss-verified.json 里没有 fetched_at")
        self.assertIn(oss_meta, html, "页面里没有出现 oss-verified.json 的 fetched_at")
        if links_meta:
            self.assertIn(links_meta, html, "页面里没有出现 links-status.json 的 checked_at")

    def test_site_is_a_single_self_contained_file(self):
        """站点必须单文件、离线可用。

        README 与 ROADMAP 都写着"单文件、离线可用"。没有这条用例，那句话就是
        一句没人验过的声明——某天有人为了图省事加一行 CDN 字体，谁也不会发现，
        直到有人断网打开页面。
        """
        html = self.any_generated_file().read_text(encoding="utf-8")
        for pattern, why in (
            (r"<link[^>]+href=[\"']https?://", "引用了外部样式表或图标"),
            (r"<script[^>]+src=[\"']https?://", "引用了外部脚本"),
            (r"@import\s+url\(", "用了 CSS @import"),
            (r"url\(\s*[\"']?https?://", "样式里引用了外部资源"),
        ):
            match = re.search(pattern, html)
            self.assertIsNone(match, f"站点{why}（{match and match.group(0)}），离线打开会残缺")
        for token, why in (("fetch(", "会在打开时发网络请求"),
                           ("XMLHttpRequest", "会在打开时发网络请求")):
            self.assertNotIn(token, html, f"站点{why}，离线打开会卡住或报错")

    def test_generated_docs_have_no_placeholder_left(self):
        """渲染函数少传一个参数，留下一个花括号占位，肉眼很难发现。"""
        self.build_quietly()
        for name in GENERATED:
            text = (self.tmp / "docs" / name).read_text(encoding="utf-8")
            self.assertNotIn("__DATA__", text, f"docs/{name} 残留模板占位符")
            self.assertGreater(len(text), 200, f"docs/{name} 几乎是空的")


class ShippedContentTest(unittest.TestCase):
    """真实内容必须过校验。这是最有用的那一条：改坏任何一个 YAML 都会在这里红。"""

    def setUp(self):
        _common.set_root(REAL_ROOT)

    def test_shipped_content_has_no_problems(self):
        problems, index, stages = validate.run_all_checks()
        self.assertEqual(
            problems.items, [],
            "仓库里的内容没有通过自洽性检查。修法看每行前缀的文件名。",
        )
        self.assertTrue(index["stages"], "总表里没有学段")
        self.assertTrue(stages, "一个学段文件都没读到")

    def test_every_point_has_a_nonempty_kid_sentence(self):
        """一年级版是这套材料的入口。它空了，整套就变成给已有基础的人写的。"""
        empty = [p["id"] for p in _common.iter_points() if not (p.get("kid") or "").strip()]
        self.assertEqual(empty, [], f"这些知识点没有一年级版讲解：{empty[:10]}")

    def test_every_point_connects_to_the_world_model(self):
        """model 字段回答"它在理解世界如何运作中担任什么角色"，是这套材料的主线。"""
        missing = [p["id"] for p in _common.iter_points() if not (p.get("model") or "").strip()]
        self.assertEqual(missing, [], f"这些知识点没有与世界模型的连接：{missing[:10]}")


if __name__ == "__main__":
    unittest.main()
