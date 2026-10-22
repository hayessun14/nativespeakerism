# 组 11／组 12 关键词质性分类编码报告

> **状态：编码过程记录（concordance 消解前）**
> 本文档保留编码当时的判断与未决理由，作为审计轨迹，内容不随后续消解改写。
> 其中的占比数字计算于 PENDING 尚未消解之时，**已不是现行口径**；
> 最终统计以 [`final_report.md`](final_report.md) 及各组 `group*_tables.md` 为准。

## Baseline ↔ L1（RQ3 第二对；十二组编码至此完成）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：组 11 全部 30 词位、组 12 全部 26 词位
> **编码复用**：组 11 沿用 23／30、组 12 沿用 23／26（note 以〔沿用组 N〕标注），新编分别为 7 项与 3 项。复用对推论的限制同组 9／组 10 报告的开篇说明。

> ### ⚠ 分母警告
> 两组各仅 8 个维度一已定标签、7 个 act 层已定标签。**本报告不给出任何有实质含义的百分比**；组 11 的「G1 100%」是 8/8，不构成分布事实。本对语料的证据价值在于**清单规模本身与词位的性质**，不在占比。

---

## 一、结果摘要

| 层 | 组 11（Baseline 侧过量） | 组 12（L1 侧过量） |
|---|---|---|
| 维度一 | 已定 8：G1 8 ／ **G2 0** | 已定 8：G1 4 ／ G2 4 |
| 维度二 act | 已定 7：A1 5／A2 1／A3 1 | 已定 7：A3 4／A2 2／A1 1 |
| 维度二 hedge | 已定 2：`may`、`fairly` | 已定 **0**，PENDING 0 |
| 维度三 | **C1 0，PENDING 0** | **C1 0，PENDING 0** |
| 最高 LL ／ 最高 LR | 17.533 ／ 1.089 | 13.248 ／ 1.056 |

---

## 二、本对语料的第一个事实：几乎没有可比的差异

### 2.1 效应量与清单规模

十二组中，本对是唯一两个方向的**最高 LL 都低于 20、最高 LR 都在 1.1 以下**的语料对。作为对照：

| 语料对 | 目标侧最高 LL | 目标侧最高 LR |
|---|---:|---:|
| German ↔ Chinese | 668.504（`german`） | 9.902 |
| German ↔ Generic | 647.497（`german`） | 7.351 |
| Chinese ↔ Generic | 77.135（`chinese`） | 5.965 |
| Baseline ↔ Generic | 74.303（`paper`） | 3.002（`correctness`） |
| L1 ↔ Generic | 60.215（`CLAIM`） | 3.284（`correctness`） |
| **Baseline ↔ L1** | **17.533**（`your`） | **1.089**（`expert`） |

组 11 的头名 `your`（LL 17.533）是一个人称代词，Freq 5617 : 5226——即两个条件都在 348 篇中每篇用几十次，差异只有约 7%。这就是本对语料能找到的最强信号。

### 2.2 维度三：两个方向都彻底归零

**组 11 与组 12 的 56 个词位中，没有任何一个被编为 C1，也没有任何一个进入 C1 待定。** 这是十二组中唯一一对在两个方向上都实现 C1 双零的语料对（组 4、组 8 是单向双零）。

至此维度三的完整形态（十二组全部编码完成）：

| 条件 | 确定 C1 | 候选（含待定） | 说明 |
|---|---:|---|---|
| **Baseline** | **0** | **相对 Generic 0；相对 L1 0** | 两个参照系下都无任何身份材料 |
| **L1** | **0** | 相对 Generic 1（`cultural`，疑为议题残留）；**相对 Baseline 0** | — |
| Generic | 0 | 相对 L1 4；相对 Baseline 4；相对 Chinese／German **0** | 身份词汇只相对「不被标记」而言存在 |
| Chinese | 1 | `chinese` ＋ 2 待定 | 无迁移框架词 |
| German | 3 | `german`、`SPEAKER`、`transfer` ＋ 最多 9 待定 | 唯一含显性迁移框架的条件 |

