# 组 3 关键词质性分类编码报告
## Chinese → Generic（目标语料 = Chinese 条件，参照语料 = Generic 条件）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：本清单全部 37 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ2（不同 L2 群体之间的差异）
> **对比性质**：本组的两侧**都是 L2 条件**。差异不是「母语者 vs 非母语者」，而是「指明母语为中文 vs 未指明母语」。

> ### ⚠ 分母警告
> 本组清单仅 37 词位，各层已定标签为：维度一 11、act 层 6、hedge 层 1、维度三 1。**任何百分比都建立在个位数或十位数的分母上，不具备与组 1、组 2 同等的稳健性**。下文凡给出占比，均同时给出绝对数；act 层与 hedge 层不作解读。
> 另需注意：组 3 与组 1／组 2 **不是同一对语料**（组 1/2 是 L1↔Generic，组 3/4 是 Chinese↔Generic）。跨这两对的占比数值不可对读；可以对读的只有「某词形出现在哪一侧」这一层面。

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A | PENDING |
|---|---:|---|---:|---:|
| 维度一 Focus | 11 | G2 10（90.9%）／ G1 1（9.1%） | 18 | 8 |
| 维度二 act | 6 | A3 3／ A2 3／ **A1 0** | 30 | 1 |
| 维度二 hedge | 1 | M1 1（`usually`） | 35 | 1 |
| 维度三 | **1** | **C1 = 1（`chinese`）** | 34 | 2 |

**一句话概括**：本组产出了全研究**第一个确定编码为 C1 的关键词**——`chinese`（LR 5.965，全研究已编码词位中最高）；其余过量词汇几乎全部落在局部层面，且构成一个由冠词、名词单复数、动词、逗号、流水句、逗号粘连组成的具体语法—标点错误清单。

---

## 二、维度三：全研究第一个确定的 C1

| Type | Freq_Tar | Freq_Ref | Range_Tar | LL | LR | 编码 |
|---|---:|---:|---:|---:|---:|---|
| `chinese` | 61 | **1** | 49 / 348 | 77.135 | **5.965** | **C1** |
| `english` | 138 | 74 | 113 | 21.164 | 0.933 | PENDING |
| `language` | 712 | 642 | 309 | 5.462 | 0.183 | PENDING |

`chinese` 的判定不待 concordance：无论它出现在身份标记（"as a Chinese speaker…"）还是迁移框架（"in Chinese, articles are not marked…"）中，两者都是 C1 的两个子类。**待 concordance 的是子类归属，不是范畴归属**，因此编码为 C1／信度 H。

关键在于参照侧的数字：**Generic 条件 348 篇反馈里，`chinese` 只出现 1 次**。两侧作文文本完全相同、都被标记为非母语者，唯一差别是有没有指明母语。指明之后，反馈开始把这个母语说出来（49 篇文档，占 14.1%）。

依手册规则，C1 词族在维度一、维度二均标 N/A，`chinese` 因此不进入前两层的分母。

**本组没有出现迁移框架的显性词汇**（`interference`、`transfer`、`mother tongue`、`translate`、`L1` 均未入选）。也就是说，在关键词层面，Chinese 条件的 C1 表现为**身份命名**，而非显性的跨语言归因——后者若存在，只能在 `chinese` 的 concordance 内部找到。

---

## 三、维度一：局部层面，且是一份具体的错误清单

已定 11 项中 G2 占 10 项（词次口径 97.9%），唯一的 G1 是 `logically`（54 词次）。

| G2 子类 | 词位 |
|---|---|
| Grammar 3 | `nouns`、`singular`、`verb` |
| Local Structure 4 | `sentences`、`RUN-ON`、`splices`、`shorter` |
| Wording 2 | `word`、`choice` |
| Mechanics 1 | `comma` |

加上 8 个 PENDING 中偏 G2 的 `ARTICLE`、`insert`、`patterns`、`check`，本组的局部词汇构成一份相当具体的清单：**冠词、名词单复数、动词形式、逗号、流水句、逗号粘连、句子过长**。

敏感性检验（附表 B8）：即使 8 个 PENDING 全归 G1，G1 也只到 47.4%（9/19）；全归 G2 则降至 5.3%。**「局部倾斜」这一方向不随 PENDING 归属翻转**——这是本组少数几个不受小分母困扰的结论之一，因为它依赖的是词位归属而非比例精度。

### 3.1 一个必须防止过度解读的地方

上述清单与 L2 写作文献中「中文母语迁移」的典型错误目录高度吻合（中文无冠词、无强制数标记；中文的逗号连接习惯产生 run-on 与 comma splice）。这个吻合很诱人，但**现有数据不支持「反馈针对中文做了特异性诊断」这一读法**，理由来自主表本身：

