# 组 2 关键词质性分类编码报告
## Generic → L1（目标语料 = Generic 条件，参照语料 = L1 条件）

> **编码日期**：2026-08-27（第一轮编码；本 commit 时间戳即 intra-rater 信度所需的第一轮时间记录）
> **编码方案**：手册 v3 —— 维度一 G1/G2；维度二两层（act 层 A1/A2/A3 ＋ hedge 层 M1，可共存）；维度三 C1
> **编码对象集**：本清单全部 131 词位　**占比分母**：各层已定标签数（N/A 与 PENDING 单列）
> **与组 1 的关系**：组 1 与组 2 是**同一对语料的两个方向**（L1 348 篇 vs Generic 348 篇）。因此「某词落在哪一侧」这一判断在两张清单之间**可直接对读**；但两张清单的占比分母不同（52 vs 36 等），**占比数值不可直接相减**。下文凡跨组对照，均只作方向性陈述。

---

## 一、结果摘要

| 层 | 已定标签 | 分布 | N/A | PENDING |
|---|---:|---|---:|---:|
| 维度一 Focus | 36 | **G2 52.8%**（19）／ G1 47.2%（17） | 70 | 25 |
| 维度二 act | 20 | A3 45.0%（9）／ A1 35.0%（7）／ A2 20.0%（4） | 94 | 17 |
| 维度二 hedge | 5 | **M1 5**（`some`、`may`、`slightly`、`sometimes`、`probably`） | 121 | 5 |
| 维度三 | 0 | C1 = 0，但 **PENDING 4**（`language`、`english`、`background`、`natural`） | 127 | 4 |

**一句话概括**：当写作者被标记为未指明母语的非母语者时，相对于英语母语者，反馈的过量词汇向**局部层面**移动（G2 52.8%，组 1 的对应值为 19.2%），出现了组 1 完全没有的**语法子类**（6 项）与**语言身份候选词**（4 项），并集中了全部 5 个高频认识型 hedge。

---

## 二、维度一：焦点向局部层面移动

### 2.1 与组 1 的方向对照

| | 组 1（L1 侧过量） | 组 2（Generic 侧过量） |
|---|---:|---:|
| G1 词位 | 42（80.8%） | 17（47.2%） |
| G2 词位 | 10（19.2%） | 19（52.8%） |
| 已定标签合计 | 52 | 36 |

**G2 子类构成的差异比总量差异更能说明问题**：

| G2 子类 | 组 1 | 组 2 |
|---|---:|---:|
| Grammar | **0** | **6**（`grammar`、`tense`、`verb`、`past`、`form`、`agreement`） |
| Correctness（总括） | 2（`correctness`、`PROOFREAD`） | 4（`corrections`、`accuracy`、`correct`、`proper`） |
| Mechanics | 3 | 1（`spelling`） |
| Wording | 4 | 5（`WORD`、`vocabulary`、`expressions`、`PHRASE`、`choice`） |
| Local Structure | 1 | 3（`sentences`、`long`、`shorter`） |

组 1 报告第二节提出的假设，其**前半部分在此得到确认**：具体执行语法纠正的词汇（`grammar`、`tense`、`verb`、`past`、`form`、`agreement`）全部落在 Generic 侧，L1 侧一个都没有；L1 侧只有 `correctness`、`mechanical` 这类**范畴元标签**。若 `ARTICLE` 经 concordance 判为英语冠词（而非引用的文章），Grammar 子类将增至 7 项。

假设的**后半部分——L1 侧的元标签是否伴随最小化修饰语——仍未验证**，仍需按组 1 报告所列方法做 concordance。

### 2.2 敏感性检验的诚实边界

| | 现状 | PENDING 全归 G1 | PENDING 全归 G2 |
|---|---:|---:|---:|
| 组 1 G1 占比 | 80.8% | 86.7% | 56.0% |
| 组 2 G1 占比 | 47.2% | 68.9% | 27.9% |

两组的极端边界区间为组 1 [56.0, 86.7]、组 2 [27.9, 68.9]，**存在重叠区 [56.0, 68.9]**。也就是说，「焦点反转」这一结论在逻辑上**尚未被 PENDING 完全排除**——要落入重叠区，需要组 1 的 23 个 PENDING 绝大多数归 G2、同时组 2 的 25 个 PENDING 绝大多数归 G1。

从两组 PENDING 的构成看这不太可能（组 2 的 PENDING 中 `ARTICLE`、`subject`、`complete`、`patterns`、`consistency`、`check` 均偏 G2；组 1 的 PENDING 中 `level`、`line`、`reads`、`shifts`、`terms` 偏 G1），但**这是推测，不是证据**。concordance 完成后必须重算此表，并以重算值而非当前点估计写入论文。

---

## 三、维度二：act 层暂不可比，hedge 层出现清晰不对称

### 3.1 act 层：两种口径互相矛盾，暂不解读

| | 组 1 词位 | 组 2 词位 | 组 1 词次 | 组 2 词次 |
|---|---:|---:|---:|---:|
| A3 建议 | 48.7% | 45.0% | 77.4% | 55.0% |
| A2 批评 | 33.3% | 20.0% | 13.8% | 28.6% |
| A1 赞扬 | 17.9% | 35.0% | 8.8% | 16.4% |

