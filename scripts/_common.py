"""共享的数据加载层。

三个脚本（validate / build / check_links / fetch_oss）与单元测试都从这里取数据，
避免各自实现一套解析。任何一处逻辑只写一遍，就不会出现"脚本 A 说 210 个知识点、
脚本 B 说 208 个"这种情况。

设计约束：
  - build.py 永不上网。它只读 data/*.json 这类已经落盘的产物，
    所以断网也能构建，CI 也不会因为某个网站挂了而失败。
  - 网络只发生在 check_links.py 与 fetch_oss.py 里，而且它们只写 data/，
    不改正文。正文事实与外部事实因此是分开的。
"""

from __future__ import annotations

import json
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CURRICULUM_DIR = ROOT / "curriculum"
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"

INDEX_FILE = CURRICULUM_DIR / "_index.yaml"
LINKS_FILE = DATA_DIR / "links.yaml"
OSS_FILE = DATA_DIR / "oss-resources.yaml"
OSS_VERIFIED_FILE = DATA_DIR / "oss-verified.json"
LINKS_STATUS_FILE = DATA_DIR / "links-status.json"


def set_root(root) -> None:
    """把上面全部路径常量整体指向另一棵目录树。

    只有测试用它。没有这个口子，校验逻辑就只能对着真实仓库跑，
    于是"某条检查能不能被弄红"就无法验证——而不能失败的检查是装饰品。
    测试用它搭一棵最小目录树，塞进一条坏数据，断言那条检查确实报错。
    """
    global ROOT, CURRICULUM_DIR, DATA_DIR, DOCS_DIR, SITE_DIR
    global INDEX_FILE, LINKS_FILE, OSS_FILE, OSS_VERIFIED_FILE, LINKS_STATUS_FILE
    ROOT = pathlib.Path(root).resolve()
    CURRICULUM_DIR = ROOT / "curriculum"
    DATA_DIR = ROOT / "data"
    DOCS_DIR = ROOT / "docs"
    SITE_DIR = ROOT / "site"
    INDEX_FILE = CURRICULUM_DIR / "_index.yaml"
    LINKS_FILE = DATA_DIR / "links.yaml"
    OSS_FILE = DATA_DIR / "oss-resources.yaml"
    OSS_VERIFIED_FILE = DATA_DIR / "oss-verified.json"
    LINKS_STATUS_FILE = DATA_DIR / "links-status.json"
    # 换根目录必须作废已解析的缓存，否则会读到上一棵树的内容——
    # 这类错误的表现是"测试偶发失败"，最难查。
    clear_caches()


# 一个知识点必须齐备的字段。缺一个就不算写完，validate.py 会拦。
REQUIRED_POINT_FIELDS = (
    "id", "title", "grade", "kid", "principle", "model", "exit",
)

ALLOWED_KINDS = {
    "tutorial", "textbook", "simulation", "dataset",
    "tool", "course_list", "practice",
}
ALLOWED_LANGS = {"zh", "en", "multi"}

# 仓库名格式：owner/name
REPO_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")

# 学段 id → 知识点 id 前缀。用它检查"一个 mid- 开头的知识点掉进了小学文件"。
STAGE_PREFIX = {
    "primary": "pri-",
    "middle": "mid-",
    "high": "hi-",
    "university": "uni-",
    "language": "lang-",
}


# 已解析的源文件，按路径缓存。
#
# 为什么不每次重新解析：构建过程会就同一个问题问几百次——每个知识点都要
# 查一遍它引用了哪些开源项目、哪些整站链接。实测 link_entries() 被调用 197
# 次、load_links() 393 次，单次构建因此从 2 秒涨到 20 秒。内容是只读的，
# 重复解析没有任何意义。
#
# 两个约束：
#   - 调用方**不得修改**返回值。要改就先自己 copy 一份。
#   - set_root() 必须清空缓存，否则换根目录后会读到上一棵树的内容。
#     tests/test_every_check_can_fail.py 里有一条用例专门盯这件事。
_YAML_CACHE: dict[pathlib.Path, object] = {}
_JSON_CACHE: dict[pathlib.Path, object] = {}


def clear_caches() -> None:
    _YAML_CACHE.clear()
    _JSON_CACHE.clear()


def load_yaml(path: pathlib.Path):
    """读一个 YAML 文件。返回值是缓存的，视作只读。"""
    path = pathlib.Path(path)
    if path not in _YAML_CACHE:
        with open(path, encoding="utf-8") as fh:
            _YAML_CACHE[path] = yaml.safe_load(fh)
    return _YAML_CACHE[path]


def read_json(path: pathlib.Path, default=None):
    """读一个 JSON 文件。返回值是缓存的，视作只读。"""
    path = pathlib.Path(path)
    if path not in _JSON_CACHE:
        if not path.exists():
            return default
        with open(path, encoding="utf-8") as fh:
            _JSON_CACHE[path] = json.load(fh)
    return _JSON_CACHE[path]


