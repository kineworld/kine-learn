"""链接检查的**判别规则**与检索链接的拼装。

链接检查最容易做成假检查，所以这个文件测的是判据本身，而不是"某条链接今天活着"。
判据错了，整份报告就在说谎，而且没人会再去读它。

核心规则只有一条：**dead 是一次指控。** 说一条链接失效，就意味着有人得去修它。
所以只有服务器明确说"没有"（404/410）才允许归 dead；连不上、被挡、没想到的
状态码，全都只能算"这次没验成"。把它写成 dead，CI 会变成随机红，
而随机红的检查等于没有检查。
"""

from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import _common  # noqa: E402
import check_links  # noqa: E402


class ClassifyTest(unittest.TestCase):
    def test_success_codes_are_verified(self):
        for code in (200, 201, 204, 301, 302, 307, 308):
            self.assertEqual(check_links.classify(code), "verified", f"HTTP {code}")

    def test_only_404_and_410_are_dead(self):
        self.assertEqual(check_links.classify(404), "dead")
        self.assertEqual(check_links.classify(410), "dead")

    def test_connection_failure_is_unreachable_never_dead(self):
        """本机到不了 ≠ 链接已死。混成一类，报告就在说谎。"""
        self.assertEqual(check_links.classify(None, "URLError"), "unreachable")
        self.assertEqual(check_links.classify(None, "timeout"), "unreachable")
        self.assertEqual(check_links.classify(None, "SSLError"), "unreachable")

    def test_unexpected_codes_are_never_dead(self):
        """400/405/451 这类"服务器在，但这次没给内容"不是失效。

        旧实现让它们落到兜底的 dead 上，等于把"没验成"说成"链接坏了"。
        误判的代价不对称：少报一条失效没人受伤，错报一条有人白跑一趟。
        """
        for code in (400, 401, 402, 403, 405, 418, 429, 451, 500, 502, 503, 504):
            self.assertEqual(check_links.classify(code), "blocked", f"HTTP {code}")

    def test_missing_code_and_missing_error_is_unreachable(self):
        self.assertEqual(check_links.classify(None), "unreachable")

    def test_dead_code_set_is_closed(self):
        """堵住"往里加状态码"这条改法：加之前先看上面那条代价不对称的理由。"""
        self.assertEqual(
            check_links.DEAD_CODES, {404, 410},
            "DEAD_CODES 是什么算失效的唯一定义。要改它，"
            "请同时改本文件和 docs/ 里对 dead 的解释。",
        )

    def test_every_code_yields_one_of_the_four_documented_states(self):
        """状态集合封闭，且与 validate.check_links_registry 允许的取值一致。"""
        allowed = {"verified", "dead", "unreachable", "blocked"}
        for code in [None, 200, 204, 301, 400, 401, 403, 404, 410, 418, 429, 451,
                     500, 503]:
            self.assertIn(check_links.classify(code), allowed, f"HTTP {code}")


class SearchUrlTest(unittest.TestCase):
    """检索式链接是"函数"不是"快照"：具体视频会下架改名，检索页不会。"""

    def test_query_is_percent_encoded(self):
        url = _common.search_url("https://search.bilibili.com/all?keyword={q}",
                                 "数学 入门")
        self.assertIn("%E6%95%B0%E5%AD%A6", url)
        self.assertNotIn(" ", url)

    def test_placeholder_is_replaced_everywhere(self):
        url = _common.search_url("https://example.test/{q}/x?q={q}", "a b")
        self.assertEqual(url, "https://example.test/a+b/x?q=a+b")

    def test_shipped_templates_expand_to_absolute_urls(self):
        """data/links.yaml 里的模板必须能拼出 http(s) 地址，否则登记无效。"""
        links = _common.load_links()
        self.assertTrue(links["search_templates"], "没有登记任何检索模板")
        for tpl in links["search_templates"]:
            self.assertIn("{q}", tpl["template"],
                          f"{tpl['key']} 的模板里没有 {{q}} 占位符，拼不出检索链接")
            url = _common.search_url(tpl["template"], "测试")
            self.assertTrue(url.startswith(("http://", "https://")),
                            f"{tpl['key']} 拼出来的不是绝对地址：{url}")
            self.assertNotIn("{q}", url)

    def test_curated_links_have_a_search_fallback_where_it_matters(self):
        """每个知识点都要有视频入口——要么登记了整站，要么能拼出检索页。

        这条在真实内容上跑：它保证"每个知识点都附带视频链接"这个需求
        不是写在文档里的一句话，而是脚本能验的事实。
        """
        templates = {t["key"] for t in _common.load_links()["search_templates"]}
        self.assertTrue(templates, "一个检索模板都没有，视频入口无从拼出")
        missing = []
        for point in _common.iter_points():
            video = point.get("video") or {}
            if not video.get("q"):
                missing.append(point["id"])
        self.assertEqual(missing, [], f"这些知识点没有 video.q：{missing[:10]}")


if __name__ == "__main__":
    unittest.main()