### 2.3 RQ3 闭合

组 9／组 10 报告已用清单重合度给出答案（Baseline–L1 重合 47%／56%，其余配对 1%–11%）。本对提供了该答案的**直接检验**：当 Baseline 与 L1 被直接放在一起对比时，

- 通过筛选的关键词只有 56 个（六对中最少，约为 Baseline↔Generic 的五分之一）；
- 最强效应量不足其他各对的十分之一；
- 语言身份维度**完全空白**。

**RQ3 的答案**：无标记 baseline 条件在关键词层面**与被标记为英语母语者的条件近乎不可区分**。这意味着：模型的默认写作者预设就是母语者；「非母语者」标签不是在中性起点上增加信息，而是使反馈**偏离**默认状态。

这一表述对 RQ1 的意义值得点出：组 1／组 2 观察到的 L1 与 Generic 之差，不能读作「两个方向各自偏离中点」，而应读作**Generic 单方向偏离了默认**。

---

## 三、维度一与维度二：小分母下能说与不能说的

### 3.1 组 11 的 G2 = 0

组 11 的 8 个维度一已定标签全部是 G1，且全部集中在论证材料层：`evidence`、`expert`、`views`、`anecdote`、`counterargument`、`opposing`、`discussing`、`balanced`。**没有任何一项局部词汇。** 组 12 的 8 项则是 G1 4（`underdeveloped`、`material`、`logic`、`defensible`）对 G2 4（`sentence`、`cut`、`word`、`punctuation`）。

敏感性检验：组 11 即使 5 个 PENDING 全归 G2，G1 仍占 61.5%；组 12 区间为 [28.6%, 71.4%]，横跨 50%。**组 12 无法判定方向，组 11 只能说「未见局部倾斜」**——考虑到 8 这个分母，连后者也只是弱陈述。

### 3.2 组 11 的 A1 = 5，是十二组中唯一 A1 占多数的清单

组 11 的 act 层：A1 5（`accurate`、`effectively`、`engaging`、`promising`、`balanced`）、A2 1、A3 1。这是十二组中**唯一一个赞扬词多于建议词的清单**——此前十一组里 A1 从未超过 A2 与 A3。

必须立刻加上三重限制：分母只有 7；四个 act 层 PENDING 未计入；且这 5 项全部属于组 1 报告 §5.2 指出的「目标态框架」高风险类（正向形容词可能实为 A3 的一部分）。**因此这不构成「baseline 条件赞扬更多」的证据**，只能作为一条待验证线索记录：若 concordance 确认它们处于评价框架而非目标态框架，则「无标记条件相对母语者标记条件略偏赞扬」将是一个可报告的细微差异；若否，本对语料在 act 层就没有任何差异。

### 3.3 hedge

组 11 有 `may`、`fairly` 两项，组 12 为 0 且无待定。方向提示 Baseline 略多于 L1，但两项的 LL 分别为 4.615 与 4.584——**都刚过 3.84 的显著性门槛**。不作方向判断。

---

## 四、十二组跨组一致性检查（本轮执行）

组 4 报告 §5 曾提出：跨组一致性检查应作为一道独立工序，在十二组全部完成后统一执行。本轮已执行机械扫描部分。

**扫描范围**：十二组共 891 个词位记录，涉及 **491 个唯一词形**，其中 **290 个出现在两组或以上**。
**扫描方法**：比对同一词形在不同组的五个编码字段（d1／d1sub／act／hedge／c）是否完全一致。

**结果：891 条记录中，编码不一致者仅 1 处。**

| 词形 | 组 1 | 组 9 |
|---|---|---|
| `tackles` | act = **A1** | act = **PENDING** |

