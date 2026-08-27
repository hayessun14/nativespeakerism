# 组 1 关键词质性分类编码报告
## L1 → Generic（目标语料 = L1 条件，参照语料 = Generic 条件）

> **编码日期**：2026-08-27（第一轮编码，本 commit 时间戳即为 intra-rater 信度所需的第一轮时间记录）
> **编码对象集**：本清单全部 128 词位，不跨清单求并集
> **占比分母**：各维度**已定标签数**（N/A 与 PENDING 单列报告，不计入分母）
> **编码依据**：Straub & Lunsford (1995) / Hyland & Hyland (2001)；Holliday 不参与本阶段判定

---

## 一、结果摘要

| 维度 | 已定标签 | 主要分布 | N/A | PENDING |
|---|---:|---|---:|---:|
| 一 Feedback Focus | 53 | **G1 81.1%**（43）／ G2 18.9%（10） | 53 | 22 |
| 二 Feedback Acts | 41 | **D3 48.8%**（20）／ D2 31.7%（13）／ D1 19.5%（8） | 81 | 6 |
| 三 Larger Contexts | 0 | **C1 = 0** | 127 | 1 |
| D0 Mitigation（补充） | — | 确认 hedge 2（`fairly`, `risk`） | 123 | 3 |

**一句话概括**：当写作者被标记为英语母语者时，相对于未指明母语的非母语者，反馈的过量词汇高度集中在**全局层面**（G1 81.1%，词次口径 86.9%），言语行为以**建议**为主（D3 词次口径 76.2%），且**完全没有出现任何语言身份或跨语言框架词**（C1 = 0）。

---

## 二、维度一：焦点向全局层面倾斜

已定标签 53 项中 G1 占 81.1%，子类以 **Ideas 54.7%**（29 项）为绝对主体：`CLAIM`、`reasoning`、`ASSERT`、`assertion`、`arguing`、`analysis`、`counterarguments`、`core`、`framing`、`skeptical`、`complexity`、`defensible`、`arguable`、`sweeping` 等，构成一个围绕**论断的可辩护性与论证质量**的密集词场。Development 18.9%（`evidence`、`detail`、`anecdote`、`credibility`、`material`、`RELY`、`integrate`、`underdeveloped`），Global Structure 7.5%（`reorganize`、`structural`、`section`、`opening`）。

敏感性检验（附表 B7）：即使 22 个 PENDING 全部归入 G2（最不利于该结论的极端假设），G1 仍占 57.3%；全归 G1 则升至 86.7%。**结论方向不随 PENDING 归属翻转**。

### 一个需要 concordance 验证的反常现象

维度一的最高效应量词位却落在 G2：`correctness`（LR 3.284，全表最高）、`mechanical`（LR 1.836）、`prose`（LR 1.654）。这看似与"L1 侧偏全局"矛盾。

值得注意的是这三个词都是**范畴的元标签**，而非该范畴的具体操作词。真正执行局部纠错的具体词汇（`grammar`、`verb`、`tense`、`article`、`plural`、`agreement`、`spelling`、`vocabulary` 等）在本清单中一个都没有出现在 L1 侧——它们成组出现在 Generic 侧（参见组 10 的 `grammar` LL 55.167、`verb` LL 41.820、`tense` LL 25.892、`vocabulary` LL 19.937）。

由此可提出一个**待检验假设**（尚不构成结论）：L1 条件的反馈倾向于把局部正确性作为一个**被命名并快速带过的范畴**处理（"a few mechanical issues"、"minor points of correctness"），而 Generic 条件则**直接实施**语法层面的纠正。支持这一读法的旁证是 `just`、`fairly`、`rather`、`minor` 类降调词同样落在 L1 侧。

**验证方法**：抽取 `correctness` / `mechanical` 全部 137 次出现的 concordance，编码其左侧 5 词窗内是否出现最小化修饰语（minor / few / only / just / a couple of / largely / mostly）。若最小化率显著高于 Generic 侧 `grammar` 的对应比率，则假设成立。这一步必须做在解读之前——目前它只是一个方向。

---

## 三、维度二：以建议为主导，赞扬最少

已定标签 41 项：D3 建议 48.8%（词次口径 76.2%）、D2 批评 31.7%、D1 赞扬 19.5%。D3 的词次优势来自少数超高频套语：`should`（1312）、`NEED`（1069）、`STRENGTHEN`（476）——正是 Hyland & Hyland (2001: 191) 点名的 "need to / should" 建议套语。

