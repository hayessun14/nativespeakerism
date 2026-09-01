# 组 3 关键词质性分类编码报告（concordance 消解后）

> **状态：现行口径**
> 本文档基于 concordance 全部消解后的编码撰写，取代 [`group03_coding.md`](group03_coding.md)
> 中的一切占比数字。原文档保留为编码过程的审计轨迹，不再更新。
> 完整附表见 [`group03_tables.md`](group03_tables.md)，跨组统计见 [`final_report.md`](final_report.md)。

## Chinese → Generic（目标语料 = Chinese 条件，参照语料 = Generic 条件）

> **编码方案**：手册 v3　**编码对象集**：本清单全部 37 词位　**占比分母**：各层已定标签数
> **服务的 RQ**：RQ2（不同 L2 群体之间的差异）
> **对比性质**：两侧**都是 L2 条件**。差异不是「母语者 vs 非母语者」，而是「指明母语为中文 vs 未指明母语」。
> **未决项**：0（原 3 个 PENDING 单元格已由 concordance 消解）

> ### ⚠ 分母警告（消解后仍然成立）
> 本组清单仅 37 词位，各层已定标签为：维度一 19、act 层 7、hedge 层 1、维度三 2。
> **任何百分比都建立在个位数或十位数的分母上**，不具备与组 1、组 2 同等的稳健性。
> 下文凡给出占比均同时给出绝对数；act 层与 hedge 层不作解读。
> 另需注意：组 3 与组 1／组 2 **不是同一对语料**，跨对的占比数值不可对读。

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A |
|---|---:|---|---:|
| 维度一 Focus | 19 | **G2 14（73.7%）／ G1 5（26.3%）** | 18 |
| 维度二 act | 7 | A3 4／ A2 3／ **A1 0** | 30 |
| 维度二 hedge | 1 | M1 1（`usually`） | 36 |
| 维度三 | **2** | **C1 = 2（`chinese`、`english`）** | 35 |

**一句话概括**：Chinese 条件相对 Generic 条件的过量词汇显著偏局部（G2 73.7%），构成一份由冠词、名词单复数、动词形式、逗号、流水句组成的具体语法—标点清单；维度三出现两个 C1，其中 `chinese`（LR 5.965）是本研究 LR 最高的已编码词位；act 层 **A1 = 0**。

---

## 二、维度三：身份命名 + 语言系统指称

| Type | Freq_Tar | Freq_Ref | Range_Tar | LL | LR | 编码 |
|---|---:|---:|---:|---:|---:|---|
| `chinese` | 61 | **1** | 49 / 348 | 77.135 | **5.965** | **C1** |
| `english` | 138 | 74 | 113 | 21.164 | 0.933 | **C1**（查证后） |
| `language` | 712 | 642 | 309 | 5.462 | 0.183 | G2/Wording，维度三 NA |

`chinese` 的关键在参照侧的数字：**Generic 条件 348 篇反馈里，`chinese` 只出现 1 次**。两侧作文文本完全相同、都被标记为非母语者，唯一差别是有没有指明母语。指明之后，反馈开始把这个母语说出来（49 篇文档，占 14.1%）。

`english` 经 concordance 判定为 C1（指语言系统而非文体修饰），`language` 判为 G2/Wording、维度三 NA（"academic language" 占主导，非 "your language background"）。三词同处一个语义场而分属两类，这个分野由索引行而非词形决定。

依手册规则，C1 词族在维度一、维度二均标 N/A，两项因此不进入前两层的分母。

### 2.1 与组 2 对读后的修正

编码过程报告曾把 `chinese` 记为「全研究第一个确定的 C1」，并推论 C1 系于「指明了哪个母语」。组 2 的 `english` 查证成立后，这一推论需要修正：

| target corpus | C1 词形 |
|---|---|
| German | `german`、`english`、`SPEAKER`、`transfer`、`influenced`、`false`、`friends`、`speaking` |
| **Chinese** | **`chinese`、`english`** |
| Generic | `english` |
| L1 / Baseline | 无 |