词位口径显示 Generic 侧 A1 多于 A2，词次口径显示相反（A2 966 词次集中在 `too` 529、`informal` 190、`unclear` 153、`difficult` 94 四个词上）。两种口径给出相反的排序，说明**本层样本量不足以支撑解读**：已定标签仅 20 项，而 PENDING 有 17 项，且 PENDING 里包含本组体量最大的几个词——`CLEAR`（1289）、`USE`（1068）、`GOOD`（949）、`strong`（711）、`can`（680）、`could`（499）、`focus`（466）。

其中 **`GOOD` 与 `strong` 的归属直接决定 A1 的量级**：两者合计 1660 词次，若判为 A1，Generic 侧的赞扬词次将从 554 跃升至 2214，是组 1 A1 总量（545）的四倍。**act 层的跨条件比较必须等 concordance，现在给出任何结论都是不负责任的。**

### 3.2 hedge 层：本组第一个方向清晰的发现

| | 组 1（L1 侧过量） | 组 2（Generic 侧过量） |
|---|---|---|
| 已定 M1 | 2 项 / 123 词次（`fairly`、`risk`） | **5 项 / 1608 词次**（`some` 939、`may` 404、`sometimes` 148、`probably` 59、`slightly` 58） |
| 待定 | 4 项（`rather`、`would`、`might`、`just`） | 5 项（`can`、`could`、`briefly`、`only`、`possible`） |

由于两组是同一对语料的两个方向，「哪些 hedge 落在哪一侧」可以直接对读：**认识型 hedge 成组落在 Generic 侧，L1 侧只有两个且词次极低**。这一差异的量级（1608 : 123）大到不太可能被 9 个待定项翻转。

act ＋ hedge 双标签共现仍为 **0 项**（附表 B5）——与组 1 相同。原因也相同：关键词层面只能捕捉承担缓和功能的独立词形，而 5 个已定 M1 的 act 层均为 N/A。**这不能读作「hedge 没有施加在 act 之上」**，只能读作「承担 hedge 的词形与承担 act 的词形是分离的」。真正的共存关系要在 concordance 层面（`may` + `want to`、`could` + `add`）才看得到，这正是 v3 共存规则要求两层分别判定的意义所在。

---

## 四、维度三：C1 仍为 0，但候选池出现不对称

已定 C1 **仍然是 0**——本轮没有任何词位被确定编为 C1。但 PENDING 从组 1 的 1 项增至 4 项：

| Type | Freq_Tar | Freq_Ref | LL | LR | 待定读法 |
|---|---:|---:|---:|---:|---|
| `language` | 642 | 285 | 150.991 | 1.210 | your language background（C1）vs academic language（G2 Wording） |
| `background` | 105 | 68 | 8.990 | 0.665 | your language background（C1）vs background information（G1 Development） |
| `english` | 74 | 16 | 42.086 | 2.248 | correct English（C1）vs English essay（N/A）——手册明列规则 |
| `natural` | 49 | 29 | 5.731 | 0.795 | sounds natural 是否以母语者语感为隐含标准（C1） |

**必须说清楚的界限**：C1 = 0 是当前的编码事实，候选池的不对称（组 2 四项 870 词次 vs 组 1 一项 80 词次）是**尚未定性的线索**，两者不能混为一谈。

不过有一点已经可以确定，且不依赖 concordance：**`english` 这个词形只出现在 Generic 侧，L1 侧的 128 个词位中没有它**（组 1 亦无 `language`、`native`、`speaker`）。按手册对 `english` 的既定规则，它只有 C1 与 N/A 两种归属——也就是说，L1 条件下连产生 C1 的**词汇材料**都不存在。组 6、组 7 的 `SPEAKER`（LL 58.482 / 79.165）与组 10 的 `language`（LL 143.329）、`english`（LL 48.406）方向一致。

RQ1 的证据形态因此可以更精确地表述为：**语言身份词汇的候选材料本身就是单向分布的**。最终判定待 `language`、`english`、`background`、`natural` 四词的 concordance。

---

## 五、组 2 特有的三个词汇簇（组 1 无对应物）

这三簇都不由三个维度捕捉（均编为 N/A），但它们在 LR 排序中位置很高，且构成组 1 完全没有的现象。建议作为**补充观察**单独报告，不修改编码手册。

### 5.1 反馈文档的结构化元话语簇

`corrections`（LR 3.208，全组最高）、`comment`（1.623）、`suggestions`（1.151）、`advice`（0.994）、`STRENGTH`（1.237）、`areas`、`final`、`below`、`here`、`eg`，以及成对出现的 `original`（1.360）／`revised`（1.136）。

读法：Generic 条件的反馈更像一份**分节的、带小标题的、含「原句 → 改后句」对照的文档**。组 1 侧没有任何对应词形；组 1 的举例标记是 `for instance`（`instance` LL 32.502），组 2 是 `e.g.`（`eg` LL 17.437）——连举例方式都不同。

### 5.2 人际礼貌簇

`thank`（LR 2.360）、`sharing`（2.078）、`luck`（1.401）、`please`（1.012）、`we`、`i`。

读法：Hyland & Hyland 所说的 paired acts（成对行为）与 personal attribution（人称归因）两类缓和策略，其词汇痕迹**成组落在 Generic 侧**。手册已明确将这两类排除出 M1（无法在关键词层面操作化），因此它们在维度二记为 N/A——但它们的方向性分布与 3.2 的 hedge 结果**指向同一侧**，两者互为旁证。若论文要论证「缓和策略集中于非母语条件」，M1 是主证据，本簇是辅证。