维度一 × 维度二交叉表（附表 B5）显示：**G1 焦点上的 D3 有 9 项，G2 焦点上只有 2 项**（`cut`、`PROOFREAD`）。即 L1 侧的建议行为几乎全部指向论证与结构，而非表层修改。

D0 层面本组信息量有限：确认的 hedge 只有 `fairly` 与 `risk` 两项，`rather`、`would`、`might` 待判。缓和策略的跨条件比较要等组 2（Generic → L1）出来才有意义——`slightly`、`probably`、`some`、`may` 这一批都在 Generic 侧。

---

## 四、维度三：C1 = 0（本组最重要的单一发现）

**128 个词位中，没有任何一个被编为 C1。** L1 条件相对 Generic 条件的过量词汇里，不含任何 transfer framing（interference / transfer / L1 / mother tongue / translate / native language）或 identity marking（native / non-native / speaker / learner / ESL）成分。

唯一的维度三 PENDING 是 `cultural`（Freq_Tar 80，LL 5.728），且它更可能是 LOCNESS 议题内容残留（见第五节）而非语言背景框架词——需 concordance 判定。若判为议题残留，本组 C1 将是**结构性的零**。

这个零值本身不足以支撑任何结论，但它规定了 RQ1 的证据形态：**语言身份框架不是双向浮动的，而是单向出现的**。若身份词汇成组出现在反向清单（组 2：Generic → L1）与 L2 各组，则说明"标记为非母语者"会引入一整套 L1 条件下完全不存在的词汇资源，而"标记为母语者"不引入任何对应物。初步旁证：`english`（组 10 LL 48.406，LR 2.536）、`language`（组 10 LL 143.329）、`SPEAKER`（组 6 LL 58.482 / 组 7 LL 79.165）全部落在非母语侧。组 2 编码完成后此点即可确证或推翻。

---

## 五、编码过程中发现的三个数据问题

### 5.1 议题内容残留 5 项未清除

交接文档称"LOCNESS 作文主题词已按 Tan et al. (2026) 先例移除"，但本组仍存留：

| # | Type | Freq_Tar | LL |
|---:|---|---:|---:|
| 70 | public | 275 | 7.105 |
| 94 | policy | 139 | 5.738 |
| 95 | cultural | 80 | 5.728 |
| 123 | power | 132 | 4.185 |
| 126 | financial | 93 | 3.920 |

（组 10 亦可见 `women`、`society`、`students` 等同类残留，待该组编码时一并处理。）

**影响评估**：这 5 项在维度一、维度二均为 N/A，因此**移除它们不改变任何已定标签的占比**，只影响 N/A 计数与清单总数（128 → 123）。唯一实质影响在维度三：`cultural` 是本组唯一的 C1 PENDING，若按议题残留移除，维度三将成为 0/0/123 的干净零值。建议在方法部分明确记录这一处理，而不是静默删除。

### 5.2 评价性形容词的"目标态框架"问题

Hyland & Hyland 是在语境中编码言语行为，而关键词层面只能看到词形。问题在于：AI 反馈中的正向形容词大量出现在**目标态框架**里（"make your thesis more defensible"）而非**评价框架**里（"your thesis is defensible"）。前者的言语行为其实是 D3，不是 D1。

受影响最大的是比较级/最高级：`sharper`（已标 D2 待定）、`strongest`、`broader`、`polished`、`measured`。我的处理是：原级正向形容词编 D1，比较级中读法分歧最大的 `sharper` 标 PENDING，其余以中等信度编 D1 并列入复核。**这会使 D1 的 8 项成为上界估计**；若 concordance 显示多数嵌于目标态框架，D1 将下修、D3 上修，方向是让本组"建议主导、赞扬稀缺"的图景更极端而非更弱。

### 5.3 `STRENGTHEN` 的子类边界

`STRENGTHEN`（Freq_Tar 476）在 G1 内部跨 Ideas 与 Development 两个子类（strengthen your argument / strengthen your evidence）。主类 G1 不受影响，仅子类占比受影响。已列入 concordance 清单。

---

## 六、下一步

1. **concordance 判定 30 个词族**（附表 B8）：22 个维度一 PENDING、6 个维度二 PENDING、3 个 D0 PENDING、1 个维度三 PENDING、2 个低信度复核（`authority`、`measured`）。`would` / `might` 按手册各随机抽 50 行。
2. **优先验证第二节的最小化假设**（`correctness` / `mechanical` 的左侧修饰语分布）——它决定第二节的反常现象如何解释。
3. **组 2（Generic → L1）编码**：这是 RQ1 的另一半，也是维度三 C1 结论的成败所在。
4. **两周后重编码 15%**（19 个词位随机抽样）计算 intra-rater κ。本次编码已 commit，时间戳可查。

