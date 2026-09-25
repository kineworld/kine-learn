# 外部链接与核验状态

这个页面里的状态码是 `scripts/check_links.py` 实测的结果，不是人工判断。最后一次检查：2026-09-25T02:50:47Z。

**判据必须分清，否则报告会骗人**：

| 状态 | 含义 | 要不要处理 |
| --- | --- | --- |
| verified | 本机实测有响应 | 不用 |
| dead | 明确 404 / 410 | 必须修，CI 会失败 |
| unreachable | 本机超时或连不上 | 换网络复核，**不代表失效** |
| blocked | 401 / 403 / 429 / 5xx，被反爬或限额挡 | 人工打开确认，**不代表失效** |

## 整站资源

| key | 名称 | 平台 | 状态 | HTTP | 说明 |
| --- | --- | --- | --- | --- | --- |
| `smartedu` | [国家中小学智慧教育平台](https://basic.smartedu.cn/) | 教育部 | verified | 200 | 小学到高中全部学科的官方微课、教材与习题，免费。中国 K-12 阶段的第一优先入口。 |
| `khan-zh` | [可汗学院（中文）](https://zh.khanacademy.org/) | Khan Academy | verified | 200 | 中文界面的可汗学院，数学主线从数数到微积分连续不断。 |
| `khan-math` | [Khan Academy · Math](https://www.khanacademy.org/math) | Khan Academy | verified | 200 | 数学课程按学段与主题完整编排，练习带即时反馈，是“知识点—练习—检验”闭环最省力的地方。 |
| `khan-science` | [Khan Academy · Science](https://www.khanacademy.org/science) | Khan Academy | verified | 200 | 物理、化学、生物、宇宙学的中英对照讲义。 |
| `khan-computing` | [Khan Academy · Computing](https://www.khanacademy.org/computing) | Khan Academy | verified | 200 | 算法、信息论、密码学的入门讲义，大学计算类知识点的补充入口。 |
| `phet` | [PhET 互动仿真实验（中文）](https://phet.colorado.edu/zh_CN/) | University of Colorado Boulder | verified | 200 | 可直接拖动的物理、化学、数学仿真。看不见的量（电场、概率、能量）能在这里被看见，是“直觉先于公式”的关键工具。 |
| `mit-ocw` | [MIT OpenCourseWare](https://ocw.mit.edu/) | MIT | verified | 200 | 麻省理工全部公开课程，含讲义、作业与答案。大学阶段自学最完整的免费来源。 |
| `ocw-1801` | [MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | MIT OCW | verified | 200 | 单变量微积分，含视频、习题与考试。配合中文教材使用。 |
| `ocw-1806` | [MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | MIT OCW | verified | 200 | 线性代数，讲解顺序从向量空间出发而不是从行列式出发，适合建立几何直觉。 |
| `ocw-804` | [MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/) | MIT OCW | verified | 200 | 量子力学第一门课，先建立波函数与概率幅的语言。 |
| `icourse163` | [中国大学MOOC](https://www.icourse163.org/) | 高教社 / 网易 | verified | 200 | 国内高校课程的慕课平台，中文讲授的大学基础课来源。选课时看开课学校与是否有作业批改。 |
| `openstax` | [OpenStax · 免费大学教材](https://openstax.org/) | Rice University | verified | 200 | 经同行评审的免费教材（物理、微积分、统计、生物、经济）。有 PDF 可下载，引用页码稳定。 |
| `3b1b` | [3Blue1Brown（英文站）](https://www.3blue1brown.com/) | 3Blue1Brown | verified | 200 | 用动画讲线性代数、微积分、概率与神经网络的直觉。价值在“先看见形状，再写公式”。 |
| `desmos` | [Desmos 图形计算器](https://www.desmos.com/calculator) | Desmos | verified | 200 | 把函数画出来再改参数，观察图像怎么变。理解“参数决定形状”的最快工具。 |
| `wolframalpha` | [Wolfram Alpha](https://www.wolframalpha.com/) | Wolfram Research | verified | 200 | 算积分、解方程、查常数。定位是**校验自己的手算**，不是替代手算；先自己算，再让它检查。 |
| `oeis` | [OEIS · 整数数列在线百科](https://oeis.org/) | OEIS Foundation | verified | 200 | 输入一串数，看它是不是已知数列、有没有公式与文献。培养“先查再猜”的习惯。 |
| `nist-constants` | [NIST 物理常数表](https://physics.nist.gov/cuu/Constants/) | NIST | verified | 200 | 光速、普朗克常数等的官方值与不确定度。写数字要带来源时用这里，不用记忆。 |
| `feynman` | [费曼物理学讲义（在线全文）](https://www.feynmanlectures.caltech.edu/) | Caltech | blocked | 403 | 物理直觉的经典来源。第 1 卷前几章可以完全不懂微积分就读。 |
| `zdic` | [汉典](https://www.zdic.net/) | 汉典 | verified | 200 | 查单字的字形演变、本义、古音与用例。中文学习的“元素周期表”入口。 |
| `gushiwen` | [古诗文网](https://www.gushiwen.cn/) | 古诗文网 | verified | 200 | 古诗文原文、注释、译文与赏析，按朝代与作者可检索。 |
| `moe-curriculum` | [教育部 · 义务教育课程方案和课程标准](http://www.moe.gov.cn/srcsite/A26/s8001/) | 教育部 | verified | 200 | 各科课程标准的官方发布页。“该学什么、学到什么程度”的最终依据，本仓库的覆盖范围以此对齐。 |
| `arxiv` | [arXiv](https://arxiv.org/) | Cornell University | verified | 200 | 论文预印本。注意预印本未经同行评审，引用时要写明这是预印本。 |
| `link-check-selftest` | [自查条目（故意指向不存在的仓库）](https://api.github.com/repos/kineworld/kine-learn-selftest-xyz) | none | dead | 404 | 这条链接**应该**返回 404。它的唯一用途是证明 check_links.py 真能识别失效链接。 |

## 检索模板

这些不是链接，是函数：给定关键词返回一个永远有效的检索页。每个知识点的具体视频都走这里，所以不存在「教材里的视频链接已下架」这个问题。

| key | 平台 | 模板 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| `bilibili` | 哔哩哔哩检索 | `https://search.bilibili.com/all?keyword={q}` | verified | 中文讲解密度最高的平台。加“微课”“板书”“推导”等词能显著提高命中率。 |
| `youtube` | YouTube 检索 | `https://www.youtube.com/results?search_query={q}` | unreachable | 英文资源量最大的一侧。大学阶段英文术语检索比中文更容易找到完整课程。 |
| `smartedu-search` | 国家中小学智慧教育平台检索 | `https://basic.smartedu.cn/search?keyword={q}` | blocked | 对应教材版本的官方微课，小学到高中首选。 |
| `ocw-search` | MIT OCW 课程检索 | `https://ocw.mit.edu/search/?q={q}` | verified | 找完整大学课程，而不是零散视频。 |