| 词形 | German 条件 | Chinese 条件 | Generic 条件 | L1 条件 |
|---|---:|---:|---:|---:|
| `ARTICLE` | 479 | 272 | 167 | 74 |
| `register` | 73 | 41 | 25 | 未入选 |

冠词并不是中文条件的特异标记——**German 条件谈冠词谈得比 Chinese 条件还多**（479 : 272），而德语是有冠词的语言。同样的单调序列出现在 `register` 上。这更像是一条「越是被具体标记为 L2，局部语言形式的词汇就越密集」的**梯度**，而不是针对各语言的特异性诊断。

真正能分辨这两种解释的是**组 5／组 6（Chinese ↔ German 直接对比）**，那是 RQ2 的决定性一对。在那两组编码完成之前，第三节的清单只应表述为「Chinese 条件相对 Generic 条件的局部词汇构成」，不应表述为「针对中文的迁移诊断」。

### 3.2 一个可以先记下的原始观察

主表中另有一项与 RQ2 直接相关、且不依赖任何编码判断的事实：

| 条件 | 母语名称词 | Freq_Tar | Freq_Ref | LL |
|---|---|---:|---:|---:|
| Chinese（vs Generic） | `chinese` | 61 | 1 | 77.135 |
| German（vs Generic） | `german` | **491** | 3 | 647.497 |

两个条件的语料规模相当（260,484 vs 267,306 tokens），提示词结构相同，唯一差别是母语名称。**德语标记被反馈复述的次数约为中文标记的 8 倍**（Range：279/348 vs 49/348）。这项差异的量级远超本报告其他任何数字，应在组 5–8 编码时优先处理。此处仅作记录，不作解释。

---

## 四、维度二：不作解读，但记录一个空缺

act 层已定仅 6 项（A3 3、A2 3），**A1 = 0**：本组没有任何词位被编为赞扬。hedge 层已定 1 项（`usually`）。

分母太小，不构成发现。但「A1 = 0」这个空缺值得在组 4（Generic → Chinese，反方向）编码后回看：若 A1 词汇成组出现在组 4，则说明赞扬词汇偏向未指明母语的一侧；若组 4 也没有，则说明这一对语料在赞扬词汇上本就没有差异。

需要注意本组的 `happy`（LR 1.557）与 `please`：二者是人际礼貌行为而非归功于文本属性，依 Hyland & Hyland 的 praise 定义不构成 A1，编码为 N/A。它们与组 2 的 `thank`／`sharing`／`luck` 属同一簇（手册排除的 paired acts 类）。

---

## 五、数据问题

### 5.1 议题内容残留 4 项 + 疑似 1 项

确认残留：`safety`（99）、`hours`（64）、`office`（48）、`returns`（40）——四者语义连贯，应来自同一批 LOCNESS 议题作文。
疑似待核：`our`（129）——可能是作文内容中的 "our society"，也可能是反馈的包容性人称。

与前两组相同，这些词在维度一、二两层均为 N/A，**移除不改变任何已定标签占比**，只影响清单总数（37 → 33 或 32）。

### 5.2 口径效应的一个确认实例

`word` 在本组以**单数独立词位**入选（Freq_Tar 519），而在组 2 是归并标签 `WORD`（word + words，537）。这正是交接文档 §三 预告的「R1 先行导致同一词在不同组形态不同」的口径效应，非操作失误。本报告予以确认，建议在方法部分以此为例说明。

### 5.3 手册 v3 强制查询清单仍未获得

本组无 `address`、`strong`、`strongest`。风险项：`issues`、`problems`（A2 类）、`should`、`check`、`insert`（A3 类）。累计待重扫词位：组 1 128 ＋ 组 2 131 ＋ 组 3 37 = **296 个**。

---

## 六、下一步

1. **组 4（Generic → Chinese）**：本组的反方向，与本组构成同一对语料，可直接对读；也是检验「A1 = 0」空缺的必要一步。
2. **组 5／组 6（Chinese ↔ German）**：RQ2 的决定性一对，直接判定 3.1 的两种竞争解释，并处理 3.2 的 8 倍差异。
3. **concordance 判定 11 个词族**（附表 B9）。优先级：
   - 第一优先：`chinese` 的**子类**判定（Identity marking vs Transfer framing）——决定 C1 在本研究中呈现为「命名身份」还是「归因迁移」，理论含义不同
   - 第二优先：`ARTICLE`（若判为英语冠词，Grammar 子类增至 4 项，且 3.1 的梯度解释更稳）
   - 第三优先：`english`、`language`（维度三，与组 2 同批处理）
4. 补齐 v3 强制查询清单，重扫累计 296 个词位。