### 5.3 规范性与模式化框架簇

规范性：`correct`、`proper`、`accurate`、`natural`、`formal`、`neutral`。
模式化：`recurring`（0.948）、`patterns`（1.038）、`common`（0.494）。

读法：前者构成「正确／恰当／自然」的语言规范框架，后者把错误表述为**反复出现的模式**（"a recurring pattern"、"a common error"）。`natural` 已列入维度三 PENDING；`common` 的「常见错误」用法是一种正常化策略（与 5.2 同属手册排除的 paired acts 类）。

---

## 六、数据问题

### 6.1 议题内容残留 12 项（组 1 为 5 项）

确认残留 7 项：`society`、`students`、`modern`、`today`、`live`、`government`、`women`。
疑似残留 5 项待核：`people`、`she`、`he`、`her`、`become`——这批第三人称代词更可能来自 LOCNESS 作文内容的引述，而非反馈本身，须 concordance 确认。

与组 1 相同，这些词在维度一、维度二两层均为 N/A，**移除不改变任何已定标签占比**，只影响 N/A 计数与清单总数（131 → 119）。

### 6.2 手册 v3 强制查询清单仍未获得（沿自组 1 报告 5.4）

本组已按已知条目处理 `strong`（A1/A3 争议）。另将同词族的 `STRENGTH` 一并转为 PENDING——理由是它同时具备「元话语小标题」与「归功」两种读法，本身即需查证，并非仅因词族牵连。

`address` 在本组未出现。仍无法核查其余 129 个词位。风险最集中的已定项：`effective`、`powerful`、`meaningful`、`easy`、`balanced`（均为 A1 类正向形容词，与 `strong` 同属手册 5.2 所述目标态框架高风险区）、`avoid`、`adding`、`try`、`must`（A3 类）。**请提供 v3 强制查询清单全文，我按同一规则重扫组 1、组 2 共 259 个词位。**

---

## 七、下一步

1. **补齐 v3 强制查询清单**，重扫组 1＋组 2。
2. **concordance 判定 43 个词族**（附表 B9）。优先级排序：
   - 第一优先：`language`、`english`、`background`、`natural`（维度三，决定 RQ1 核心结论）
   - 第二优先：`GOOD`、`strong`、`CLEAR`、`important`（act 层，决定 A1 量级与 3.1 能否解读）
   - 第三优先：`ARTICLE`、`subject`、`complete`、`patterns`、`consistency`、`check`（维度一，决定 2.2 敏感性边界能否收窄）
   - `can`、`could` 按手册各抽 50 行，两层分别判
3. **验证组 1 第二节的最小化假设**（`correctness`／`mechanical` 左侧修饰语），本组已确认其前半部分。
4. **组 9／组 10（Baseline ↔ Generic）与组 11／组 12（Baseline ↔ L1）**：RQ3 的两对，可判断无标记 baseline 更接近哪一侧。
5. 两周后重编码 15%（组 1、2 合计 259 词位，抽 39 项）计算 intra-rater κ。

