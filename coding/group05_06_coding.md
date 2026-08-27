# 组 5／组 6 关键词质性分类编码报告
## Chinese ↔ German（RQ2 的决定性一对）

> **编码日期**：2026-08-27（第一轮编码）
> **编码方案**：手册 v3　**编码对象集**：组 5 全部 56 词位、组 6 全部 59 词位　**占比分母**：各层已定标签数
> **对比性质**：两侧**都是具体指明母语的 L2 条件**，且指明的具体程度相同。差异不能归因于「是否被标记为 L2」，只能归因于**被标记为哪一种 L2**。
> **报告形式**：两组是同一对语料的两个方向，合并为一份报告；附表按组分列。

---

## 一、结果摘要

| 层 | 组 5（Chinese 侧过量） | 组 6（German 侧过量） |
|---|---|---|
| 维度一 | 已定 18：**G1 13（72.2%）**／ G2 5（27.8%） | 已定 14：**G2 10（71.4%）**／ G1 4（28.6%） |
| 维度二 act | 已定 11：A3 5／A2 5／A1 1 | 已定 4：A3 3／A2 1／**A1 0** |
| 维度二 hedge | 已定 1：`some` | 已定 3：`likely`、`often`、`quite` |
| 维度三 | **C1 1**（`chinese`），PENDING 0 | **C1 3**（`german`、`SPEAKER`、`transfer`），**PENDING 7** |
| N/A ／ PENDING（维度一） | 29 ／ 9 | 30 ／ 15 |

**一句话概括**：两个同等具体的 L2 标记产生了方向相反的反馈——中文标记侧偏全局（组织、论点、读者），德语标记侧偏局部（标点、大写、从句、语序），并且德语侧集中了全研究**唯一的显性迁移框架词汇**。

---

## 二、维度一：组 3 提出的两种解释都需要修正

组 3 §3.1 曾列出两种竞争解释：(a) 针对中文的特异性迁移诊断；(b)「越被具体标记为 L2，局部词汇越密集」的梯度。本对语料同时否证了两者的简单形式。

**(a) 被否证**：若反馈是在针对中文做特异性迁移诊断，Chinese 侧相对 German 侧应更局部。实际相反——Chinese 侧 G1 72.2%，German 侧 G2 71.4%。组 3 观察到的「Chinese 局部倾斜」是**相对 Generic** 而言的，不是中文的特异属性。

**(b) 需要修正**：Chinese 与 German 的标记具体程度完全相同，却分到相反的焦点。因此驱动因素不是「标记的具体程度」，而是**被标记为哪一种语言**。

把四个条件按局部倾向排序（组 7／组 8 尚未编码，German ↔ Generic 一段暂以主表原始频次代替编码结果）：

| | German | Chinese | Generic | L1 |
|---|---|---|---|---|
| 编码结果 | G2 71.4%（vs Chinese） | G2 90.9%（vs Generic）／ G1 72.2%（vs German） | G2 52.8%（vs L1） | G1 80.8%（vs Generic） |
| `ARTICLE` 原始频次 | 479 | 272 | 167 | 74 |
| `register` 原始频次 | 73 | 41 | 25 | 未入选 |

序列是 **German > Chinese > Generic > L1**。梯度存在，但它在 L2 一端是**语言特异**的，不是「L2 标记程度」的函数。

### 2.1 敏感性检验：本对结论尚未被 PENDING 排除

| | 现状 | 下界 | 上界 |
|---|---:|---:|---:|
| 组 5 G1 占比 | 72.2% | 48.1% | 81.5% |
| 组 6 G1 占比 | 28.6% | 13.8% | 65.5% |

区间**存在重叠 [48.1, 65.5]**，与组 1／组 2 的情形相同，而不同于组 3／组 4（那一对不重叠）。组 6 的 PENDING 多达 15 项（占清单 25.4%），是目前 PENDING 比例最高的一组，因此其点估计 28.6% 的可靠性最低。

不过组 6 的 PENDING 构成偏向 G2：`ARTICLE`、`order`、`patterns`、`rewrite`、`register`、`precise`、`used`、`style` 中多数偏局部，`INFLUENCE`、`basis`、`rhetorical`、`academic`、`emotionally`、`natural`、`direct` 偏全局或跨层。这提示实际值更可能靠近下界而非上界——**但这是构成推测，不是证据**，必须以 concordance 重算值写入论文。

### 2.2 两侧局部词汇的内容不同

组 6 的 G2 子类里 Mechanics 有 3 项（`commas`、`capitalization`、`punctuation`），Local Structure 2 项（`clauses`、`cut`）。加上 PENDING 中的 `order`（word order），德语侧的局部清单是：**标点、名词大写、从句、语序**。

组 3（Chinese vs Generic）的局部清单是：**冠词、名词单复数、动词形式、逗号、流水句、逗号粘连**。

两份清单确实不同，且各自与相应语言的常见迁移描述吻合（德语名词首字母大写、德语从句语序；中文无冠词与数标记、中文逗号连接习惯）。但请注意：**这一吻合只能说明局部词汇的内容随标记语言而变，不能说明反馈在做正确的语言学诊断**——后者需要核对这些建议是否真的对应作文中的实际错误，而本研究的作文文本在所有条件下完全相同（LOCNESS 英语母语者作文），因此**这些"迁移错误"在文本中本就不应存在**。这是本研究设计的关键之处，应在讨论部分明确点出。