---
## 附表 A：组 1 完整编码表（128 词位，按 LL 降序）

| # | Type | Freq_Tar | LL | LR | 维度一 | 子类 | 维度二 | D0 | 维度三 | 信度 | 判定依据 |
|---:|---|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | CLAIM | 1663 | 60.215 | 0.419 | G1 | Ideas | NA | — | NA | H | 论断/主张名词，Ideas 明示；本身中性，D2 不赋值 |
| 2 | rather | 833 | 53.374 | 0.574 | NA | — | NA | PEND | NA | — | D0待定：手册列为 hedge，但"rather than"（建议对比框架）可能占主导 |
| 3 | correctness | 60 | 49.868 | 3.284 | G2 | Correctness | NA | — | NA | H | 直接命名 Correctness 焦点 |
| 4 | aim | 92 | 40.757 | 1.900 | G1 | Ideas | PENDING | — | NA | — | D2待定："aim to/for"（D3）vs "your aim"（名词，NA） |
| 5 | paper | 216 | 40.595 | 1.073 | NA | — | NA | — | NA | H | 文本指称语，不指示层级 |
| 6 | SHARPEN | 138 | 38.143 | 1.370 | G1 | Ideas | D3 | — | NA | M | 主导搭配 sharpen your claim/thesis/argument |
| 7 | mechanical | 77 | 32.556 | 1.836 | G2 | Mechanics | NA | — | NA | H | mechanical errors |
| 8 | instance | 202 | 32.502 | 0.976 | NA | — | NA | — | NA | M | 主导为"for instance"元话语（反馈自身举例，非要求学生举例） |
| 9 | level | 298 | 26.954 | 0.697 | PENDING | — | NA | — | NA | — | D1待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev) |
| 10 | edit | 122 | 26.167 | 1.165 | PENDING | — | D3 | — | NA | — | D1待定：表层编辑(G2)vs全局修改(G1) |
| 11 | would | 786 | 25.427 | 0.395 | NA | — | PENDING | PEND | NA | — | 手册指定共享项，concordance 抽 50 行判 D3/D0 |
| 12 | reasoning | 281 | 25.299 | 0.695 | G1 | Ideas | NA | — | NA | H | Ideas 定义明示 lines of thought and reasoning |
| 13 | tighten | 44 | 24.264 | 2.251 | PENDING | — | D3 | — | NA | — | D1待定：tighten prose/sentences(G2)vs tighten argument(G1) |
| 14 | NEED | 1069 | 24.237 | 0.327 | NA | — | D3 | — | NA | H | need to = Hyland&Hyland 明示建议套语 |
| 15 | material | 166 | 23.774 | 0.910 | G1 | Development | NA | — | NA | M | source material，属支撑材料 |
| 16 | CLARIFY | 272 | 23.193 | 0.674 | PENDING | — | D3 | — | NA | — | D1待定：手册 clear/clarity 系列一律 PENDING |
| 17 | defensible | 53 | 23.177 | 1.882 | G1 | Ideas | D1 | — | NA | M | 域固定于 claim/thesis；正向评价，但存在目标态框架风险 |
| 18 | cut | 90 | 22.504 | 1.284 | G2 | Local Structure | D3 | — | NA | M | 删削冗余，句内/句间 |
| 19 | phrasing | 229 | 22.137 | 0.724 | G2 | Wording | NA | — | NA | H | Wording 明示 |
| 20 | RELY | 125 | 20.820 | 0.997 | G1 | Development | NA | — | NA | M | rely on evidence/sources |
| 21 | sweeping | 56 | 19.484 | 1.599 | G1 | Ideas | D2 | — | NA | H | sweeping generalization，域固定于论断 |
| 22 | vague | 126 | 19.002 | 0.939 | PENDING | — | D2 | — | NA | — | D1待定：与 unclear 同族，可指论证或用词 |
| 23 | credible | 125 | 18.466 | 0.928 | G1 | Development | D1 | — | NA | M | credible sources/evidence |
| 24 | distract | 58 | 18.333 | 1.498 | PENDING | — | D2 | — | NA | — | D1待定：typos distract(G2)vs digression distracts(G1) |
| 25 | authority | 65 | 17.372 | 1.340 | G1 | Ideas | NA | — | NA | L | 写作者论述权威/立场，归修辞语境→G1 |
| 26 | complexity | 63 | 17.104 | 1.354 | G1 | Ideas | NA | — | NA | M | acknowledge the complexity of the issue |
| 27 | might | 187 | 15.483 | 0.663 | NA | — | PENDING | PEND | NA | — | 手册指定共享项 |
| 28 | prose | 42 | 15.334 | 1.654 | G2 | Wording | NA | — | NA | M | 主导搭配 tighten/clarify your prose，句级文风 |
| 29 | even | 232 | 14.745 | 0.572 | NA | — | NA | — | NA | H | 焦点副词，非 hedge |
| 30 | something | 157 | 14.362 | 0.702 | NA | — | NA | — | NA | H | 不定指代 |
| 31 | credibility | 243 | 14.242 | 0.547 | G1 | Development | NA | — | NA | M | 与 credible 同域 |
| 32 | reads | 180 | 14.237 | 0.646 | PENDING | — | NA | — | NA | — | D1待定：the essay reads(整体)vs this sentence reads(句级) |
| 33 | just | 263 | 13.922 | 0.517 | NA | — | PENDING | — | NA | — | D0待定：最小化降调(D0)vs"仅仅是"强化批评(NA) |
| 34 | PROOFREAD | 317 | 13.708 | 0.463 | G2 | Correctness | D3 | — | NA | H | 校对行动，Correctness+建议 |
| 35 | currently | 259 | 13.426 | 0.511 | NA | — | NA | — | NA | M | 元话语对比框架（现状→建议），本身非行为 |
| 36 | analysis | 319 | 13.244 | 0.453 | G1 | Ideas | NA | — | NA | H | Ideas 明示 analysis |
| 37 | precision | 99 | 12.952 | 0.863 | PENDING | — | NA | — | NA | — | D1待定：precision of language(G2)vs of claims(G1) |
| 38 | ASSERT | 99 | 12.952 | 0.863 | G1 | Ideas | NA | — | NA | H | assertions 属 Ideas |
| 39 | MATTER | 235 | 12.814 | 0.525 | G1 | Ideas | NA | — | NA | M | why this matters，论点意义 |
| 40 | shifts | 82 | 12.100 | 0.927 | PENDING | — | NA | — | NA | — | D1待定：tense shifts(G2-Grammar)vs shifts in focus(G1) |
| 41 | case | 269 | 11.659 | 0.463 | G1 | Ideas | NA | — | NA | M | make the case for，论证整体 |
| 42 | arguing | 95 | 11.652 | 0.831 | G1 | Ideas | NA | — | NA | H | Ideas 明示 arguments |
| 43 | GIVE | 296 | 11.493 | 0.436 | NA | — | NA | — | NA | M | gives/given 混合，无固定层级所指 |
| 44 | contains | 53 | 10.442 | 1.105 | NA | — | NA | — | NA | H | 描述性动词 |
| 45 | address | 264 | 10.241 | 0.436 | G1 | Ideas | D3 | — | NA | M | 主导 address counterarguments/objections |
| 46 | reorganize | 109 | 10.115 | 0.708 | G1 | Global Structure | D3 | — | NA | H | 大单位重排，Global Structure 明示 |
| 47 | distinct | 82 | 9.980 | 0.827 | G1 | Ideas | NA | — | NA | M | distinct points/ideas |
| 48 | STRENGTHEN | 476 | 9.959 | 0.314 | G1 | Ideas | D3 | — | NA | M | strengthen your argument/thesis；Ideas/Development 子类边界待核 |
| 49 | assertion | 58 | 9.909 | 1.012 | G1 | Ideas | NA | — | NA | H | Ideas 明示 |
| 50 | strongest | 180 | 9.728 | 0.523 | NA | — | D1 | — | NA | M | 通用评价级差词，层级由宾语决定→D1 归属受目标态框架影响 |
| 51 | then | 382 | 9.538 | 0.344 | NA | — | NA | — | NA | H | 连接副词 |
| 52 | measured | 65 | 9.069 | 0.897 | PENDING | — | D1 | — | NA | L | D1待定：属 tone/register，手册列 PENDING；D2 判定信度低 |
| 53 | arguable | 76 | 9.057 | 0.817 | G1 | Ideas | D1 | — | NA | M | an arguable thesis，域固定于论断 |
| 54 | should | 1312 | 8.964 | 0.175 | NA | — | D3 | — | NA | H | Hyland&Hyland 明示建议套语 |
| 55 | right | 548 | 8.749 | 0.272 | PENDING | — | NA | — | NA | — | D1待定：the right word(G2)vs right now(NA) |
| 56 | line | 86 | 8.715 | 0.744 | PENDING | — | NA | — | NA | — | D1待定：line of reasoning(G1)vs this line(G2) |
| 57 | now | 594 | 8.532 | 0.257 | NA | — | NA | — | NA | H | 时间/话语副词 |
| 58 | structural | 92 | 8.460 | 0.704 | G1 | Global Structure | NA | — | NA | H | structural issues，大单位 |
| 59 | engage | 45 | 8.306 | 1.061 | G1 | Ideas | D3 | — | NA | M | engage with counterarguments/the reader |
| 60 | piece | 123 | 8.076 | 0.582 | NA | — | NA | — | NA | H | 文本指称语 |
| 61 | imprecise | 46 | 8.032 | 1.026 | PENDING | — | D2 | — | NA | — | D1待定：同 precision |
| 62 | detail | 43 | 7.996 | 1.066 | G1 | Development | NA | — | NA | H | Development 明示 detail |
| 63 | alone | 60 | 7.933 | 0.869 | NA | — | NA | — | NA | H | 限定副词 |
| 64 | written | 47 | 7.774 | 0.993 | NA | — | NA | — | NA | M | 被动分词，无固定层级所指 |
| 65 | section | 164 | 7.768 | 0.486 | G1 | Global Structure | NA | — | NA | M | 大于段落的单位 |
| 66 | analytical | 153 | 7.758 | 0.505 | G1 | Ideas | NA | — | NA | M | analytical depth/analytical claim；描述论述方式而非归功 |
| 67 | building | 48 | 7.532 | 0.962 | G1 | Ideas | NA | — | NA | M | building on/building your argument |
| 68 | similarly | 67 | 7.365 | 0.780 | NA | — | NA | — | NA | H | 连接副词 |
| 69 | typos | 71 | 7.360 | 0.754 | G2 | Mechanics | NA | — | NA | H | Mechanics 明示 |
| 70 | public | 275 | 7.105 | 0.351 | NA | — | NA | — | NA | H | 议题内容残留（LOCNESS 主题词） |
| 71 | underdeveloped | 65 | 7.062 | 0.775 | G1 | Development | D2 | — | NA | H | Development 域固定，负向 |
| 72 | actual | 176 | 7.047 | 0.444 | NA | — | NA | — | NA | M | 对比性强调词 |
| 73 | carefully | 324 | 6.984 | 0.319 | NA | — | NA | — | NA | M | 方式副词，非 hedge 非行为 |
| 74 | precisely | 41 | 6.834 | 0.997 | NA | — | NA | — | NA | M | 方式副词 |
| 75 | define | 94 | 6.696 | 0.609 | PENDING | — | D3 | — | NA | — | D1待定：define your terms 属 Wording(G2)还是概念澄清(G1) |
| 76 | evidence | 1389 | 6.644 | 0.145 | G1 | Development | NA | — | NA | H | Development 核心 |
| 77 | four | 49 | 6.572 | 0.876 | NA | — | NA | — | NA | M | 数量词，多为反馈条目枚举 |
| 78 | specifically | 96 | 6.502 | 0.592 | NA | — | NA | — | NA | M | 元话语副词（区别于手册中 PENDING 的 specific） |
| 79 | concerns | 78 | 6.440 | 0.662 | NA | — | D2 | — | NA | M | my main concerns are…，批评标记语 |
| 80 | placeholder | 70 | 6.353 | 0.699 | G2 | Wording | D2 | — | NA | M | placeholder phrases/language，空泛措辞 |
| 81 | loosely | 40 | 6.277 | 0.962 | PENDING | — | D2 | — | NA | — | D1待定：loosely connected(G1 连贯)vs loosely worded(G2) |
| 82 | replace | 166 | 6.264 | 0.430 | PENDING | — | D3 | — | NA | — | D1待定：replace this word(G2)vs replace this paragraph(G1) |
| 83 | takes | 37 | 6.207 | 1.001 | NA | — | NA | — | NA | M | 轻动词 |
| 84 | core | 63 | 6.167 | 0.730 | G1 | Ideas | NA | — | NA | H | core claim/argument |
| 85 | acknowledge | 106 | 6.071 | 0.540 | G1 | Ideas | D3 | — | NA | M | acknowledge counterarguments |
| 86 | distinguish | 41 | 6.049 | 0.927 | G1 | Ideas | D3 | — | NA | M | distinguish between claims |
| 87 | improving | 64 | 6.030 | 0.714 | NA | — | D3 | — | NA | M | 改进指向，层级由宾语决定 |
| 88 | risk | 64 | 6.030 | 0.714 | NA | — | NA | ✔ | NA | M | D0：risks sounding X，删除后批评仍在且更强 |
| 89 | making | 147 | 5.966 | 0.447 | NA | — | NA | — | NA | H | 轻动词 |
| 90 | counterarguments | 125 | 5.880 | 0.485 | G1 | Ideas | NA | — | NA | H | Ideas 明示 counterargument |
| 91 | sharper | 57 | 5.858 | 0.750 | NA | — | PENDING | — | NA | — | D2待定：比较级多嵌于目标态框架（make it sharper=D3）而非评价（D1） |
| 92 | terms | 79 | 5.830 | 0.622 | PENDING | — | NA | — | NA | — | D1待定：key terms(G2-Wording)vs in terms of(NA) |
| 93 | tackles | 66 | 5.773 | 0.684 | NA | — | D1 | — | NA | M | your essay tackles a difficult question，开场归功套语 |
| 94 | policy | 139 | 5.738 | 0.451 | NA | — | NA | — | NA | H | 议题内容残留 |
| 95 | cultural | 80 | 5.728 | 0.611 | NA | — | NA | — | PENDING | — | C1待定：议题内容残留 vs 文化/语言背景框架（理论上关键） |
| 96 | turn | 51 | 5.560 | 0.776 | NA | — | NA | — | NA | H | in turn / turn to |
| 97 | framing | 51 | 5.560 | 0.776 | G1 | Ideas | NA | — | NA | M | 论点呈现方式 |
| 98 | weaken | 103 | 5.490 | 0.519 | NA | — | D2 | — | NA | M | weakens your argument，层级由宾语决定 |
| 99 | wording | 144 | 5.465 | 0.431 | G2 | Wording | NA | — | NA | H | Wording 明示 |
| 100 | abstract | 48 | 5.416 | 0.792 | PENDING | — | D2 | — | NA | — | D1待定：too abstract=缺具体支撑(G1-Dev)vs abstract language(G2) |
| 101 | readers | 327 | 5.368 | 0.276 | G1 | Ideas | NA | — | NA | M | 受众；按窄口径 C1 规定归 G1 |
| 102 | mechanics | 175 | 5.238 | 0.380 | G2 | Mechanics | NA | — | NA | H | Mechanics 明示 |
| 103 | significant | 149 | 5.213 | 0.413 | NA | — | NA | — | NA | M | 程度形容词，极性依宾语 |
| 104 | skeptical | 38 | 5.213 | 0.888 | G1 | Ideas | NA | — | NA | M | a skeptical reader will ask…，预设反驳 |
| 105 | entirely | 46 | 5.112 | 0.785 | NA | — | NA | — | NA | M | 强化词；"not entirely"否定缓和待观察 |
| 106 | anecdote | 82 | 5.088 | 0.564 | G1 | Development | NA | — | NA | H | 证据类型 |
| 107 | inconsistent | 68 | 5.036 | 0.623 | PENDING | — | D2 | — | NA | — | D1待定：inconsistent tense(G2)vs inconsistent argument(G1) |
| 108 | fairly | 59 | 5.031 | 0.674 | NA | — | NA | ✔ | NA | H | 手册 D0 明示 hedge |
| 109 | integrate | 39 | 5.018 | 0.855 | G1 | Development | D3 | — | NA | M | integrate evidence/quotations |
| 110 | come | 73 | 5.011 | 0.597 | NA | — | NA | — | NA | M | comes across/comes from |
| 111 | actually | 154 | 4.981 | 0.396 | NA | — | NA | — | NA | M | 强化/对比副词 |
| 112 | want | 144 | 4.836 | 0.404 | NA | — | D3 | — | NA | M | you'll want to = 建议套语（常与 may 叠加） |
| 113 | serve | 40 | 4.836 | 0.824 | NA | — | NA | — | NA | M | 描述性动词 |
| 114 | broader | 103 | 4.730 | 0.478 | G1 | Ideas | NA | — | NA | M | broader context/implications |
| 115 | move | 142 | 4.627 | 0.397 | PENDING | PENDING | PENDING | — | NA | — | D1待定：move this paragraph(G1)vs move on to(NA)；D2 随之待定 |
| 116 | genuine | 99 | 4.621 | 0.483 | NA | — | D1 | — | NA | M | a genuine strength/insight |
| 117 | casual | 63 | 4.588 | 0.617 | PENDING | — | D2 | — | NA | — | D1待定：属 tone/register，手册列 PENDING |
| 118 | single | 95 | 4.512 | 0.487 | NA | — | NA | — | NA | H | 数量词 |
| 119 | sense | 114 | 4.435 | 0.437 | NA | — | NA | — | NA | M | makes sense / a sense of |
| 120 | overly | 39 | 4.361 | 0.788 | NA | — | D2 | — | NA | M | 标记过度=内在负向 |
| 121 | polished | 61 | 4.314 | 0.607 | PENDING | — | D1 | — | NA | — | D1待定：手册明列 polished 为 PENDING |
| 122 | biggest | 72 | 4.218 | 0.547 | NA | — | NA | — | NA | M | 级差强化词 |
| 123 | power | 132 | 4.185 | 0.391 | NA | — | NA | — | NA | M | 疑似议题内容残留（政治权力）；the power of your argument 待核 |
| 124 | draft | 164 | 4.039 | 0.342 | NA | — | NA | — | NA | H | 文本指称/写作过程；窄口径下不设类 |
| 125 | heavily | 46 | 3.959 | 0.678 | NA | — | NA | — | NA | M | 强化词（rely heavily），非 hedge |
| 126 | financial | 93 | 3.920 | 0.456 | NA | — | NA | — | NA | H | 议题内容残留 |
| 127 | opening | 176 | 3.895 | 0.323 | G1 | Global Structure | NA | — | NA | H | 引言段，大单位 |
| 128 | develop | 169 | 3.873 | 0.329 | G1 | Development | D3 | — | NA | H | Development 明示 |