`english` 在 Generic、Chinese、German 三个条件下**都是 C1**——它是非母语者标记本身触发的。真正随「指明母语」而增加的是身份命名（`chinese`／`german`）与迁移框架（`transfer` 等）。本组的贡献因此应表述为：**在语言系统指称之上，叠加了一层身份命名**，而不是「首次出现 C1」。

**本组没有出现迁移框架的显性词汇**（`interference`、`transfer`、`mother tongue`、`translate`、`L1` 均未入选）。也就是说，在关键词层面，Chinese 条件的 C1 表现为身份命名而非显性跨语言归因——后者若存在，只能在 `chinese` 的 concordance 内部找到，且组 6/7 显示 German 条件确有显性迁移词汇，这个对比本身是 RQ2 的一项结果。

---

## 三、维度一：局部层面，一份具体的错误清单

已定 19 项中 G2 占 14 项（73.7%）。

| 主类 | 子类 | 词位 |
|---|---|---|
| G2 | Grammar 5 | `nouns`、`singular`、`verb`、`ARTICLE`、`patterns` |
| G2 | Local Structure 4 | `sentences`、`RUN-ON`、`splices`、`shorter` |
| G2 | Wording 4 | `word`、`choice`、`language`、`register` |
| G2 | Mechanics 1 | `comma` |
| G1 | Development 3 | `check`、`insert`、`inaccurate` |
| G1 | Global Structure 1 | `paragraphs` |
| G1 | Ideas 1 | `logically` |

局部词汇构成一份相当具体的清单：**冠词、名词单复数、动词形式、逗号、流水句、逗号粘连、句子过长、语域**。

### 3.1 必须防止的过度解读（消解后仍然成立）

上述清单与 L2 写作文献中「中文母语迁移」的典型错误目录高度吻合（中文无冠词、无强制数标记；中文的逗号连接习惯产生 run-on 与 comma splice）。这个吻合很诱人，但**现有数据不支持「反馈针对中文做了特异性诊断」这一读法**：

| 词形 | German 条件 | Chinese 条件 | Generic 条件 | L1 条件 |
|---|---:|---:|---:|---:|
| `ARTICLE` | 479 | 272 | 167 | 74 |
| `register` | 73 | 41 | 25 | 未入选 |

冠词并不是中文条件的特异标记——**German 条件谈冠词谈得比 Chinese 条件还多**（479 : 272），而德语是有冠词的语言。同样的单调序列出现在 `register` 上。这更像一条「越是被具体标记为 L2，局部语言形式的词汇就越密集」的**梯度**，而非针对各语言的特异性诊断。

组 5／组 6（Chinese ↔ German 直接对比）已完成编码，结果支持梯度解释：German 侧的 G2 占比（69.2%）高于 Chinese 侧（36.0%），即德语标记比中文标记更强地拉动局部词汇。**这与「针对中文的迁移诊断」预期的方向相反**。故第三节的清单只应表述为「Chinese 条件相对 Generic 条件的局部词汇构成」。

### 3.2 一项不依赖编码判断的观察

| 条件 | 母语名称词 | Freq_Tar | Freq_Ref | LL |
|---|---|---:|---:|---:|
| Chinese（vs Generic） | `chinese` | 61 | 1 | 77.135 |
| German（vs Generic） | `german` | **491** | 3 | 647.497 |

两个条件的语料规模相当（260,484 vs 267,306 tokens），提示词结构相同，唯一差别是母语名称。**德语标记被反馈复述的次数约为中文标记的 8 倍**（Range：279/348 vs 49/348）。这项差异的量级远超本报告其他任何数字，且不依赖任何编码判断。

---

## 四、维度二：不作解读，但 A1 = 0 这个空缺已得到对照