---

## 三、维度三：本研究迄今最强的单一结果

| | 组 5（Chinese 侧） | 组 6（German 侧） |
|---|---|---|
| C1 已定 | 1 项 / 61 词次 | **3 项 / 647 词次** |
| C1 PENDING | **0 项** | **7 项 / 1044 词次** |
| 候选材料合计 | 1 项 / 61 词次 | 10 项 / 1691 词次 |

### 3.1 已定 C1

| Type | Freq_Tar | Freq_Ref | Range_Tar | LL | LR | 子类 |
|---|---:|---:|---:|---:|---:|---|
| `german` | 491 | **0** | 279 / 348 | 668.504 | **9.902** | Identity marking |
| `SPEAKER` | 113 | 25 | ≥71 | 58.482 | 2.139 | Identity marking |
| `transfer` | 43 | 6 | 39 | 30.549 | 2.804 | **Transfer framing** |
| `chinese`（组 5） | 61 | 1 | 49 / 348 | 77.281 | 5.968 | 待定子类 |

`transfer` 是手册 Transfer framing 词族例的明列条目，也是**全研究第一个确定的迁移框架词**。它出现在德语条件，不出现在中文条件——组 3 与组 5 的中文侧清单中，没有任何迁移框架词汇（`interference`、`transfer`、`mother tongue`、`translate`、`literal` 全部缺席）。

`german` 的 Freq_Ref = 0（交接文档 §2.2 记录的唯一 +0.5 平滑例），Range 279/348 = 80.2%——**五分之四的德语条件反馈会把「German」这个词说出来**。中文条件的对应值是 49/348 = 14.1%。

### 3.2 待定 C1 与「false friends」假设

`false`（49 vs 9，LR 2.407）与 `friends`（46 vs 20，LR 1.164）的 Freq_Tar 与 Range_Tar 近乎同步（42 / 43 篇文档），提示二者主要出现在同一个搭配 **false friends**（跨语言假同源词）中。若成立，这是第二个 Transfer framing 词族。

反证线索：`friends` 在参照侧（Chinese 条件）仍有 20 次，说明存在非 "false friends" 的基线用法（很可能是作文内容 "friends and family"）。因此**不能凭词形判定**，须做 `false` 的右搭配 concordance——这一项判定成本极低、信息回报极高，建议列为第一优先。

其余 5 项待定：`english`（508 vs 138）、`INFLUENCE`（103 vs 50）、`natural`（113 vs 62）、`speaking`（61 vs 21）、`direct`（164 vs 107）。其中 `english` 的共现语境使 C1 先验极高，但手册对 `english` 有明文规则（"correct English"→C1／"English essay"→NA），仍依规则待查。

### 3.3 一个必须谨慎处理的理论张力

本结果的方向与 native-speakerism 的朴素预期**不一致**：被标记为德语母语者（欧洲、西方背景）的写作者，得到的显性语言身份框架**远多于**被标记为中文母语者的写作者（1691 : 61 词次候选材料）。

有两点必须在讨论中分开：

1. **框架的数量 ≠ 缺陷叙事的强度。** Holliday 的论点是非西方背景者被施加文化缺陷叙事，而非「被更频繁地提及母语」。中文条件完全可能在**不点名语言**的情况下承载缺陷叙事——组 3 的局部错误清单（冠词、单复数、流水句）就是候选载体。判定二者的差别需要 concordance 层面的**语力与评价极性**分析，而不是词位计数。
2. **本阶段不引入 Holliday。** 按研究设计，分类阶段由 Straub & Lunsford 与 Hyland & Hyland 驱动，Holliday 只在解释类别分布时出场。上述张力属于解释层面，此处仅登记，不在编码阶段处理。

---

## 四、维度二

### 4.1 act 层：仍不足以解读，但记录一个持续的空缺

组 5 已定 11 项（A3 5、A2 5、A1 1——唯一的 A1 是 `debatable`），组 6 已定 4 项（A3 3、A2 1、**A1 0**）。

至此，**A1 = 0 已在组 3、组 4、组 6 连续出现**；组 5 也仅 1 项。四个 L2 相关清单中赞扬词汇几近全无。但 act 层 PENDING 在组 5 有 6 项、组 6 有 7 项，其中 `REQUIRE`、`raise`、`create`、`read`、`explain`、`say`、`discuss`、`using` 都可能翻转，因此**仍不构成发现**。

### 4.2 hedge 层：中文条件是目前最贫乏的一侧

| 对比 | hedge 富集侧 |
|---|---|
| L1 ↔ Generic | Generic（5 项 1608 词次 vs 2 项 123 词次） |
| Generic ↔ Chinese | Generic（`feels`；Chinese 侧 0） |
| Chinese ↔ German | German（`likely`、`often`、`quite`；Chinese 侧仅 `some`） |

中文条件在它参与的两个对比中都是 hedge 更少的一侧。这与 3.1 的 C1 结果方向一致（中文条件既少被点名语言身份，也少被缓和），但两者都受小分母限制，且组 6 的 hedge PENDING 有 3 项（`few`、`could`、`would`）。**待 concordance 后与组 7／组 8 一并复核。**

---