def write_text(path: pathlib.Path, text: str) -> None:
    """写文本，强制 LF 且强制末尾换行。

    换行符必须显式指定：Windows 上默认会把 \\n 变成 \\r\\n，
    于是同一份生成物在两台机器上 diff 不同，CI 的"生成物是否最新"检查
    会变成一条永远失败的检查。
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def write_json(path: pathlib.Path, obj) -> None:
    write_text(path, json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=False))


def load_index() -> dict:
    return load_yaml(INDEX_FILE)


def stage_files() -> list[dict]:
    """按 _index.yaml 的顺序返回学段定义，并附上文件路径。"""
    index = load_index()
    out = []
    for stage in index["stages"]:
        out.append({**stage, "path": CURRICULUM_DIR / stage["file"]})
    return out


def load_stages(skip_missing: bool = False) -> list[dict]:
    """返回每个学段文件的完整内容，外加 stage 元信息。

    skip_missing=True 时，总表声明了、但文件不存在的学段不进结果。
    校验器用这个参数：文件缺失时它的职责是**报告**这件事，而不是抛
    FileNotFoundError。抛栈会把整份报告吃掉，只剩一行回溯——
    而"总表声明了 X 文件、X 文件不存在"恰恰是校验器最该说清的那类缺陷。
    构建则用默认的严格模式：产出半张站点比构建失败更糟。
    """
    out = []
    for stage in stage_files():
        if skip_missing and not stage["path"].exists():
            continue
        raw = load_yaml(stage["path"])
        out.append({**stage, "units": raw.get("units") or []})
    return out


def iter_points(skip_missing: bool = False) -> list[dict]:
    """把所有知识点摊平成一维列表，每项带上它所属的学段与学科。

    摊平是为了让"跨学段查找"（例如检查前置知识点是否存在）只需要一次遍历。
    参数含义见 load_stages。
    """
    index = load_index()
    subjects = index["subjects"]
    out = []
    for stage in load_stages(skip_missing=skip_missing):
        for unit in stage["units"]:
            sid = unit["subject_id"]
            for point in unit.get("points") or []:
                out.append({
                    **point,
                    "stage_id": stage["id"],
                    "stage_name": stage["name"],
                    "subject_id": sid,
                    "subject_name": subjects.get(sid, {}).get("name", sid),
                })
    return out


# 阶段二（主干精写）里"算得上段落"的字数下限。
#
# 这是**代理指标**，不是判据，别拿它当验收线。
# 真正的判据是那条原理有没有指出"它从哪条更基本的事实推出"——那得靠人读，
# 脚本判不了。字数只是判据的下限影子：提纲句一定短，但写到 120 字也未必讲清。
# 所以它只用来报进度，不用来拦构建。拿它当门槛，结果一定是有人往句子里灌水。
PARAGRAPH_MIN_CHARS = 120


def paragraph_stats(points: list[dict]) -> dict:
    """主干知识点的 principle 长度分布，用来回答"阶段二进行到哪了"。

    刻意返回分布（中位、最短、最长）而不是"合格 / 不合格"：
    合格与否取决于能不能读懂，不取决于字数。给一个二元结论，人就会去凑字数。
    """
    lengths = sorted(
        len(" ".join((p.get("principle") or "").split()))
        for p in points if p.get("core")
    )
    if not lengths:
        return {"n": 0, "median": 0, "shortest": 0, "longest": 0, "paragraph": 0}
    return {
        "n": len(lengths),
        "median": lengths[len(lengths) // 2],
        "shortest": lengths[0],
        "longest": lengths[-1],
        "paragraph": sum(1 for n in lengths if n >= PARAGRAPH_MIN_CHARS),
    }


def load_links() -> dict:
    raw = load_yaml(LINKS_FILE)
    return {
        "links": raw.get("links") or [],
        "search_templates": raw.get("search_templates") or [],
    }


def link_entries() -> dict:
    """key → 链接定义。"""
    return {item["key"]: item for item in load_links()["links"]}


def load_oss() -> list[dict]:
    return load_yaml(OSS_FILE).get("resources") or []


def oss_verified() -> dict:
    """repo（小写）→ API 返回的元数据。没有落盘时返回空表。

    用 repo.lower() 做键，因为 GitHub 的 owner/repo 查询不区分大小写，
    而人写的时候大小写常常不一致（QGIS 写成 qgis）。
    """
    data = read_json(OSS_VERIFIED_FILE, default=None) or {}
    return {k.lower(): v for k, v in (data.get("entries") or {}).items()}


def oss_verified_meta() -> dict:
    data = read_json(OSS_VERIFIED_FILE, default=None) or {}
    return {"fetched_at": data.get("fetched_at"), "source": data.get("source")}


def link_status() -> dict:
    data = read_json(LINKS_STATUS_FILE, default=None) or {}
    return {k: v for k, v in (data.get("entries") or {}).items()}


def link_status_meta() -> dict:
    data = read_json(LINKS_STATUS_FILE, default=None) or {}
    return {"checked_at": data.get("checked_at"), "note": data.get("note")}


def search_url(template: str, query: str) -> str:
    from urllib.parse import quote_plus
    return template.replace("{q}", quote_plus(query))
