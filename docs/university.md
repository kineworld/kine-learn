# 大学基础 · 本科一至三年级

[目录](CATALOG.md) · [主线视图](STRANDS.md) · [开源资源](RESOURCES.md) · [覆盖情况](COVERAGE.md)

> 大学阶段做两件事：把直觉换成严格语言（极限、线性、概率的公理化）， 以及把严格语言装回直觉（变分、场、对称性）。学完的标志不是会算， 而是知道每个定义为什么必须长成那样、去掉哪一条会坏掉什么。

本学段共 **58** 个知识点，其中主干 **51** 个；覆盖 **12** 个学科单元。「主干」= 缺了它后面的世界认知会断链的那些条目。

## 微积分（6 个知识点）

> 微积分只回答两个问题：一件事变化得多快，以及把无数小变化加起来是多少。 它之所以威力大，是因为所有光滑的东西在足够小的范围内都近似是线性的。

### uni-cal-01 · 极限的严格定义

大一 · **主干** · 主线：尺度与极限

- **一年级版**：极限不是“走到底”，而是“你说要多近，我就能让它多近”。
- **第一性原理**：极限用“任意给定的误差都能被满足”替代了“越来越接近”这种模糊说法。 它把直觉换成了可检验的命题，这是现代分析的起点。
- **与世界模型的连接**：把模糊说法改写成可检验条件，是全部科学定义化的通用手法。
- **出口标准**：能用误差语言说明一个数列收敛的确切含义，并指出“越来越接近”这种说法在哪里不够用。
- **视频入口**：[B站：高等数学 极限 定义 严格证明](https://search.bilibili.com/all?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E6%9E%81%E9%99%90+%E5%AE%9A%E4%B9%89+%E4%B8%A5%E6%A0%BC%E8%AF%81%E6%98%8E) · [官方微课：高等数学 极限 定义 严格证明](https://basic.smartedu.cn/search?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E6%9E%81%E9%99%90+%E5%AE%9A%E4%B9%89+%E4%B8%A5%E6%A0%BC%E8%AF%81%E6%98%8E) · [YouTube：epsilon delta limit intuition](https://www.youtube.com/results?search_query=epsilon+delta+limit+intuition) · [MIT OCW：epsilon delta limit intuition](https://ocw.mit.edu/search/?q=epsilon+delta+limit+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) · ★41,102 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：大学段找中文考试范围与往年题时用。它的价值在题型与范围，不在讲解质量。
- **开源项目**：[北大课程资料整理](https://github.com/lib-pku/libpku) · ★34,034 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：当作中文资料的另一个入口。
- **开源项目**：[中科大课程资源](https://github.com/USTC-Resource/USTC-Course) · ★16,283 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：找中文物理与数学课程材料时用。
- **开源项目**：[OSSU 数学自学路径](https://github.com/ossu/math) · ★9,183 · MIT · 在用
  - 怎么用：用它解决“我该按什么顺序学”的问题，而不是解决“这个定义是什么”。读它的课程顺序，教材换成本仓库对应的中文入口。
- **开源项目**：[OpenStax 微积分](https://github.com/openstax/osbooks-calculus-bundle) · ★6 · NOASSERTION · 在用
  - 怎么用：配合 MIT 18.01 使用：MIT 给讲解，这本给题量与答案。

### uni-cal-02 · 导数与局部线性化

大一 · **主干** · 主线：变化与守恒

- **一年级版**：任何弯曲的东西，凑近看都是直的。
- **第一性原理**：可微意味着函数在一点附近可以用一条直线近似，误差比距离更高阶地小。 求导就是一个“局部找最像的直线”的过程。
- **与世界模型的连接**：梯度下降的全部合法性来自局部线性化：能线性近似，才能指出往哪走能降低。
- **出口标准**：能写出一个函数在某点的线性近似并说明误差量级。
- **视频入口**：[B站：高等数学 导数 微分 局部线性化](https://search.bilibili.com/all?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%AF%BC%E6%95%B0+%E5%BE%AE%E5%88%86+%E5%B1%80%E9%83%A8%E7%BA%BF%E6%80%A7%E5%8C%96) · [官方微课：高等数学 导数 微分 局部线性化](https://basic.smartedu.cn/search?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%AF%BC%E6%95%B0+%E5%BE%AE%E5%88%86+%E5%B1%80%E9%83%A8%E7%BA%BF%E6%80%A7%E5%8C%96) · [YouTube：local linearization](https://www.youtube.com/results?search_query=local+linearization) · [MIT OCW：local linearization](https://ocw.mit.edu/search/?q=local+linearization)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[OpenStax 微积分](https://github.com/openstax/osbooks-calculus-bundle) · ★6 · NOASSERTION · 在用
  - 怎么用：配合 MIT 18.01 使用：MIT 给讲解，这本给题量与答案。

### uni-cal-03 · 泰勒展开

大一 · **主干** · 主线：尺度与极限

- **一年级版**：用一串越来越小的修正项去拼一条曲线，拼得越多就越像。
- **第一性原理**：展开的每一阶都对应一个可测的局部性质：值、斜率、弯曲、弯曲的变化率。 常见函数可以被多项式任意精度地逼近。
- **与世界模型的连接**：用简单函数逼近复杂函数，是数值计算与神经网络逼近定理的共同思想。
- **出口标准**：能写出某个函数的前三阶展开并估计在某点的误差。
- **视频入口**：[B站：高等数学 泰勒公式 展开 应用](https://search.bilibili.com/all?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E6%B3%B0%E5%8B%92%E5%85%AC%E5%BC%8F+%E5%B1%95%E5%BC%80+%E5%BA%94%E7%94%A8) · [官方微课：高等数学 泰勒公式 展开 应用](https://basic.smartedu.cn/search?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E6%B3%B0%E5%8B%92%E5%85%AC%E5%BC%8F+%E5%B1%95%E5%BC%80+%E5%BA%94%E7%94%A8) · [YouTube：Taylor series intuition](https://www.youtube.com/results?search_query=Taylor+series+intuition) · [MIT OCW：Taylor series intuition](https://ocw.mit.edu/search/?q=Taylor+series+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[数学资源索引](https://github.com/rossant/awesome-math) · ★16,478 · CC0-1.0 · 在用
  - 怎么用：遇到本仓库没展开的主题（拓扑、数论、代数几何）时，用它找入口。
- **开源项目**：[SymPy 符号计算](https://github.com/sympy/sympy) · ★14,967 · NOASSERTION · 在用
  - 怎么用：定位是**校验你的手算**。先自己算，再让它检查，不要反过来。

### uni-cal-04 · 积分与基本定理

大一 · **主干** · 主线：变化与守恒

- **一年级版**：把无数条细长条加起来就是积分；反过来，“一件东西累积了多少”的变化率就是它本身。
- **第一性原理**：微积分基本定理说明积分与微分互为逆运算。 它的实际含义是：只要知道变化率，就能算出总量，不需要知道每个瞬间。
- **与世界模型的连接**：对偶算子（累积与瞬时）让许多问题在另一个域里变成简单问题。
- **出口标准**：能解释为什么求面积可以不做任何“逐条相加”的动作。
- **视频入口**：[B站：高等数学 定积分 微积分基本定理 牛顿莱布尼茨](https://search.bilibili.com/all?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%AE%9A%E7%A7%AF%E5%88%86+%E5%BE%AE%E7%A7%AF%E5%88%86%E5%9F%BA%E6%9C%AC%E5%AE%9A%E7%90%86+%E7%89%9B%E9%A1%BF%E8%8E%B1%E5%B8%83%E5%B0%BC%E8%8C%A8) · [官方微课：高等数学 定积分 微积分基本定理 牛顿莱布尼茨](https://basic.smartedu.cn/search?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%AE%9A%E7%A7%AF%E5%88%86+%E5%BE%AE%E7%A7%AF%E5%88%86%E5%9F%BA%E6%9C%AC%E5%AE%9A%E7%90%86+%E7%89%9B%E9%A1%BF%E8%8E%B1%E5%B8%83%E5%B0%BC%E8%8C%A8)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[OpenStax 微积分](https://github.com/openstax/osbooks-calculus-bundle) · ★6 · NOASSERTION · 在用
  - 怎么用：配合 MIT 18.01 使用：MIT 给讲解，这本给题量与答案。

### uni-cal-05 · 多元微积分与梯度

大二 · **主干** · 主线：结构与层次

- **一年级版**：山上每一点都有一个“最陡的上坡方向”，梯度就指这个方向。
- **第一性原理**：梯度是由所有偏导数组成的向量，指向函数增大最快的方向。 梯度的方向与等高线垂直——这是“上升最快”与“不改变值”两个要求互相垂直。
- **与世界模型的连接**：优化全靠它。梯度为零是驻点，是极小、极大还是鞍点要看二阶信息。
- **出口标准**：能对二元函数算梯度，并解释为什么沿梯度方向走函数值上升最快。
- **视频入口**：[B站：高等数学 偏导数 梯度 方向导数](https://search.bilibili.com/all?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%81%8F%E5%AF%BC%E6%95%B0+%E6%A2%AF%E5%BA%A6+%E6%96%B9%E5%90%91%E5%AF%BC%E6%95%B0) · [官方微课：高等数学 偏导数 梯度 方向导数](https://basic.smartedu.cn/search?keyword=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6+%E5%81%8F%E5%AF%BC%E6%95%B0+%E6%A2%AF%E5%BA%A6+%E6%96%B9%E5%90%91%E5%AF%BC%E6%95%B0) · [YouTube：gradient descent intuition](https://www.youtube.com/results?search_query=gradient+descent+intuition) · [MIT OCW：gradient descent intuition](https://ocw.mit.edu/search/?q=gradient+descent+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[PyTorch](https://github.com/pytorch/pytorch) · ★103,264 · NOASSERTION · 在用
  - 怎么用：用它验证链式法则：自己手推梯度，再和 autograd 的结果比。
- **开源项目**：[动手学深度学习（中文）](https://github.com/d2l-ai/d2l-zh) · ★81,087 · Apache-2.0 · 在用
  - 怎么用：中文读者学深度学习的第一选择。数学不熟就一边看一边补微积分与线代。
- **开源项目**：[科学计算讲义](https://github.com/scipy-lectures/scientific-python-lectures) · ★3,217 · NOASSERTION · 在用
  - 怎么用：大学段一切数值实验的工具手册。遇错先查这里，再查搜索引擎。
- **开源项目**：[OpenStax 微积分](https://github.com/openstax/osbooks-calculus-bundle) · ★6 · NOASSERTION · 在用
  - 怎么用：配合 MIT 18.01 使用：MIT 给讲解，这本给题量与答案。

### uni-cal-06 · 微分方程

大二 · **主干** · 主线：变化与守恒

- **一年级版**：只知道“变化快慢跟现在有多少有关”，也能推出以后会变成多少。
- **第一性原理**：微分方程给出局部规则，解给出全局行为。 指数增长、振动、衰减都是同一类方程在不同参数下的样子。
- **与世界模型的连接**：世界模型最自然的写法就是学习一个离散化的微分方程。动力学建模的公共语言。
- **出口标准**：能写出指数增长与简谐振动各自对应的微分方程并指出参数含义。
- **视频入口**：[B站：常微分方程 一阶 线性 通解](https://search.bilibili.com/all?keyword=%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B+%E4%B8%80%E9%98%B6+%E7%BA%BF%E6%80%A7+%E9%80%9A%E8%A7%A3) · [官方微课：常微分方程 一阶 线性 通解](https://basic.smartedu.cn/search?keyword=%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B+%E4%B8%80%E9%98%B6+%E7%BA%BF%E6%80%A7+%E9%80%9A%E8%A7%A3) · [YouTube：differential equations intuition](https://www.youtube.com/results?search_query=differential+equations+intuition) · [MIT OCW：differential equations intuition](https://ocw.mit.edu/search/?q=differential+equations+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.01 · Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）

## 线性代数（6 个知识点）

> 线性代数研究“保持加法和数乘的变换”。它重要，是因为非线性问题在局部可以线性化， 以及因为它是唯一一门能被彻底搞清楚的高维几何。

### uni-lin-01 · 向量空间与基

大一 · **主干** · 主线：结构与层次

- **一年级版**：一堆箭头可以互相拼出别的箭头，能拼出的全部就叫一个空间。
- **第一性原理**：基是能表示空间中一切向量的一组最小的向量。同一个向量在不同基下坐标不同， 但向量本身没变——坐标是描述，不是对象。
- **与世界模型的连接**：区分“对象”与“描述”，是表示学习的核心。换基就是换一组特征。
- **出口标准**：能判断一组向量是否线性无关，并说明它能不能作为某个空间的基。
- **视频入口**：[B站：线性代数 向量组 线性相关 基 维数](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%90%91%E9%87%8F%E7%BB%84+%E7%BA%BF%E6%80%A7%E7%9B%B8%E5%85%B3+%E5%9F%BA+%E7%BB%B4%E6%95%B0) · [官方微课：线性代数 向量组 线性相关 基 维数](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%90%91%E9%87%8F%E7%BB%84+%E7%BA%BF%E6%80%A7%E7%9B%B8%E5%85%B3+%E5%9F%BA+%E7%BB%B4%E6%95%B0) · [YouTube：linear independence basis](https://www.youtube.com/results?search_query=linear+independence+basis) · [MIT OCW：linear independence basis](https://ocw.mit.edu/search/?q=linear+independence+basis)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[动手学深度学习（中文）](https://github.com/d2l-ai/d2l-zh) · ★81,087 · Apache-2.0 · 在用
  - 怎么用：中文读者学深度学习的第一选择。数学不熟就一边看一边补微积分与线代。
- **开源项目**：[浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) · ★41,102 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：大学段找中文考试范围与往年题时用。它的价值在题型与范围，不在讲解质量。
- **开源项目**：[OSSU 数学自学路径](https://github.com/ossu/math) · ★9,183 · MIT · 在用
  - 怎么用：用它解决“我该按什么顺序学”的问题，而不是解决“这个定义是什么”。读它的课程顺序，教材换成本仓库对应的中文入口。

### uni-lin-02 · 线性变换与矩阵

大一 · **主干** · 主线：结构与层次

- **一年级版**：矩阵不是一张数字表，是一个动作：把箭头拉长、压扁、转身。
- **第一性原理**：矩阵是线性变换在给定基下的坐标记录。矩阵乘法的规则就是“先做一个再做另一个”， 所以它一般不满足交换律。
- **与世界模型的连接**：把运算当作变换而不是数表，才能理解为什么非线性层是必要的。
- **出口标准**：能说出一个 2 乘 2 矩阵把单位方格变成什么形状，并解释行列式的意义。
- **视频入口**：[B站：线性代数 线性变换 矩阵 几何意义](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E7%BA%BF%E6%80%A7%E5%8F%98%E6%8D%A2+%E7%9F%A9%E9%98%B5+%E5%87%A0%E4%BD%95%E6%84%8F%E4%B9%89) · [官方微课：线性代数 线性变换 矩阵 几何意义](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E7%BA%BF%E6%80%A7%E5%8F%98%E6%8D%A2+%E7%9F%A9%E9%98%B5+%E5%87%A0%E4%BD%95%E6%84%8F%E4%B9%89) · [YouTube：linear transformations matrices 3blue1brown](https://www.youtube.com/results?search_query=linear+transformations+matrices+3blue1brown) · [MIT OCW：linear transformations matrices 3blue1brown](https://ocw.mit.edu/search/?q=linear+transformations+matrices+3blue1brown)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[NumPy](https://github.com/numpy/numpy) · ★32,824 · NOASSERTION · 在用
  - 怎么用：把线性代数的矩阵运算亲手写一遍，再和 NumPy 的结果对照。

### uni-lin-03 · 行列式与可逆性

大一 · **主干** · 主线：结构与层次

- **一年级版**：行列式量的是“这个动作把面积放大了几倍”。如果是零，说明它把空间压扁了，回不去。
- **第一性原理**：行列式为零等价于变换不可逆，等价于存在非零向量被映射到零，等价于列向量线性相关。 这串等价关系是线性代数里最值钱的一句话。
- **与世界模型的连接**：不可逆意味着信息丢失。可辨识性与可逆性在数学上是同一件事的两种说法。
- **出口标准**：能说明为什么奇异矩阵没有逆，并举出一个具体的例子。
- **视频入口**：[B站：线性代数 行列式 逆矩阵 秩](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E8%A1%8C%E5%88%97%E5%BC%8F+%E9%80%86%E7%9F%A9%E9%98%B5+%E7%A7%A9) · [官方微课：线性代数 行列式 逆矩阵 秩](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E8%A1%8C%E5%88%97%E5%BC%8F+%E9%80%86%E7%9F%A9%E9%98%B5+%E7%A7%A9) · [YouTube：determinant inverse matrix](https://www.youtube.com/results?search_query=determinant+inverse+matrix) · [MIT OCW：determinant inverse matrix](https://ocw.mit.edu/search/?q=determinant+inverse+matrix)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）

### uni-lin-04 · 特征值与特征向量

大一 · **主干** · 主线：变化与守恒

- **一年级版**：有的方向被拉伸后方向不变，只是变长变短。这样的方向最特殊，叫特征方向。
- **第一性原理**：特征向量给出变换的不变方向，特征值给出该方向的伸缩倍数。 在特征基下，复杂的重复变换变成各方向独立缩放，迭代就变得极易计算。
- **与世界模型的连接**：迭代系统的长期行为由最大特征值主导。理解长期趋势只需要看一个数。
- **出口标准**：能算出一个矩阵的特征值，并说出它反复作用很多次后结果会往哪个方向偏。
- **视频入口**：[B站：线性代数 特征值 特征向量 对角化](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E7%89%B9%E5%BE%81%E5%80%BC+%E7%89%B9%E5%BE%81%E5%90%91%E9%87%8F+%E5%AF%B9%E8%A7%92%E5%8C%96) · [官方微课：线性代数 特征值 特征向量 对角化](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E7%89%B9%E5%BE%81%E5%80%BC+%E7%89%B9%E5%BE%81%E5%90%91%E9%87%8F+%E5%AF%B9%E8%A7%92%E5%8C%96) · [YouTube：eigenvectors intuition](https://www.youtube.com/results?search_query=eigenvectors+intuition) · [MIT OCW：eigenvectors intuition](https://ocw.mit.edu/search/?q=eigenvectors+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[SymPy 符号计算](https://github.com/sympy/sympy) · ★14,967 · NOASSERTION · 在用
  - 怎么用：定位是**校验你的手算**。先自己算，再让它检查，不要反过来。

### uni-lin-05 · 内积、正交与投影

大一 · **主干** · 主线：数量与度量

- **一年级版**：投影就是“影子”。把一个东西投到某个方向上，剩下的部分跟那个方向垂直。
- **第一性原理**：内积定义了长度与角度，从而定义了“垂直”与“最近”。 最小二乘就是用投影求一个不可解方程组的最优近似解。
- **与世界模型的连接**：有内积才有距离，有距离才有“最近”，有最近才有学习。损失函数的地基在这里。
- **出口标准**：能推导最小二乘的正规方程，并说明它为什么是投影的另一种写法。
- **视频入口**：[B站：线性代数 内积 正交 投影 最小二乘](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%86%85%E7%A7%AF+%E6%AD%A3%E4%BA%A4+%E6%8A%95%E5%BD%B1+%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98) · [官方微课：线性代数 内积 正交 投影 最小二乘](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%86%85%E7%A7%AF+%E6%AD%A3%E4%BA%A4+%E6%8A%95%E5%BD%B1+%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98) · [YouTube：least squares projection](https://www.youtube.com/results?search_query=least+squares+projection) · [MIT OCW：least squares projection](https://ocw.mit.edu/search/?q=least+squares+projection)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）

### uni-lin-06 · 奇异值分解

大二 · **主干** · 主线：结构与层次

- **一年级版**：任何拉伸压缩的动作，都可以拆成“转身、拉长、再转身”三步。
- **第一性原理**：奇异值分解把任意矩阵写成旋转、对角缩放、旋转的乘积。 奇异值的大小直接说明这个变换在各个方向上放大了多少，也说明有多少信息被丢掉。
- **与世界模型的连接**：判断一个表征是否坍缩，看的就是它的奇异值谱。这是本组织表征健康度探针的数学来源。
- **出口标准**：能说明一个矩阵的奇异值全部很小时意味着什么，以及它为什么表示信息丢失。
- **视频入口**：[B站：线性代数 奇异值分解 SVD 应用](https://search.bilibili.com/all?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3+SVD+%E5%BA%94%E7%94%A8) · [官方微课：线性代数 奇异值分解 SVD 应用](https://basic.smartedu.cn/search?keyword=%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0+%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3+SVD+%E5%BA%94%E7%94%A8) · [YouTube：singular value decomposition intuition](https://www.youtube.com/results?search_query=singular+value+decomposition+intuition) · [MIT OCW：singular value decomposition intuition](https://ocw.mit.edu/search/?q=singular+value+decomposition+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 18.06 · Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（MIT OCW）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）

## 概率与统计（6 个知识点）

> 概率是唯一一门能同时容纳“不知道”和“算得清”的语言。 不会概率的人只能给出确定答案，而世界的多数问题没有确定答案。

### uni-pro-01 · 概率公理与条件概率

大二 · **主干** · 主线：因果与证据

- **一年级版**：“在已经知道某事的前提下，另一件事发生的概率”跟原来不一样，这就是条件概率。
- **第一性原理**：概率是对一组事件的度量，满足三条基本规则。条件概率是重新划定样本空间后的度量。 独立是乘积成立，不是“毫无关系”这种模糊说法。
- **与世界模型的连接**：观测会改变信念。任何“我知道多少”都必须写成条件。
- **出口标准**：能算出两个不独立事件的联合概率，并说明独立假设在这里为什么错。
- **视频入口**：[B站：概率论 条件概率 独立性 全概率公式](https://search.bilibili.com/all?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E6%9D%A1%E4%BB%B6%E6%A6%82%E7%8E%87+%E7%8B%AC%E7%AB%8B%E6%80%A7+%E5%85%A8%E6%A6%82%E7%8E%87%E5%85%AC%E5%BC%8F) · [官方微课：概率论 条件概率 独立性 全概率公式](https://basic.smartedu.cn/search?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E6%9D%A1%E4%BB%B6%E6%A6%82%E7%8E%87+%E7%8B%AC%E7%AB%8B%E6%80%A7+%E5%85%A8%E6%A6%82%E7%8E%87%E5%85%AC%E5%BC%8F) · [YouTube：conditional probability](https://www.youtube.com/results?search_query=conditional+probability) · [MIT OCW：conditional probability](https://ocw.mit.edu/search/?q=conditional+probability)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **开源项目**：[浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) · ★41,102 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：大学段找中文考试范围与往年题时用。它的价值在题型与范围，不在讲解质量。
- **开源项目**：[OSSU 数据科学自学路径](https://github.com/ossu/data-science) · ★21,981 · NOASSERTION · 在用
  - 怎么用：在大学段概率与统计学完后当作应用路线的补充。
- **开源项目**：[OSSU 数学自学路径](https://github.com/ossu/math) · ★9,183 · MIT · 在用
  - 怎么用：用它解决“我该按什么顺序学”的问题，而不是解决“这个定义是什么”。读它的课程顺序，教材换成本仓库对应的中文入口。

### uni-pro-02 · 贝叶斯公式

大二 · **主干** · 主线：因果与证据

- **一年级版**：体检查出阳性，不等于一定有病，要看这种病本来有多常见。
- **第一性原理**：后验正比于似然乘先验。忽略先验会得出荒谬结论—— 这就是为什么罕见病的阳性结果多数是假阳性。
- **与世界模型的连接**：更新信念的标准公式。先验就是模型原有的假设，数据只做修正。
- **出口标准**：能算出一个罕见病检测的阳性预测值，并说明为什么它低得反直觉。
- **视频入口**：[B站：概率论 贝叶斯公式 先验 后验](https://search.bilibili.com/all?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E8%B4%9D%E5%8F%B6%E6%96%AF%E5%85%AC%E5%BC%8F+%E5%85%88%E9%AA%8C+%E5%90%8E%E9%AA%8C) · [官方微课：概率论 贝叶斯公式 先验 后验](https://basic.smartedu.cn/search?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E8%B4%9D%E5%8F%B6%E6%96%AF%E5%85%AC%E5%BC%8F+%E5%85%88%E9%AA%8C+%E5%90%8E%E9%AA%8C) · [YouTube：Bayes theorem intuition](https://www.youtube.com/results?search_query=Bayes+theorem+intuition) · [MIT OCW：Bayes theorem intuition](https://ocw.mit.edu/search/?q=Bayes+theorem+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[深度学习（花书）中文翻译](https://github.com/exacity/deeplearningbook-chinese) · ★37,621 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：当参考书查，不要当教程顺读。第一部分（数学基础）值得通读。

### uni-pro-03 · 随机变量与分布

大二 · **主干** · 主线：变化与守恒

- **一年级版**：把每种结果配上发生的可能，再配上数值，就能算平均和波动。
- **第一性原理**：分布完整描述了随机变量，期望与方差只是它的两个摘要。 只报这两个数字，等于用两张照片代替一个立体对象。
- **与世界模型的连接**：摘要统计不是分布。模型评估里“均值加误差棒”经常掩盖关键的多峰或长尾结构。
- **出口标准**：能构造两个期望方差相同但形状完全不同的分布。
- **视频入口**：[B站：概率论 随机变量 分布函数 期望 方差](https://search.bilibili.com/all?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F+%E5%88%86%E5%B8%83%E5%87%BD%E6%95%B0+%E6%9C%9F%E6%9C%9B+%E6%96%B9%E5%B7%AE) · [官方微课：概率论 随机变量 分布函数 期望 方差](https://basic.smartedu.cn/search?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F+%E5%88%86%E5%B8%83%E5%87%BD%E6%95%B0+%E6%9C%9F%E6%9C%9B+%E6%96%B9%E5%B7%AE) · [YouTube：random variables distributions](https://www.youtube.com/results?search_query=random+variables+distributions) · [MIT OCW：random variables distributions](https://ocw.mit.edu/search/?q=random+variables+distributions)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **开源项目**：[微软机器学习入门（12 周，26 课）](https://github.com/microsoft/ML-For-Beginners) · ★90,950 · MIT · 在用
  - 怎么用：大学段“机器学习最小闭环”的主要配套课程。先跑通它的第一个实验再谈别的。

### uni-pro-04 · 大数定律与中心极限定理

大二 · **主干** · 主线：尺度与极限

- **一年级版**：扔硬币次数越多，正面比例越接近一半；而“偏离一半的量”自己有个固定的形状。
- **第一性原理**：大数定律说样本均值收敛到期望；中心极限定理说波动部分的分布趋近正态， 且与原本的分布形状无关。
- **与世界模型的连接**：这是“大量独立小因素相加”能普遍用正态描述的原因，也是统计推断的合法性来源。
- **出口标准**：能解释为什么误差往往近似正态，即使原始量完全不是正态分布。
- **视频入口**：[B站：概率论 大数定律 中心极限定理 应用](https://search.bilibili.com/all?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E5%A4%A7%E6%95%B0%E5%AE%9A%E5%BE%8B+%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86+%E5%BA%94%E7%94%A8) · [官方微课：概率论 大数定律 中心极限定理 应用](https://basic.smartedu.cn/search?keyword=%E6%A6%82%E7%8E%87%E8%AE%BA+%E5%A4%A7%E6%95%B0%E5%AE%9A%E5%BE%8B+%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86+%E5%BA%94%E7%94%A8) · [YouTube：central limit theorem](https://www.youtube.com/results?search_query=central+limit+theorem) · [MIT OCW：central limit theorem](https://ocw.mit.edu/search/?q=central+limit+theorem)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）

### uni-pro-05 · 估计与置信区间

大二 · **主干** · 主线：因果与证据

- **一年级版**：用一小部分数据猜整体，猜出来的数一定有余地，这个余地就是区间。
- **第一性原理**：置信区间的含义是“这套造区间的办法在长期里有百分之九十五的概率覆盖真值”， 不是“真值有百分之九十五的概率落在本区间里”。
- **与世界模型的连接**：区间的解释是程序性质的，不是单次结果的。混淆两者是最常见的统计误读。
- **出口标准**：能说出置信区间的正确解释，并指出常见错误说法错在哪。
- **视频入口**：[B站：数理统计 参数估计 置信区间 含义](https://search.bilibili.com/all?keyword=%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1+%E5%8F%82%E6%95%B0%E4%BC%B0%E8%AE%A1+%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4+%E5%90%AB%E4%B9%89) · [官方微课：数理统计 参数估计 置信区间 含义](https://basic.smartedu.cn/search?keyword=%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1+%E5%8F%82%E6%95%B0%E4%BC%B0%E8%AE%A1+%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4+%E5%90%AB%E4%B9%89) · [YouTube：confidence interval interpretation](https://www.youtube.com/results?search_query=confidence+interval+interpretation) · [MIT OCW：confidence interval interpretation](https://ocw.mit.edu/search/?q=confidence+interval+interpretation)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **开源项目**：[微软数据科学入门（10 周，20 课）](https://github.com/microsoft/Data-Science-For-Beginners) · ★37,300 · MIT · 在用
  - 怎么用：用来学“从一份脏数据到一个可信结论”的完整流程，这部分数学课不会教。
- **开源项目**：[OpenIntro 统计学教材](https://github.com/OpenIntroStat/openintro-statistics) · ★454 · NOASSERTION · 在用
  - 怎么用：直接读置信区间与假设检验两章，用它的数据自己算一遍，比读定义记得住。

### uni-pro-06 · 假设检验与 p 值

大二 · **主干** · 主线：因果与证据

- **一年级版**：p 值小只说明“如果本来没效果，出现这么极端的结果很难”，不代表效果大。
- **第一性原理**：p 值是“在零假设为真时观测到当前或更极端数据的概率”，不是“零假设为真的概率”。 它同时受效应量与样本量影响，所以不能当效果大小的度量。
- **与世界模型的连接**：检验是决策程序，不是真值发现器。多重比较不做校正必然产出假阳性。
- **出口标准**：能指出一个“p 小于 0.05 所以有效”的结论里缺了哪两样东西。
- **视频入口**：[B站：数理统计 假设检验 p值 误区](https://search.bilibili.com/all?keyword=%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1+%E5%81%87%E8%AE%BE%E6%A3%80%E9%AA%8C+p%E5%80%BC+%E8%AF%AF%E5%8C%BA) · [官方微课：数理统计 假设检验 p值 误区](https://basic.smartedu.cn/search?keyword=%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1+%E5%81%87%E8%AE%BE%E6%A3%80%E9%AA%8C+p%E5%80%BC+%E8%AF%AF%E5%8C%BA) · [YouTube：p value misinterpretation](https://www.youtube.com/results?search_query=p+value+misinterpretation) · [MIT OCW：p value misinterpretation](https://ocw.mit.edu/search/?q=p+value+misinterpretation)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Math](https://www.khanacademy.org/math)（Khan Academy）
- **开源项目**：[scikit-learn](https://github.com/scikit-learn/scikit-learn) · ★67,357 · BSD-3-Clause · 在用
  - 怎么用：用它对比不同模型在同一数据上的表现，训练集与测试集必须自己分好。
- **开源项目**：[OpenIntro 统计学教材](https://github.com/OpenIntroStat/openintro-statistics) · ★454 · NOASSERTION · 在用
  - 怎么用：直接读置信区间与假设检验两章，用它的数据自己算一遍，比读定义记得住。

## 离散数学与计算（5 个知识点）

> 计算机处理的是离散对象。这门课给的是“可计算的精确语言”， 以及判断一个问题难到什么程度的能力。

### uni-dis-01 · 集合、关系与函数

大一 · **主干** · 主线：结构与层次

- **一年级版**：关系就是“谁跟谁有关系”，比如“谁是谁的爸爸”。函数是一种特殊的关系。
- **第一性原理**：关系是笛卡尔积的子集，于是“传递”“对称”这些性质可以被精确定义与证明。 等价关系把集合切成互不相交的块，这就是分类的数学形式。
- **与世界模型的连接**：分类、聚类、等价类在数学上是同一个结构。
- **出口标准**：能判断一个给定关系是否满足自反、对称、传递，并说明它能否分类。
- **视频入口**：[B站：离散数学 集合 关系 等价关系 偏序](https://search.bilibili.com/all?keyword=%E7%A6%BB%E6%95%A3%E6%95%B0%E5%AD%A6+%E9%9B%86%E5%90%88+%E5%85%B3%E7%B3%BB+%E7%AD%89%E4%BB%B7%E5%85%B3%E7%B3%BB+%E5%81%8F%E5%BA%8F) · [官方微课：离散数学 集合 关系 等价关系 偏序](https://basic.smartedu.cn/search?keyword=%E7%A6%BB%E6%95%A3%E6%95%B0%E5%AD%A6+%E9%9B%86%E5%90%88+%E5%85%B3%E7%B3%BB+%E7%AD%89%E4%BB%B7%E5%85%B3%E7%B3%BB+%E5%81%8F%E5%BA%8F)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[OSSU 计算机科学自学路径](https://github.com/ossu/computer-science) · ★209,437 · MIT · 在用
  - 怎么用：当索引看。国内学生优先换成 QSCTech/zju-icicles 或 PKUanonym/REKCARC-TSC-UHT 里对应的课程材料。
- **开源项目**：[清华计算机系课程攻略](https://github.com/PKUanonym/REKCARC-TSC-UHT) · ★37,641 · CC-BY-SA-4.0 · 在用
  - 怎么用：想了解“一门课真正要求到什么程度”时看它的作业与实验说明。
- **开源项目**：[开源逻辑学教材](https://github.com/OpenLogicProject/OpenLogic) · ★1,369 · CC-BY-4.0 · 在用
  - 怎么用：只读前三章就够用：形式化、真值表、有效性。之后遇到“这个论证对不对”就有工具了。

### uni-dis-02 · 图论

大一 · **主干** · 主线：结构与层次

- **一年级版**：点和线连起来就是图。谁跟谁连通，决定了消息能不能传过去。
- **第一性原理**：图把“关系”从“位置”里剥出来单独研究。连通性、最短路径、二分性、树的判定 都是结构性质，与实际画法无关。
- **与世界模型的连接**：神经网络的连接结构、世界的状态转移图、依赖关系都是图。
- **出口标准**：能判断一个图能否二染色，并说明这一性质在调度问题里有什么用。
- **视频入口**：[B站：离散数学 图论 连通性 树 最短路](https://search.bilibili.com/all?keyword=%E7%A6%BB%E6%95%A3%E6%95%B0%E5%AD%A6+%E5%9B%BE%E8%AE%BA+%E8%BF%9E%E9%80%9A%E6%80%A7+%E6%A0%91+%E6%9C%80%E7%9F%AD%E8%B7%AF) · [官方微课：离散数学 图论 连通性 树 最短路](https://basic.smartedu.cn/search?keyword=%E7%A6%BB%E6%95%A3%E6%95%B0%E5%AD%A6+%E5%9B%BE%E8%AE%BA+%E8%BF%9E%E9%80%9A%E6%80%A7+%E6%A0%91+%E6%9C%80%E7%9F%AD%E8%B7%AF)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[代码随想录](https://github.com/youngyangyang04/leetcode-master) · ★62,571 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：配合 Hello 算法：一个讲结构，一个给题目。按它的顺序刷，不要乱序刷。

### uni-dis-03 · 递归与计算复杂度

大一 · **主干** · 主线：尺度与极限

- **一年级版**：一个办法要跑多久，跟事情变多快长大后有本质区别：有的慢一点，有的一下子就爆掉。
- **第一性原理**：复杂度描述的是增长的量级，忽略常数因子，因为规模一大常数就不重要了。 指数与多项式之间的差距不是快慢问题，是可行与不可行的问题。
- **与世界模型的连接**：判断一个算法是否可行，先看量级。这条判断让很多实验免于白跑。
- **出口标准**：能比较两个算法在输入规模翻倍时的工作量变化，并说出哪个在大规模下不可用。
- **视频入口**：[B站：算法 时间复杂度 大O 递归](https://search.bilibili.com/all?keyword=%E7%AE%97%E6%B3%95+%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6+%E5%A4%A7O+%E9%80%92%E5%BD%92) · [官方微课：算法 时间复杂度 大O 递归](https://basic.smartedu.cn/search?keyword=%E7%AE%97%E6%B3%95+%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6+%E5%A4%A7O+%E9%80%92%E5%BD%92) · [YouTube：big O notation](https://www.youtube.com/results?search_query=big+O+notation) · [MIT OCW：big O notation](https://ocw.mit.edu/search/?q=big+O+notation)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[OSSU 计算机科学自学路径](https://github.com/ossu/computer-science) · ★209,437 · MIT · 在用
  - 怎么用：当索引看。国内学生优先换成 QSCTech/zju-icicles 或 PKUanonym/REKCARC-TSC-UHT 里对应的课程材料。
- **开源项目**：[Hello 算法](https://github.com/krahets/hello-algo) · ★130,460 · NOASSERTION · 在用
  - 怎么用：本仓库离散数学与计算单元的主要配套读物。先看动画建立直觉，再自己写一遍。
- **开源项目**：[代码随想录](https://github.com/youngyangyang04/leetcode-master) · ★62,571 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：配合 Hello 算法：一个讲结构，一个给题目。按它的顺序刷，不要乱序刷。

### uni-dis-04 · 可计算性与图灵机

大二 · **主干** · 主线：尺度与极限

- **一年级版**：有些问题不是“还没想出来怎么算”，是原则上算不出来。
- **第一性原理**：图灵机给出了“可计算”的精确定义。停机问题不可判定， 说明存在原则上无法用算法解决的问题——这与算力大小无关。
- **与世界模型的连接**：先问“这个问题可不可判定”，再问“能不能算得快”。顺序反了会浪费几年。
- **出口标准**：能说明停机问题为什么不可判定，以及它与“程序查错器不存在”的关系。
- **视频入口**：[B站：可计算性 图灵机 停机问题 不可判定](https://search.bilibili.com/all?keyword=%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%80%A7+%E5%9B%BE%E7%81%B5%E6%9C%BA+%E5%81%9C%E6%9C%BA%E9%97%AE%E9%A2%98+%E4%B8%8D%E5%8F%AF%E5%88%A4%E5%AE%9A) · [官方微课：可计算性 图灵机 停机问题 不可判定](https://basic.smartedu.cn/search?keyword=%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%80%A7+%E5%9B%BE%E7%81%B5%E6%9C%BA+%E5%81%9C%E6%9C%BA%E9%97%AE%E9%A2%98+%E4%B8%8D%E5%8F%AF%E5%88%A4%E5%AE%9A)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[从零重造技术](https://github.com/codecrafters-io/build-your-own-x) · ★549,364 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：想真正理解“一个系统内部怎么运作”时用它。挑一个与你当前方向相关的做完。

### uni-dis-05 · 数值方法与浮点误差

大二 · **主干** · 主线：数量与度量

- **一年级版**：电脑里的数只有有限多位，0.1 加 0.2 不一定刚好等于 0.3。
- **第一性原理**：浮点数是二进制下的有限表示，因此有舍入误差、上溢与下溢。 两个很接近的大数相减会突然失去精度——这叫灾难性抵消。
- **与世界模型的连接**：一切数值实验都要问误差来源与量级。报告里位数写得越多不代表越准。
- **出口标准**：能举出一个在浮点下不成立的算术事实，并说明结果该怎么报告。
- **视频入口**：[B站：数值分析 浮点数 误差 稳定性](https://search.bilibili.com/all?keyword=%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90+%E6%B5%AE%E7%82%B9%E6%95%B0+%E8%AF%AF%E5%B7%AE+%E7%A8%B3%E5%AE%9A%E6%80%A7) · [官方微课：数值分析 浮点数 误差 稳定性](https://basic.smartedu.cn/search?keyword=%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90+%E6%B5%AE%E7%82%B9%E6%95%B0+%E8%AF%AF%E5%B7%AE+%E7%A8%B3%E5%AE%9A%E6%80%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）

## 大学物理（8 个知识点）

> 大学物理把中学的“公式”换成“定律加适用条件”。 判断掌握与否的方法是：能不能说出这个定律在什么情况下失效。

### uni-phy-01 · 质点力学

大一 · **主干** · 主线：变化与守恒

- **一年级版**：只要知道受力，就能推出以后怎么动。反过来，观察到怎么动就能推出受力。
- **第一性原理**：牛顿方程是二阶微分方程，给定初始位置与初始速度才有唯一解。 也就是说“现在”不够，还要知道“变化的方向”。
- **与世界模型的连接**：状态必须包含足够的信息才能唯一决定未来。这是马尔可夫状态的定义性要求。
- **出口标准**：能说明为什么一阶状态描述不足、必须给出初始速度。
- **视频入口**：[B站：大学物理 质点力学 牛顿方程 初始条件](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E8%B4%A8%E7%82%B9%E5%8A%9B%E5%AD%A6+%E7%89%9B%E9%A1%BF%E6%96%B9%E7%A8%8B+%E5%88%9D%E5%A7%8B%E6%9D%A1%E4%BB%B6) · [官方微课：大学物理 质点力学 牛顿方程 初始条件](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E8%B4%A8%E7%82%B9%E5%8A%9B%E5%AD%A6+%E7%89%9B%E9%A1%BF%E6%96%B9%E7%A8%8B+%E5%88%9D%E5%A7%8B%E6%9D%A1%E4%BB%B6)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[OpenStax · 免费大学教材](https://openstax.org/)（Rice University）
- **开源项目**：[中科大课程资源](https://github.com/USTC-Resource/USTC-Course) · ★16,283 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：找中文物理与数学课程材料时用。
- **开源项目**：[PhET 引力与轨道](https://github.com/phetsims/gravity-and-orbits) · ★12 · GPL-3.0 · 在用
  - 怎么用：只改初速度不改变其它量，找到圆轨道与逃逸的两个临界值。
- **开源项目**：[OpenStax 大学物理（含高中物理）](https://github.com/openstax/osbooks-physics) · ★6 · CC-BY-4.0 · 在用
  - 怎么用：用它补英文术语：中文会了但读英文文献卡住，多数卡在术语而不是概念。
- **开源项目**：[OpenStax 大学物理（三卷本，微积分基础）](https://github.com/openstax/osbooks-university-physics-bundle) · ★5 · NOASSERTION · 在用
  - 怎么用：学完微积分再读，顺序反过来会很痛苦。

### uni-phy-02 · 刚体转动

大一 · 主线：结构与层次

- **一年级版**：转的东西不容易停下来，而且转得越开越难停。
- **第一性原理**：转动惯量相当于平动的质量，力矩相当于力。整套平动公式有转动版本， 因为数学结构相同。
- **与世界模型的连接**：结构相同的方程可以整体迁移，这是类比推理最可靠的用法。
- **出口标准**：能说出转动惯量取决于什么，并解释花样滑冰收臂为什么会加速旋转。
- **视频入口**：[B站：大学物理 刚体 转动惯量 角动量守恒](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E5%88%9A%E4%BD%93+%E8%BD%AC%E5%8A%A8%E6%83%AF%E9%87%8F+%E8%A7%92%E5%8A%A8%E9%87%8F%E5%AE%88%E6%81%92) · [官方微课：大学物理 刚体 转动惯量 角动量守恒](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E5%88%9A%E4%BD%93+%E8%BD%AC%E5%8A%A8%E6%83%AF%E9%87%8F+%E8%A7%92%E5%8A%A8%E9%87%8F%E5%AE%88%E6%81%92)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[OpenStax · 免费大学教材](https://openstax.org/)（Rice University）
- **开源项目**：[OpenStax 大学物理（三卷本，微积分基础）](https://github.com/openstax/osbooks-university-physics-bundle) · ★5 · NOASSERTION · 在用
  - 怎么用：学完微积分再读，顺序反过来会很痛苦。

### uni-phy-03 · 振动与波

大一 · **主干** · 主线：变化与守恒

- **一年级版**：被拉开的弹簧会来回动，因为它被拉得越远，往回拉的力越大。
- **第一性原理**：回复力与位移成正比就得到简谐振动，此时方程是线性的。 线性使它有叠加性，于是任何复杂的振动都能拆成简单振动之和。
- **与世界模型的连接**：线性系统可分解，是最重要的结构性事实之一。它解释了为什么傅里叶方法到处能用。
- **出口标准**：能写出简谐振动方程并说明周期由什么决定、与振幅无关。
- **视频入口**：[B站：大学物理 简谐振动 波动方程 叠加](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E7%AE%80%E8%B0%90%E6%8C%AF%E5%8A%A8+%E6%B3%A2%E5%8A%A8%E6%96%B9%E7%A8%8B+%E5%8F%A0%E5%8A%A0) · [官方微课：大学物理 简谐振动 波动方程 叠加](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E7%AE%80%E8%B0%90%E6%8C%AF%E5%8A%A8+%E6%B3%A2%E5%8A%A8%E6%96%B9%E7%A8%8B+%E5%8F%A0%E5%8A%A0)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[PhET 互动仿真实验（中文）](https://phet.colorado.edu/zh_CN/)（University of Colorado Boulder）
- **开源项目**：[PhET 质量与弹簧](https://github.com/phetsims/masses-and-springs) · ★4 · GPL-3.0 · 在用
  - 怎么用：改变振幅，确认周期不变——这是简谐振动最反直觉也最核心的一条。

### uni-phy-04 · 热力学定律与统计意义

大二 · **主干** · 主线：能量与转化

- **一年级版**：热量只会自己从热的地方跑到冷的地方，不会倒着跑。
- **第一性原理**：第一定律是能量守恒，第二定律给出过程方向。 第二定律的统计解释是：宏观状态之所以从不均匀趋向均匀， 只是因为均匀状态对应的微观排列数多得多——不是不可能倒过来，是概率极低。
- **与世界模型的连接**：这条统计解释改变了对“不可逆”的理解：它是概率的，不是禁止的。物理定律里第一次出现必然性只是近似。
- **出口标准**：能解释为什么倒放热扩散不是被禁止而是极不可能，并估算它的量级。
- **视频入口**：[B站：热力学 第二定律 统计解释 熵](https://search.bilibili.com/all?keyword=%E7%83%AD%E5%8A%9B%E5%AD%A6+%E7%AC%AC%E4%BA%8C%E5%AE%9A%E5%BE%8B+%E7%BB%9F%E8%AE%A1%E8%A7%A3%E9%87%8A+%E7%86%B5) · [官方微课：热力学 第二定律 统计解释 熵](https://basic.smartedu.cn/search?keyword=%E7%83%AD%E5%8A%9B%E5%AD%A6+%E7%AC%AC%E4%BA%8C%E5%AE%9A%E5%BE%8B+%E7%BB%9F%E8%AE%A1%E8%A7%A3%E9%87%8A+%E7%86%B5) · [YouTube：entropy statistical mechanics](https://www.youtube.com/results?search_query=entropy+statistical+mechanics) · [MIT OCW：entropy statistical mechanics](https://ocw.mit.edu/search/?q=entropy+statistical+mechanics)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[费曼物理学讲义（在线全文）](https://www.feynmanlectures.caltech.edu/)（Caltech）
- **开源项目**：[OpenStax 大学物理（三卷本，微积分基础）](https://github.com/openstax/osbooks-university-physics-bundle) · ★5 · NOASSERTION · 在用
  - 怎么用：学完微积分再读，顺序反过来会很痛苦。

### uni-phy-05 · 麦克斯韦方程组

大二 · **主干** · 主线：能量与转化

- **一年级版**：四条式子把电和磁的所有事都写完了，还顺手说明了光是什么。
- **第一性原理**：四个方程描述电荷产生电场、变化磁场产生电场、磁单极不存在、电流与变化电场产生磁场。 把它们联立会得到波动方程，波速由两个电磁学常数算出——正好等于光速。
- **与世界模型的连接**：两条彼此无关的实验常数，组合出光的速度，这种“意外吻合”是历史上最有力的理论证据。
- **出口标准**：能说明为什么由此可以断定光就是电磁波，而不是恰好速度相同的东西。
- **视频入口**：[B站：电动力学 麦克斯韦方程组 电磁波 光速](https://search.bilibili.com/all?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E9%BA%A6%E5%85%8B%E6%96%AF%E9%9F%A6%E6%96%B9%E7%A8%8B%E7%BB%84+%E7%94%B5%E7%A3%81%E6%B3%A2+%E5%85%89%E9%80%9F) · [官方微课：电动力学 麦克斯韦方程组 电磁波 光速](https://basic.smartedu.cn/search?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E9%BA%A6%E5%85%8B%E6%96%AF%E9%9F%A6%E6%96%B9%E7%A8%8B%E7%BB%84+%E7%94%B5%E7%A3%81%E6%B3%A2+%E5%85%89%E9%80%9F)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[费曼物理学讲义（在线全文）](https://www.feynmanlectures.caltech.edu/)（Caltech）
- **开源项目**：[OpenStax 大学物理（三卷本，微积分基础）](https://github.com/openstax/osbooks-university-physics-bundle) · ★5 · NOASSERTION · 在用
  - 怎么用：学完微积分再读，顺序反过来会很痛苦。

### uni-phy-06 · 光的干涉与衍射

大二 · 主线：尺度与极限

- **一年级版**：光绕过一个缝会散开，两条缝会互相叠成明暗条纹。
- **第一性原理**：条纹间距与波长成正比，因此可以用它测量极小的长度。 光学干涉仪把“测长度”换成了“数条纹”，精度提升了几个数量级。
- **与世界模型的连接**：把难测的量转换成易测的量，是测量科学的核心技巧。
- **出口标准**：能说明双缝条纹间距由哪些量决定，并解释它为什么能测波长。
- **视频入口**：[B站：大学物理 光的干涉 衍射 双缝干涉仪](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E5%85%89%E7%9A%84%E5%B9%B2%E6%B6%89+%E8%A1%8D%E5%B0%84+%E5%8F%8C%E7%BC%9D%E5%B9%B2%E6%B6%89%E4%BB%AA) · [官方微课：大学物理 光的干涉 衍射 双缝干涉仪](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E5%85%89%E7%9A%84%E5%B9%B2%E6%B6%89+%E8%A1%8D%E5%B0%84+%E5%8F%8C%E7%BC%9D%E5%B9%B2%E6%B6%89%E4%BB%AA)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[OpenStax · 免费大学教材](https://openstax.org/)（Rice University）
- **开源项目**：[PhET 波的干涉](https://github.com/phetsims/wave-interference) · ★20 · MIT · 在用
  - 怎么用：改频率与间距，观察条纹间距变化，这是“用条纹数长度”的直观来源。
- **开源项目**：[PhET 几何光学](https://github.com/phetsims/geometric-optics) · ★9 · GPL-3.0 · 在用
  - 怎么用：拖动物体穿过焦点，看实像何时变成虚像。

### uni-phy-07 · 狭义相对论

大二 · **主干** · 主线：尺度与极限

- **一年级版**：光速对谁来说都一样快，这件事逼着我们改掉“时间对所有人都一样”的想法。
- **第一性原理**：两条假设（物理规律在一切惯性系相同、真空光速不变）推出时间膨胀、长度收缩、 同时性的相对性。代价是放弃绝对时间。
- **与世界模型的连接**：一个反常的观测事实，如果不肯放弃某个“显然”的假设，就会一直被当成悖论。
- **出口标准**：能说明同时性的相对性是怎么从光速不变推出来的。
- **视频入口**：[B站：大学物理 狭义相对论 光速不变 时间膨胀](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E7%8B%AD%E4%B9%89%E7%9B%B8%E5%AF%B9%E8%AE%BA+%E5%85%89%E9%80%9F%E4%B8%8D%E5%8F%98+%E6%97%B6%E9%97%B4%E8%86%A8%E8%83%80) · [官方微课：大学物理 狭义相对论 光速不变 时间膨胀](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E7%8B%AD%E4%B9%89%E7%9B%B8%E5%AF%B9%E8%AE%BA+%E5%85%89%E9%80%9F%E4%B8%8D%E5%8F%98+%E6%97%B6%E9%97%B4%E8%86%A8%E8%83%80)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[费曼物理学讲义（在线全文）](https://www.feynmanlectures.caltech.edu/)（Caltech）

### uni-phy-08 · 量子假设与不确定性

大二 · **主干** · 主线：尺度与极限

- **一年级版**：极小的东西，你越想知道它在哪儿，就越不知道它跑多快。
- **第一性原理**：不确定性不是仪器不行，是共轭量不可能同时确定，这是波的本性。 能量量子化是实验逼出来的：不假设它，黑体辐射与原子光谱都算不对。
- **与世界模型的连接**：测量的极限来自理论本身而不是工具。知道极限在哪，才知道哪些目标不该定。
- **出口标准**：能解释为什么“因为仪器精度不够”是错的解释。
- **视频入口**：[B站：大学物理 量子力学 不确定性原理 波粒二象性](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7%E5%8E%9F%E7%90%86+%E6%B3%A2%E7%B2%92%E4%BA%8C%E8%B1%A1%E6%80%A7) · [官方微课：大学物理 量子力学 不确定性原理 波粒二象性](https://basic.smartedu.cn/search?keyword=%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86+%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7%E5%8E%9F%E7%90%86+%E6%B3%A2%E7%B2%92%E4%BA%8C%E8%B1%A1%E6%80%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/)（MIT OCW）
- **整站资源**：[费曼物理学讲义（在线全文）](https://www.feynmanlectures.caltech.edu/)（Caltech）

## 理论力学（4 个知识点）

> 理论力学换了一套写法：不追踪力，而追踪能量。换写法之后， 约束力自动消失，复杂问题变简单——这是“换表示”威力的经典展示。

### uni-mec-01 · 拉格朗日力学

大二 · **主干** · 主线：变化与守恒

- **一年级版**：不用管绳子和轨道的拉力，只看“有多少种走法”，再从中挑出真正会走的那一条。
- **第一性原理**：用广义坐标描述系统，从动能减势能构造拉格朗日量， 由变分原理导出运动方程。约束力因为不出现在广义坐标里而自动消失。
- **与世界模型的连接**：选对坐标，问题就解决了一半。表示的选择直接决定求解难度。
- **出口标准**：能用拉格朗日方法写出一根摆的运动方程，并指出它比牛顿方法省掉了什么。
- **视频入口**：[B站：理论力学 拉格朗日方程 广义坐标](https://search.bilibili.com/all?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E6%96%B9%E7%A8%8B+%E5%B9%BF%E4%B9%89%E5%9D%90%E6%A0%87) · [官方微课：理论力学 拉格朗日方程 广义坐标](https://basic.smartedu.cn/search?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E6%96%B9%E7%A8%8B+%E5%B9%BF%E4%B9%89%E5%9D%90%E6%A0%87) · [YouTube：Lagrangian mechanics](https://www.youtube.com/results?search_query=Lagrangian+mechanics) · [MIT OCW：Lagrangian mechanics](https://ocw.mit.edu/search/?q=Lagrangian+mechanics)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-mec-02 · 最小作用量原理

大二 · **主干** · 主线：变化与守恒

- **一年级版**：光知道要抄近路，球知道要走最省力的一条路。
- **第一性原理**：真实路径使作用量取驻值（通常最小）。这条全局性的陈述， 等价于牛顿的局部因果方程，但它允许一次考虑整条路径。
- **与世界模型的连接**：局部规则与全局极值原理互为等价写法。选择哪一种取决于问题结构。
- **出口标准**：能说明为什么最小作用量原理与牛顿方程给出同一个结果。
- **视频入口**：[B站：理论力学 最小作用量原理 变分法](https://search.bilibili.com/all?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E6%9C%80%E5%B0%8F%E4%BD%9C%E7%94%A8%E9%87%8F%E5%8E%9F%E7%90%86+%E5%8F%98%E5%88%86%E6%B3%95) · [官方微课：理论力学 最小作用量原理 变分法](https://basic.smartedu.cn/search?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E6%9C%80%E5%B0%8F%E4%BD%9C%E7%94%A8%E9%87%8F%E5%8E%9F%E7%90%86+%E5%8F%98%E5%88%86%E6%B3%95)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-mec-03 · 哈密顿力学与相空间

大二 · **主干** · 主线：结构与层次

- **一年级版**：把一个系统的位置和速度各画一根轴，它的状态就是这张图上的一个点。
- **第一性原理**：哈密顿方程把运动写成位置与动量的对称形式，状态演化对应于相空间中的流动。 相空间体积守恒（刘维尔定理）是统计力学的入口。
- **与世界模型的连接**：状态空间视角：预测就是状态点沿确定性（或随机）流场的推进。世界模型的语言。
- **出口标准**：能画出单摆的相图，并说出闭合曲线与开放曲线分别代表什么运动。
- **视频入口**：[B站：理论力学 哈密顿方程 相空间 相图](https://search.bilibili.com/all?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E5%93%88%E5%AF%86%E9%A1%BF%E6%96%B9%E7%A8%8B+%E7%9B%B8%E7%A9%BA%E9%97%B4+%E7%9B%B8%E5%9B%BE) · [官方微课：理论力学 哈密顿方程 相空间 相图](https://basic.smartedu.cn/search?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E5%93%88%E5%AF%86%E9%A1%BF%E6%96%B9%E7%A8%8B+%E7%9B%B8%E7%A9%BA%E9%97%B4+%E7%9B%B8%E5%9B%BE) · [YouTube：Hamiltonian phase space](https://www.youtube.com/results?search_query=Hamiltonian+phase+space) · [MIT OCW：Hamiltonian phase space](https://ocw.mit.edu/search/?q=Hamiltonian+phase+space)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-mec-04 · 对称性与守恒定律

大二 · **主干** · 主线：能量与转化

- **一年级版**：世界往哪个方向看都一样，所以转圈的东西会保持转下去。
- **第一性原理**：诺特定理：每一个连续对称性对应一个守恒量。 时间平移对称对应能量守恒，空间平移对应动量守恒，旋转对应角动量守恒。
- **与世界模型的连接**：守恒律的来源不是“实验结果”，而是对称性。这条认识改变了物理学找规律的方式。
- **出口标准**：能说出三种对称性各对应哪个守恒量，并解释为什么对称性能给出守恒。
- **视频入口**：[B站：理论力学 诺特定理 对称性 守恒量](https://search.bilibili.com/all?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E8%AF%BA%E7%89%B9%E5%AE%9A%E7%90%86+%E5%AF%B9%E7%A7%B0%E6%80%A7+%E5%AE%88%E6%81%92%E9%87%8F) · [官方微课：理论力学 诺特定理 对称性 守恒量](https://basic.smartedu.cn/search?keyword=%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6+%E8%AF%BA%E7%89%B9%E5%AE%9A%E7%90%86+%E5%AF%B9%E7%A7%B0%E6%80%A7+%E5%AE%88%E6%81%92%E9%87%8F) · [YouTube：Noether theorem symmetry conservation](https://www.youtube.com/results?search_query=Noether+theorem+symmetry+conservation) · [MIT OCW：Noether theorem symmetry conservation](https://ocw.mit.edu/search/?q=Noether+theorem+symmetry+conservation)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

## 电动力学（3 个知识点）

> 电动力学是“场”的样板课。学完它，你会发现物理学里很多别的对象 （引力、流体、甚至扩散）都在用同一套数学。

### uni-ele-01 · 静电场与高斯定律

大三 · **主干** · 主线：能量与转化

- **一年级版**：把电荷装在盒子里，穿出盒面的电场总量只跟盒里装了多少电有关，跟盒子多大多小无关。
- **第一性原理**：高斯定律把电场与电荷的关系写成通量与源的形式，它只在有对称性时才好用来求场。 场线始于正电荷、终于负电荷。
- **与世界模型的连接**：用积分守恒量求局部量，前提是够对称。判断对称性是选工具的第一步。
- **出口标准**：能用高斯定律求出带电球面内外的电场，并说明为什么内部电场为零。
- **视频入口**：[B站：电动力学 静电场 高斯定理 应用](https://search.bilibili.com/all?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E9%9D%99%E7%94%B5%E5%9C%BA+%E9%AB%98%E6%96%AF%E5%AE%9A%E7%90%86+%E5%BA%94%E7%94%A8) · [官方微课：电动力学 静电场 高斯定理 应用](https://basic.smartedu.cn/search?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E9%9D%99%E7%94%B5%E5%9C%BA+%E9%AB%98%E6%96%AF%E5%AE%9A%E7%90%86+%E5%BA%94%E7%94%A8)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-ele-02 · 稳恒磁场与安培环路定理

大三 · **主干** · 主线：能量与转化

- **一年级版**：电流周围会有一圈一圈的磁力线，绕着电流转。
- **第一性原理**：安培环路定理把磁场的环量与穿过回路的电流联系起来。 磁场是有旋无散的场，所以磁力线永远是闭合的——磁单极不存在。
- **与世界模型的连接**：区分“无散”（有源）与“无旋”（有势）是场论里最基础的一条分类。
- **出口标准**：能说明为什么磁力线一定闭合，而电场线可以终止在电荷上。
- **视频入口**：[B站：电动力学 安培环路定理 稳恒磁场](https://search.bilibili.com/all?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E5%AE%89%E5%9F%B9%E7%8E%AF%E8%B7%AF%E5%AE%9A%E7%90%86+%E7%A8%B3%E6%81%92%E7%A3%81%E5%9C%BA) · [官方微课：电动力学 安培环路定理 稳恒磁场](https://basic.smartedu.cn/search?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E5%AE%89%E5%9F%B9%E7%8E%AF%E8%B7%AF%E5%AE%9A%E7%90%86+%E7%A8%B3%E6%81%92%E7%A3%81%E5%9C%BA)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-ele-03 · 电磁波与辐射

大三 · 主线：能量与转化

- **一年级版**：电荷一旦加速，就会把能量甩出去，甩出去的东西就是电磁波。
- **第一性原理**：加速电荷产生辐射场，辐射功率与加速度的平方成正比。 这条平方律解释了为什么天线要做成特定形状，以及为什么高频电路容易干扰别人。
- **与世界模型的连接**：平方律在物理里反复出现，它通常意味着“代价随速率急剧上升”，是设计约束的来源。
- **出口标准**：能解释为什么无线电天线要有合适尺寸，以及为什么不能用低频信号远距离传输很高带宽。
- **视频入口**：[B站：电动力学 电磁波 辐射 天线](https://search.bilibili.com/all?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E7%94%B5%E7%A3%81%E6%B3%A2+%E8%BE%90%E5%B0%84+%E5%A4%A9%E7%BA%BF) · [官方微课：电动力学 电磁波 辐射 天线](https://basic.smartedu.cn/search?keyword=%E7%94%B5%E5%8A%A8%E5%8A%9B%E5%AD%A6+%E7%94%B5%E7%A3%81%E6%B3%A2+%E8%BE%90%E5%B0%84+%E5%A4%A9%E7%BA%BF)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

## 量子力学（4 个知识点）

> 量子力学是“用不可直接观测的表示对象做精确预测”的范本。 它教的东西远超物理：如何对待一个无法直觉化的状态空间。

### uni-qua-01 · 波函数与叠加

大三 · **主干** · 主线：尺度与极限

- **一年级版**：一个东西在没被看之前，可以同时处于几种可能的混合状态。
- **第一性原理**：波函数是概率幅，不是概率。幅值可以相加产生干涉， 概率只在取模平方后出现——这就是叠加与干涉的来源。
- **与世界模型的连接**：状态可以是分布而不是取值。用分布表示不确定性是量子力学对其它领域最大的输出。
- **出口标准**：能说明为什么“同时处于两种状态”不等于“其实只是我们不知道”。
- **视频入口**：[B站：量子力学 波函数 概率幅 叠加态](https://search.bilibili.com/all?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E6%B3%A2%E5%87%BD%E6%95%B0+%E6%A6%82%E7%8E%87%E5%B9%85+%E5%8F%A0%E5%8A%A0%E6%80%81) · [官方微课：量子力学 波函数 概率幅 叠加态](https://basic.smartedu.cn/search?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E6%B3%A2%E5%87%BD%E6%95%B0+%E6%A6%82%E7%8E%87%E5%B9%85+%E5%8F%A0%E5%8A%A0%E6%80%81)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/)（MIT OCW）
- **开源项目**：[微软量子编程习题](https://github.com/microsoft/QuantumKatas) · ★4,910 · MIT · 已归档
  - 怎么用：量子力学的三个反直觉点（叠加、测量、纠缠）在这里被逼着写成代码，比读定义有效。
- **开源项目**：[Qiskit 大学量子计算课程](https://github.com/qiskit-community/qiskit-textbook) · ★1,033 · Apache-2.0 · 已归档
  - 怎么用：与 Qiskit 一起用，边读边跑。

### uni-qua-02 · 薛定谔方程

大三 · **主干** · 主线：变化与守恒

- **一年级版**：粒子怎么随时间变化，被这一个方程全说完了。
- **第一性原理**：方程是线性的，所以解可以叠加；解是复数的，所以有相位与干涉。 定态对应能量本征值，能级分化就是量子化的来源。
- **与世界模型的连接**：线性使得整个理论的结构与线性代数一一对应：状态是向量，观测量是算子，测量是投影。
- **出口标准**：能说出为什么量子力学可以完全用线性代数表述。
- **视频入口**：[B站：量子力学 薛定谔方程 本征态 能级](https://search.bilibili.com/all?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E8%96%9B%E5%AE%9A%E8%B0%94%E6%96%B9%E7%A8%8B+%E6%9C%AC%E5%BE%81%E6%80%81+%E8%83%BD%E7%BA%A7) · [官方微课：量子力学 薛定谔方程 本征态 能级](https://basic.smartedu.cn/search?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E8%96%9B%E5%AE%9A%E8%B0%94%E6%96%B9%E7%A8%8B+%E6%9C%AC%E5%BE%81%E6%80%81+%E8%83%BD%E7%BA%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/)（MIT OCW）
- **开源项目**：[Qiskit 量子计算 SDK](https://github.com/Qiskit/qiskit) · ★7,830 · Apache-2.0 · 在用
  - 怎么用：用模拟器把薛定谔方程的小例子跑一遍，观察叠加与纠缠的实际输出分布。
- **开源项目**：[微软量子编程习题](https://github.com/microsoft/QuantumKatas) · ★4,910 · MIT · 已归档
  - 怎么用：量子力学的三个反直觉点（叠加、测量、纠缠）在这里被逼着写成代码，比读定义有效。

### uni-qua-03 · 测量与不确定

大三 · **主干** · 主线：尺度与极限

- **一年级版**：一测量，混合的状态就塌缩成一个结果。
- **第一性原理**：测量不是被动读取，它会改变状态。两个不对易的可观测量不能同时有确定值， 这就是不确定性关系的一般形式。
- **与世界模型的连接**：观测会干扰被观测对象。这在宏观世界表现为“任何测量都有代价”。
- **出口标准**：能说明为什么测得越准的代价是“另一个量变得更不准”。
- **视频入口**：[B站：量子力学 测量 塌缩 对易关系 不确定性](https://search.bilibili.com/all?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E6%B5%8B%E9%87%8F+%E5%A1%8C%E7%BC%A9+%E5%AF%B9%E6%98%93%E5%85%B3%E7%B3%BB+%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7) · [官方微课：量子力学 测量 塌缩 对易关系 不确定性](https://basic.smartedu.cn/search?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E6%B5%8B%E9%87%8F+%E5%A1%8C%E7%BC%A9+%E5%AF%B9%E6%98%93%E5%85%B3%E7%B3%BB+%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/)（MIT OCW）
- **开源项目**：[Qiskit 大学量子计算课程](https://github.com/qiskit-community/qiskit-textbook) · ★1,033 · Apache-2.0 · 已归档
  - 怎么用：与 Qiskit 一起用，边读边跑。

### uni-qua-04 · 自旋与纠缠

大三 · **主干** · 主线：结构与层次

- **一年级版**：两个粒子一旦配成对，无论隔多远，测一个就能立刻知道另一个。
- **第一性原理**：纠缠态不能写成两个子系统状态的乘积。它不传递信息， 但关联强于任何经典机制所能给出的——贝尔不等式的实验否定了定域实在论。
- **与世界模型的连接**：“整体不是部分的简单相加”最干净的反例。系统层面的信息不在任何单个部分里。
- **出口标准**：能说明为什么纠缠不能用来超光速通信。
- **视频入口**：[B站：量子力学 自旋 纠缠 贝尔不等式](https://search.bilibili.com/all?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E8%87%AA%E6%97%8B+%E7%BA%A0%E7%BC%A0+%E8%B4%9D%E5%B0%94%E4%B8%8D%E7%AD%89%E5%BC%8F) · [官方微课：量子力学 自旋 纠缠 贝尔不等式](https://basic.smartedu.cn/search?keyword=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6+%E8%87%AA%E6%97%8B+%E7%BA%A0%E7%BC%A0+%E8%B4%9D%E5%B0%94%E4%B8%8D%E7%AD%89%E5%BC%8F)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT 8.04 · Quantum Physics I](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/)（MIT OCW）
- **开源项目**：[Qiskit 量子计算 SDK](https://github.com/Qiskit/qiskit) · ★7,830 · Apache-2.0 · 在用
  - 怎么用：用模拟器把薛定谔方程的小例子跑一遍，观察叠加与纠缠的实际输出分布。

## 热力学与统计物理（3 个知识点）

> 统计物理回答的是“微观规则怎样涌出宏观定律”。 它是理解“个体随机、群体确定”这一结构性事实的正规训练。

### uni-the-01 · 熵的微观解释

大三 · **主干** · 主线：能量与转化

- **一年级版**：乱的排法数量比整齐的排法多得多，所以东西自己会走向乱。
- **第一性原理**：熵是微观状态数的对数。系统自发走向微观状态数最多的宏观状态， 因为那是概率最大的状态。熵不是“混乱”，是“可实现方式的数量”。
- **与世界模型的连接**：用计数解释必然性：宏观规律是大量可能性上的统计事实，不是个体层面的强制。
- **出口标准**：能用一个简单的计数例子说明为什么整齐的状态概率极低。
- **视频入口**：[B站：热力学统计物理 熵 微观状态数 玻尔兹曼](https://search.bilibili.com/all?keyword=%E7%83%AD%E5%8A%9B%E5%AD%A6%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%86%B5+%E5%BE%AE%E8%A7%82%E7%8A%B6%E6%80%81%E6%95%B0+%E7%8E%BB%E5%B0%94%E5%85%B9%E6%9B%BC) · [官方微课：热力学统计物理 熵 微观状态数 玻尔兹曼](https://basic.smartedu.cn/search?keyword=%E7%83%AD%E5%8A%9B%E5%AD%A6%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%86%B5+%E5%BE%AE%E8%A7%82%E7%8A%B6%E6%80%81%E6%95%B0+%E7%8E%BB%E5%B0%94%E5%85%B9%E6%9B%BC)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-the-02 · 玻尔兹曼分布

大三 · **主干** · 主线：能量与转化

- **一年级版**：能量高的状态也能出现，只是更少见，能量越高越少见。
- **第一性原理**：处于能量为 E 的状态的概率与 e 的负 E 比 kT 次方成正比。 温度决定这个指数衰减有多陡：温度越高，高能状态越常见。
- **与世界模型的连接**：指数型的概率分布来自“最大化可能性”这一个要求。软最大化与它同源。
- **出口标准**：能说明温度趋近于零与趋近于无穷时分布各会变成什么样。
- **视频入口**：[B站：统计物理 玻尔兹曼分布 配分函数](https://search.bilibili.com/all?keyword=%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%8E%BB%E5%B0%94%E5%85%B9%E6%9B%BC%E5%88%86%E5%B8%83+%E9%85%8D%E5%88%86%E5%87%BD%E6%95%B0) · [官方微课：统计物理 玻尔兹曼分布 配分函数](https://basic.smartedu.cn/search?keyword=%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%8E%BB%E5%B0%94%E5%85%B9%E6%9B%BC%E5%88%86%E5%B8%83+%E9%85%8D%E5%88%86%E5%87%BD%E6%95%B0)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）

### uni-the-03 · 相变与临界现象

大三 · 主线：尺度与极限

- **一年级版**：水到了零度会突然变成冰，中间没有过渡状态。
- **第一性原理**：相变是参量连续变化引起状态不连续改变。临界点附近的系统具有尺度不变性， 因此不同材料表现出相同的临界指数——这叫普适性。
- **与世界模型的连接**：微观细节在临界点附近失效，只有对称性与维度起作用。这是“忽略细节仍能成立”的最强例子。
- **出口标准**：能举出一个相变例子并说明“临界点附近细节不重要”表现在哪。
- **视频入口**：[B站：统计物理 相变 临界现象 普适性](https://search.bilibili.com/all?keyword=%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%9B%B8%E5%8F%98+%E4%B8%B4%E7%95%8C%E7%8E%B0%E8%B1%A1+%E6%99%AE%E9%80%82%E6%80%A7) · [官方微课：统计物理 相变 临界现象 普适性](https://basic.smartedu.cn/search?keyword=%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86+%E7%9B%B8%E5%8F%98+%E4%B8%B4%E7%95%8C%E7%8E%B0%E8%B1%A1+%E6%99%AE%E9%80%82%E6%80%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
- **整站资源**：[PhET 互动仿真实验（中文）](https://phet.colorado.edu/zh_CN/)（University of Colorado Boulder）

## 计算与编程（5 个知识点）

> 编程是“把想法变成可以被机械执行的东西”。它与数学的区别在于必须落地， 与工程的区别在于可以随便试。这使它成为最好的思维训练场。

### uni-com-01 · 程序就是数据加变换

大一 · **主干** · 主线：结构与层次

- **一年级版**：程序就是：把东西整理成一种格式，然后一步步换掉它。
- **第一性原理**：所有程序都可以理解为“定义数据表示 + 定义变换 + 组合变换”。 提前设计表示，比提前优化代码收益大得多。
- **与世界模型的连接**：建模就是选表示。表示选错，后面所有努力都在修补这个错误。
- **出口标准**：能说出自己写的一个程序里数据结构是什么、核心变换是哪几个。
- **视频入口**：[B站：编程入门 数据结构 函数 抽象](https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8+%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84+%E5%87%BD%E6%95%B0+%E6%8A%BD%E8%B1%A1) · [官方微课：编程入门 数据结构 函数 抽象](https://basic.smartedu.cn/search?keyword=%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8+%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84+%E5%87%BD%E6%95%B0+%E6%8A%BD%E8%B1%A1) · [YouTube：learn to code basics](https://www.youtube.com/results?search_query=learn+to+code+basics) · [MIT OCW：learn to code basics](https://ocw.mit.edu/search/?q=learn+to+code+basics)
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **开源项目**：[从零重造技术](https://github.com/codecrafters-io/build-your-own-x) · ★549,364 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：想真正理解“一个系统内部怎么运作”时用它。挑一个与你当前方向相关的做完。
- **开源项目**：[开发者路线图](https://github.com/nilbuild/developer-roadmap) · ★368,045 · NOASSERTION · 在用
  - 怎么用：当“我需要学什么”的检查表用，不当学习材料用。
- **开源项目**：[基于项目的学习清单](https://github.com/practical-tutorials/project-based-learning) · ★284,499 · MIT · 在用
  - 怎么用：学完基础语法后，从这里挑一个项目做完。只看不做等于没学。
- **开源项目**：[OSSU 计算机科学自学路径](https://github.com/ossu/computer-science) · ★209,437 · MIT · 在用
  - 怎么用：当索引看。国内学生优先换成 QSCTech/zju-icicles 或 PKUanonym/REKCARC-TSC-UHT 里对应的课程材料。
- **开源项目**：[Hello 算法](https://github.com/krahets/hello-algo) · ★130,460 · NOASSERTION · 在用
  - 怎么用：本仓库离散数学与计算单元的主要配套读物。先看动画建立直觉，再自己写一遍。
- **开源项目**：[微软 Web 开发入门（12 周课程）](https://github.com/microsoft/Web-Dev-For-Beginners) · ★96,763 · MIT · 在用
  - 怎么用：结构完整、有作业有测验，是“有人替你把关进度”的少数免费课程之一。
- **开源项目**：[清华计算机系课程攻略](https://github.com/PKUanonym/REKCARC-TSC-UHT) · ★37,641 · CC-BY-SA-4.0 · 在用
  - 怎么用：想了解“一门课真正要求到什么程度”时看它的作业与实验说明。

### uni-com-02 · 版本控制与可复现实验

大一 · **主干** · 主线：因果与证据

- **一年级版**：每次改完都拍一张照，以后能翻回任何一张。别人也能照着你说的步骤重做一遍。
- **第一性原理**：可复现意味着别人拿到代码、环境、数据、命令与随机种子，能得出同方向的结果。 不能复现的结果只能算观察，不能算证据。
- **与世界模型的连接**：这是本组织全部工程约定的最小版本：没有可复现依据的主张不成立。
- **出口标准**：能在另一台机器上照着文档跑出同方向的结论，并说出两次运行的差异在哪。
- **视频入口**：[B站：git 入门 版本控制 复现性](https://search.bilibili.com/all?keyword=git+%E5%85%A5%E9%97%A8+%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6+%E5%A4%8D%E7%8E%B0%E6%80%A7) · [官方微课：git 入门 版本控制 复现性](https://basic.smartedu.cn/search?keyword=git+%E5%85%A5%E9%97%A8+%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6+%E5%A4%8D%E7%8E%B0%E6%80%A7) · [YouTube：reproducible research practices](https://www.youtube.com/results?search_query=reproducible+research+practices) · [MIT OCW：reproducible research practices](https://ocw.mit.edu/search/?q=reproducible+research+practices)
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[Jupyter Notebook](https://github.com/jupyter/notebook) · ★13,361 · BSD-3-Clause · 在用
  - 怎么用：用它写实验记录：一步代码、一个结果、一句结论。这就是可复现实验的最小形式。

### uni-com-03 · 机器学习最小闭环

大三 · **主干** · 主线：变化与守恒

- **一年级版**：给机器很多例子，让它自己调参数，调到最后犯的错最小。
- **第一性原理**：学习等于“定义损失 + 求梯度 + 沿负梯度方向改参数”三件事的反复。 训练误差小不代表有用：能泛化才是目标，所以在没见过数据上的表现才是判据。
- **与世界模型的连接**：世界模型与一切学习系统的公共骨架。勘境的全部工作都建在这条闭环上。
- **出口标准**：能写出一段最小训练循环，并说明为什么必须留出验证集。
- **视频入口**：[B站：机器学习 入门 损失函数 梯度下降 泛化](https://search.bilibili.com/all?keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0+%E5%85%A5%E9%97%A8+%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0+%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D+%E6%B3%9B%E5%8C%96) · [官方微课：机器学习 入门 损失函数 梯度下降 泛化](https://basic.smartedu.cn/search?keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0+%E5%85%A5%E9%97%A8+%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0+%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D+%E6%B3%9B%E5%8C%96) · [YouTube：machine learning basics](https://www.youtube.com/results?search_query=machine+learning+basics) · [MIT OCW：machine learning basics](https://ocw.mit.edu/search/?q=machine+learning+basics)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[微软生成式 AI 入门（21 课）](https://github.com/microsoft/generative-ai-for-beginners) · ★120,485 · MIT · 在用
  - 怎么用：只在本仓库大学段基础过完之后进入。跳过数学直接学提示工程，会停在“会用不会判断”。
- **开源项目**：[PyTorch](https://github.com/pytorch/pytorch) · ★103,264 · NOASSERTION · 在用
  - 怎么用：用它验证链式法则：自己手推梯度，再和 autograd 的结果比。
- **开源项目**：[微软机器学习入门（12 周，26 课）](https://github.com/microsoft/ML-For-Beginners) · ★90,950 · MIT · 在用
  - 怎么用：大学段“机器学习最小闭环”的主要配套课程。先跑通它的第一个实验再谈别的。
- **开源项目**：[LLM 课程](https://github.com/mlabonne/llm-course) · ★83,126 · Apache-2.0 · 在用
  - 怎么用：当索引用，挑“科学”部分扫一遍建立术语表。
- **开源项目**：[动手学深度学习（中文）](https://github.com/d2l-ai/d2l-zh) · ★81,087 · Apache-2.0 · 在用
  - 怎么用：中文读者学深度学习的第一选择。数学不熟就一边看一边补微积分与线代。
- **开源项目**：[微软 AI 入门（12 周，24 课）](https://github.com/microsoft/AI-For-Beginners) · ★69,003 · MIT · 在用
  - 怎么用：比 ML-For-Beginners 更偏概念，适合先建立全局观再学具体算法。
- **开源项目**：[scikit-learn](https://github.com/scikit-learn/scikit-learn) · ★67,357 · BSD-3-Clause · 在用
  - 怎么用：用它对比不同模型在同一数据上的表现，训练集与测试集必须自己分好。
- **开源项目**：[深度学习（花书）中文翻译](https://github.com/exacity/deeplearningbook-chinese) · ★37,621 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：当参考书查，不要当教程顺读。第一部分（数学基础）值得通读。
- **开源项目**：[微软数据科学入门（10 周，20 课）](https://github.com/microsoft/Data-Science-For-Beginners) · ★37,300 · MIT · 在用
  - 怎么用：用来学“从一份脏数据到一个可信结论”的完整流程，这部分数学课不会教。
- **开源项目**：[JAX](https://github.com/jax-ml/jax) · ★36,333 · Apache-2.0 · 在用
  - 怎么用：想理解“函数式视角下的求导与向量化”时读它的教程，视角与 PyTorch 不同但更干净。
- **开源项目**：[OSSU 数据科学自学路径](https://github.com/ossu/data-science) · ★21,981 · NOASSERTION · 在用
  - 怎么用：在大学段概率与统计学完后当作应用路线的补充。
- **开源项目**：[机器学习实战（第三版）](https://github.com/ageron/handson-ml3) · ★14,207 · Apache-2.0 · 在用
  - 怎么用：每个 notebook 都跑一遍并改参数，是“最小闭环”最省力的练习路径。
- **开源项目**：[Spinning Up 强化学习](https://github.com/openai/spinningup) · ★11,971 · MIT · 在用
  - 怎么用：学“反馈与控制”之后读它，能把反馈回路与序列决策连起来。
- **开源项目**：[Hugging Face 课程](https://github.com/huggingface/course) · ★4,239 · Apache-2.0 · 在用
  - 怎么用：需要先有 PyTorch 与线性代数基础，再进来。
- **开源项目**：[神经网络与深度学习（蒲公英书）主站](https://github.com/nndl/nndl.github.io) · ★15 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：比花书更接近教学顺序，适合中文读者从零建立深度学习框架。

### uni-com-04 · 数值稳定性

大三 · **主干** · 主线：数量与度量

- **一年级版**：一步一步算的时候，前面的一点点小错会被后面放大成很大的错。
- **第一性原理**：有些算法对输入的一点点扰动极其敏感（病态），有些则稳定。 判断标准是条件数：输入相对变化放大多少倍到输出。
- **与世界模型的连接**：长期预测为何必然发散，答案在这里而不在“模型不够大”。
- **出口标准**：能说明为什么迭代很多步的系统一定会累积误差，并能举出一个放大机制。
- **视频入口**：[B站：数值分析 条件数 数值稳定性 误差放大](https://search.bilibili.com/all?keyword=%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90+%E6%9D%A1%E4%BB%B6%E6%95%B0+%E6%95%B0%E5%80%BC%E7%A8%B3%E5%AE%9A%E6%80%A7+%E8%AF%AF%E5%B7%AE%E6%94%BE%E5%A4%A7) · [官方微课：数值分析 条件数 数值稳定性 误差放大](https://basic.smartedu.cn/search?keyword=%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90+%E6%9D%A1%E4%BB%B6%E6%95%B0+%E6%95%B0%E5%80%BC%E7%A8%B3%E5%AE%9A%E6%80%A7+%E8%AF%AF%E5%B7%AE%E6%94%BE%E5%A4%A7)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）
- **开源项目**：[NumPy](https://github.com/numpy/numpy) · ★32,824 · NOASSERTION · 在用
  - 怎么用：把线性代数的矩阵运算亲手写一遍，再和 NumPy 的结果对照。
- **开源项目**：[Matplotlib](https://github.com/matplotlib/matplotlib) · ★23,262 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：每个数值实验都先画图再下结论。画图是最便宜的错误检查。
- **开源项目**：[SciPy](https://github.com/scipy/scipy) · ★15,038 · BSD-3-Clause · 在用
  - 怎么用：学优化时用它验证自己写的梯度下降是否收敛到同一个点。
- **开源项目**：[机器学习实战（第三版）](https://github.com/ageron/handson-ml3) · ★14,207 · Apache-2.0 · 在用
  - 怎么用：每个 notebook 都跑一遍并改参数，是“最小闭环”最省力的练习路径。
- **开源项目**：[科学计算讲义](https://github.com/scipy-lectures/scientific-python-lectures) · ★3,217 · NOASSERTION · 在用
  - 怎么用：大学段一切数值实验的工具手册。遇错先查这里，再查搜索引擎。

### uni-com-05 · 从代码到证据

大三 · **主干** · 主线：因果与证据

- **一年级版**：跑出好看的数不等于发现规律，要能证明不是因为巧合。
- **第一性原理**：一个结论要被接受，需要对照、可失败的检验与随机的重复。 能失败的检验才有信息量：永远不会失败的检查等于没检查。
- **与世界模型的连接**：这条是本组织文件里重复次数最多的一句。缺了它，全部实验都无法解释。
- **出口标准**：能给自己刚做的实验补上一条对照组，并说出如果结论是错的，这条对照会怎样显示出来。
- **视频入口**：[B站：实验设计 对照组 消融实验 可失败检验](https://search.bilibili.com/all?keyword=%E5%AE%9E%E9%AA%8C%E8%AE%BE%E8%AE%A1+%E5%AF%B9%E7%85%A7%E7%BB%84+%E6%B6%88%E8%9E%8D%E5%AE%9E%E9%AA%8C+%E5%8F%AF%E5%A4%B1%E8%B4%A5%E6%A3%80%E9%AA%8C) · [官方微课：实验设计 对照组 消融实验 可失败检验](https://basic.smartedu.cn/search?keyword=%E5%AE%9E%E9%AA%8C%E8%AE%BE%E8%AE%A1+%E5%AF%B9%E7%85%A7%E7%BB%84+%E6%B6%88%E8%9E%8D%E5%AE%9E%E9%AA%8C+%E5%8F%AF%E5%A4%B1%E8%B4%A5%E6%A3%80%E9%AA%8C)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）

## 信息与系统（4 个知识点）

> 信息论只回答一件事：什么叫做“知道了”。它把“不确定减少了多少”变成了可计算的量， 于是“学习”“预测”“惊讶”都有了数值。

### uni-inf-01 · 信息量与比特

大三 · **主干** · 主线：数量与度量

- **一年级版**：一件事越难猜，它发生了告诉你的东西就越多。
- **第一性原理**：信息量随概率减小而增大，且独立事件的信息量相加。 满足这两条的函数只有对数形式，所以信息量以 log 的倒数计。
- **与世界模型的连接**：“惊讶程度”可以被量化，这是学习理论中损失函数设计的来源之一。
- **出口标准**：能算出一个事件的信息量，并说明为什么必然事件的信息量为零。
- **视频入口**：[B站：信息论 信息量 比特 熵](https://search.bilibili.com/all?keyword=%E4%BF%A1%E6%81%AF%E8%AE%BA+%E4%BF%A1%E6%81%AF%E9%87%8F+%E6%AF%94%E7%89%B9+%E7%86%B5) · [官方微课：信息论 信息量 比特 熵](https://basic.smartedu.cn/search?keyword=%E4%BF%A1%E6%81%AF%E8%AE%BA+%E4%BF%A1%E6%81%AF%E9%87%8F+%E6%AF%94%E7%89%B9+%E7%86%B5) · [YouTube：information theory intuition](https://www.youtube.com/results?search_query=information+theory+intuition) · [MIT OCW：information theory intuition](https://ocw.mit.edu/search/?q=information+theory+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）

### uni-inf-02 · 熵与压缩极限

大三 · **主干** · 主线：尺度与极限

- **一年级版**：内容越有规律，能压得越小；完全随机的数据一个字都压不掉。
- **第一性原理**：熵是平均信息量，它给出无损压缩的下限。这个下限无法突破， 因为压缩本质上就是利用规律性。
- **与世界模型的连接**：“能压多小”是衡量数据里有多少结构的直接指标。它同时告诉我们生成有多少自由度。
- **出口标准**：能说明为什么纯随机数据无法被压缩，以及为什么压缩率可以看作复杂度的度量。
- **视频入口**：[B站：信息论 熵 信源编码 压缩极限](https://search.bilibili.com/all?keyword=%E4%BF%A1%E6%81%AF%E8%AE%BA+%E7%86%B5+%E4%BF%A1%E6%BA%90%E7%BC%96%E7%A0%81+%E5%8E%8B%E7%BC%A9%E6%9E%81%E9%99%90) · [官方微课：信息论 熵 信源编码 压缩极限](https://basic.smartedu.cn/search?keyword=%E4%BF%A1%E6%81%AF%E8%AE%BA+%E7%86%B5+%E4%BF%A1%E6%BA%90%E7%BC%96%E7%A0%81+%E5%8E%8B%E7%BC%A9%E6%9E%81%E9%99%90)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[Khan Academy · Computing](https://www.khanacademy.org/computing)（Khan Academy）

### uni-inf-03 · 反馈与控制

大三 · **主干** · 主线：系统与反馈

- **一年级版**：走路时眼睛一直看着偏了多少，偏了就修正，所以不会摔。
- **第一性原理**：开环控制按预先计划走，闭环控制根据实际偏差修正。 反馈带来稳定，但延迟过大会产生振荡甚至失控——增益不能无限加大。
- **与世界模型的连接**：世界模型在规划中的角色就是“提前试算”，而闭环纠错是落地的必备部分。
- **出口标准**：能说出一个反馈系统在什么条件下会振荡，并说明延迟起了什么作用。
- **视频入口**：[B站：控制论 反馈 闭环 稳定性 振荡](https://search.bilibili.com/all?keyword=%E6%8E%A7%E5%88%B6%E8%AE%BA+%E5%8F%8D%E9%A6%88+%E9%97%AD%E7%8E%AF+%E7%A8%B3%E5%AE%9A%E6%80%A7+%E6%8C%AF%E8%8D%A1) · [官方微课：控制论 反馈 闭环 稳定性 振荡](https://basic.smartedu.cn/search?keyword=%E6%8E%A7%E5%88%B6%E8%AE%BA+%E5%8F%8D%E9%A6%88+%E9%97%AD%E7%8E%AF+%E7%A8%B3%E5%AE%9A%E6%80%A7+%E6%8C%AF%E8%8D%A1) · [YouTube：control theory feedback](https://www.youtube.com/results?search_query=control+theory+feedback) · [MIT OCW：control theory feedback](https://ocw.mit.edu/search/?q=control+theory+feedback)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **开源项目**：[系统设计入门](https://github.com/donnemartin/system-design-primer) · ★371,615 · NOASSERTION · 在用
  - 怎么用：在本仓库的信息与系统单元之后读，把反馈、噪声、可靠性的概念落到真实架构上。
- **开源项目**：[Spinning Up 强化学习](https://github.com/openai/spinningup) · ★11,971 · MIT · 在用
  - 怎么用：学“反馈与控制”之后读它，能把反馈回路与序列决策连起来。

### uni-inf-04 · 噪声与信噪比

大三 · 主线：数量与度量

- **一年级版**：信号弱、杂音大的时候，喊得再大声也没用，要把杂音压下去。
- **第一性原理**：可检出的最小变化受噪声水平限制。提高信噪比的办法是平均多次 （噪声按根号 N 下降，信号线性累积）或改善测量条件。
- **与世界模型的连接**：任何测量的分辨率都由噪声决定。报告结论必须同时报告噪声水平。
- **出口标准**：能算出把噪声降低一半需要多少倍的数据量。
- **视频入口**：[B站：信号处理 信噪比 噪声 平均降噪](https://search.bilibili.com/all?keyword=%E4%BF%A1%E5%8F%B7%E5%A4%84%E7%90%86+%E4%BF%A1%E5%99%AA%E6%AF%94+%E5%99%AA%E5%A3%B0+%E5%B9%B3%E5%9D%87%E9%99%8D%E5%99%AA) · [官方微课：信号处理 信噪比 噪声 平均降噪](https://basic.smartedu.cn/search?keyword=%E4%BF%A1%E5%8F%B7%E5%A4%84%E7%90%86+%E4%BF%A1%E5%99%AA%E6%AF%94+%E5%99%AA%E5%A3%B0+%E5%B9%B3%E5%9D%87%E9%99%8D%E5%99%AA)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **开源项目**：[系统设计入门](https://github.com/donnemartin/system-design-primer) · ★371,615 · NOASSERTION · 在用
  - 怎么用：在本仓库的信息与系统单元之后读，把反馈、噪声、可靠性的概念落到真实架构上。

## 数学方法（4 个知识点）

> 这一组是把数学“当工具用”的通用语言。它们的共同点是：换一个域， 难问题变简单问题。

### uni-met-01 · 傅里叶变换

大二 · **主干** · 主线：变化与守恒

- **一年级版**：任何一段波形都能拆成很多不同快慢的波，加起来正好是它。
- **第一性原理**：傅里叶变换把信号从“随时间的形状”换成“各频率的强度”。 卷积在时域难算，在频域是逐点相乘——同一件事在另一个域里变简单了。
- **与世界模型的连接**：换基改变问题难度。这条经验在表示学习里同样成立，而且是其核心动机。
- **出口标准**：能说明卷积定理为什么让计算变简单，并解释“高频”对应图像里的什么。
- **视频入口**：[B站：傅里叶变换 频域 卷积定理](https://search.bilibili.com/all?keyword=%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2+%E9%A2%91%E5%9F%9F+%E5%8D%B7%E7%A7%AF%E5%AE%9A%E7%90%86) · [官方微课：傅里叶变换 频域 卷积定理](https://basic.smartedu.cn/search?keyword=%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2+%E9%A2%91%E5%9F%9F+%E5%8D%B7%E7%A7%AF%E5%AE%9A%E7%90%86) · [YouTube：Fourier transform intuition](https://www.youtube.com/results?search_query=Fourier+transform+intuition) · [MIT OCW：Fourier transform intuition](https://ocw.mit.edu/search/?q=Fourier+transform+intuition)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[Manim（3Blue1Brown 动画引擎）](https://github.com/3b1b/manim) · ★94,227 · MIT · 在用
  - 怎么用：想真正理解一个概念，就用它把概念画出来。能画出来说明真的懂了。
- **开源项目**：[Manim 社区版](https://github.com/ManimCommunity/manim) · ★41,039 · MIT · 在用
  - 怎么用：新用户从这一版开始，不要从原版开始。
- **开源项目**：[数学资源索引](https://github.com/rossant/awesome-math) · ★16,478 · CC0-1.0 · 在用
  - 怎么用：遇到本仓库没展开的主题（拓扑、数论、代数几何）时，用它找入口。
- **开源项目**：[Hugging Face 课程](https://github.com/huggingface/course) · ★4,239 · Apache-2.0 · 在用
  - 怎么用：需要先有 PyTorch 与线性代数基础，再进来。
- **开源项目**：[科学计算讲义](https://github.com/scipy-lectures/scientific-python-lectures) · ★3,217 · NOASSERTION · 在用
  - 怎么用：大学段一切数值实验的工具手册。遇错先查这里，再查搜索引擎。

### uni-met-02 · 复变函数与解析性

大二 · 主线：结构与层次

- **一年级版**：用带方向的数算题，很多看起来无关的公式会突然变成同一件事。
- **第一性原理**：解析函数由局部信息决定整体（柯西积分公式），这比实函数强得多。 留数定理把复杂的实积分换成数几个点。
- **与世界模型的连接**：“局部决定整体”是很强的附加结构。给系统加结构性约束，常常让问题变得可解。
- **出口标准**：能说明为什么解析函数比一般光滑函数“更受约束”。
- **视频入口**：[B站：复变函数 解析函数 留数定理](https://search.bilibili.com/all?keyword=%E5%A4%8D%E5%8F%98%E5%87%BD%E6%95%B0+%E8%A7%A3%E6%9E%90%E5%87%BD%E6%95%B0+%E7%95%99%E6%95%B0%E5%AE%9A%E7%90%86) · [官方微课：复变函数 解析函数 留数定理](https://basic.smartedu.cn/search?keyword=%E5%A4%8D%E5%8F%98%E5%87%BD%E6%95%B0+%E8%A7%A3%E6%9E%90%E5%87%BD%E6%95%B0+%E7%95%99%E6%95%B0%E5%AE%9A%E7%90%86)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）

### uni-met-03 · 优化

大三 · **主干** · 主线：尺度与极限

- **一年级版**：在一个有坡度的地方找最低点，一直朝下坡走就会到。
- **第一性原理**：凸问题的局部最优就是全局最优；非凸问题则没有这个保证。 学习率决定步长：太大跳过谷底振荡，太小走不到。
- **与世界模型的连接**：训练世界模型就是解一个非凸优化问题。知道它的失败模式，比知道成功案例重要。
- **出口标准**：能解释为什么学习率太大会发散，并说明凸与非凸的区别在实践上意味着什么。
- **视频入口**：[B站：优化理论 梯度下降 凸优化 学习率](https://search.bilibili.com/all?keyword=%E4%BC%98%E5%8C%96%E7%90%86%E8%AE%BA+%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D+%E5%87%B8%E4%BC%98%E5%8C%96+%E5%AD%A6%E4%B9%A0%E7%8E%87) · [官方微课：优化理论 梯度下降 凸优化 学习率](https://basic.smartedu.cn/search?keyword=%E4%BC%98%E5%8C%96%E7%90%86%E8%AE%BA+%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D+%E5%87%B8%E4%BC%98%E5%8C%96+%E5%AD%A6%E4%B9%A0%E7%8E%87) · [YouTube：gradient descent optimization](https://www.youtube.com/results?search_query=gradient+descent+optimization) · [MIT OCW：gradient descent optimization](https://ocw.mit.edu/search/?q=gradient+descent+optimization)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[3Blue1Brown（英文站）](https://www.3blue1brown.com/)（3Blue1Brown）
- **开源项目**：[JAX](https://github.com/jax-ml/jax) · ★36,333 · Apache-2.0 · 在用
  - 怎么用：想理解“函数式视角下的求导与向量化”时读它的教程，视角与 PyTorch 不同但更干净。
- **开源项目**：[SciPy](https://github.com/scipy/scipy) · ★15,038 · BSD-3-Clause · 在用
  - 怎么用：学优化时用它验证自己写的梯度下降是否收敛到同一个点。
- **开源项目**：[神经网络与深度学习（蒲公英书）主站](https://github.com/nndl/nndl.github.io) · ★15 · NO-LICENSE（未声明） · 未声明许可证
  - 怎么用：比花书更接近教学顺序，适合中文读者从零建立深度学习框架。

### uni-met-04 · 变分法与泛函

大三 · 主线：变化与守恒

- **一年级版**：不是问“哪个数最小”，而是问“哪条曲线最好”。
- **第一性原理**：泛函把函数映到数，变分法求泛函的极值。 它给出物理学里的最小作用量原理，也给出机器学习里的变分推断。
- **与世界模型的连接**：把优化对象从点扩展到函数，是把方法一般化的标准操作。
- **出口标准**：能说明“对函数求极值”与“对点求极值”在方法上的异同。
- **视频入口**：[B站：变分法 泛函 欧拉方程 变分推断](https://search.bilibili.com/all?keyword=%E5%8F%98%E5%88%86%E6%B3%95+%E6%B3%9B%E5%87%BD+%E6%AC%A7%E6%8B%89%E6%96%B9%E7%A8%8B+%E5%8F%98%E5%88%86%E6%8E%A8%E6%96%AD) · [官方微课：变分法 泛函 欧拉方程 变分推断](https://basic.smartedu.cn/search?keyword=%E5%8F%98%E5%88%86%E6%B3%95+%E6%B3%9B%E5%87%BD+%E6%AC%A7%E6%8B%89%E6%96%B9%E7%A8%8B+%E5%8F%98%E5%88%86%E6%8E%A8%E6%96%AD)
- **整站资源**：[中国大学MOOC](https://www.icourse163.org/)（高教社 / 网易）
- **整站资源**：[MIT OpenCourseWare](https://ocw.mit.edu/)（MIT）