## 五、一个应当整批处理的编码类别：内容动词

编码过程中反复出现同一类判定困难：一批动词本身不构成言语行为，其 act 归属完全取决于所嵌入的框架。

已累计：`explain`、`discuss`、`say`、`mention`、`write`、`use`／`using`／`used`、`focus`、`create`、`read`、`choose`、`check`、`raise`／`raises`。

逐词判定既低效又容易产生跨组不一致（组 1 `tackles` 与组 4 `raises` 已出现一次，见组 4 报告 §5）。建议**制定一条统一的 concordance 判定规则**，一次性适用于全部内容动词，例如：

> 抽 50 行，统计该动词是否出现在祈使句、`you should/need to/can/could + V`、`try V-ing`、`consider V-ing` 等补救框架中。占比 ≥ 60% 判 A3；≤ 40% 判 NA；中间区间报告为不可判定并在敏感性分析中双向计算。

阈值可另议，但规则应先于逐词判定确定，并写入手册 v4。

---

## 六、数据问题

### 6.1 议题内容残留

组 5 确认 5 项：`schools`、`office`、`hours`、`safety`、`social`；疑似 4 项：`tool`、`effects`、`data`、`action`。
组 6 疑似 1 项：`friends`（与 3.2 的判定绑定）。

一个内部一致性佐证：`safety`、`hours`、`office` 同时出现在组 3 与组 5——两组的目标语料都是 Chinese 条件，出现同一批议题词符合预期，说明残留来自语料而非编码波动。

### 6.2 组 6 的 PENDING 比例偏高

组 6 维度一 PENDING 15/59 = 25.4%，维度三 PENDING 7/59 = 11.9%，均为十二组中最高。原因是德语侧清单集中了大量跨层歧义词（`order`、`style`、`basis`、`INFLUENCE`、`natural`、`direct`、`register`、`precise`）。这不是编码保守，而是该清单本身的语义构成——但它确实降低了组 6 点估计的可靠性，已在 2.1 说明。

### 6.3 手册 v3 强制查询清单仍未获得

两组均无 `address`／`strong`／`strongest`。累计待重扫词位：128 ＋ 131 ＋ 37 ＋ 30 ＋ 56 ＋ 59 = **441 个**。

---

## 七、下一步

1. **`false` 的右搭配 concordance**（第一优先，成本极低）：判定 "false friends" 假设，直接决定 Transfer framing 是 1 项还是 2 项。
2. **`transfer`、`INFLUENCE`、`speaking`、`english` 的 concordance**：确定德语条件的迁移框架规模。
3. **`chinese` 的子类判定**（沿自组 3）：中文条件的 C1 是纯身份命名还是也含迁移归因。若为纯命名，则「显性迁移框架只出现在德语条件」这一陈述成立。
4. **组 7／组 8（German ↔ Generic）**：补齐 §2 序列中唯一仍靠原始频次代替的一段，并检验 4.2 的 hedge 形态。
5. **确定内容动词的统一判定规则**（§5），写入手册 v4，再启动逐词 concordance。
6. 补齐 v3 强制查询清单，重扫累计 441 个词位。

---

# 附表：组 5（Chinese → German）

