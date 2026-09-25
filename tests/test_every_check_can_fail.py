"""证明 scripts/validate.py 里的每条检查都能变红。

为什么值得单独写一个文件：一个永远通过的检查比没有检查更糟。它给出"已经验过
了"的错觉，还把真正的缺陷挡在视野之外。组织 CONTRIBUTING.md 把这条写成流程要求——

    If you add a self-check or test, make sure it can fail. Before submitting,
    ask: *what defect would turn this red?* If you cannot answer, the check is
    decorative — remove it.

做法：在临时目录里搭一棵最小但完整的目录树（总表 + 一个学段 + 一个学科 + 一个
知识点 + 一条链接 + 一条开源资源），然后每个用例只改坏一处，断言那一条检查确实
报出问题。`_common.set_root()` 是这套测试能存在的前提——校验逻辑若只能对着真实
仓库跑，"能不能弄红"就无从验证。

两条自己给自己上的箍：

  1. `test_baseline_tree_is_clean`：未改造的基线必须零问题。基线本来就红的话，
     后面每条"能变红"的用例都是假阳性，什么也证明不了。
  2. `test_every_check_is_covered`：模块里的 check_ 函数集合、validate.ALL_CHECKS、
     本文件的 COVERED 三者的键集合必须完全相等。新加一条检查却忘了给它写
     "能弄红"的用例，会在那里被拦下——而不是等它某天默默失效。
"""

from __future__ import annotations

import copy
import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import _common  # noqa: E402
import validate  # noqa: E402

REAL_ROOT = ROOT


# ---------------------------------------------------------------- 最小基线内容
INDEX = {
    "version": 1,
    "updated": "2026-09-25",
    "stages": [
        {"id": "primary", "name": "小学", "file": "primary.yaml",
         "anchor": "从一个苹果开始"},
    ],
    "subjects": {"math": {"name": "数学", "strand_hint": "number"}},
    "strands": [{"id": "number", "name": "数量", "question": "有多少个？"}],
}

POINT = {
    "id": "pri-math-01",
    "title": "数数",
    "grade": "一年级",
    "core": True,
    "strand": "number",
    "kid": "一个一个地数，数到十。",
    "principle": "数量是可以被数出来的。",
    "model": "能数出来，就能比较多少。",
    "exit": "能从一数到十，并说出哪个多。",
    "video": {"q": "一年级 数数", "c": ["smartedu"]},
}

PRIMARY = {
    "units": [{
        "subject_id": "math",
        "why": "数学是描述世界的语言。",
        "points": [copy.deepcopy(POINT)],
    }],
}

LINKS = {
    "links": [
        {"key": "smartedu", "title": "国家中小学智慧教育平台",
         "url": "https://basic.smartedu.cn/", "platform": "smartedu", "lang": "zh",
         "what": "官方课程与教材。", "use_for": ["video"]},
        {"key": "link-check-selftest", "title": "自查条目（故意指向不存在的仓库）",
         "url": "https://api.github.com/repos/kineworld/kine-learn-selftest-xyz",
         "platform": "none", "lang": "en",
         "what": "它应该返回 404，用来证明链接检查器不是永远说通过。",
         "expect": "dead"},
    ],
    "search_templates": [
        {"key": "bilibili", "title": "B 站检索",
         "template": "https://search.bilibili.com/all?keyword={q}"},
    ],
}

OSS = {
    "resources": [{
        "repo": "example/demo",
        "title": "演示项目",
        "lang": "zh",
        "kind": "tutorial",
        "points": ["pri-math-01"],
        "what": "只用来做测试的演示项目。",
        "how": "读一遍它的 README。",
        "caution": "它不是真实推荐。",
    }],
}

OSS_VERIFIED = {
    "fetched_at": "2026-09-25T00:00:00Z",
    "source": "GitHub REST API v3",
    "entries": {"example/demo": {
        "ok": True, "full_name": "example/demo", "stars": 3, "license": "MIT",
    }},
}

README = "# 测试用说明\n\n这个文件只是给措辞检查一个可以扫的对象。\n"