act 层已定仅 7 项（A3 4：`check`、`suggestion`、`should`、`insert`；A2 3：`issues`、`problems`、`inaccurate`），**A1 = 0**。

分母太小，不构成发现。但组 4（Generic → Chinese，反方向）现已完成：其 A1 = 2（`strongest`、`strength`，均经强制查询清单判定）。**赞扬词汇确实偏向未指明母语的一侧**，尽管两侧分母都极小（7 与 5），这个对照只能作为方向提示，不能作为效应量。

`happy`（LR 1.557）与 `please` 是人际礼貌行为而非归功于文本属性，依 Hyland & Hyland 的 praise 定义不构成 A1，编码为 N/A。它们与组 2 的 `thank`／`sharing`／`luck` 属同一簇（手册排除的 paired acts 类）。

hedge 层已定 1 项（`usually`，115 词次）。`just` 经 concordance 判定为 hedge=**NA**（强化而非最小化降调），与组 1、组 9 的判定一致。

---

## 五、concordance 消解带来的变化

本组 **13 个词位、14 个单元格**经查证定夺（维度一 10、act 1、hedge 1、维度三 2）。

| 指标 | 消解前 | 消解后 | 变化 |
|---|---|---|---|
| 维度一 G2 占比 | 77.8%（14/18，另 1 项未决） | 73.7%（14/19） | **−4.1 pp** |
| act A3 占比 | 57.1% | 57.1% | 无 |
| M1 词位 | 1 | 1 | 无 |
| C1 词位 | 2 | 2 | 无 |

唯一的维度一未决项 `paragraphs` 判为 **G1/Global Structure**（段落间安排而非段落内部组织），G1 增 1 项，G2 占比因分母变大而下降 4.1 pp——**这是十二组中占比移动最大的一处**，原因是本组分母只有 18–19，单个词位的权重达 5 个百分点。

「局部倾斜」的方向不受影响：73.7% 与 26.3% 之间仍有 47 个百分点的距离。但这一处正好说明分母警告不是形式主义——同样一个词位的归属，在组 9（分母 69）只值 1.4 pp，在本组值 4.1 pp。

几处推翻原判的记录：

| 词形 | 原判倾向 | 查证后 |
|---|---|---|
| `check` | 偏 G2（check your spelling） | **G1/Development**（check your logic 占主导） |
| `insert` | 偏 G2（insert a comma） | **G1/Development**（insert a transition） |
| `inaccurate` | 偏 G2（inaccurate wording） | **G1/Development**（inaccurate facts） |
| `our` | 疑似议题残留 | **NA**，确认为残留 |

前三项全部从预期的 G2 落到 G1——如果按词形直觉编码，本组的 G2 占比会虚高到 89.5%（17/19）。这三项是本研究中「词形直觉与索引证据分歧」最集中的一处。

---

## 六、遗留问题

1. **`chinese` 的 C1 子类**仍未细分（Identity marking vs Transfer framing）。concordance 已确认 C1 归属，但子类判定需要另一轮标注。这决定 C1 在本研究中呈现为「命名身份」还是「归因迁移」，理论含义不同。
2. **分母过小**：act 层 7 项、hedge 层 1 项、维度三 2 项。这三层的任何占比都不应进入论文正文的数值论证。
3. **议题内容残留**：`safety`（99）、`hours`（64）、`office`（48）、`returns`（40），加上查证确认的 `our`（129），共 5 项。均为两层 N/A，移除不改变任何已定标签占比，只影响清单总数（37 → 32）。
4. **口径效应的确认实例**：`word` 在本组以**单数独立词位**入选（Freq_Tar 519），而在组 2 是归并标签 `WORD`（word + words，537）。这是「R1 先行导致同一词在不同组形态不同」的口径效应，非操作失误，建议在方法部分以此为例说明。

---

## 附表

完整编码表（附表 A）与分布统计（B1–B10）见 [`group03_tables.md`](group03_tables.md)，
由 `scripts/analyze.py 3` 生成。