---
## 附表 A：组 2 完整编码表（131 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 act | 维度二 hedge | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | GOOD | 949 | 155.568 | 0.969 | NA | — | PENDING | NA | NA | — | act 层待定：good+better 归并，comparative 多嵌于目标态框架（make it better=A3）vs 评价（A1）；LL 全组最高，须查 |
| 2 | language | 642 | 150.991 | 1.210 | PENDING | — | NA | NA | PENDING | — | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词 |
| 3 | writing | 439 | 90.672 | 1.116 | NA | — | NA | NA | NA | M | 文本指称/写作过程，不指示层级 |
| 4 | corrections | 90 | 75.765 | 3.208 | G2 | Correctness | NA | NA | NA | M | 命名 Correctness 焦点的元话语标签；中性焦点名词，act 层不赋值 |
| 5 | academic | 841 | 73.006 | 0.669 | PENDING | — | NA | NA | NA | — | 维度一待定：属 register，手册列 tone/formal/register 为 PENDING |
| 6 | STRENGTH | 257 | 62.497 | 1.237 | NA | — | PENDING | NA | NA | — | act 层待定：反馈自身小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| 7 | grammar | 658 | 61.732 | 0.700 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示；中性焦点名词 |
| 8 | main | 716 | 50.709 | 0.597 | G1 | Ideas | NA | NA | NA | M | main point/argument/idea；子类 Ideas 与 Global Structure 边界待核 |
| 9 | english | 74 | 42.086 | 2.248 | NA | — | NA | NA | PENDING | — | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| 10 | USE | 1068 | 40.969 | 0.427 | PENDING | — | PENDING | NA | NA | — | 维度一待定：your use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定：use more examples(A3)vs 描述(NA) |
| 11 | ARTICLE | 167 | 39.363 | 1.213 | PENDING | — | NA | NA | NA | — | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；L2 语法标记的关键判别点 |
| 12 | original | 135 | 38.059 | 1.360 | NA | — | NA | NA | NA | M | 与 revised 配对的"原句/改后句"对照格式，元话语 |
| 13 | WORD | 537 | 36.891 | 0.587 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 14 | IDEA | 830 | 36.787 | 0.461 | G1 | Ideas | NA | NA | NA | H | Ideas 明示 |
| 15 | tense | 99 | 36.317 | 1.623 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 16 | suggestions | 160 | 34.698 | 1.151 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题"Suggestions:"（元话语 NA）vs 名词化建议行为（A3） |
| 17 | verb | 221 | 34.609 | 0.944 | G2 | Grammar | NA | NA | NA | H | Correctness/Grammar 明示 |
| 18 | vocabulary | 42 | 31.338 | 2.846 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 19 | try | 431 | 30.295 | 0.595 | NA | — | A3 | NA | NA | H | Hyland&Hyland 明示建议套语（the verb try） |
| 20 | thank | 50 | 30.185 | 2.360 | NA | — | NA | NA | NA | M | 人际礼貌行为（thank you for sharing），未归功于文本属性，不构成 A1；属手册排除的 paired acts 类 |
| 21 | some | 939 | 27.389 | 0.368 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 22 | important | 323 | 25.774 | 0.639 | NA | — | PENDING | NA | NA | — | act 层待定：an important point(A1)vs it is important to…(A3 框架) |
| 23 | OPINION | 215 | 23.490 | 0.764 | G1 | Ideas | NA | NA | NA | M | your opinion / opinion vs fact，属论断层 |
| 24 | revised | 107 | 22.721 | 1.136 | NA | — | NA | NA | NA | M | 与 original 配对的改写对照，元话语 |
| 25 | understandable | 62 | 22.275 | 1.600 | PENDING | — | A1 | NA | NA | L | 维度一待定（clear 系）；act 低信度：作为"低门槛褒扬"（your English is understandable）与 A1 定义是否相符须查 |
| 26 | too | 529 | 22.252 | 0.449 | NA | — | A2 | NA | NA | M | 标记过度=内在负向（同组 1 overly 口径）；polysemy 高于 overly，信度中等 |
| 27 | advice | 128 | 21.853 | 0.994 | NA | — | PENDING | NA | NA | — | act 层待定：反馈小标题（NA）vs my advice is to…（A3） |
| 28 | expressions | 49 | 21.536 | 1.846 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 29 | CLEAR | 1289 | 21.466 | 0.274 | PENDING | — | PENDING | NA | NA | — | 维度一待定（手册 clear 系）；act 层待定：clear(A1)vs clearer 目标态框架(A3) |
| 30 | clearly | 502 | 21.342 | 0.451 | PENDING | — | NA | NA | NA | — | 维度一待定（clear 系）；方式副词，act 层不赋值 |
| 31 | comment | 57 | 20.908 | 1.623 | NA | — | NA | NA | NA | M | 元话语（a comment on… / 小标题） |
| 32 | IMPROVE | 351 | 19.082 | 0.516 | NA | — | A3 | NA | NA | M | 改进指向，层级由宾语决定 |
| 33 | sharing | 37 | 19.045 | 2.078 | NA | — | NA | NA | NA | M | 人际礼貌（thank you for sharing） |
| 34 | sentences | 596 | 18.775 | 0.384 | G2 | Local Structure | NA | NA | NA | H | Local Structure 明示 |
| 35 | formal | 364 | 18.406 | 0.496 | PENDING | — | NA | NA | NA | — | 维度一待定（register）；命名目标态而非评价，act 层不赋值 |
| 36 | choice | 395 | 18.378 | 0.474 | G2 | Wording | NA | NA | NA | M | word choice；your choice of topic 读法待观察 |
| 37 | many | 557 | 17.631 | 0.385 | NA | — | NA | NA | NA | M | 量词 |
| 38 | eg | 339 | 17.437 | 0.501 | NA | — | NA | NA | NA | M | 举例元话语（e.g.），与组 1 的 for instance 构成对照 |
| 39 | people | 608 | 17.362 | 0.364 | NA | — | NA | NA | NA | M | 疑似议题内容残留（LOCNESS 主题）；people reading your essay 读法待核 |
| 40 | avoid | 308 | 17.180 | 0.524 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 41 | strong | 711 | 16.819 | 0.330 | NA | — | PENDING | NA | NA | — | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类 |
| 42 | may | 404 | 15.676 | 0.430 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 43 | final | 414 | 15.633 | 0.423 | PENDING | — | NA | NA | NA | — | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA) |
| 44 | topic | 602 | 15.441 | 0.344 | PENDING | — | NA | NA | NA | — | 维度一待定：the topic of your essay(G1-Ideas)vs topic sentence(G2/G1 边界) |
| 45 | example | 1106 | 14.446 | 0.241 | G1 | Development | NA | NA | NA | H | Development 明示 |
| 46 | very | 173 | 14.331 | 0.653 | NA | — | NA | NA | NA | M | 强化词，非 hedge |
| 47 | past | 73 | 13.816 | 1.058 | G2 | Grammar | NA | NA | NA | M | past tense |
| 48 | here | 250 | 13.390 | 0.512 | NA | — | NA | NA | NA | M | 指示元话语 |
| 49 | informal | 190 | 12.535 | 0.575 | PENDING | — | A2 | NA | NA | — | 维度一待定（register）；学术语境下标记偏离=负向（同组 1 casual 口径） |
| 50 | recurring | 77 | 12.139 | 0.948 | NA | — | NA | NA | NA | M | recurring errors/patterns，层级由宾语决定；构成"错误模式化"框架 |
| 51 | easy | 70 | 12.024 | 0.998 | NA | — | A1 | NA | NA | M | easy to follow/read，正向评价；目标态框架风险 |
| 52 | society | 248 | 11.650 | 0.477 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 53 | form | 106 | 11.633 | 0.766 | G2 | Grammar | NA | NA | NA | M | verb form / the correct form |
| 54 | below | 163 | 11.362 | 0.593 | NA | — | NA | NA | NA | M | 指示元话语（see below） |
| 55 | she | 70 | 11.242 | 0.958 | NA | — | NA | NA | NA | M | 疑似议题内容残留（引述作文内容），待核 |
| 56 | correct | 152 | 10.825 | 0.600 | G2 | Correctness | PENDING | NA | NA | — | act 层待定：correct these errors(A3)vs the correct form(NA) |
| 57 | luck | 36 | 10.613 | 1.401 | NA | — | NA | NA | NA | M | 人际礼貌（good luck） |
| 58 | your | 5416 | 10.514 | 0.090 | NA | — | NA | NA | NA | M | 人称代词，无固定层级所指 |
| 59 | introduction | 579 | 10.393 | 0.285 | G1 | Global Structure | NA | NA | NA | H | 大单位，Global Structure 明示 |
| 60 | PHRASE | 320 | 10.301 | 0.389 | G2 | Wording | NA | NA | NA | H | Wording 明示 |
| 61 | patterns | 56 | 10.274 | 1.038 | PENDING | — | NA | NA | NA | — | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| 62 | briefly | 119 | 10.223 | 0.666 | NA | — | NA | PENDING | NA | — | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA） |
| 63 | please | 55 | 9.677 | 1.012 | NA | — | NA | NA | NA | M | 礼貌标记；手册 M1 限于 hedges，礼貌标记不入 M1 |
| 64 | helps | 95 | 9.479 | 0.725 | NA | — | NA | NA | NA | M | 描述性动词（this helps the reader） |
| 65 | adding | 128 | 8.996 | 0.595 | NA | — | A3 | NA | NA | H | 手册 A3 明示（add） |
| 66 | consistency | 105 | 8.990 | 0.665 | PENDING | — | NA | NA | NA | — | 维度一待定：consistency of tense(G2)vs of argument(G1) |
| 67 | background | 105 | 8.990 | 0.665 | PENDING | — | NA | NA | PENDING | — | 维度三待定：your language background(C1)vs background information(G1-Development) |
| 68 | can | 680 | 8.843 | 0.241 | NA | — | PENDING | PENDING | NA | — | 与 could/might/would 同类共享项：you can add(A3)vs this can be confusing(M1)；两层分别判 |
| 69 | check | 144 | 8.774 | 0.550 | PENDING | — | A3 | NA | NA | — | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示 |
| 70 | students | 151 | 8.758 | 0.535 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 71 | balanced | 87 | 8.698 | 0.726 | G1 | Ideas | A1 | NA | NA | M | a balanced argument/view，域固定于论断；正向评价 |
| 72 | mention | 130 | 8.417 | 0.569 | NA | — | PENDING | NA | NA | — | act 层待定：you mention X（描述 NA）vs consider mentioning（A3） |
| 73 | accuracy | 112 | 8.387 | 0.617 | G2 | Correctness | NA | NA | NA | H | Correctness 明示 |
| 74 | subject | 181 | 8.346 | 0.472 | PENDING | — | NA | NA | NA | — | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1) |
| 75 | agreement | 182 | 8.302 | 0.469 | G2 | Grammar | NA | NA | NA | H | subject-verb agreement |
| 76 | complex | 76 | 8.273 | 0.763 | PENDING | — | NA | NA | NA | — | 维度一待定：complex sentences(G2-Local)vs complex ideas(G1) |
| 77 | suggested | 86 | 8.255 | 0.710 | NA | — | PENDING | NA | NA | — | act 层待定：the suggested revision（NA）vs I suggested（A3） |
| 78 | long | 248 | 8.131 | 0.393 | G2 | Local Structure | NA | NA | NA | M | long sentences，句级冗长；评价由 too 承担 |
| 79 | modern | 117 | 8.010 | 0.587 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 80 | meaningful | 41 | 7.948 | 1.074 | NA | — | A1 | NA | NA | M | 正向评价；目标态框架风险 |
| 81 | i | 431 | 7.786 | 0.286 | NA | — | NA | NA | NA | M | 反馈者自称（I suggest/I noticed）＝人称归因，属手册排除的缓和策略，不入 M1 |
| 82 | write | 264 | 7.688 | 0.368 | NA | — | PENDING | NA | NA | — | act 层待定：when you write（描述 NA）vs write this as…（A3） |
| 83 | he | 110 | 7.625 | 0.591 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核 |
| 84 | today | 54 | 7.606 | 0.886 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 85 | spelling | 294 | 7.492 | 0.343 | G2 | Mechanics | NA | NA | NA | H | Mechanics 明示 |
| 86 | only | 333 | 7.195 | 0.314 | NA | — | NA | PENDING | NA | — | hedge 层待定：最小化降调（only a few errors=M1）vs 限定（NA）；同组 1 just |
| 87 | complete | 99 | 7.088 | 0.602 | PENDING | — | NA | NA | NA | — | 维度一待定：complete sentence（句子残缺，G2-Grammar）vs complete your argument(G1) |
| 88 | slightly | 58 | 6.988 | 0.809 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 89 | must | 121 | 6.914 | 0.531 | NA | — | A3 | NA | NA | H | 手册 A3 明示 |
| 90 | makes | 216 | 6.788 | 0.384 | NA | — | NA | NA | NA | M | 轻动词 |
| 91 | possible | 192 | 6.642 | 0.404 | NA | — | NA | PENDING | NA | — | hedge 层待定：it is possible that（M1）vs possible improvements（NA） |
| 92 | areas | 267 | 6.350 | 0.331 | NA | — | NA | NA | NA | M | 元话语（areas for improvement，反馈小标题） |
| 93 | probably | 59 | 6.252 | 0.751 | NA | — | NA | M1 | NA | H | 认识型 hedge，与手册 possibly/maybe 同类 |
| 94 | become | 293 | 6.098 | 0.308 | NA | — | NA | NA | NA | M | 疑似议题内容残留（has become），待核 |
| 95 | natural | 49 | 5.731 | 0.795 | PENDING | — | PENDING | NA | PENDING | — | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；若判 C1 则维度一二依规则归 NA |
| 96 | statement | 156 | 5.716 | 0.417 | G1 | Ideas | NA | NA | NA | M | thesis statement |
| 97 | live | 55 | 5.576 | 0.732 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 98 | facts | 103 | 5.575 | 0.515 | G1 | Development | NA | NA | NA | M | facts vs opinion，证据类型 |
| 99 | content | 107 | 5.369 | 0.494 | G1 | Ideas | NA | NA | NA | M | 内容层，与 organization 对举 |
| 100 | common | 107 | 5.369 | 0.494 | NA | — | NA | NA | NA | M | 常见性标记（a common error）＝正常化框架；属手册排除的缓和策略，不入 M1 |
| 101 | contain | 80 | 5.345 | 0.579 | NA | — | NA | NA | NA | M | 描述性动词 |
| 102 | effective | 170 | 5.285 | 0.382 | NA | — | A1 | NA | NA | M | 手册 A1 明示；目标态框架风险 |
| 103 | details | 49 | 5.133 | 0.746 | G1 | Development | NA | NA | NA | H | Development 明示 |
| 104 | sometimes | 148 | 5.076 | 0.402 | NA | — | NA | M1 | NA | H | 手册 v3 M1 明示 hedge |
| 105 | relevant | 114 | 5.048 | 0.462 | G1 | Development | NA | NA | NA | M | relevant evidence/examples |
| 106 | view | 99 | 5.029 | 0.498 | G1 | Ideas | NA | NA | NA | M | your view / opposing views |
| 107 | powerful | 61 | 4.974 | 0.647 | NA | — | A1 | NA | NA | M | 手册 A1 明示 |
| 108 | restate | 134 | 4.933 | 0.418 | G1 | Global Structure | A3 | NA | NA | M | restate your thesis in the conclusion，大单位安排 |
| 109 | focus | 466 | 4.919 | 0.216 | PENDING | — | PENDING | NA | NA | — | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定：focus on X(A3)vs 描述(NA) |
| 110 | essays | 46 | 4.914 | 0.754 | NA | — | NA | NA | NA | M | 文体指称（academic essays），常见于规范陈述框架 |
| 111 | end | 243 | 4.736 | 0.298 | G1 | Global Structure | NA | NA | NA | M | the end of your essay/paragraph |
| 112 | organization | 396 | 4.671 | 0.229 | G1 | Global Structure | NA | NA | NA | H | Global Structure 明示 |
| 113 | shorter | 59 | 4.659 | 0.636 | G2 | Local Structure | NA | NA | NA | M | shorter sentences；比较级，评价由框架承担 |
| 114 | government | 117 | 4.599 | 0.433 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 115 | thinking | 57 | 4.347 | 0.623 | G1 | Ideas | NA | NA | NA | M | your thinking / critical thinking，论述能力 |
| 116 | accurate | 63 | 4.346 | 0.589 | PENDING | — | A1 | NA | NA | — | 维度一待定：accurate facts(G1-Dev)vs accurate grammar(G2)；正向评价 |
| 117 | her | 91 | 4.326 | 0.480 | NA | — | NA | NA | NA | M | 疑似议题内容残留，待核 |
| 118 | could | 499 | 4.275 | 0.194 | NA | — | PENDING | PENDING | NA | — | 手册指定共享项，抽 50 行分别判 act 层与 hedge 层 |
| 119 | effort | 71 | 4.243 | 0.544 | NA | — | NA | NA | NA | L | 低信度：归功对象为写作者努力而非文本属性；若与 GOOD/great 共现构成归功则应改判 A1 |
| 120 | women | 316 | 4.215 | 0.244 | NA | — | NA | NA | NA | H | 议题内容残留 |
| 121 | reduce | 139 | 4.200 | 0.376 | PENDING | — | A3 | NA | NA | — | 维度一待定：reduce wordiness(G2)vs reduce scope(G1) |
| 122 | choose | 102 | 4.199 | 0.444 | NA | — | A3 | NA | NA | M | choose more precise words，层级由宾语决定 |
| 123 | difficult | 94 | 4.192 | 0.464 | NA | — | A2 | NA | NA | M | difficult to follow，负向评价 |
| 124 | shows | 255 | 4.158 | 0.271 | NA | — | NA | NA | NA | M | 描述性框架动词 |
| 125 | proper | 73 | 4.125 | 0.528 | G2 | Correctness | NA | NA | NA | M | proper grammar/punctuation；规范性框架词 |
| 126 | unclear | 153 | 4.114 | 0.353 | PENDING | — | A2 | NA | NA | — | 维度一待定（手册 clear 系）；负向评价 |
| 127 | emotional | 217 | 4.076 | 0.292 | PENDING | — | NA | NA | NA | — | 维度一待定：emotional language(G2-Wording/register)vs emotional appeal(G1-Ideas)；亦可能为议题残留 |
| 128 | especially | 204 | 4.066 | 0.301 | NA | — | NA | NA | NA | M | 焦点副词 |
| 129 | neutral | 62 | 3.980 | 0.566 | PENDING | — | NA | NA | NA | — | 维度一待定（tone/register）；客观性规范框架词 |
| 130 | discuss | 110 | 3.913 | 0.410 | G1 | Ideas | PENDING | NA | NA | — | act 层待定：you discuss X（描述 NA）vs discuss counterarguments（A3） |
| 131 | we | 152 | 3.884 | 0.344 | NA | — | NA | NA | NA | M | 包容性人称，团结策略；不入 M1 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G2 | 19 | 52.8% | 4306 | 45.8% | 0.969 |
| G1 | 17 | 47.2% | 5101 | 54.2% | 0.481 |
| **已定标签合计** | **36** | **100.0%** | **9407** | **100.0%** | — |
| N/A（不计入分母） | 70 | — | — | — | — |
| PENDING（不计入分母） | 25 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

