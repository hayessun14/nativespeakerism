# concordance 待判定词形总表

> **状态：已完成（历史存档）**
> 本清单所列待决项已全部由 concordance 消解，总表现存 0 个 PENDING。
> 保留以记录当时的筛查依据；最终统计见 [`final_report.md`](final_report.md)。

> 由 `scripts/make_pending.py` 从 `coding/all_codes.tsv` 生成。
> **单位是词形，不是词位**：concordance 对一个词形在语料中的用法作一次判定，结果回填到它出现的所有组，因此同一词形在多组的 PENDING 合并为一行。
> 总表共 24 个 PENDING 单元格，聚合为 **45 个待判定词形**；另含 note 标记待核项与两项特殊情况（见 P1、P5）。

## 优先级与判定规则

| 优先级 | 含义 | 数量 | 判定规则 |
|---|---|---:|---|
| **P1** | 维度三候选（决定 RQ1／RQ2 核心结论） | 5 | 先做。决定 RQ1／RQ2 的核心结论。`false` 只需查右搭配是否为 friends，成本最低、回报最高；`natural`／`unnatural`／`sounds` 判定唯一可能的「规范型」C1；`chinese` 只判子类，范畴已定 |
| **P2** | 强制查询清单、共享情态项与高体量 act | 10 | 三类合并于此。① 手册 v3 强制查询清单已知条目，一律不得凭词形归类；② `could`／`would`／`might`／`can` 按手册各随机抽 50 行，**在 v3 共存规则下须分别判 act 层与 hedge 层**，不是二选一；③ 其余高体量 act 项（单组 Freq_Tar ≥ 400），其归属直接决定 A1／A3 的量级，进而决定 act 层能否跨组解读 |
| **P3** | 高体量维度一待定项 | 2 | 单组 Freq_Tar ≥ 400 的维度一待定项。它们决定各组敏感性区间能否收窄，尤其是组 1／组 2——十二组中唯一仍存在实质重叠区 [56.0, 68.9] 的一对 |
| **P4** | 内容动词类（待统一规则后整批处理） | 0 | **先定统一规则再逐词判**，勿因体量拆散（本级含 `use` 897、`EXPLAIN` 603 等高频项）。建议：抽 50 行，统计该动词是否出现在祈使句、`you should/need to/can/could + V`、`try/consider V-ing` 等补救框架中；≥60% 判 A3，≤40% 判 NA，中间区间报不可判定并在敏感性分析中双向计算 |
| **P5** | note 标记的待核项（议题残留疑似、子类边界、其他） | 18 | 第三人称代词群（`she`／`he`／`her`／`people`）建议一次性判定后统一处理，不要逐组单判；子类边界项只影响子类占比，不影响主类 |
| **P6** | 其余待定与低信度复核 | 10 | 其余维度一／act／hedge 待定与低信度复核。可在前五级完成后批量处理 |

## P1 维度三候选（决定 RQ1／RQ2 核心结论）（5 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `language` | 维度三 | 2/10 | 795 | 150.991 | 1.210 | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词〔concordance 判定：d1=G2-Wording〕 |
| `english` | 维度三 | 2/10 | 508 | 362.732 | 2.776 | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| `direct` | 维度三 | 10 | 164 | 10.656 | 0.579 | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA)〔concordance 判定：d1=G1-Ideas，c=NA〕 |
| `tackles` | 跨组一致性回填 | 1/9 | 82 | 13.974 | 1.008 | 组 1 编为 A1、组 9 编为 PENDING（有意保留的唯一跨组不一致）；须与组 4 raises 并案判定后统一回填组 1、4、9 |
| `chinese` | C1 子类判定 | 3/5 | 61 | 77.281 | 5.968 | 已定 C1，但 Identity marking 与 Transfer framing 的子类归属未定；决定中文条件的 C1 是纯身份命名还是含迁移归因 |

## P2 强制查询清单、共享情态项与高体量 act（10 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `would` | act 层 | 9 | 786 | 25.427 | 0.395 | 手册指定共享项，concordance 抽 50 行判 A3/M1〔concordance 判定：act=A3(54%)，hedge=M1(54%)〕 |
| `strong` | 强制查询清单项（本轮已给标签，须复核） | 2/10 | 711 | 21.022 | 0.372 | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类〔concordance 判定：act=A1(91%)〕 |
| `STRENGTHEN` | 强制查询清单项（本轮已给标签，须复核） | 1/9 | 525 | 23.078 | 0.466 | strengthen your argument/thesis；Ideas/Development 子类边界待核 |
| `stronger` | 强制查询清单项（本轮已给标签，须复核） | 8 | 477 | 7.934 | 0.276 | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类〔concordance 判定：act=A3〕 |
| `strengthen` | 强制查询清单项（本轮已给标签，须复核） | 8 | 346 | 9.071 | 0.351 | strengthen your argument/thesis；同组 1 STRENGTHEN 口径。注：属 strong 词族，若 v3 强制查询清单覆盖则须改判 PENDING |
| `address` | 强制查询清单项（本轮已给标签，须复核） | 1/8/9 | 302 | 23.654 | 0.641 | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类：address counterarguments(G1+A3) vs 元话语"address the points below"(NA)〔concordance 判定：d1=G1-Ideas，act=A3〕 |
| `STRENGTH` | 强制查询清单项（本轮已给标签，须复核） | 2 | 257 | 62.497 | 1.237 | act 层待定：反馈自身小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定〔concordance 判定：act=A1〕 |
| `strongest` | 强制查询清单项（本轮已给标签，须复核） | 1/4/9 | 180 | 9.728 | 0.523 | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类：your strongest evidence(A1) vs 目标态框架(A3)〔concordance 判定：act=A1〕 |
| `strengths` | 强制查询清单项（本轮已给标签，须复核） | 10 | 165 | 49.273 | 1.417 | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定。注：组 2 为归并 STRENGTH，本组为 strengths 单独入选，系口径效应〔concordance 判定：act=A1〕 |
| `strength` | 强制查询清单项（本轮已给标签，须复核） | 4 | 92 | 4.419 | 0.490 | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定〔concordance 判定：act=A1〕 |