## 附表 A：组 5 完整编码表（56 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | chinese | 61 | 77.281 | 5.968 | NA | — | NA | NA | C1 | H | Identity marking 明示；子类（身份标记 vs 迁移框架）待 concordance，范畴不待定。依手册规则维度一、二均标 NA |
| 2 | organization | 417 | 27.659 | 0.576 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示 |
| 3 | readers | 285 | 25.669 | 0.684 | G1 | Ideas | NA | NA | NA | M | 受众；依窄口径 C1 规定归 G1 |
| 4 | explain | 565 | 18.733 | 0.395 | NA | — | PENDING | NA | NA | — | act 层待定：you explain X well（描述 NA）vs explain this further（A3）。属"内容动词"类，见报告 §5 |
| 5 | body | 595 | 15.010 | 0.341 | G1 | Global Structure | NA | NA | NA | H | body paragraphs，大单位 |
| 6 | grammar | 680 | 14.747 | 0.315 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 7 | schools | 109 | 13.676 | 0.828 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 8 | suggestion | 126 | 13.251 | 0.748 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3） |
| 9 | revise | 378 | 12.249 | 0.390 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 10 | using | 188 | 12.198 | 0.570 | PENDING | — | PENDING | NA | NA | — | 维度一待定：use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定，属内容动词类 |
| 11 | mechanics | 99 | 11.922 | 0.809 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 12 | level | 177 | 11.653 | 0.574 | PENDING | — | NA | NA | NA | — | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1)；同组 1 口径 |
| 13 | specific | 502 | 9.382 | 0.291 | PENDING | — | NA | NA | NA | — | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2) |
| 14 | should | 1241 | 9.125 | 0.179 | NA | — | A3 | NA | NA | H | Hyland&Hyland 明示建议套语 |
| 15 | discuss | 132 | 9.121 | 0.590 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：you discuss X（描述）vs discuss counterarguments（A3）；内容动词类 |
| 16 | restate | 134 | 8.978 | 0.580 | G1 | Global Structure | A3 | NA | NA | M | restate your thesis in the conclusion，大单位安排 |
| 17 | office | 48 | 8.789 | 1.037 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 18 | your | 5029 | 8.478 | 0.084 | NA | — | NA | NA | NA | M | 人称代词 |
| 19 | can | 735 | 7.822 | 0.217 | NA | — | PENDING | PENDING | NA | — | 与 could/might/would 同类共享项，两层分别判 |
| 20 | organizing | 54 | 7.589 | 0.885 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示 |
| 21 | hours | 64 | 7.392 | 0.789 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 22 | confusing | 55 | 6.764 | 0.819 | PENDING | — | A2 | NA | NA | — | 维度一待定（clear 系）；手册 A2 词族例明列 confusing |
| 23 | details | 47 | 6.683 | 0.891 | G1 | Development | NA | NA | NA | H | Development 明示 |
| 24 | recommend | 56 | 6.622 | 0.800 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 25 | safety | 99 | 6.619 | 0.579 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 26 | tool | 57 | 6.488 | 0.783 | NA | — | NA | NA | NA | M | 疑似议题内容残留 vs "a useful tool"元话语，待核 |
| 27 | clarity | 228 | 6.435 | 0.362 | PENDING | — | NA | NA | NA | — | 维度一待定（手册 clear 系） |
| 28 | paragraphs | 605 | 6.315 | 0.215 | PENDING | — | NA | NA | NA | — | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| 29 | ideas | 441 | 6.260 | 0.252 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 30 | help | 210 | 6.094 | 0.368 | NA | — | NA | NA | NA | M | 描述性动词（this helps the reader） |
| 31 | current | 86 | 5.781 | 0.581 | NA | — | NA | NA | NA | M | 元话语现状框架（your current draft），同组 1 currently |
| 32 | places | 69 | 5.731 | 0.654 | NA | — | NA | NA | NA | M | 指示元话语（places where…） |
| 33 | errors | 249 | 5.722 | 0.325 | G2 | Correctness | A2 | NA | NA | H | 手册边界规则明示：error/mistake 归 G2-Correctness 且同时得批评标签 |
| 34 | debatable | 54 | 5.678 | 0.748 | G1 | Ideas | A1 | NA | NA | M | a debatable claim，域固定于论断；同组 1 arguable/defensible 口径，目标态框架风险 |
| 35 | effects | 140 | 5.319 | 0.425 | NA | — | NA | NA | NA | M | 疑似议题内容残留（effects of X）vs 对读者的效果，待核 |
| 36 | some | 987 | 5.238 | 0.151 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 37 | problems | 174 | 5.149 | 0.372 | NA | — | A2 | NA | NA | H | 手册 A2 明示（problem） |
| 38 | logic | 128 | 5.126 | 0.437 | G1 | Ideas | NA | NA | NA | H | 手册 Ideas 词族例明列 logic |
| 39 | awkward | 138 | 5.079 | 0.418 | PENDING | — | A2 | NA | NA | — | 维度一待定：awkward phrasing(G2-Wording)vs awkward transition(G1)；手册 A2 词族例明列 awkward |
| 40 | adding | 131 | 5.015 | 0.427 | NA | — | A3 | NA | NA | H | 手册 A3 明示（add） |
| 41 | data | 72 | 5.015 | 0.593 | G1 | Development | NA | NA | NA | M | 证据类型；疑似议题内容残留，待核 |
| 42 | far | 46 | 4.901 | 0.754 | NA | — | NA | NA | NA | M | so far / far from |
| 43 | summary | 120 | 4.785 | 0.436 | PENDING | — | NA | NA | NA | — | 维度一待定：your summary 段落(G1-Structure)vs "in summary"元话语(NA) |
| 44 | social | 253 | 4.762 | 0.292 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 45 | shows | 248 | 4.628 | 0.291 | NA | — | NA | NA | NA | M | 描述性框架动词 |
| 46 | conclusion | 710 | 4.555 | 0.167 | G1 | Global Structure | NA | NA | NA | H | 大单位，Global Structure 明示 |
| 47 | effort | 73 | 4.514 | 0.555 | NA | — | NA | NA | NA | L | 低信度：归功对象为写作者努力而非文本属性；若与评价词共现构成归功则应改判 A1。同组 2 |
| 48 | further | 67 | 4.488 | 0.580 | NA | — | NA | NA | NA | M | 程度/延续副词，非 hedge |
| 49 | inaccurate | 46 | 4.340 | 0.703 | PENDING | — | A2 | NA | NA | — | 维度一待定：inaccurate wording(G2)vs inaccurate facts(G1-Development) |
| 50 | say | 145 | 4.290 | 0.372 | NA | — | PENDING | NA | NA | — | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| 51 | thesis | 1534 | 4.267 | 0.109 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 52 | forward | 48 | 4.140 | 0.668 | NA | — | NA | NA | NA | M | going forward / put forward |
| 53 | significant | 95 | 4.132 | 0.457 | NA | — | NA | NA | NA | M | 程度形容词，极性依宾语 |
| 54 | choice | 457 | 4.054 | 0.197 | G2 | Wording | NA | NA | NA | M | word choice |
| 55 | action | 70 | 3.887 | 0.523 | NA | — | NA | NA | NA | M | 疑似议题内容残留 vs call to action（结论段套语），待核 |
| 56 | RUN-ON | 175 | 3.874 | 0.319 | G2 | Local Structure | NA | NA | NA | H | 手册 Local Structure 词族例明列 run-on |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 13 | 72.2% | 4603 | 73.5% | 0.527 |
| G2 | 5 | 27.8% | 1660 | 26.5% | 0.393 |
| **已定标签合计** | **18** | **100.0%** | **6263** | **100.0%** | — |
| N/A（不计入分母） | 29 | — | — | — | — |
| PENDING（不计入分母） | 9 | — | — | — | — |
| 清单总数 | 56 | — | — | — | — |