### B1 维度一 Feedback Focus

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| G1 | 43 | 81.1% | 8471 | 86.9% | 0.792 |
| G2 | 10 | 18.9% | 1275 | 13.1% | 1.151 |
| **已定标签合计** | **53** | **100.0%** | **9746** | **100.0%** | — |
| N/A（不计入分母） | 53 | — | — | — | — |
| PENDING（不计入分母） | 22 | — | — | — | — |
| 清单总数 | 128 | — | — | — | — |

**子类分布（分母同为已定标签 53）**

| 主类 | 子类 | 词位数 | 占比 |
|---|---|---:|---:|
| G1 | Development | 10 | 18.9% |
| G1 | Global Structure | 4 | 7.5% |
| G1 | Ideas | 29 | 54.7% |
| G2 | Correctness | 2 | 3.8% |
| G2 | Local Structure | 1 | 1.9% |
| G2 | Mechanics | 3 | 5.7% |
| G2 | Wording | 4 | 7.5% |

### B2 维度二 Feedback Acts

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| D3 | 20 | 48.8% | 5081 | 76.2% | 0.752 |
| D2 | 13 | 31.7% | 860 | 12.9% | 0.885 |
| D1 | 8 | 19.5% | 725 | 10.9% | 0.853 |
| **已定标签合计** | **41** | **100.0%** | **6666** | **100.0%** | — |
| N/A（不计入分母） | 81 | — | — | — | — |
| PENDING（不计入分母） | 6 | — | — | — | — |
| 清单总数 | 128 | — | — | — | — |