这正是组 9／组 10 报告 §4.1 中**有意保留**的那一处：组 4 已认定 `tackles`（组 1，A1）与 `raises`（组 4，PENDING）构式相同而判定不一致，本人认为 PENDING 为正确处理，故在组 9 改判，同时不追溯改动组 1 的第一轮记录。

**除此之外零冲突。** 这一结果部分归功于组 9 起采用的编码复用机制（相同词形直接沿用既有编码），因此它**不能作为编码者判断稳定性的证据**——它证明的是记录层面的一致性，不是判断层面的可靠性。判断可靠性仍须由两周后的 intra-rater κ 提供。

**待办**：`tackles` 与 `raises` 并案 concordance，判定后统一回填组 1、组 4、组 9 三处，并在修订日志中记为「跨组一致性复核」。

---

## 五、数据问题

### 5.1 议题内容残留

组 11、组 12 均**无确认残留**，也无疑似项。与组 7 一样，是十二组中少数干净的清单。

### 5.2 口径效应实例增至九个

本轮新增三例：`counterargument`（组 11，单数）vs `counterarguments`（组 1）vs 归并 `COUNTERARGUMENT`（组 9）——**同一词族在三组呈现三种形态**，是全研究最完整的一个口径效应实例；`sentence`（组 12）vs `sentences`（组 2）vs 归并 `SENTENCE`（组 10）；`ones`（组 12）vs 归并 `ONE`（组 10）。

连同此前的 `word`／`WORD`、`claims`／`CLAIM`、`use`／`USE`、`strengths`／`STRENGTH`、`gives`／`GIVE`，共九例。建议方法部分以 `counterargument` 三形态为主例。

### 5.3 手册 v3 强制查询清单仍未获得

两组均无清单已知条目。累计待重扫词位：835 ＋ 30 ＋ 26 = **891 个（即全部）**。

---

## 六、十二组编码完成后的下一步

1. **补齐 v3 强制查询清单**，重扫全部 891 个词位（491 个唯一词形）。这一步应先于 concordance，因为它可能改变待办清单构成。
2. **确定内容动词统一判定规则**（组 5／组 6 报告 §5），写入手册 v4。
3. **执行 concordance**，优先级：
   - `false` 右搭配（判定 false friends，成本极低）
   - `natural`／`unnatural`／`sounds`（判定唯一的「规范型」C1）
   - `chinese` 子类（判定中文条件是否含迁移归因）
   - `tackles`／`raises` 并案（跨组一致性回填）
   - `english`／`language`／`background`／`influenced`／`speaking`（维度三候选池）
   - 第三人称代词群 `she`／`he`／`her`／`people`（议题残留统一判定）
4. **重算全部敏感性区间**，以 concordance 后的值定稿，特别是组 1／组 2（唯一仍存在实质重叠区 [56.0, 68.9] 的一对）。
5. **两周后重编码 15%**：十二组 891 词位抽 134 项，计算 intra-rater κ。第一轮记录已由本分支的 commit 序列固定时间戳。
6. **维度三的 Szczepanik 式深度分析**（交接文档已规划）：跨条件频率百分比 → LL → Log Ratio → concordance 共现。

---

# 附表：组 11（Baseline → L1）