**子类分布（分母同为已定标签 18）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 2 | 11.1% |
| G1 | Global Structure | 5 | 27.8% |
| G1 | Ideas | 6 | 33.3% |
| G2 | Correctness | 1 | 5.6% |
| G2 | Grammar | 1 | 5.6% |
| G2 | Local Structure | 1 | 5.6% |
| G2 | Mechanics | 1 | 5.6% |
| G2 | Wording | 1 | 5.6% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 5 | 45.5% | 1940 | 73.0% | 0.475 |
| A2 | 5 | 45.5% | 662 | 24.9% | 0.527 |
| A1 | 1 | 9.1% | 54 | 2.0% | 0.748 |
| **已定标签合计** | **11** | **100.0%** | **2656** | **100.0%** | — |
| N/A（不计入分母） | 39 | — | — | — | — |
| PENDING（不计入分母） | 6 | — | — | — | — |
| 清单总数 | 56 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 1 | 100.0% | 987 | 100.0% | 0.151 |
| **已定标签合计** | **1** | **100.0%** | **987** | **100.0%** | — |
| N/A（不计入分母） | 54 | — | — | — | — |
| PENDING（不计入分母） | 1 | — | — | — | — |
| 清单总数 | 56 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| C1 | 1 | 100.0% | 61 | 100.0% | 5.968 |
| **已定标签合计** | **1** | **100.0%** | **61** | **100.0%** | — |
| N/A（不计入分母） | 55 | — | — | — | — |
| PENDING（不计入分母） | 0 | — | — | — | — |
| 清单总数 | 56 | — | — | — | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 1 | 0 | **1** |
| **A2** | 0 | 5 | 0 | **5** |
| **A3** | 0 | 5 | 0 | **5** |
| **NA** | 1 | 38 | 0 | **39** |
| **PENDING** | 0 | 5 | 1 | **6** |
| **合计** | 1 | 54 | 1 | **56** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 1 | 0 | 1 | 10 | 1 | **13** |
| **G2** | 0 | 1 | 0 | 4 | 0 | **5** |
| **NA** | 0 | 1 | 4 | 20 | 4 | **29** |
| **PENDING** | 0 | 3 | 0 | 5 | 1 | **9** |
| **合计** | 1 | 5 | 5 | 39 | 6 | **56** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 6 | 2 | 9 | 3 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 13 | 5 | 72.2% |
| 9 个 PENDING 全归 G1（上界） | 22 | 5 | 81.5% |
| 9 个 PENDING 全归 G2（下界） | 13 | 14 | 48.1% |

### B9 concordance 待办清单

共 **15** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `explain` | 565 | act | act 层待定：you explain X well（描述 NA）vs explain this further（A3）。属"内容动词"类，见报告 §5 |
| `suggestion` | 126 | act | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3） |
| `using` | 188 | 维度一、act | 维度一待定：use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定，属内容动词类 |
| `level` | 177 | 维度一 | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1)；同组 1 口径 |
| `specific` | 502 | 维度一 | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2) |
| `discuss` | 132 | act | act 层待定：you discuss X（描述）vs discuss counterarguments（A3）；内容动词类 |
| `can` | 735 | act、hedge | 与 could/might/would 同类共享项，两层分别判 |
| `confusing` | 55 | 维度一 | 维度一待定（clear 系）；手册 A2 词族例明列 confusing |
| `clarity` | 228 | 维度一 | 维度一待定（手册 clear 系） |
| `paragraphs` | 605 | 维度一 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `awkward` | 138 | 维度一 | 维度一待定：awkward phrasing(G2-Wording)vs awkward transition(G1)；手册 A2 词族例明列 awkward |
| `summary` | 120 | 维度一 | 维度一待定：your summary 段落(G1-Structure)vs "in summary"元话语(NA) |
| `effort` | 73 | 低信度复核 | 低信度：归功对象为写作者努力而非文本属性；若与评价词共现构成归功则应改判 A1。同组 2 |
| `inaccurate` | 46 | 维度一 | 维度一待定：inaccurate wording(G2)vs inaccurate facts(G1-Development) |
| `say` | 145 | act | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| chinese | 77.281 | 5.968 | NA | NA | NA |

# 附表：组 6（German → Chinese）