### B3 维度三 Larger Contexts of Writing

| 标签 | 词位数 | 占已定标签 | Freq_Tar 合计 | 占已定标签词次 | LR 均值 |
|---|---:|---:|---:|---:|---:|
| **已定标签合计** | **0** | **100.0%** | **1** | **100.0%** | — |
| N/A（不计入分母） | 127 | — | — | — | — |
| PENDING（不计入分母） | 1 | — | — | — | — |
| 清单总数 | 128 | — | — | — | — |

### B4 D0 Mitigation（补充观察，不计入主维度）

- 确认 hedge：2 个 —— `risk`、`fairly`
- 待定：3 个 —— `rather`、`would`、`might`
- 非 hedge：123 个

### B5 维度一 × 维度二 交叉表（词位数）

| 维度一＼维度二 | D1 | D2 | D3 | NA | PENDING | 合计 |
|---|---:|---:|---:|---:|---:|---:|
| **G1** | 3 | 2 | 9 | 28 | 1 | **43** |
| **G2** | 0 | 1 | 2 | 7 | 0 | **10** |
| **NA** | 3 | 3 | 4 | 39 | 4 | **53** |
| **PENDING** | 2 | 7 | 5 | 7 | 1 | **22** |
| **合计** | 8 | 13 | 20 | 81 | 6 | **128** |