## 附表 A：组 11 完整编码表（30 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | your | 5617 | 17.533 | 0.115 | NA | — | NA | NA | NA | M | 人称代词，无固定层级所指〔沿用组 2〕 |
| 2 | accurate | 79 | 11.057 | 0.888 | PENDING | — | A1 | NA | NA | — | 维度一待定：accurate facts(G1-Dev)vs accurate grammar(G2)；正向评价〔沿用组 2〕 |
| 3 | evidence | 1543 | 9.338 | 0.163 | G1 | Development | NA | NA | NA | H | Development 核心〔沿用组 1〕 |
| 4 | presents | 51 | 7.688 | 0.928 | NA | — | NA | NA | NA | M | 描述性框架动词（your essay presents…）；同组 8 shows 口径 |
| 5 | revised | 81 | 7.642 | 0.707 | NA | — | NA | NA | NA | M | 与 original 配对的改写对照，元话语〔沿用组 2〕 |
| 6 | expert | 38 | 7.454 | 1.089 | G1 | Development | NA | NA | NA | M | expert sources/opinion，证据来源类型 |
| 7 | editing | 75 | 7.239 | 0.716 | PENDING | — | A3 | NA | NA | — | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit／组 9 EDIT 口径 |
| 8 | effectively | 120 | 6.661 | 0.525 | NA | — | A1 | NA | NA | M | effectively argues／effectively supports，方式副词但携正向评价；与组 2 effective 同族，目标态框架风险〔沿用组 9〕 |
| 9 | helps | 89 | 6.352 | 0.604 | NA | — | NA | NA | NA | M | 描述性动词（this helps the reader）〔沿用组 2〕 |
| 10 | engaging | 98 | 6.095 | 0.559 | NA | — | A1 | NA | NA | M | an engaging introduction，正向评价；目标态框架风险 |
| 11 | views | 77 | 5.990 | 0.634 | G1 | Ideas | NA | NA | NA | M | opposing views，反驳层；同组 8 opposing 口径〔沿用组 9〕 |
| 12 | suggestion | 101 | 5.888 | 0.540 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3）〔沿用组 3〕 |
| 13 | concerns | 110 | 5.718 | 0.507 | NA | — | A2 | NA | NA | M | my main concerns are…，批评标记语〔沿用组 1〕 |
| 14 | promising | 51 | 5.666 | 0.776 | NA | — | A1 | NA | NA | M | a promising start，正向评价；目标态框架风险〔沿用组 9〕 |
| 15 | paper | 265 | 5.379 | 0.306 | NA | — | NA | NA | NA | H | 文本指称语，不指示层级〔沿用组 1〕 |
| 16 | deserves | 57 | 4.943 | 0.674 | NA | — | PENDING | NA | NA | — | act 层待定：this point deserves more attention＝隐性建议（A3）vs 正向评价（A1）〔沿用组 9〕 |
| 17 | additionally | 36 | 4.757 | 0.859 | NA | — | NA | NA | NA | M | 连接副词〔沿用组 9〕 |
| 18 | may | 361 | 4.615 | 0.240 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 2〕 |
| 19 | anecdote | 111 | 4.596 | 0.448 | G1 | Development | NA | NA | NA | H | 证据类型〔沿用组 1〕 |
| 20 | fairly | 84 | 4.584 | 0.520 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge〔沿用组 1〕 |
| 21 | clearly | 434 | 4.455 | 0.214 | PENDING | — | NA | NA | NA | — | 维度一待定（clear 系）；方式副词，act 层不赋值〔沿用组 2〕 |
| 22 | counterargument | 263 | 4.362 | 0.275 | G1 | Ideas | NA | NA | NA | H | Ideas 明示。注：组 1 为 counterarguments、组 9 为归并 COUNTERARGUMENT，本组为单数单独入选，系口径效应 |
| 23 | citations | 159 | 4.341 | 0.358 | PENDING | — | NA | NA | NA | — | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics)；同组 10 citation 口径 |
| 24 | forward | 44 | 4.239 | 0.715 | NA | — | NA | NA | NA | M | going forward / put forward〔沿用组 5〕 |
| 25 | explain | 601 | 4.230 | 0.176 | NA | — | PENDING | NA | NA | — | act 层待定：you explain X well（描述 NA）vs explain this further（A3）。属"内容动词"类，见报告 §5〔沿用组 5〕 |
| 26 | repeated | 72 | 4.156 | 0.537 | PENDING | — | NA | NA | NA | — | 维度一待定：repeated errors(G2)vs repeated ideas(G2-Local，手册 repetitive 口径)vs 论点重复(G1)〔沿用组 9〕 |
| 27 | discussing | 74 | 4.029 | 0.520 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：you discuss X（描述）vs discuss counterarguments（A3）；内容动词类 |
| 28 | opposing | 152 | 4.019 | 0.352 | G1 | Ideas | NA | NA | NA | H | opposing views，反驳层〔沿用组 8〕 |
| 29 | balanced | 76 | 3.909 | 0.504 | G1 | Ideas | A1 | NA | NA | M | a balanced argument/view，域固定于论断；正向评价〔沿用组 2〕 |
| 30 | current | 97 | 3.903 | 0.441 | NA | — | NA | NA | NA | M | 元话语现状框架（your current draft），同组 1 currently〔沿用组 5〕 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 8 | 100.0% | 2334 | 100.0% | 0.498 |
| **已定标签合计** | **8** | **100.0%** | **2334** | **100.0%** | — |
| N/A（不计入分母） | 17 | — | — | — | — |
| PENDING（不计入分母） | 5 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