## P3 高体量维度一待定项（2 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `paragraphs` | 维度一 | 3/5 | 605 | 6.315 | 0.215 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `clearly` | 维度一 | 2/8/10 | 502 | 21.342 | 0.451 | 维度一待定（clear 系）；方式副词，act 层不赋值 |

## P5 note 标记的待核项（议题残留疑似、子类边界、其他）（18 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `main` | 子类边界待核 | 2/10 | 716 | 60.781 | 0.663 | main point/argument/idea；子类 Ideas 与 Global Structure 边界待核 |
| `people` | 议题残留待核 | 2/10 | 608 | 17.362 | 0.364 | 疑似议题内容残留（LOCNESS 主题）；people reading your essay 读法待核 |
| `become` | 议题残留待核 | 2 | 293 | 6.098 | 0.308 | 疑似议题内容残留（has become），待核 |
| `effects` | 议题残留待核 | 5/8 | 143 | 5.319 | 0.425 | 疑似议题内容残留（effects of X）vs 对读者的效果，待核 |
| `power` | 议题残留待核 | 1 | 132 | 4.185 | 0.391 | 疑似议题内容残留（政治权力）；the power of your argument 待核 |
| `our` | 议题残留待核 | 3 | 129 | 4.396 | 0.401 | 疑似议题内容残留（our society）vs 包容性人称，待核 |
| `studies` | 议题残留待核 | 9 | 112 | 6.270 | 0.532 | 来源/证据类型（studies show）；疑似议题内容残留，待核 |
| `he` | 议题残留待核 | 2/10 | 110 | 7.625 | 0.591 | 疑似议题内容残留，待核 |
| `her` | 议题残留待核 | 2/4/10 | 91 | 11.531 | 0.835 | 疑似议题内容残留，待核 |
| `story` | 议题残留待核 | 8/10 | 86 | 4.381 | 0.500 | 疑似议题内容残留，待核 |
| `data` | 议题残留待核 | 5/8 | 85 | 9.881 | 0.798 | 证据类型；疑似议题内容残留，待核 |
| `discussion` | 子类边界待核 | 9 | 83 | 4.778 | 0.540 | your discussion of X；子类 Ideas 与 Global Structure 边界待核 |
| `she` | 议题残留待核 | 2/10 | 70 | 11.242 | 0.958 | 疑似议题内容残留（引述作文内容），待核 |
| `action` | 议题残留待核 | 5 | 70 | 3.887 | 0.523 | 疑似议题内容残留 vs call to action（结论段套语），待核 |
| `treatment` | 其他待核 | 9 | 70 | 7.125 | 0.744 | 维度一待定：your treatment of the topic(G1-Ideas)vs 议题内容残留，待核〔concordance 判定：d1=NA〕 |
| `therefore` | 其他待核 | 7 | 63 | 6.194 | 0.726 | 连接副词；亦可能为被建议使用的衔接词，待核 |
| `tool` | 议题残留待核 | 5 | 57 | 6.488 | 0.783 | 疑似议题内容残留 vs "a useful tool"元话语，待核 |
| `dates` | 议题残留待核 | 9 | 44 | 4.345 | 0.732 | 疑似议题内容残留（与 historical 共现）vs 引证信息，待核 |

## P6 其余待定与低信度复核（10 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `formal` | 维度一 | 2/10 | 364 | 27.609 | 0.622 | 维度一待定（register）；命名目标态而非评价，act 层不赋值 |
| `MEAN` | 维度一 | 7 | 206 | 9.061 | 0.464 | 维度一待定：what you mean（G1 表意清晰）vs by means of（NA） |
| `possible` | hedge 层 | 2/10 | 192 | 6.642 | 0.404 | hedge 层待定：it is possible that（M1）vs possible improvements（NA） |
| `subject` | 维度一 | 2/10 | 181 | 18.887 | 0.746 | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1) |
| `few` | hedge 层 | 6/7 | 173 | 12.568 | 0.616 | hedge 层待定：a few errors 最小化降调（M1）vs 单纯量词（NA）；同组 1 just、组 2 only |
| `edit` | 维度一 | 1/12 | 122 | 26.167 | 1.165 | 维度一待定：表层编辑(G2)vs全局修改(G1) |
| `effort` | 低信度复核 | 2/5 | 73 | 4.514 | 0.555 | 低信度：归功对象为写作者努力而非文本属性；若与 GOOD/great 共现构成归功则应改判 A1 |
| `fine` | 低信度复核 | 7 | 71 | 13.236 | 1.059 | 低信度：this is fine 属低门槛褒扬，与 A1「归功于正面价值特征」的定义是否相符须查；同组 2 understandable |
| `authority` | 低信度复核 | 1/9 | 65 | 17.372 | 1.340 | 写作者论述权威/立场，归修辞语境→G1 |
| `confusing` | 维度一 | 8/10 | 56 | 6.764 | 0.819 | 维度一待定（clear 系）；手册 A2 词族例明列 confusing〔concordance 判定：d1=G2-Local Structure〕 |