---
## 附表 A：组 3 完整编码表（37 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | chinese | 61 | 77.135 | 5.965 | NA | — | NA | NA | C1 | H | Identity marking 明示（写作者语言身份）；亦可能为 Transfer framing（"in Chinese, articles…"），子类待 concordance 区分，但 C1 归属不待定。依手册规则 C1 词族维度一、二均标 NA |
| 2 | ARTICLE | 272 | 27.904 | 0.738 | PENDING | — | NA | NA | NA | — | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；本组与 nouns/singular/verb 构成语法簇，判为冠词的先验概率高于组 2，但仍须查 |
| 3 | english | 138 | 21.164 | 0.933 | NA | — | NA | NA | PENDING | — | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| 4 | happy | 46 | 15.857 | 1.557 | NA | — | NA | NA | NA | M | 人际礼貌（happy to help / I'd be happy to…）；属手册排除的 paired acts 类，不入 M1 |
| 5 | safety | 99 | 11.819 | 0.805 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 6 | check | 200 | 10.524 | 0.508 | PENDING | — | A3 | NA | NA | — | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示 |
| 7 | patterns | 93 | 10.176 | 0.766 | PENDING | — | NA | NA | NA | — | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| 8 | eg | 417 | 10.009 | 0.333 | NA | — | NA | NA | NA | M | 举例元话语（e.g.） |
| 9 | issues | 374 | 9.727 | 0.347 | NA | — | A2 | NA | NA | M | 问题标记，内在负向（同手册 problem 口径）；层级由宾语决定 |
| 10 | please | 90 | 9.375 | 0.744 | NA | — | NA | NA | NA | M | 礼貌标记；手册 M1 限于 hedges，礼貌标记不入 M1 |
| 11 | hours | 64 | 9.316 | 0.905 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 12 | word | 519 | 8.712 | 0.275 | G2 | Wording | NA | NA | NA | H | Wording 明示。注：本组为单数 word 独立入选（组 2 为归并 WORD），系 R1 先行的口径效应 |
| 13 | suggestion | 126 | 8.563 | 0.585 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3） |
| 14 | should | 1241 | 7.926 | 0.166 | NA | — | A3 | NA | NA | H | Hyland&Hyland 明示建议套语 |
| 15 | further | 67 | 7.537 | 0.778 | NA | — | NA | NA | NA | M | 程度/延续副词（further develop），非 hedge |
| 16 | problems | 174 | 6.814 | 0.432 | NA | — | A2 | NA | NA | H | 手册 A2 明示（problem） |
| 17 | returns | 40 | 6.472 | 0.963 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 18 | RUN-ON | 175 | 6.464 | 0.419 | G2 | Local Structure | NA | NA | NA | H | 手册 Local Structure 词族例明列 run-on；语义为流水句 |
| 19 | office | 48 | 6.463 | 0.864 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 20 | choice | 457 | 6.096 | 0.244 | G2 | Wording | NA | NA | NA | M | word choice |
| 21 | sentences | 667 | 5.846 | 0.196 | G2 | Local Structure | NA | NA | NA | H | Local Structure 明示 |
| 22 | splices | 112 | 5.756 | 0.501 | G2 | Local Structure | NA | NA | NA | H | comma splice 与 run-on 同属句界错误，依手册 run-on 口径归 Local Structure |
| 23 | i | 492 | 5.601 | 0.225 | NA | — | NA | NA | NA | M | 反馈者自称（I suggest/I noticed）＝人称归因，属手册排除的缓和策略，不入 M1 |
| 24 | language | 712 | 5.462 | 0.183 | PENDING | — | NA | NA | PENDING | — | 维度三待定：your language background/first language(C1)vs academic language(G2 Wording) |
| 25 | nouns | 42 | 5.404 | 0.841 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 26 | insert | 73 | 4.884 | 0.580 | PENDING | — | A3 | NA | NA | — | 维度一待定：insert a comma(G2-Mechanics)vs insert a transition(G1)；建议动词 |
| 27 | inaccurate | 46 | 4.856 | 0.750 | PENDING | — | A2 | NA | NA | — | 维度一待定：inaccurate wording(G2)vs inaccurate facts(G1-Development)；负向评价 |
| 28 | comma | 200 | 4.699 | 0.329 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 29 | paragraphs | 605 | 4.449 | 0.179 | PENDING | — | NA | NA | NA | — | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| 30 | our | 129 | 4.396 | 0.401 | NA | — | NA | NA | NA | M | 疑似议题内容残留（our society）vs 包容性人称，待核 |
| 31 | verb | 261 | 4.331 | 0.274 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 32 | shorter | 82 | 4.328 | 0.509 | G2 | Local Structure | NA | NA | NA | M | shorter sentences；比较级，评价由框架承担 |
| 33 | register | 41 | 4.302 | 0.748 | PENDING | — | NA | NA | NA | — | 维度一待定（手册列 tone/formal/register 为 PENDING）；元语言学术语，显性命名语域规范 |
| 34 | logically | 54 | 4.060 | 0.619 | G1 | Ideas | NA | NA | NA | M | 手册 Ideas 词族例含 logic；若主导搭配为 organize…logically 则应改判 Global Structure |
| 35 | singular | 49 | 4.005 | 0.649 | G2 | Grammar | NA | NA | NA | H | 单复数，Correctness/Grammar 明示 |
| 36 | just | 214 | 3.999 | 0.291 | NA | — | NA | PENDING | NA | — | hedge 层待定：最小化降调（M1）vs"仅仅是"强化批评（NA）；同组 1 口径 |
| 37 | usually | 115 | 3.962 | 0.404 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 10 | 90.9% | 2564 | 97.9% | 0.424 |
| G1 | 1 | 9.1% | 54 | 2.1% | 0.619 |
| **已定标签合计** | **11** | **100.0%** | **2618** | **100.0%** | — |
| N/A（不计入分母） | 18 | — | — | — | — |
| PENDING（不计入分母） | 8 | — | — | — | — |
| 清单总数 | 37 | — | — | — | — |