## 附表 A：组 6 完整编码表（59 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | german | 491 | 668.504 | 9.902 | NA | — | NA | NA | C1 | H | Identity marking 明示。Freq_Ref = 0（组内唯一 +0.5 平滑例），LR 9.902 为全研究最高 |
| 2 | english | 508 | 216.155 | 1.843 | NA | — | NA | NA | PENDING | — | 手册明列：指语言系统（correct English）→C1；作文体修饰→NA。本组共现语境使 C1 先验极高，但仍依规则待查 |
| 3 | SPEAKER | 113 | 58.482 | 2.139 | NA | — | NA | NA | C1 | H | 手册 Identity marking 词族例明列 speaker；German speakers / native speakers 两读法均属 C1 |
| 4 | ARTICLE | 479 | 52.649 | 0.779 | PENDING | — | NA | NA | NA | — | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development) |
| 5 | order | 118 | 43.921 | 1.675 | PENDING | — | NA | NA | NA | — | 维度一待定：word order（G2-Grammar，德语语序迁移的典型项）vs "in order to"（NA） |
| 6 | transfer | 43 | 30.549 | 2.804 | NA | — | NA | NA | C1 | H | 手册 Transfer framing 词族例明列 transfer |
| 7 | false | 49 | 29.321 | 2.407 | NA | — | NA | NA | PENDING | — | 维度三待定：false friends（跨语言词汇概念，C1）vs false dichotomy（逻辑谬误，G1-Ideas）。与 friends 的 Freq/Range 近乎同步，见报告 §3.2 |
| 8 | style | 410 | 29.187 | 0.609 | PENDING | — | NA | NA | NA | — | 维度一待定（手册列 tone/register 为 PENDING） |
| 9 | moment | 107 | 26.580 | 1.278 | NA | — | NA | NA | NA | M | 元话语现状框架（at the moment），与组 1 currently、组 5 current 同构 |
| 10 | common | 223 | 21.881 | 0.730 | NA | — | NA | NA | NA | M | 常见性标记（a common error）＝正常化框架；属手册排除的 paired acts 类，不入 M1 |
| 11 | argumentation | 112 | 20.952 | 1.070 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 12 | patterns | 170 | 20.941 | 0.833 | PENDING | — | NA | NA | NA | — | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| 13 | speaking | 61 | 19.353 | 1.501 | NA | — | NA | NA | PENDING | — | 维度三待定：German-speaking / German speakers（C1）vs generally speaking（NA） |
| 14 | INFLUENCE | 103 | 17.406 | 1.005 | PENDING | — | NA | NA | PENDING | — | 维度三待定：the influence of German on your English（Transfer framing，C1）vs influence the reader（G1） |
| 15 | basis | 44 | 17.018 | 1.722 | PENDING | — | NA | NA | NA | — | 维度一待定：the basis of your claim(G1-Ideas)vs on a …basis（NA） |
| 16 | watch | 252 | 15.680 | 0.565 | NA | — | A3 | NA | NA | M | watch for / watch out for＝注意指令，属建议行为 |
| 17 | usage | 122 | 15.526 | 0.849 | G2 | Correctness | NA | NA | NA | M | article usage / comma usage，语言使用规范层 |
| 18 | likely | 166 | 14.894 | 0.694 | NA | — | NA | M1 | NA | H | 认识型 hedge，与手册 probably/possibly 同类 |
| 19 | REQUIRE | 109 | 14.540 | 0.873 | NA | — | PENDING | NA | NA | — | act 层待定：this requires a comma（补救指令 A3）vs German requires…（描述，且可能属 C1 共现语境） |
| 20 | natural | 113 | 13.796 | 0.829 | PENDING | — | PENDING | NA | PENDING | — | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；同组 2 口径 |
| 21 | commas | 108 | 13.356 | 0.835 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 22 | structure | 795 | 13.247 | 0.278 | G1 | Global Structure | NA | NA | NA | H | 手册边界规则明示：structure 主导义为篇章结构，归 G1 |
| 23 | often | 320 | 13.245 | 0.452 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 24 | clauses | 73 | 12.699 | 1.023 | G2 | Local Structure | NA | NA | NA | H | 手册 Local Structure 词族例明列 clause |
| 25 | few | 173 | 12.568 | 0.616 | NA | — | NA | PENDING | NA | — | hedge 层待定：a few errors 最小化降调（M1）vs 单纯量词（NA）；同组 1 just、组 2 only |
| 26 | writer | 65 | 11.446 | 1.031 | NA | — | NA | NA | NA | M | 第三人称指称写作者（the writer），与 your 的第二人称形成对照，值得单独记录 |
| 27 | direct | 164 | 10.656 | 0.579 | PENDING | — | NA | NA | PENDING | — | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA) |
| 28 | noun | 53 | 10.461 | 1.106 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示；德语名词大写为典型迁移项 |
| 29 | friends | 46 | 9.865 | 1.164 | NA | — | NA | NA | PENDING | — | 维度三待定：false friends（C1）vs 议题内容残留（friends and family）。参照侧 Freq 20 提示存在非 C1 基线用法 |
| 30 | steps | 73 | 9.628 | 0.867 | NA | — | NA | NA | NA | M | 元话语（next steps） |
| 31 | phrasing | 188 | 9.197 | 0.495 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 32 | rhetorical | 192 | 8.573 | 0.471 | PENDING | — | NA | NA | NA | — | 维度一待定：rhetorical question（局部修辞手段）vs rhetorical strategy/situation（G1） |
| 33 | very | 236 | 8.501 | 0.419 | NA | — | NA | NA | NA | M | 强化词，非 hedge |
| 34 | rewrite | 97 | 8.396 | 0.680 | PENDING | — | A3 | NA | NA | — | 维度一待定：rewrite this sentence(G2)vs rewrite this paragraph(G1)；建议动词 |
| 35 | register | 73 | 8.298 | 0.795 | PENDING | — | NA | NA | NA | — | 维度一待定（手册列 register 为 PENDING）；元语言学术语，显性命名语域规范 |
| 36 | could | 499 | 8.120 | 0.275 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项，抽 50 行分别判两层 |
| 37 | notes | 46 | 8.048 | 1.027 | NA | — | NA | NA | NA | M | 元话语（a few notes on…） |
| 38 | question | 127 | 7.751 | 0.559 | G1 | Ideas | NA | NA | NA | M | the question your essay raises；同组 4 口径 |
| 39 | cut | 42 | 7.422 | 1.033 | G2 | Local Structure | A3 | NA | NA | M | 删削冗余，句内/句间；同组 1 口径 |
| 40 | capitalization | 136 | 6.297 | 0.480 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示；德语名词首字母大写为典型迁移项 |
| 41 | argumentative | 673 | 6.252 | 0.205 | NA | — | NA | NA | NA | M | 文体标签（argumentative essay/writing），不指示层级 |
| 42 | punctuation | 244 | 6.164 | 0.347 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 43 | new | 219 | 6.018 | 0.362 | NA | — | NA | NA | NA | M | a new paragraph / new ideas，层级由宾语决定 |
| 44 | would | 628 | 5.977 | 0.207 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项，抽 50 行分别判两层 |
| 45 | academic | 997 | 5.580 | 0.158 | PENDING | — | NA | NA | NA | — | 维度一待定（register）；同组 2 口径 |
| 46 | find | 50 | 5.121 | 0.749 | NA | — | NA | NA | NA | M | I find… / readers may find…＝人称归因，属手册排除的缓和策略 |
| 47 | always | 117 | 4.964 | 0.458 | NA | — | NA | NA | NA | M | 最大化副词，非 hedge（区别于手册 often/usually/sometimes） |
| 48 | precise | 294 | 4.750 | 0.274 | PENDING | — | NA | NA | NA | — | 维度一待定：precise wording(G2)vs precise claims(G1)；同组 1 precision 口径 |
| 49 | raise | 37 | 4.719 | 0.850 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：raises an important question 属开场归功套语(A1)vs 描述(NA)；与组 1 tackles、组 4 raises 并案 |
| 50 | above | 51 | 4.425 | 0.681 | NA | — | NA | NA | NA | M | 指示元话语（see above） |
| 51 | emotionally | 47 | 4.388 | 0.710 | PENDING | — | NA | NA | NA | — | 维度一待定：emotionally charged language(G2)vs emotional appeal(G1)；同组 4 口径 |
| 52 | quite | 56 | 4.363 | 0.641 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 53 | properly | 61 | 4.329 | 0.608 | G2 | Correctness | NA | NA | NA | M | 规范性副词（used properly）；同组 2 proper 口径 |
| 54 | place | 67 | 4.225 | 0.569 | NA | — | NA | NA | NA | M | in place of / places where，指示元话语 |
| 55 | placeholder | 53 | 4.192 | 0.646 | G2 | Wording | A2 | NA | NA | M | placeholder phrases/language，空泛措辞；同组 1 口径 |
| 56 | second | 127 | 4.132 | 0.397 | NA | — | NA | NA | NA | M | 序数词，反馈条目枚举 |
| 57 | create | 87 | 3.945 | 0.475 | NA | — | PENDING | NA | NA | — | act 层待定：create a clearer transition（A3）vs 描述（NA）；内容动词类 |
| 58 | read | 93 | 3.937 | 0.457 | NA | — | PENDING | NA | NA | — | act 层待定：read your essay aloud（A3）vs 描述（NA）；内容动词类 |
| 59 | used | 146 | 3.921 | 0.358 | PENDING | — | NA | NA | NA | — | 维度一待定：同 USE/using 口径 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 10 | 71.4% | 1080 | 50.2% | 0.742 |
| G1 | 4 | 28.6% | 1071 | 49.8% | 0.689 |
| **已定标签合计** | **14** | **100.0%** | **2151** | **100.0%** | — |
| N/A（不计入分母） | 30 | — | — | — | — |
| PENDING（不计入分母） | 15 | — | — | — | — |
| 清单总数 | 59 | — | — | — | — |

