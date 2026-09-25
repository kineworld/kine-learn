# KineLearn · 勘境基础学习路径

**用一年级小孩能听懂的话，从第一性原理讲清世界怎么运转；每个知识点都配外部讲解视频。**

小学 → 初中 → 高中 → 大学基础 → 语言，一条线走完。每个知识点都回答四个问题：
**它到底在说什么（一年级版）**、**它的第一性原理是什么**、**它在理解世界如何运作中
担任什么角色**、**怎么算学会了（出口标准）**。

这个仓库不是课程，是一张**地图**：它标出每个阶段该掌握什么、为什么是这些、去哪里
看讲解；讲解本身尽量指向已有的公开资源，不重复造。

- 线上视图（单文件，离线可用）：[`site/index.html`](site/index.html)
- 全部知识点总表：[`docs/CATALOG.md`](docs/CATALOG.md)
- 八条世界认知主线：[`docs/STRANDS.md`](docs/STRANDS.md)
- 开源项目索引：[`docs/RESOURCES.md`](docs/RESOURCES.md)
- 外部链接登记：[`docs/LINKS.md`](docs/LINKS.md)
- 当前覆盖情况：[`docs/COVERAGE.md`](docs/COVERAGE.md)
- 阶段与出口标准：[`ROADMAP.md`](ROADMAP.md)

## 先看这份材料拒绝做什么

写在最前面，因为这几句决定了后面每一句的可信度：

- **不承诺结果。** 材料里没有"保证学会""读完就懂"这类句子，这不是写作风格，
  是脚本强制的：`scripts/validate.py` 里有一组措辞红线正则，命中就让构建失败。
- **"全球前 1% 的认知水平"是这份材料的方向，不是它的承诺。** 它无法被这份材料
  单方面兑现——那取决于练习量、纠错质量、以及你是否真的动手算过。它唯一能保证
  的是：不会用含糊的话掩盖没讲清的地方。
- **不编造实体。** 不虚构合作方、专家推荐、认证或课程编号。登记的外部链接都是
  真实存在的平台地址，由 `scripts/check_links.py` 实际访问过。
- **讲不清就写"讲不清"。** 有些知识点（比如概率的直觉、量子力学的诠释）在基础
  阶段没有既简单又正确的说法。这类地方会明说，而不是编一个顺口的类比糊过去。

## 一个知识点长什么样

源文件是 `curriculum/*.yaml`，每个知识点五个必备字段：

| 字段 | 回答什么 | 写法要求 |
| --- | --- | --- |
| `kid` | 这个东西到底在说什么 | 一年级能听懂，不用术语 |
| `principle` | 第一性原理是什么 | 说清它从哪条最基本的事实推出来 |
| `model` | 它在理解世界如何运作中担任什么角色 | 明确连到八条主线之一 |
| `exit` | 怎么算学会了 | 可检查的动作，不是"理解"这种空词 |
| `video` | 去哪里看讲解 | 检索关键词 + 已核验的整站入口 |

外加 `core`（是否主干）、`strand`（所属主线）、`prereq`（前置知识点）。

八条主线是这套材料的骨：**number 数量** · **structure 结构** · **change 变化** ·
**energy 能量** · **cause 因果** · **system 系统** · **symbol 符号** ·
**scale 尺度**。每条主线有一个它负责回答的问题，见 [`docs/STRANDS.md`](docs/STRANDS.md)。

## 怎么读

三条读法，按你的起点选：

1. **十年线**（`ten-year`）：从小学第一条开始，按学段顺序推进。适合打地基。
2. **直觉优先**（`intuition-first`）：先只读每个知识点的"一年级版"和"与世界模型的
   连接"，把整张地图过一遍，再回头抠细节。适合已有基础、想补全视野的人。
3. **世界模型线**（`world-model`）：按八条主线横着读，一次只跟一条线走到底。
   适合想弄清"这些科目之间到底什么关系"的人。

每条读法的完整清单在 [`docs/CATALOG.md`](docs/CATALOG.md)。

## 视频链接为什么长这样