### B6 LL 前 20 词位的类别构成

| 前 20 中 | G1 | G2 | N/A | PENDING |
|---|---:|---:|---:|---:|
| 维度一 | 7 | 4 | 5 | 4 |

### B7 敏感性分析：维度一 PENDING 的极端归属

| 情形 | G1 词位 | G2 词位 | G1 占比 |
|---|---:|---:|---:|
| 现状（PENDING 不计入） | 43 | 10 | 81.1% |
| 22 个 PENDING 全归 G1（上界） | 65 | 10 | 86.7% |
| 22 个 PENDING 全归 G2（下界） | 43 | 32 | 57.3% |

### B8 concordance 待办清单

共 **30** 个词族需 concordance 判定（含 2 个低信度已定项）。

| Type | 待定维度 | 竞争读法 |
|---|---|---|
| `rather` | D0 | D0待定：手册列为 hedge，但"rather than"（建议对比框架）可能占主导 |
| `aim` | 二 | D2待定："aim to/for"（D3）vs "your aim"（名词，NA） |
| `level` | 一 | D1待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev) |
| `edit` | 一 | D1待定：表层编辑(G2)vs全局修改(G1) |
| `would` | 二、D0 | 手册指定共享项，concordance 抽 50 行判 D3/D0 |
| `tighten` | 一 | D1待定：tighten prose/sentences(G2)vs tighten argument(G1) |
| `CLARIFY` | 一 | D1待定：手册 clear/clarity 系列一律 PENDING |
| `vague` | 一 | D1待定：与 unclear 同族，可指论证或用词 |
| `distract` | 一 | D1待定：typos distract(G2)vs digression distracts(G1) |
| `authority` | 低信度复核 | 写作者论述权威/立场，归修辞语境→G1 |
| `might` | 二、D0 | 手册指定共享项 |
| `reads` | 一 | D1待定：the essay reads(整体)vs this sentence reads(句级) |
| `just` | 二 | D0待定：最小化降调(D0)vs"仅仅是"强化批评(NA) |
| `precision` | 一 | D1待定：precision of language(G2)vs of claims(G1) |
| `shifts` | 一 | D1待定：tense shifts(G2-Grammar)vs shifts in focus(G1) |
| `measured` | 一、低信度复核 | D1待定：属 tone/register，手册列 PENDING；D2 判定信度低 |
| `right` | 一 | D1待定：the right word(G2)vs right now(NA) |
| `line` | 一 | D1待定：line of reasoning(G1)vs this line(G2) |
| `imprecise` | 一 | D1待定：同 precision |
| `define` | 一 | D1待定：define your terms 属 Wording(G2)还是概念澄清(G1) |
| `loosely` | 一 | D1待定：loosely connected(G1 连贯)vs loosely worded(G2) |
| `replace` | 一 | D1待定：replace this word(G2)vs replace this paragraph(G1) |
| `sharper` | 二 | D2待定：比较级多嵌于目标态框架（make it sharper=D3）而非评价（D1） |
| `terms` | 一 | D1待定：key terms(G2-Wording)vs in terms of(NA) |
| `cultural` | 三 | C1待定：议题内容残留 vs 文化/语言背景框架（理论上关键） |
| `abstract` | 一 | D1待定：too abstract=缺具体支撑(G1-Dev)vs abstract language(G2) |
| `inconsistent` | 一 | D1待定：inconsistent tense(G2)vs inconsistent argument(G1) |
| `move` | 一、二 | D1待定：move this paragraph(G1)vs move on to(NA)；D2 随之待定 |
| `casual` | 一 | D1待定：属 tone/register，手册列 PENDING |
| `polished` | 一 | D1待定：手册明列 polished 为 PENDING |

### B9 高效应量词位（LR ≥ 1.5）

| Type | LL | LR | 维度一 | 维度二 |
|---|---:|---:|---|---|
| correctness | 49.868 | 3.284 | G2/Correctness | NA |
| tighten | 24.264 | 2.251 | PENDING | D3 |
| aim | 40.757 | 1.900 | G1/Ideas | PENDING |
| defensible | 23.177 | 1.882 | G1/Ideas | D1 |
| mechanical | 32.556 | 1.836 | G2/Mechanics | NA |
| prose | 15.334 | 1.654 | G2/Wording | NA |
| sweeping | 19.484 | 1.599 | G1/Ideas | D2 |