**子类分布（分母同为已定标签 14）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Global Structure | 1 | 7.1% |
| G1 | Ideas | 3 | 21.4% |
| G2 | Correctness | 2 | 14.3% |
| G2 | Grammar | 1 | 7.1% |
| G2 | Local Structure | 2 | 14.3% |
| G2 | Mechanics | 3 | 21.4% |
| G2 | Wording | 2 | 14.3% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 3 | 75.0% | 391 | 88.1% | 0.759 |
| A2 | 1 | 25.0% | 53 | 11.9% | 0.646 |
| **已定标签合计** | **4** | **100.0%** | **444** | **100.0%** | — |
| N/A（不计入分母） | 48 | — | — | — | — |
| PENDING（不计入分母） | 7 | — | — | — | — |
| 清单总数 | 59 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 3 | 100.0% | 542 | 100.0% | 0.596 |
| **已定标签合计** | **3** | **100.0%** | **542** | **100.0%** | — |
| N/A（不计入分母） | 53 | — | — | — | — |
| PENDING（不计入分母） | 3 | — | — | — | — |
| 清单总数 | 59 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| C1 | 3 | 100.0% | 647 | 100.0% | 4.948 |
| **已定标签合计** | **3** | **100.0%** | **647** | **100.0%** | — |
| N/A（不计入分母） | 49 | — | — | — | — |
| PENDING（不计入分母） | 7 | — | — | — | — |
| 清单总数 | 59 | — | — | — | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 0 | 0 | **0** |
| **A2** | 0 | 1 | 0 | **1** |
| **A3** | 0 | 3 | 0 | **3** |
| **NA** | 3 | 44 | 1 | **48** |
| **PENDING** | 0 | 5 | 2 | **7** |
| **合计** | 3 | 53 | 3 | **59** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 0 | 0 | 0 | 3 | 1 | **4** |
| **G2** | 0 | 1 | 1 | 8 | 0 | **10** |
| **NA** | 0 | 0 | 1 | 24 | 5 | **30** |
| **PENDING** | 0 | 0 | 1 | 13 | 1 | **15** |
| **合计** | 0 | 1 | 3 | 48 | 7 | **59** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 1 | 1 | 11 | 7 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 4 | 10 | 28.6% |
| 15 个 PENDING 全归 G1（上界） | 19 | 10 | 65.5% |
| 15 个 PENDING 全归 G2（下界） | 4 | 25 | 13.8% |