分成两种，各有各的道理：

- **整站入口**（`data/links.yaml`）：国家中小学智慧教育平台、Khan Academy、
  PhET、MIT OCW、B 站等。约二十条，每条都实际访问过，状态登记在
  [`data/links-status.json`](data/links-status.json)。
- **检索式链接**（每个知识点的 `video.q`）：一个关键词，拼成 B 站 / 国家平台 /
  YouTube / OCW 的检索页。

为什么不直接给具体视频地址？因为具体视频会下架、改名、被搬运。**检索页是函数，
具体视频是快照。** 一份要教十年的材料里放快照，两年后满地死链，而且没人会去修。
少量确实值得固定的入口放在 `data/links.yaml` 里，由检查脚本盯着。

## 开源项目索引

大学及以上阶段大量指向已有的开源项目（仿真实验、教材、工具链、习题库），
索引在 `data/oss-resources.yaml`。

关于这个文件有一件事必须说清：**它里面没有星数和许可证。** 那些数字由
`scripts/fetch_oss.py` 从 GitHub API 现拉，落进 `data/oss-verified.json`。
手打的数字会漂移，漂移了还没人发现——这是本仓库最想避免的那类缺陷。

被列入索引**不等于**被验证、被推荐、或被背书。每条都带一个 `caution` 字段，
写清它的限制和坑，见 [`docs/RESOURCES.md`](docs/RESOURCES.md)。

## 数据与产物

```
curriculum/*.yaml      人工维护：知识点正文（唯一的源）
data/links.yaml        人工维护：整站链接登记 + 自查条目
data/oss-resources.yaml 人工维护：开源项目索引
        │
        ├── scripts/fetch_oss.py   → data/oss-verified.json   （联网，拉 API）
        ├── scripts/check_links.py → data/links-status.json   （联网，探链接）
        │
        └── scripts/build.py       → docs/*.md + site/index.html  （永不上网）
```

`docs/` 和 `site/` 是**生成物**，但它们进了版本库。能这么做的唯一前提是构建可复现：
两次构建逐字节相同。CI 会重新生成再 `git diff --exit-code`，源文件改了却没重新
生成，CI 直接失败。产物里不含构建时刻——那会让每次构建都产生 diff。

## 自己跑一遍

```bash
pip install -r requirements.txt

python scripts/validate.py -v      # 内容自洽性：目录与正文是否对得上
python scripts/build.py            # 重新生成 docs/ 与 site/
python -m unittest discover -s tests -t .   # 测试（含"每条检查都能变红"）
python tests/check_collection.py   # 确认没有测试对运行器隐形

# 需要联网的两支（只有它们会上网）：
python scripts/check_links.py      # 探测外部链接，产出 data/links-status.json
python scripts/fetch_oss.py        # 拉 GitHub 元数据，产出 data/oss-verified.json
```

链接检查**刻意不进 CI**：外部站点的可用性不受本仓库控制，把它接进 CI 会让无关的
PR 随机变红，而随机红的检查等于没有检查。它由维护者在维护链接时手动跑，
结果落进 `data/links-status.json`，站点页脚会显示上次检查的时间。判据本身有测试
覆盖（`tests/test_link_classify.py`）：只有 404/410 算失效，连不上和被挡只算"没验成"。

## 贡献

改动前请读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。最短的版本：**先给证据，再给结论**，
以及**你加的每条检查都要能说明"什么缺陷会让它变红"**。分不出这个答案的检查是装饰品，
应当删掉。

第三方材料归属见 [`ATTRIBUTION.md`](ATTRIBUTION.md)。

## 许可

代码与文档以 MIT 发布，见 [`LICENSE`](LICENSE)。被索引的第三方开源项目各自
保留其原有许可证——**本仓库的 MIT 不覆盖它们**，详见 [`ATTRIBUTION.md`](ATTRIBUTION.md)。

---

维护：KineWorld 勘境 · [kineworld.com](https://kineworld.com) · 上游组织级社区文件见
[`kineworld/.github`](https://github.com/kineworld/.github)