**子类分布（分母同为已定标签 36）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 4 | 11.1% |
| G1 | Global Structure | 4 | 11.1% |
| G1 | Ideas | 9 | 25.0% |
| G2 | Correctness | 4 | 11.1% |
| G2 | Grammar | 6 | 16.7% |
| G2 | Local Structure | 3 | 8.3% |
| G2 | Mechanics | 1 | 2.8% |
| G2 | Wording | 5 | 13.9% |

### B2 维度二 · act 层（A1 Praise / A2 Criticism / A3 Suggestion）

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| A3 | 9 | 45.0% | 1858 | 55.0% | 0.505 |
| A1 | 7 | 35.0% | 554 | 16.4% | 0.859 |
| A2 | 4 | 20.0% | 966 | 28.6% | 0.460 |
| **已定标签合计** | **20** | **100.0%** | **3378** | **100.0%** | — |
| N/A（不计入分母） | 94 | — | — | — | — |
| PENDING（不计入分母） | 17 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

### B3 维度二 · hedge 层（M1 Hedges）

hedge 层与 act 层并行判定、可共存（Hyland & Hyland：hedge 施加于 act 之上）。分母为本层已定标签数。

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| M1 | 5 | 100.0% | 1608 | 100.0% | 0.552 |
| **已定标签合计** | **5** | **100.0%** | **1608** | **100.0%** | — |
| N/A（不计入分母） | 121 | — | — | — | — |
| PENDING（不计入分母） | 5 | — | — | — | — |
| 清单总数 | 131 | — | — | — | — |