**子类分布（分母同为已定标签 11）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Ideas | 1 | 9.1% |
| G2 | Grammar | 3 | 27.3% |
| G2 | Local Structure | 4 | 36.4% |
| G2 | Mechanics | 1 | 9.1% |
| G2 | Wording | 2 | 18.2% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 3 | 50.0% | 1514 | 71.8% | 0.418 |
| A2 | 3 | 50.0% | 594 | 28.2% | 0.510 |
| **已定标签合计** | **6** | **100.0%** | **2108** | **100.0%** | — |
| N/A（不计入分母） | 30 | — | — | — | — |
| PENDING（不计入分母） | 1 | — | — | — | — |
| 清单总数 | 37 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 1 | 100.0% | 115 | 100.0% | 0.404 |
| **已定标签合计** | **1** | **100.0%** | **115** | **100.0%** | — |
| N/A（不计入分母） | 35 | — | — | — | — |
| PENDING（不计入分母） | 1 | — | — | — | — |
| 清单总数 | 37 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| C1 | 1 | 100.0% | 61 | 100.0% | 5.965 |
| **已定标签合计** | **1** | **100.0%** | **61** | **100.0%** | — |
| N/A（不计入分母） | 34 | — | — | — | — |
| PENDING（不计入分母） | 2 | — | — | — | — |
| 清单总数 | 37 | — | — | — | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 0 | 0 | **0** |
| **A2** | 0 | 3 | 0 | **3** |
| **A3** | 0 | 3 | 0 | **3** |
| **NA** | 1 | 28 | 1 | **30** |
| **PENDING** | 0 | 1 | 0 | **1** |
| **合计** | 1 | 35 | 1 | **37** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 0 | 1 | 0 | **1** |
| **G2** | 0 | 0 | 0 | 10 | 0 | **10** |
| **NA** | 0 | 2 | 1 | 14 | 1 | **18** |
| **PENDING** | 0 | 1 | 2 | 5 | 0 | **8** |
| **合计** | 0 | 3 | 3 | 30 | 1 | **37** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 0 | 3 | 14 | 3 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 1 | 10 | 9.1% |
| 8 个 PENDING 全归 G1（上界） | 9 | 10 | 47.4% |
| 8 个 PENDING 全归 G2（下界） | 1 | 18 | 5.3% |

### B9 concordance 待办清单

共 **11** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `ARTICLE` | 272 | 维度一 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；本组与 nouns/singular/verb 构成语法簇，判为冠词的先验概率高于组 2，但仍须查 |
| `english` | 138 | 维度三 | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| `check` | 200 | 维度一 | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示 |
| `patterns` | 93 | 维度一 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `suggestion` | 126 | act | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3） |
| `language` | 712 | 维度一、维度三 | 维度三待定：your language background/first language(C1)vs academic language(G2 Wording) |
| `insert` | 73 | 维度一 | 维度一待定：insert a comma(G2-Mechanics)vs insert a transition(G1)；建议动词 |
| `inaccurate` | 46 | 维度一 | 维度一待定：inaccurate wording(G2)vs inaccurate facts(G1-Development)；负向评价 |
| `paragraphs` | 605 | 维度一 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `register` | 41 | 维度一 | 维度一待定（手册列 tone/formal/register 为 PENDING）；元语言学术语，显性命名语域规范 |
| `just` | 214 | hedge | hedge 层待定：最小化降调（M1）vs"仅仅是"强化批评（NA）；同组 1 口径 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| chinese | 77.135 | 5.965 | NA | NA | NA |
| happy | 15.857 | 1.557 | NA | NA | NA |