**子类分布（分母同为已定标签 8）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 3 | 37.5% |
| G1 | Ideas | 5 | 62.5% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A1 | 5 | 71.4% | 424 | 69.6% | 0.650 |
| A3 | 1 | 14.3% | 75 | 12.3% | 0.716 |
| A2 | 1 | 14.3% | 110 | 18.1% | 0.507 |
| **已定标签合计** | **7** | **100.0%** | **609** | **100.0%** | — |
| N/A（不计入分母） | 19 | — | — | — | — |
| PENDING（不计入分母） | 4 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 2 | 100.0% | 445 | 100.0% | 0.380 |
| **已定标签合计** | **2** | **100.0%** | **445** | **100.0%** | — |
| N/A（不计入分母） | 28 | — | — | — | — |
| PENDING（不计入分母） | 0 | — | — | — | — |
| 清单总数 | 30 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 30 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 30 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 5 | 0 | **5** |
| **A2** | 0 | 1 | 0 | **1** |
| **A3** | 0 | 1 | 0 | **1** |
| **NA** | 2 | 17 | 0 | **19** |
| **PENDING** | 0 | 4 | 0 | **4** |
| **合计** | 2 | 28 | 0 | **30** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 1 | 0 | 0 | 6 | 1 | **8** |
| **G2** | 0 | 0 | 0 | 0 | 0 | **0** |
| **NA** | 3 | 1 | 0 | 10 | 3 | **17** |
| **PENDING** | 1 | 0 | 1 | 3 | 0 | **5** |
| **合计** | 5 | 1 | 1 | 19 | 4 | **30** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 4 | 0 | 14 | 2 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 8 | 0 | 100.0% |
| 5 个 PENDING 全归 G1（上界） | 13 | 0 | 100.0% |
| 5 个 PENDING 全归 G2（下界） | 8 | 5 | 61.5% |

### B9 concordance 待办清单

共 **9** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `accurate` | 79 | 维度一 | 维度一待定：accurate facts(G1-Dev)vs accurate grammar(G2)；正向评价〔沿用组 2〕 |
| `editing` | 75 | 维度一 | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit／组 9 EDIT 口径 |
| `suggestion` | 101 | act | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3）〔沿用组 3〕 |
| `deserves` | 57 | act | act 层待定：this point deserves more attention＝隐性建议（A3）vs 正向评价（A1）〔沿用组 9〕 |
| `clearly` | 434 | 维度一 | 维度一待定（clear 系）；方式副词，act 层不赋值〔沿用组 2〕 |
| `citations` | 159 | 维度一 | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics)；同组 10 citation 口径 |
| `explain` | 601 | act | act 层待定：you explain X well（描述 NA）vs explain this further（A3）。属"内容动词"类，见报告 §5〔沿用组 5〕 |
| `repeated` | 72 | 维度一 | 维度一待定：repeated errors(G2)vs repeated ideas(G2-Local，手册 repetitive 口径)vs 论点重复(G1)〔沿用组 9〕 |
| `discussing` | 74 | act | act 层待定：you discuss X（描述）vs discuss counterarguments（A3）；内容动词类 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|