### B4 维度三 Larger Contexts of Writing

**已定标签 0 项** —— 本层无任何词位获得标签，占比不适用（分母为 0）。

| 标签 | 词位数 | Freq_Tar 合计 |
|---|---:|---:|
| 已定标签合计 | 0 | 0 |
| N/A（不计入分母） | 127 | — |
| PENDING（不计入分母） | 4 | — |
| 清单总数 | 131 | — |

### B5 维度二两层共现（词位数）

| act ＼ hedge | M1 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|
| **A1** | 0 | 7 | 0 | **7** |
| **A2** | 0 | 4 | 0 | **4** |
| **A3** | 0 | 9 | 0 | **9** |
| **NA** | 5 | 86 | 3 | **94** |
| **PENDING** | 0 | 15 | 2 | **17** |
| **合计** | 5 | 121 | 5 | **131** |

act ＋ hedge 双标签共现：**0** 项

### B6 维度一 × 维度二 act 层 交叉表（词位数）

| 维度一＼act | A1 | A2 | A3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 1 | 0 | 1 | 14 | 1 | **17** |
| **G2** | 0 | 0 | 0 | 18 | 1 | **19** |
| **NA** | 4 | 2 | 6 | 47 | 11 | **70** |
| **PENDING** | 2 | 2 | 2 | 15 | 4 | **25** |
| **合计** | 7 | 4 | 9 | 94 | 17 | **131** |