ROADMAP = "# 测试用路线图\n\n只描述阶段，不写任何承诺句。\n"

# 每条检查 → 让它变红的那个用例名。test_every_check_is_covered 会校验这张表。
COVERED = {
    "check_index": "test_index_without_strands_is_rejected",
    "check_stage_files": "test_undeclared_stage_file_is_rejected",
    "check_point": "test_point_without_model_is_rejected",
    "check_against_registry": "test_duplicate_point_id_is_rejected",
    "check_claims": "test_guarantee_wording_is_rejected",
    "check_percent_wording": "test_unqualified_top_percent_line_is_rejected",
    "check_links_registry": "test_non_http_link_is_rejected",
    "check_oss": "test_oss_kind_outside_the_allowed_set_is_rejected",
    "check_oss_points_exist": "test_oss_point_reference_that_does_not_exist_is_rejected",
}


class TreeCase(unittest.TestCase):
    """每个用例一棵干净的临时目录树，跑完恢复 _common 的路径。"""

    def setUp(self):
        # 兜底：上一个用例若中途炸在恢复之前，这里先把路径掰回真实仓库。
        _common.set_root(REAL_ROOT)
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="kine-learn-validate-"))
        # cleanup 是后进先出：先 set_root 回真实仓库，再删临时目录。
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.addCleanup(_common.set_root, REAL_ROOT)
        self.write_base()

    # ------------------------------------------------------------ 写文件
    def write_yaml(self, rel: str, obj, root: pathlib.Path | None = None) -> None:
        import yaml
        path = (root or self.tmp) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(obj, allow_unicode=True, sort_keys=False),
            encoding="utf-8", newline="\n",
        )

    def write_json(self, rel: str, obj) -> None:
        import json
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=1),
                        encoding="utf-8", newline="\n")

    def write_text(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def write_base(self) -> None:
        self.write_yaml("curriculum/_index.yaml", copy.deepcopy(INDEX))
        self.write_yaml("curriculum/primary.yaml", copy.deepcopy(PRIMARY))
        self.write_yaml("data/links.yaml", copy.deepcopy(LINKS))
        self.write_yaml("data/oss-resources.yaml", copy.deepcopy(OSS))
        self.write_json("data/oss-verified.json", copy.deepcopy(OSS_VERIFIED))
        self.write_json("data/links-status.json", {"checked_at": None, "entries": {}})
        self.write_text("README.md", README)
        self.write_text("ROADMAP.md", ROADMAP)

    # ------------------------------------------------------------ 跑检查
    def problems(self) -> list[str]:
        _common.set_root(self.tmp)
        problems, _index, _stages = validate.run_all_checks()
        return list(problems.items)

    def assertProblem(self, needle: str) -> list[str]:
        items = self.problems()
        hits = [i for i in items if needle in i]
        self.assertTrue(
            hits, f"预期出现含「{needle}」的问题，实际只有：{items or '（零问题）'}"
        )
        return items


class BaselineTest(TreeCase):
    """基线是这套测试的地基：它必须干净。"""

    def test_baseline_tree_is_clean(self):
        items = self.problems()
        self.assertEqual(
            items, [],
            "最小基线目录树本身就有问题，那么其它用例的「变红」全是假阳性。"
            "先把基线修干净，再谈检查能不能失败。",
        )

    def test_set_root_redirects_every_read_path(self):
        """set_root 若只改了一半路径，下面的用例会静默地检查真实仓库。"""
        _common.set_root(self.tmp)
        for name in ("ROOT", "CURRICULUM_DIR", "DATA_DIR", "DOCS_DIR", "SITE_DIR",
                     "INDEX_FILE", "LINKS_FILE", "OSS_FILE", "OSS_VERIFIED_FILE",
                     "LINKS_STATUS_FILE"):
            path = pathlib.Path(getattr(_common, name))
            self.assertTrue(
                path == self.tmp or self.tmp in path.parents,
                f"_common.{name} 没有跟着 set_root 走：{path}",
            )

    def test_caches_are_invalidated_when_the_root_changes(self):
        """解析缓存必须跟着 set_root 作废。

        _common 会缓存已解析的 YAML（否则单次构建要 20 秒）。缓存不清的表现是
        "换个目录后读到上一棵树的内容"，也就是测试偶发失败——所有失败里最难查的
        一种。所以宁可单写一条用例盯着它。
        """
        _common.set_root(self.tmp)
        self.assertIn("smartedu", _common.link_entries())

        other = pathlib.Path(tempfile.mkdtemp(prefix="kine-learn-second-"))
        self.addCleanup(shutil.rmtree, other, ignore_errors=True)
        links = copy.deepcopy(LINKS)
        links["links"] = [dict(links["links"][0], key="other-platform", title="另一个平台")]
        self.write_yaml("data/links.yaml", links, root=other)

        _common.set_root(other)
        self.assertNotIn("smartedu", _common.link_entries(),
                         "换根目录后仍读到上一棵树的链接，缓存没有作废")
        self.assertIn("other-platform", _common.link_entries())

    def test_baseline_is_actually_read_from_the_temp_tree(self):
        """反向确认：往临时树里塞一条链接，检查必须看到它。

        没有这一条，set_root 万一是个空操作，上面所有用例都会对着真实仓库跑，
        而真实仓库恰好是干净的——于是整套测试全绿，什么也没验。
        """
        links = copy.deepcopy(LINKS)
        links["links"].append({
            "key": "ghost", "title": "幽灵链接", "url": "ftp://ghost.example/",
            "platform": "none", "lang": "en", "what": "只为制造一个必然报错。",
        })
        self.write_yaml("data/links.yaml", links)
        self.assertProblem("url 必须是 http(s) 绝对地址")


class IndexCheckTest(TreeCase):
    def test_index_without_strands_is_rejected(self):
        index = copy.deepcopy(INDEX)
        index["strands"] = []
        self.write_yaml("curriculum/_index.yaml", index)
        self.assertProblem("缺少或为空：strands")

    def test_index_with_unregistered_stage_is_rejected(self):
        """学段没在 STAGE_PREFIX 登记 → 知识点 id 前缀就没法校验。"""
        index = copy.deepcopy(INDEX)
        index["stages"].append({"id": "kindergarten", "name": "幼儿园",
                                "file": "kindergarten.yaml", "anchor": "还没有"})
        self.write_yaml("curriculum/_index.yaml", index)
        self.write_yaml("curriculum/kindergarten.yaml", {"units": []})
        self.assertProblem("未在 STAGE_PREFIX 登记")


class StageFileCheckTest(TreeCase):
    def test_undeclared_stage_file_is_rejected(self):
        self.write_yaml("curriculum/orphan.yaml", {"units": []})
        self.assertProblem("文件存在但总表未登记")

    def test_declared_stage_file_that_is_missing_is_rejected(self):
        index = copy.deepcopy(INDEX)
        index["stages"][0]["file"] = "ghost.yaml"
        self.write_yaml("curriculum/_index.yaml", index)
        (self.tmp / "curriculum" / "primary.yaml").unlink()
        self.assertProblem("文件不存在")

    def test_unit_without_why_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["why"] = ""
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("缺少 why（为什么学这一科）")

    def test_unit_without_points_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"] = []
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("没有任何知识点")

    def test_unit_with_unregistered_subject_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["subject_id"] = "alchemy"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("学科 id 未在总表登记")


class PointCheckTest(TreeCase):
    def test_point_without_model_is_rejected(self):
        """model 字段是"这个知识点在理解世界运作中担任什么角色"，最容易漏写。"""
        primary = copy.deepcopy(PRIMARY)
        del primary["units"][0]["points"][0]["model"]
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("缺少或为空：model")

    def test_point_with_wrong_id_prefix_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["id"] = "mid-math-01"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("id 前缀应为 pri-")

    def test_point_without_video_query_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["video"] = {"c": ["smartedu"]}
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("缺少 video.q")

    def test_point_referencing_unknown_link_key_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["video"]["c"] = ["nonexistent-platform"]
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("data/links.yaml 里不存在的 key")

    def test_point_with_unregistered_strand_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["strand"] = "vibes"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("主线未登记")


class RegistryCheckTest(TreeCase):
    def test_duplicate_point_id_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"].append(copy.deepcopy(POINT))
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("知识点 id 重复：pri-math-01")

    def test_prereq_pointing_nowhere_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["prereq"] = ["pri-math-99"]
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("前置知识点不存在：pri-math-99")

    def test_prereq_pointing_at_itself_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["prereq"] = ["pri-math-01"]
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("前置指向自己")

    def test_subject_registered_but_never_used_is_rejected(self):
        index = copy.deepcopy(INDEX)
        index["subjects"]["physics"] = {"name": "物理", "strand_hint": "energy"}
        self.write_yaml("curriculum/_index.yaml", index)
        self.assertProblem("在总表登记但没有任何学段使用它")


class ClaimWordingTest(TreeCase):
    def test_guarantee_wording_is_rejected(self):
        """「保证学会」是本组织的措辞红线：有这句就没有读者能分辨哪句有证据。"""
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["exit"] = "保证学会数到十。"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("命中措辞红线（保证性承诺）")

    def test_ranking_claim_is_rejected(self):
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["principle"] = "读过之后就是全球第一的理解力。"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertProblem("命中措辞红线（排名或最强声明）")

    def test_plain_sentence_with_characters_baozheng_is_accepted(self):
        """「保证」二字本身不是红线——「不能保证」是合法且必要的表述。

        没有这一条对照，正则写成 `保证` 也能让上面那条通过，
        而那样会把所有诚实的限定句一起干掉。
        """
        primary = copy.deepcopy(PRIMARY)
        primary["units"][0]["points"][0]["exit"] = "本材料不能保证你掌握，只说明出口标准。"
        self.write_yaml("curriculum/primary.yaml", primary)
        self.assertEqual(self.problems(), [])

    def test_guarantee_wording_in_oss_caution_is_rejected(self):
        oss = copy.deepcopy(OSS)
        oss["resources"][0]["caution"] = "这个项目保证学会编程。"
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("data/oss-resources.yaml :: example/demo.caution")


class PercentWordingTest(TreeCase):
    def test_unqualified_top_percent_line_is_rejected(self):
        """「前 1%」是用户明确提出的目标措辞，也是最容易被改成承诺句的地方。"""
        self.write_text("README.md", "# 标题\n\n学完可达到全球前 1% 的认知水平。\n")
        self.assertProblem("出现「前 1%」但同句没有 目标/不是承诺 之类限定语")

    def test_qualified_top_percent_line_is_accepted(self):
        """对照：同句带限定语时放行，否则这条检查退化成「禁止提起前 1%」。

        用的正是最初把这条检查弄红的那句写法——"是方向，不是它的承诺"。
        只认字面的"不是承诺"是不够的：限定语的具体措辞不该由检查来规定，
        该被规定的是"有没有在撇清"。
        """
        self.write_text("README.md", "# 标题\n\n全球前 1% 是方向，不是它的承诺。\n")
        self.assertEqual(self.problems(), [])

    def test_percent_rule_also_scans_roadmap(self):
        self.write_text("ROADMAP.md", "# 路线图\n\n一直走到前 1%。\n")
        self.assertProblem("ROADMAP.md:3")

    def test_missing_percent_files_are_skipped_not_crashed(self):
        (self.tmp / "README.md").unlink()
        (self.tmp / "ROADMAP.md").unlink()
        self.assertEqual(self.problems(), [])


class LinksRegistryTest(TreeCase):
    def test_non_http_link_is_rejected(self):
        links = copy.deepcopy(LINKS)
        links["links"][0]["url"] = "ftp://basic.smartedu.cn/"
        self.write_yaml("data/links.yaml", links)
        self.assertProblem("url 必须是 http(s) 绝对地址")

    def test_duplicate_link_key_is_rejected(self):
        links = copy.deepcopy(LINKS)
        links["links"].append(copy.deepcopy(links["links"][0]))
        self.write_yaml("data/links.yaml", links)
        self.assertProblem("key 重复：smartedu")

    def test_unknown_expect_value_is_rejected(self):
        """expect 是自查条目的判据，取值写错等于自查失效，必须拦住。"""
        links = copy.deepcopy(LINKS)
        links["links"][1]["expect"] = "probably-fine"
        self.write_yaml("data/links.yaml", links)
        self.assertProblem("expect 取值必须是")

    def test_empty_search_template_is_rejected(self):
        links = copy.deepcopy(LINKS)
        links["links"][1]["title"] = ""
        self.write_yaml("data/links.yaml", links)
        self.assertProblem("缺少：title")


class OssRegistryTest(TreeCase):
    def test_oss_kind_outside_the_allowed_set_is_rejected(self):
        oss = copy.deepcopy(OSS)
        oss["resources"][0]["kind"] = "awesome-list"
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("kind 不在允许集合内")

    def test_oss_repo_without_owner_is_rejected(self):
        oss = copy.deepcopy(OSS)
        oss["resources"][0]["repo"] = "no-slash-here"
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("repo 必须是 owner/name 形式")

    def test_oss_repo_case_drift_from_api_is_rejected(self):
        """GitHub 的 owner/repo 不区分大小写，但截图和引用要能和 API 对上。"""
        oss = copy.deepcopy(OSS)
        oss["resources"][0]["repo"] = "Example/Demo"
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("大小写与 API 返回的 full_name 不一致，应为 example/demo")

    def test_oss_repo_the_api_cannot_find_is_rejected(self):
        verified = copy.deepcopy(OSS_VERIFIED)
        verified["entries"]["example/demo"] = {"ok": False, "code": 404}
        self.write_json("data/oss-verified.json", verified)
        self.assertProblem("API 查不到该仓库（HTTP 404）")

    def test_oss_point_reference_that_does_not_exist_is_rejected(self):
        oss = copy.deepcopy(OSS)
        oss["resources"][0]["points"] = ["pri-math-99"]
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("points 引用了不存在的知识点：pri-math-99")

    def test_duplicate_oss_repo_differing_only_by_case_is_rejected(self):
        oss = copy.deepcopy(OSS)
        twin = copy.deepcopy(oss["resources"][0])
        twin["repo"] = "Example/DEMO"
        twin["points"] = []
        oss["resources"].append(twin)
        self.write_yaml("data/oss-resources.yaml", oss)
        self.assertProblem("GitHub 仓库名不区分大小写")


class CoverageOfChecksTest(unittest.TestCase):
    """这套测试自己的箍：检查清单、COVERED 表、真实函数集合三者必须一致。"""

    def test_every_check_is_covered(self):
        defined = {
            name for name, value in vars(validate).items()
            if name.startswith("check_") and callable(value)
        }
        self.assertEqual(
            defined, set(validate.ALL_CHECKS),
            "validate.ALL_CHECKS 与模块里真实的 check_ 函数对不上。"
            "新增检查时请同时更新那份清单，并给它写一条能弄红它的用例。",
        )
        self.assertEqual(
            set(validate.ALL_CHECKS), set(COVERED),
            "有检查没有对应的「能弄红」用例，或 COVERED 里留了已删除的检查名。",
        )

    def test_every_covered_entry_names_a_real_test(self):
        """COVERED 指向的用例名必须真的存在，否则这张表本身就是装饰品。"""
        module = sys.modules[__name__]
        for check, test_name in sorted(COVERED.items()):
            self.assertTrue(
                hasattr(module, test_name) or any(
                    hasattr(cls, test_name) for cls in vars(module).values()
                    if isinstance(cls, type) and issubclass(cls, unittest.TestCase)
                ),
                f"COVERED['{check}'] 指向 {test_name}，但这个名字在文件里找不到。",
            )


if __name__ == "__main__":
    unittest.main()