# 附表：组 12（L1 → Baseline）

## 附表 A：组 12 完整编码表（26 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | consistent | 135 | 13.248 | 0.726 | PENDING | — | NA | NA | NA | — | 维度一待定：consistent tense(G2)vs consistent argument(G1)；同组 2 consistency 口径〔沿用组 10〕 |
| 2 | sentence | 942 | 9.321 | 0.211 | G2 | Local Structure | NA | NA | NA | H | Local Structure 明示。注：组 2 为 sentences、组 10 为归并 SENTENCE，本组为单数单独入选，系口径效应 |
| 3 | think | 84 | 8.471 | 0.738 | NA | — | NA | NA | NA | M | I think…＝人称归因，属手册排除的缓和策略，不入 M1〔沿用组 10〕 |
| 4 | above | 44 | 8.147 | 1.056 | NA | — | NA | NA | NA | M | 指示元话语（see above）〔沿用组 6〕 |
| 5 | cut | 90 | 6.738 | 0.623 | G2 | Local Structure | A3 | NA | NA | M | 删削冗余，句内/句间〔沿用组 1〕 |
| 6 | recurring | 41 | 6.420 | 0.954 | NA | — | NA | NA | NA | M | recurring errors/patterns，层级由宾语决定；构成"错误模式化"框架〔沿用组 2〕 |
| 7 | underdeveloped | 65 | 6.377 | 0.726 | G1 | Development | A2 | NA | NA | H | Development 域固定，负向〔沿用组 1〕 |
| 8 | check | 101 | 6.242 | 0.560 | PENDING | — | A3 | NA | NA | — | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示〔沿用组 2〕 |
| 9 | paragraph | 1688 | 5.672 | 0.121 | PENDING | — | NA | NA | NA | — | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1〔沿用组 10〕 |
| 10 | then | 382 | 5.397 | 0.254 | NA | — | NA | NA | NA | H | 连接副词〔沿用组 1〕 |
| 11 | third | 51 | 5.352 | 0.755 | NA | — | NA | NA | NA | M | 序数词，反馈条目枚举〔沿用组 10〕 |
| 12 | material | 166 | 5.204 | 0.387 | G1 | Development | NA | NA | NA | M | source material，属支撑材料〔沿用组 1〕 |
| 13 | ones | 62 | 5.114 | 0.658 | NA | — | NA | NA | NA | M | 指代词。注：组 10 为归并 ONE（one+ones），本组为 ones 单独入选，系口径效应 |
| 14 | come | 73 | 5.018 | 0.594 | NA | — | NA | NA | NA | M | comes across/comes from〔沿用组 1〕 |
| 15 | sounds | 108 | 4.991 | 0.477 | NA | — | NA | NA | NA | M | 听感评价框架动词（sounds awkward/natural）；与 natural/unnatural 共现，其 C1 权重由后者承担〔沿用组 7〕 |
| 16 | edit | 122 | 4.940 | 0.444 | PENDING | — | A3 | NA | NA | — | 维度一待定：表层编辑(G2)vs全局修改(G1)〔沿用组 1〕 |
| 17 | similar | 59 | 4.924 | 0.662 | NA | — | NA | NA | NA | M | a similar point／similar phrasing，层级由宾语决定 |
| 18 | needed | 42 | 4.838 | 0.797 | NA | — | A3 | NA | NA | M | more detail is needed，need 系建议套语的被动形式〔沿用组 10〕 |
| 19 | way | 139 | 4.802 | 0.408 | NA | — | NA | NA | NA | M | a way to／the way you，无固定层级所指〔沿用组 10〕 |
| 20 | word | 299 | 4.778 | 0.271 | G2 | Wording | NA | NA | NA | H | Wording 明示。注：本组为单数 word 独立入选（组 2 为归并 WORD），系 R1 先行的口径效应〔沿用组 3〕 |
| 21 | logic | 144 | 4.601 | 0.391 | G1 | Ideas | NA | NA | NA | H | 手册 Ideas 词族例明列 logic〔沿用组 5〕 |
| 22 | work | 238 | 4.595 | 0.299 | NA | — | NA | NA | NA | M | 文本指称语（your work）〔沿用组 10〕 |
| 23 | punctuation | 252 | 4.293 | 0.280 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示〔沿用组 4〕 |
| 24 | level | 298 | 4.222 | 0.254 | PENDING | — | NA | NA | NA | — | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev)〔沿用组 1〕 |
| 25 | defensible | 53 | 4.043 | 0.630 | G1 | Ideas | A1 | NA | NA | M | 域固定于 claim/thesis；正向评价，但存在目标态框架风险〔沿用组 1〕 |
| 26 | vague | 126 | 3.846 | 0.382 | PENDING | — | A2 | NA | NA | — | 维度一待定：与 unclear 同族，可指论证或用词〔沿用组 1〕 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 4 | 50.0% | 1583 | 78.7% | 0.346 |
| G1 | 4 | 50.0% | 428 | 21.3% | 0.533 |
| **已定标签合计** | **8** | **100.0%** | **2011** | **100.0%** | — |
| N/A（不计入分母） | 12 | — | — | — | — |
| PENDING（不计入分母） | 6 | — | — | — | — |
| 清单总数 | 26 | — | — | — | — |