### B9 concordance 待办清单

共 **26** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `english` | 508 | 维度三 | 手册明列：指语言系统（correct English）→C1；作文体修饰→NA。本组共现语境使 C1 先验极高，但仍依规则待查 |
| `ARTICLE` | 479 | 维度一 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development) |
| `order` | 118 | 维度一 | 维度一待定：word order（G2-Grammar，德语语序迁移的典型项）vs "in order to"（NA） |
| `false` | 49 | 维度三 | 维度三待定：false friends（跨语言词汇概念，C1）vs false dichotomy（逻辑谬误，G1-Ideas）。与 friends 的 Freq/Range 近乎同步，见报告 §3.2 |
| `style` | 410 | 维度一 | 维度一待定（手册列 tone/register 为 PENDING） |
| `patterns` | 170 | 维度一 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `speaking` | 61 | 维度三 | 维度三待定：German-speaking / German speakers（C1）vs generally speaking（NA） |
| `INFLUENCE` | 103 | 维度一、维度三 | 维度三待定：the influence of German on your English（Transfer framing，C1）vs influence the reader（G1） |
| `basis` | 44 | 维度一 | 维度一待定：the basis of your claim(G1-Ideas)vs on a …basis（NA） |
| `REQUIRE` | 109 | act | act 层待定：this requires a comma（补救指令 A3）vs German requires…（描述，且可能属 C1 共现语境） |
| `natural` | 113 | 维度一、act、维度三 | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；同组 2 口径 |
| `few` | 173 | hedge | hedge 层待定：a few errors 最小化降调（M1）vs 单纯量词（NA）；同组 1 just、组 2 only |
| `direct` | 164 | 维度一、维度三 | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA) |
| `friends` | 46 | 维度三 | 维度三待定：false friends（C1）vs 议题内容残留（friends and family）。参照侧 Freq 20 提示存在非 C1 基线用法 |
| `rhetorical` | 192 | 维度一 | 维度一待定：rhetorical question（局部修辞手段）vs rhetorical strategy/situation（G1） |
| `rewrite` | 97 | 维度一 | 维度一待定：rewrite this sentence(G2)vs rewrite this paragraph(G1)；建议动词 |
| `register` | 73 | 维度一 | 维度一待定（手册列 register 为 PENDING）；元语言学术语，显性命名语域规范 |
| `could` | 499 | act、hedge | 手册指定共享项，抽 50 行分别判两层 |
| `would` | 628 | act、hedge | 手册指定共享项，抽 50 行分别判两层 |
| `academic` | 997 | 维度一 | 维度一待定（register）；同组 2 口径 |
| `precise` | 294 | 维度一 | 维度一待定：precise wording(G2)vs precise claims(G1)；同组 1 precision 口径 |
| `raise` | 37 | act | act 层待定：raises an important question 属开场归功套语(A1)vs 描述(NA)；与组 1 tackles、组 4 raises 并案 |
| `emotionally` | 47 | 维度一 | 维度一待定：emotionally charged language(G2)vs emotional appeal(G1)；同组 4 口径 |
| `create` | 87 | act | act 层待定：create a clearer transition（A3）vs 描述（NA）；内容动词类 |
| `read` | 93 | act | act 层待定：read your essay aloud（A3）vs 描述（NA）；内容动词类 |
| `used` | 146 | 维度一 | 维度一待定：同 USE/using 口径 |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| german | 668.504 | 9.902 | NA | NA | NA |
| transfer | 30.549 | 2.804 | NA | NA | NA |
| false | 29.321 | 2.407 | NA | NA | NA |
| SPEAKER | 58.482 | 2.139 | NA | NA | NA |
| english | 216.155 | 1.843 | NA | NA | NA |
| basis | 17.018 | 1.722 | PENDING | NA | NA |
| order | 43.921 | 1.675 | PENDING | NA | NA |
| speaking | 19.353 | 1.501 | NA | NA | NA |