### B7 LL 前 20 词位的维度一构成

| | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 词位数 | 2 | 6 | 8 | 4 |

### B8 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 17 | 19 | 47.2% |
| 25 个 PENDING 全归 G1（上界） | 42 | 19 | 68.9% |
| 25 个 PENDING 全归 G2（下界） | 17 | 44 | 27.9% |

### B9 concordance 待办清单

共 **43** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | Freq_Tar | 待定层 | 竞争读法 |
|---|---:|---|---|
| `GOOD` | 949 | act | act 层待定：good+better 归并，comparative 多嵌于目标态框架（make it better=A3）vs 评价（A1）；LL 全组最高，须查 |
| `language` | 642 | 维度一、维度三 | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词 |
| `academic` | 841 | 维度一 | 维度一待定：属 register，手册列 tone/formal/register 为 PENDING |
| `STRENGTH` | 257 | act | act 层待定：反馈自身小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| `english` | 74 | 维度三 | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| `USE` | 1068 | 维度一、act | 维度一待定：your use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定：use more examples(A3)vs 描述(NA) |
| `ARTICLE` | 167 | 维度一 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；L2 语法标记的关键判别点 |
| `suggestions` | 160 | act | act 层待定：反馈小标题"Suggestions:"（元话语 NA）vs 名词化建议行为（A3） |
| `important` | 323 | act | act 层待定：an important point(A1)vs it is important to…(A3 框架) |
| `understandable` | 62 | 维度一、低信度复核 | 维度一待定（clear 系）；act 低信度：作为"低门槛褒扬"（your English is understandable）与 A1 定义是否相符须查 |
| `advice` | 128 | act | act 层待定：反馈小标题（NA）vs my advice is to…（A3） |
| `CLEAR` | 1289 | 维度一、act | 维度一待定（手册 clear 系）；act 层待定：clear(A1)vs clearer 目标态框架(A3) |
| `clearly` | 502 | 维度一 | 维度一待定（clear 系）；方式副词，act 层不赋值 |
| `formal` | 364 | 维度一 | 维度一待定（register）；命名目标态而非评价，act 层不赋值 |
| `strong` | 711 | act | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类 |
| `final` | 414 | 维度一 | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA) |
| `topic` | 602 | 维度一 | 维度一待定：the topic of your essay(G1-Ideas)vs topic sentence(G2/G1 边界) |
| `informal` | 190 | 维度一 | 维度一待定（register）；学术语境下标记偏离=负向（同组 1 casual 口径） |
| `correct` | 152 | act | act 层待定：correct these errors(A3)vs the correct form(NA) |
| `patterns` | 56 | 维度一 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `briefly` | 119 | hedge | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA） |
| `consistency` | 105 | 维度一 | 维度一待定：consistency of tense(G2)vs of argument(G1) |
| `background` | 105 | 维度一、维度三 | 维度三待定：your language background(C1)vs background information(G1-Development) |
| `can` | 680 | act、hedge | 与 could/might/would 同类共享项：you can add(A3)vs this can be confusing(M1)；两层分别判 |
| `check` | 144 | 维度一 | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示 |
| `mention` | 130 | act | act 层待定：you mention X（描述 NA）vs consider mentioning（A3） |
| `subject` | 181 | 维度一 | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1) |
| `complex` | 76 | 维度一 | 维度一待定：complex sentences(G2-Local)vs complex ideas(G1) |
| `suggested` | 86 | act | act 层待定：the suggested revision（NA）vs I suggested（A3） |
| `write` | 264 | act | act 层待定：when you write（描述 NA）vs write this as…（A3） |
| `only` | 333 | hedge | hedge 层待定：最小化降调（only a few errors=M1）vs 限定（NA）；同组 1 just |
| `complete` | 99 | 维度一 | 维度一待定：complete sentence（句子残缺，G2-Grammar）vs complete your argument(G1) |
| `possible` | 192 | hedge | hedge 层待定：it is possible that（M1）vs possible improvements（NA） |
| `natural` | 49 | 维度一、act、维度三 | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；若判 C1 则维度一二依规则归 NA |
| `focus` | 466 | 维度一、act | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定：focus on X(A3)vs 描述(NA) |
| `accurate` | 63 | 维度一 | 维度一待定：accurate facts(G1-Dev)vs accurate grammar(G2)；正向评价 |
| `could` | 499 | act、hedge | 手册指定共享项，抽 50 行分别判 act 层与 hedge 层 |
| `effort` | 71 | 低信度复核 | 低信度：归功对象为写作者努力而非文本属性；若与 GOOD/great 共现构成归功则应改判 A1 |
| `reduce` | 139 | 维度一 | 维度一待定：reduce wordiness(G2)vs reduce scope(G1) |
| `unclear` | 153 | 维度一 | 维度一待定（手册 clear 系）；负向评价 |
| `emotional` | 217 | 维度一 | 维度一待定：emotional language(G2-Wording/register)vs emotional appeal(G1-Ideas)；亦可能为议题残留 |
| `neutral` | 62 | 维度一 | 维度一待定（tone/register）；客观性规范框架词 |
| `discuss` | 110 | act | act 层待定：you discuss X（描述 NA）vs discuss counterarguments（A3） |

### B10 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | act | hedge |
|---|---:|---:|---|---|---|
| corrections | 75.765 | 3.208 | G2/Correctness | NA | NA |
| vocabulary | 31.338 | 2.846 | G2/Wording | NA | NA |
| thank | 30.185 | 2.360 | NA | NA | NA |
| english | 42.086 | 2.248 | NA | NA | NA |
| sharing | 19.045 | 2.078 | NA | NA | NA |
| expressions | 21.536 | 1.846 | G2/Wording | NA | NA |
| tense | 36.317 | 1.623 | G2/Grammar | NA | NA |
| comment | 20.908 | 1.623 | NA | NA | NA |
| understandable | 22.275 | 1.600 | PENDING | A1 | NA |