**子类分布（分母同为已定标签 8）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 2 | 25.0% |
| G1 | Ideas | 2 | 25.0% |
| G2 | Local Structure | 2 | 25.0% |
| G2 | Mechanics | 1 | 12.5% |
| G2 | Wording | 1 | 12.5% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 4 | 57.1% | 355 | 59.3% | 0.606 |
| A2 | 2 | 28.6% | 191 | 31.9% | 0.554 |
| A1 | 1 | 14.3% | 53 | 8.8% | 0.630 |
| **已定标签合计** | **7** | **100.0%** | **599** | **100.0%** | — |
| N/A（不计入分母） | 19 | — | — | — | — |
| PENDING（不计入分母） | 0 | — | — | — | — |
| 清单总数 | 26 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 26 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 26 | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 26 | — |
| PENDING（不计入分母） | 0 | — |
| 清单总数 | 26 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 1 | 0 | **1** |
| **A2** | 0 | 2 | 0 | **2** |
| **A3** | 0 | 4 | 0 | **4** |
| **NA** | 0 | 19 | 0 | **19** |
| **PENDING** | 0 | 0 | 0 | **0** |
| **合计** | 0 | 26 | 0 | **26** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 1 | 1 | 0 | 2 | 0 | **4** |
| **G2** | 0 | 0 | 1 | 3 | 0 | **4** |
| **NA** | 0 | 0 | 1 | 11 | 0 | **12** |
| **PENDING** | 0 | 1 | 2 | 3 | 0 | **6** |
| **合计** | 1 | 2 | 4 | 19 | 0 | **26** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 2 | 3 | 11 | 4 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 4 | 4 | 50.0% |
| 6 个 PENDING 全归 G1（上界） | 10 | 4 | 71.4% |
| 6 个 PENDING 全归 G2（下界） | 4 | 10 | 28.6% |

### B9 concordance 待办清单

共 **6** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `consistent` | 135 | 维度一 | 维度一待定：consistent tense(G2)vs consistent argument(G1)；同组 2 consistency 口径〔沿用组 10〕 |
| `check` | 101 | 维度一 | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示〔沿用组 2〕 |
| `paragraph` | 1688 | 维度一 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1〔沿用组 10〕 |
| `edit` | 122 | 维度一 | 维度一待定：表层编辑(G2)vs全局修改(G1)〔沿用组 1〕 |
| `level` | 298 | 维度一 | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev)〔沿用组 1〕 |
| `vague` | 126 | 维度一 | 维度一待定：与 unclear 同族，可指论证或用词〔沿用组 1〕 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
