# concordance 待判定词形总表

> 由 `scripts/make_pending.py` 从 `coding/all_codes.tsv` 生成。
> **单位是词形，不是词位**：concordance 对一个词形在语料中的用法作一次判定，结果回填到它出现的所有组，因此同一词形在多组的 PENDING 合并为一行。
> 总表共 315 个 PENDING 单元格，聚合为 **171 个待判定词形**；另含 note 标记待核项与两项特殊情况（见 P1、P5）。

## 优先级与判定规则

| 优先级 | 含义 | 数量 | 判定规则 |
|---|---|---:|---|
| **P1** | 维度三候选（决定 RQ1／RQ2 核心结论） | 14 | 先做。决定 RQ1／RQ2 的核心结论。`false` 只需查右搭配是否为 friends，成本最低、回报最高；`natural`／`unnatural`／`sounds` 判定唯一可能的「规范型」C1；`chinese` 只判子类，范畴已定 |
| **P2** | 强制查询清单、共享情态项与高体量 act | 15 | 三类合并于此。① 手册 v3 强制查询清单已知条目，一律不得凭词形归类；② `could`／`would`／`might`／`can` 按手册各随机抽 50 行，**在 v3 共存规则下须分别判 act 层与 hedge 层**，不是二选一；③ 其余高体量 act 项（单组 Freq_Tar ≥ 400），其归属直接决定 A1／A3 的量级，进而决定 act 层能否跨组解读 |
| **P3** | 高体量维度一待定项 | 11 | 单组 Freq_Tar ≥ 400 的维度一待定项。它们决定各组敏感性区间能否收窄，尤其是组 1／组 2——十二组中唯一仍存在实质重叠区 [56.0, 68.9] 的一对 |
| **P4** | 内容动词类（待统一规则后整批处理） | 23 | **先定统一规则再逐词判**，勿因体量拆散（本级含 `use` 897、`EXPLAIN` 603 等高频项）。建议：抽 50 行，统计该动词是否出现在祈使句、`you should/need to/can/could + V`、`try/consider V-ing` 等补救框架中；≥60% 判 A3，≤40% 判 NA，中间区间报不可判定并在敏感性分析中双向计算 |
| **P5** | note 标记的待核项（议题残留疑似、子类边界、其他） | 17 | 第三人称代词群（`she`／`he`／`her`／`people`）建议一次性判定后统一处理，不要逐组单判；子类边界项只影响子类占比，不影响主类 |
| **P6** | 其余待定与低信度复核 | 91 | 其余维度一／act／hedge 待定与低信度复核。可在前五级完成后批量处理 |

## P1 维度三候选（决定 RQ1／RQ2 核心结论）（14 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `language` | 维度一＋维度三 | 2/3/7/10 | 795 | 150.991 | 1.210 | 维度三待定：your language background/first language(C1) vs academic language(G2 Wording)；本组理论枢纽词 |
| `english` | 维度三 | 2/3/6/7/10 | 508 | 362.732 | 2.776 | 手册明列：指语言系统（correct English）→C1；作文体修饰（English essay）→NA。两读法维度一均为 NA |
| `direct` | 维度一＋维度三 | 6/7/10 | 164 | 10.656 | 0.579 | 维度三待定（先验较低）：German writing is direct（文化—语用框架，C1）vs be more direct(G2)/direct quotation(NA) |
| `natural` | 维度一＋act 层＋维度三 | 2/6/7/10 | 113 | 25.840 | 1.394 | 三层皆待定：sounds natural 是否以母语者语感为隐含标准（C1）；若判 C1 则维度一二依规则归 NA |
| `background` | 维度一＋维度三 | 2 | 105 | 8.990 | 0.665 | 维度三待定：your language background(C1)vs background information(G1-Development) |
| `INFLUENCE` | 维度一＋维度三 | 6 | 103 | 17.406 | 1.005 | 维度三待定：the influence of German on your English（Transfer framing，C1）vs influence the reader（G1） |
| `tackles` | act 层＋跨组一致性回填 | 9 | 82 | 13.974 | 1.008 | 组 1 编为 A1、组 9 编为 PENDING（有意保留的唯一跨组不一致）；须与组 4 raises 并案判定后统一回填组 1、4、9 |
| `cultural` | 维度三 | 1 | 80 | 5.728 | 0.611 | C1待定：议题内容残留 vs 文化/语言背景框架（理论上关键） |
| `chinese` | C1 子类判定 | 3/5 | 61 | 77.281 | 5.968 | 已定 C1，但 Identity marking 与 Transfer framing 的子类归属未定；决定中文条件的 C1 是纯身份命名还是含迁移归因 |
| `speaking` | 维度三 | 6/7 | 61 | 19.353 | 1.501 | 维度三待定：German-speaking / German speakers（C1）vs generally speaking（NA） |
| `false` | 维度三 | 6/7 | 49 | 29.321 | 2.407 | 维度三待定：false friends（跨语言词汇概念，C1）vs false dichotomy（逻辑谬误，G1-Ideas）。与 friends 的 Freq/Range 近乎同步，见报告 §3.2 |
| `influenced` | 维度一＋维度三 | 7 | 47 | 22.112 | 1.966 | 维度三待定：influenced by German（Transfer framing，C1）vs influence the reader（G1）；与组 6 INFLUENCE 同族 |
| `friends` | 维度三 | 6/7 | 46 | 9.865 | 1.164 | 维度三待定：false friends（C1）vs 议题内容残留（friends and family）。参照侧 Freq 20 提示存在非 C1 基线用法 |
| `unnatural` | 维度一＋act 层＋维度三 | 7 | 39 | 9.866 | 1.282 | 三层皆待定：与 natural 同族，是否以母语者语感为隐含标准（C1）；若非 C1 则 act 为 A2 |

## P2 强制查询清单、共享情态项与高体量 act（15 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `CLEAR` | 维度一＋act 层 | 2/10 | 1289 | 21.466 | 0.274 | 维度一待定（手册 clear 系）；act 层待定：clear(A1)vs clearer 目标态框架(A3) |
| `GOOD` | act 层 | 2/10 | 949 | 185.834 | 1.082 | act 层待定：good+better 归并，comparative 多嵌于目标态框架（make it better=A3）vs 评价（A1）；LL 全组最高，须查 |
| `would` | act 层＋hedge 层 | 1/6/9 | 786 | 25.427 | 0.395 | 手册指定共享项，concordance 抽 50 行判 A3/M1 |
| `can` | act 层＋hedge 层 | 2/5 | 735 | 8.843 | 0.241 | 与 could/might/would 同类共享项：you can add(A3)vs this can be confusing(M1)；两层分别判 |
| `strong` | act 层 | 2/10 | 711 | 21.022 | 0.372 | 手册 v3 强制查询清单（A1/A3 争议），不得凭词形归类 |
| `STRENGTHEN` | 强制查询清单项（本轮已给标签，须复核） | 1/9 | 525 | 23.078 | 0.466 | strengthen your argument/thesis；Ideas/Development 子类边界待核 |
| `good` | act 层 | 8 | 509 | 6.680 | 0.243 | act 层待定：评价（A1）vs 目标态框架；同组 2 GOOD 口径 |
| `could` | act 层＋hedge 层 | 2/4/6 | 499 | 8.327 | 0.278 | 手册指定共享项，抽 50 行分别判 act 层与 hedge 层 |
| `stronger` | act 层 | 8 | 477 | 7.934 | 0.276 | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类 |
| `strengthen` | 强制查询清单项（本轮已给标签，须复核） | 8 | 346 | 9.071 | 0.351 | strengthen your argument/thesis；同组 1 STRENGTHEN 口径。注：属 strong 词族，若 v3 强制查询清单覆盖则须改判 PENDING |
| `address` | 维度一＋act 层 | 1/8/9 | 302 | 23.654 | 0.641 | 手册 v3 强制查询清单（G1/A3 争议），不得凭词形归类：address counterarguments(G1+A3) vs 元话语"address the points below"(NA) |
| `STRENGTH` | act 层 | 2 | 257 | 62.497 | 1.237 | act 层待定：反馈自身小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| `might` | act 层＋hedge 层 | 1/9 | 189 | 16.823 | 0.689 | 手册指定共享项 |
| `strongest` | act 层 | 1/4/9 | 180 | 9.728 | 0.523 | 手册 v3 强制查询清单（strong 系 A1/A3 争议），不得凭词形归类：your strongest evidence(A1) vs 目标态框架(A3) |
| `strengths` | act 层 | 10 | 165 | 49.273 | 1.417 | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定。注：组 2 为归并 STRENGTH，本组为 strengths 单独入选，系口径效应 |

## P3 高体量维度一待定项（11 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `paragraph` | 维度一 | 10/12 | 1699 | 11.077 | 0.168 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `academic` | 维度一 | 2/6/7/10 | 997 | 73.006 | 0.669 | 维度一待定：属 register，手册列 tone/formal/register 为 PENDING |
| `specific` | 维度一 | 5/8/9 | 630 | 16.535 | 0.379 | 手册明列 specific 为 PENDING：细节不足(G1-Dev)vs 用词不准(G2) |
| `paragraphs` | 维度一 | 3/5 | 605 | 6.315 | 0.215 | 维度一待定：手册明示段落内部组织→G2、段落间安排→G1 |
| `topic` | 维度一 | 2/10 | 602 | 15.441 | 0.344 | 维度一待定：the topic of your essay(G1-Ideas)vs topic sentence(G2/G1 边界) |
| `right` | 维度一 | 1/8/9 | 548 | 8.749 | 0.272 | 维度一待定：the right word(G2)vs right now(NA) |
| `clearly` | 维度一 | 2/8/10/11 | 502 | 21.342 | 0.451 | 维度一待定（clear 系）；方式副词，act 层不赋值 |
| `ARTICLE` | 维度一 | 2/3/6/7/10 | 479 | 156.605 | 1.517 | 维度一待定：英语冠词(G2-Grammar)vs 引用的文章(G1-Development)；L2 语法标记的关键判别点 |
| `personal` | 维度一 | 9 | 463 | 5.613 | 0.235 | 维度一待定：personal experience/anecdote(G1-Development)vs personal opinion(G1-Ideas)vs too personal(register) |
| `final` | 维度一 | 2/4/10 | 414 | 15.633 | 0.423 | 维度一待定：your final paragraph(G1-Structure)vs"Final thoughts:"小标题(NA) |
| `style` | 维度一 | 6/7 | 410 | 29.187 | 0.609 | 维度一待定（手册列 tone/register 为 PENDING） |

## P4 内容动词类（待统一规则后整批处理）（23 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `USE` | 维度一＋act 层 | 2 | 1068 | 40.969 | 0.427 | 维度一待定：your use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定：use more examples(A3)vs 描述(NA) |
| `use` | 维度一＋act 层 | 10 | 897 | 39.259 | 0.459 | 维度一与 act 层皆待定；内容动词类。注：组 2 为归并 USE（use+using），本组为 use 单独入选——交接文档 §三 预告的口径效应实例 |
| `EXPLAIN` | act 层 | 8 | 603 | 16.353 | 0.357 | act 层待定：you explain X well（描述）vs explain this further（A3）；内容动词类 |
| `explain` | act 层 | 5/11 | 601 | 18.733 | 0.395 | act 层待定：you explain X well（描述 NA）vs explain this further（A3）。属"内容动词"类，见报告 §5 |
| `FOCUS` | 维度一＋act 层 | 8 | 579 | 8.749 | 0.262 | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定，内容动词类 |
| `focus` | 维度一＋act 层 | 2 | 466 | 4.919 | 0.216 | 维度一待定：your focus(G1)vs focus on this sentence(G2)；act 层待定：focus on X(A3)vs 描述(NA) |
| `state` | act 层 | 8 | 279 | 4.065 | 0.257 | act 层待定：state your thesis clearly（A3）vs 描述；内容动词类 |
| `write` | act 层 | 2/10 | 264 | 17.207 | 0.572 | act 层待定：when you write（描述 NA）vs write this as…（A3） |
| `check` | 维度一 | 2/3/7/10/12 | 243 | 29.339 | 1.110 | 维度一待定：check your spelling(G2)vs check your logic(G1)；手册 A3 明示 |
| `using` | 维度一＋act 层 | 5/8 | 188 | 12.198 | 0.570 | 维度一待定：use of evidence(G1)/word use(G2)/use of tenses(G2)；act 层待定，属内容动词类 |
| `say` | act 层 | 5/8 | 171 | 11.177 | 0.576 | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| `used` | 维度一 | 6 | 146 | 3.921 | 0.358 | 维度一待定：同 USE/using 口径 |
| `discuss` | act 层 | 2/5 | 132 | 9.121 | 0.590 | act 层待定：you discuss X（描述 NA）vs discuss counterarguments（A3） |
| `mention` | act 层 | 2 | 130 | 8.417 | 0.569 | act 层待定：you mention X（描述 NA）vs consider mentioning（A3） |
| `saying` | act 层 | 9 | 110 | 4.536 | 0.450 | act 层待定：you say X（描述）vs say more about（A3）；内容动词类 |
| `read` | act 层 | 6 | 93 | 3.937 | 0.457 | act 层待定：read your essay aloud（A3）vs 描述（NA）；内容动词类 |
| `create` | act 层 | 6 | 87 | 3.945 | 0.475 | act 层待定：create a clearer transition（A3）vs 描述（NA）；内容动词类 |
| `discussing` | act 层 | 11 | 74 | 4.029 | 0.520 | act 层待定：you discuss X（描述）vs discuss counterarguments（A3）；内容动词类 |
| `double` | 维度一＋act 层 | 7 | 73 | 6.642 | 0.695 | 维度一与 act 层皆待定：double-check（A3）vs double negative（G2-Grammar） |
| `vary` | 维度一＋act 层 | 7 | 65 | 5.951 | 0.697 | 维度一与 act 层皆待定：vary your sentence length(G2＋A3)vs 描述；内容动词类 |
| `raises` | act 层 | 4 | 47 | 7.846 | 0.997 | act 层待定：raises an important question 属开场归功套语(A1)vs 单纯描述(NA)；与组 1 tackles 同构，须并案处理 |
| `offer` | act 层 | 9 | 38 | 6.100 | 0.973 | act 层待定：offer more evidence（A3）vs you offer（描述）；内容动词类 |
| `raise` | act 层 | 6/7 | 37 | 4.719 | 0.850 | act 层待定：raises an important question 属开场归功套语(A1)vs 描述(NA)；与组 1 tackles、组 4 raises 并案 |

## P5 note 标记的待核项（议题残留疑似、子类边界、其他）（17 个）

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
| `therefore` | 其他待核 | 7 | 63 | 6.194 | 0.726 | 连接副词；亦可能为被建议使用的衔接词，待核 |
| `tool` | 议题残留待核 | 5 | 57 | 6.488 | 0.783 | 疑似议题内容残留 vs "a useful tool"元话语，待核 |
| `dates` | 议题残留待核 | 9 | 44 | 4.345 | 0.732 | 疑似议题内容残留（与 historical 共现）vs 引证信息，待核 |

## P6 其余待定与低信度复核（91 个）

| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |
|---|---|---|---:|---:|---:|---|
| `rather` | hedge 层 | 1/9 | 833 | 53.374 | 0.574 | M1待定：手册列为 hedge，但"rather than"（建议对比框架）可能占主导 |
| `only` | hedge 层 | 2/7/10 | 398 | 12.235 | 0.418 | hedge 层待定：最小化降调（only a few errors=M1）vs 限定（NA）；同组 1 just |
| `formal` | 维度一 | 2/10 | 364 | 27.609 | 0.622 | 维度一待定（register）；命名目标态而非评价，act 层不赋值 |
| `important` | act 层 | 2/10 | 323 | 25.774 | 0.639 | act 层待定：an important point(A1)vs it is important to…(A3 框架) |
| `level` | 维度一 | 1/5/8/9/12 | 298 | 26.954 | 0.697 | 维度一待定：sentence-level(G2)/paragraph-level(G1)/level of detail(G1-Dev) |
| `precise` | 维度一 | 6 | 294 | 4.750 | 0.274 | 维度一待定：precise wording(G2)vs precise claims(G1)；同组 1 precision 口径 |
| `CLARIFY` | 维度一 | 1 | 272 | 23.193 | 0.674 | 维度一待定：手册 clear/clarity 系列一律 PENDING |
| `just` | hedge 层 | 1/3/9 | 271 | 17.246 | 0.571 | M1待定：最小化降调(M1)vs"仅仅是"强化批评(NA)；竞争读法全在 hedge 层，与 act 层无关 |
| `clarity` | 维度一 | 5/8 | 271 | 17.830 | 0.578 | 维度一待定（手册 clear 系） |
| `PATTERN` | 维度一 | 7 | 241 | 54.634 | 1.195 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `emotional` | 维度一 | 2/10 | 217 | 6.657 | 0.380 | 维度一待定：emotional language(G2-Wording/register)vs emotional appeal(G1-Ideas)；亦可能为议题残留 |
| `clarify` | 维度一 | 8/9 | 212 | 8.494 | 0.454 | 维度一待定（手册 clear 系）；建议动词 |
| `MEAN` | 维度一 | 7 | 206 | 9.061 | 0.464 | 维度一待定：what you mean（G1 表意清晰）vs by means of（NA） |
| `possible` | hedge 层 | 2/10 | 192 | 6.642 | 0.404 | hedge 层待定：it is possible that（M1）vs possible improvements（NA） |
| `rhetorical` | 维度一 | 6/7 | 192 | 8.573 | 0.471 | 维度一待定：rhetorical question（局部修辞手段）vs rhetorical strategy/situation（G1） |
| `informal` | 维度一 | 2/10 | 190 | 12.535 | 0.575 | 维度一待定（register）；学术语境下标记偏离=负向（同组 1 casual 口径） |
| `reads` | 维度一 | 1/9 | 188 | 18.055 | 0.720 | 维度一待定：the essay reads(整体)vs this sentence reads(句级) |
| `subject` | 维度一 | 2/10 | 181 | 18.887 | 0.746 | 维度一待定：subject-verb agreement(G2-Grammar)vs the subject of your essay(G1) |
| `few` | hedge 层 | 6/7 | 173 | 12.568 | 0.616 | hedge 层待定：a few errors 最小化降调（M1）vs 单纯量词（NA）；同组 1 just、组 2 only |
| `patterns` | 维度一 | 2/3/6/10 | 170 | 27.794 | 2.027 | 维度一待定：error patterns(G2)vs sentence patterns(G2-Local)vs 论证模式(G1) |
| `replace` | 维度一 | 1/9 | 167 | 6.866 | 0.449 | 维度一待定：replace this word(G2)vs replace this paragraph(G1) |
| `EDIT` | 维度一 | 9 | 164 | 13.953 | 0.672 | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit 口径 |
| `suggestions` | act 层 | 2/10 | 160 | 34.698 | 1.151 | act 层待定：反馈小标题"Suggestions:"（元话语 NA）vs 名词化建议行为（A3） |
| `citations` | 维度一 | 11 | 159 | 4.341 | 0.358 | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics)；同组 10 citation 口径 |
| `unclear` | 维度一 | 2/10 | 153 | 6.487 | 0.452 | 维度一待定（手册 clear 系）；负向评价 |
| `correct` | act 层 | 2/10 | 152 | 10.825 | 0.600 | act 层待定：correct these errors(A3)vs the correct form(NA) |
| `move` | 维度一＋act 层 | 1/9 | 146 | 5.972 | 0.448 | 维度一待定：move this paragraph(G1)vs move on to(NA)；act 层随之待定 |
| `awkward` | 维度一 | 5/8 | 142 | 5.334 | 0.425 | 维度一待定：awkward phrasing(G2-Wording)vs awkward transition(G1)；手册 A2 词族例明列 awkward |
| `reduce` | 维度一 | 2 | 139 | 4.200 | 0.376 | 维度一待定：reduce wordiness(G2)vs reduce scope(G1) |
| `consistent` | 维度一 | 10/12 | 135 | 13.248 | 0.726 | 维度一待定：consistent tense(G2)vs consistent argument(G1)；同组 2 consistency 口径 |
| `citation` | 维度一 | 10 | 132 | 3.886 | 0.371 | 维度一待定：引用来源的使用(G1-Development)vs 引用格式(G2-Mechanics) |
| `advice` | act 层 | 2/10 | 128 | 21.853 | 0.994 | act 层待定：反馈小标题（NA）vs my advice is to…（A3） |
| `vague` | 维度一 | 1/9/12 | 126 | 19.002 | 0.939 | 维度一待定：与 unclear 同族，可指论证或用词 |
| `suggestion` | act 层 | 3/5/11 | 126 | 13.251 | 0.748 | act 层待定：反馈小标题（NA）vs 名词化建议行为（A3） |
| `edit` | 维度一 | 1/12 | 122 | 26.167 | 1.165 | 维度一待定：表层编辑(G2)vs全局修改(G1) |
| `summary` | 维度一 | 5 | 120 | 4.785 | 0.436 | 维度一待定：your summary 段落(G1-Structure)vs "in summary"元话语(NA) |
| `briefly` | hedge 层 | 2/8/10 | 119 | 10.223 | 0.666 | hedge 层待定：briefly explain 削减要求强度（M1）vs 单纯方式副词（NA） |
| `order` | 维度一 | 6/7 | 118 | 43.921 | 1.675 | 维度一待定：word order（G2-Grammar，德语语序迁移的典型项）vs "in order to"（NA） |
| `ask` | 维度一 | 9 | 118 | 4.136 | 0.412 | 维度一待定：a reader will ask（G1-Ideas 预设反驳）vs ask yourself（元话语） |
| `early` | 维度一 | 9 | 115 | 5.670 | 0.496 | 维度一待定：early in your essay（G1-Structure 位置）vs early on（NA） |
| `REQUIRE` | act 层 | 6/7 | 109 | 25.193 | 1.210 | act 层待定：this requires a comma（补救指令 A3）vs German requires…（描述，且可能属 C1 共现语境） |
| `consistency` | 维度一 | 2/10 | 105 | 8.990 | 0.665 | 维度一待定：consistency of tense(G2)vs of argument(G1) |
| `remove` | 维度一 | 10 | 102 | 3.997 | 0.433 | 维度一待定：remove this word(G2)vs remove this paragraph(G1)；建议动词 |
| `precision` | 维度一 | 1/7/9 | 99 | 12.952 | 0.863 | 维度一待定：precision of language(G2)vs of claims(G1) |
| `complete` | 维度一 | 2 | 99 | 7.088 | 0.602 | 维度一待定：complete sentence（句子残缺，G2-Grammar）vs complete your argument(G1) |
| `rewrite` | 维度一 | 6 | 97 | 8.396 | 0.680 | 维度一待定：rewrite this sentence(G2)vs rewrite this paragraph(G1)；建议动词 |
| `define` | 维度一 | 1/9 | 94 | 6.696 | 0.609 | 维度一待定：define your terms 属 Wording(G2)还是概念澄清(G1) |
| `aim` | act 层 | 1/9 | 92 | 40.757 | 1.900 | act 层待定："aim to/for"（A3）vs "your aim"（名词，NA） |
| `strength` | act 层 | 4 | 92 | 4.419 | 0.490 | act 层待定：反馈小标题"Strengths:"（元话语 NA）vs 归功（A1）；且属 strong 词族，按 v3 强制查询规则不得凭词形定 |
| `understandable` | 维度一＋低信度复核 | 2/7/10 | 91 | 22.275 | 1.600 | 维度一待定（clear 系）；act 低信度：作为"低门槛褒扬"（your English is understandable）与 A1 定义是否相符须查 |
| `line` | 维度一 | 1/9 | 86 | 8.715 | 0.744 | 维度一待定：line of reasoning(G1)vs this line(G2) |
| `suggested` | act 层 | 2/10 | 86 | 8.255 | 0.710 | act 层待定：the suggested revision（NA）vs I suggested（A3） |
| `shifts` | 维度一 | 1 | 82 | 12.100 | 0.927 | 维度一待定：tense shifts(G2-Grammar)vs shifts in focus(G1) |
| `fix` | 维度一 | 8 | 82 | 4.992 | 0.554 | 维度一待定：fix these errors(G2)vs fix the structure(G1)；建议动词 |
| `terms` | 维度一 | 1 | 79 | 5.830 | 0.622 | 维度一待定：key terms(G2-Wording)vs in terms of(NA) |
| `accurate` | 维度一 | 2/11 | 79 | 11.057 | 0.888 | 维度一待定：accurate facts(G1-Dev)vs accurate grammar(G2)；正向评价 |
| `moves` | 维度一 | 4 | 79 | 4.160 | 0.515 | 维度一待定：the essay moves from X to Y(G1-Structure)vs move this paragraph(元话语/G1)；同组 1 move 口径 |
| `complex` | 维度一 | 2 | 76 | 8.273 | 0.763 | 维度一待定：complex sentences(G2-Local)vs complex ideas(G1) |
| `editing` | 维度一 | 11 | 75 | 7.239 | 0.716 | 维度一待定：表层编辑(G2)vs 全局修改(G1)；沿用组 1 edit／组 9 EDIT 口径 |
| `effort` | 低信度复核 | 2/5 | 73 | 4.514 | 0.555 | 低信度：归功对象为写作者努力而非文本属性；若与 GOOD/great 共现构成归功则应改判 A1 |
| `insert` | 维度一 | 3 | 73 | 4.884 | 0.580 | 维度一待定：insert a comma(G2-Mechanics)vs insert a transition(G1)；建议动词 |
| `register` | 维度一 | 3/6/7 | 73 | 24.443 | 1.542 | 维度一待定（手册列 tone/formal/register 为 PENDING）；元语言学术语，显性命名语域规范 |
| `inconsistent` | 维度一 | 1/9 | 72 | 6.852 | 0.716 | 维度一待定：inconsistent tense(G2)vs inconsistent argument(G1) |
| `repeated` | 维度一 | 9/11 | 72 | 4.827 | 0.588 | 维度一待定：repeated errors(G2)vs repeated ideas(G2-Local，手册 repetitive 口径)vs 论点重复(G1) |
| `fine` | 低信度复核 | 7 | 71 | 13.236 | 1.059 | 低信度：this is fine 属低门槛褒扬，与 A1「归功于正面价值特征」的定义是否相符须查；同组 2 understandable |
| `treatment` | 维度一 | 9 | 70 | 7.125 | 0.744 | 维度一待定：your treatment of the topic(G1-Ideas)vs 议题内容残留，待核 |
| `distract` | 维度一 | 1/9 | 66 | 25.073 | 1.695 | 维度一待定：typos distract(G2)vs digression distracts(G1) |
| `authority` | 低信度复核 | 1/9 | 65 | 17.372 | 1.340 | 写作者论述权威/立场，归修辞语境→G1 |
| `measured` | 维度一＋低信度复核 | 1 | 65 | 9.069 | 0.897 | 维度一待定：属 tone/register，手册列 PENDING；D2 判定信度低 |
| `worth` | act 层 | 10 | 64 | 9.184 | 0.898 | act 层待定：it's worth adding X＝隐性建议（A3）vs 价值评价（A1）；与组 9 deserves 同构 |
| `casual` | 维度一 | 1 | 63 | 4.588 | 0.617 | 维度一待定：属 tone/register，手册列 PENDING |
| `emotionally` | 维度一 | 4/6 | 63 | 13.009 | 1.136 | 维度一待定：emotionally charged language(G2-Wording/register)vs emotional appeal(G1-Ideas)；同组 2 emotional 口径 |
| `neutral` | 维度一 | 2 | 62 | 3.980 | 0.566 | 维度一待定（tone/register）；客观性规范框架词 |
| `polished` | 维度一 | 1 | 61 | 4.314 | 0.607 | 维度一待定：手册明列 polished 为 PENDING |
| `sharper` | act 层 | 1/9 | 59 | 6.963 | 0.811 | act 层待定：比较级多嵌于目标态框架（make it sharper=A3）而非评价（A1） |
| `essential` | act 层 | 4 | 59 | 7.514 | 0.849 | act 层待定：an essential point(A1)vs it is essential to…(A3 框架)；同组 2 important 口径 |
| `meaning` | 维度一 | 10 | 59 | 11.892 | 1.103 | 维度一待定：the meaning is unclear（G1 表意）vs 词义(G2-Wording) |
| `number` | 维度一 | 7 | 58 | 4.631 | 0.645 | 维度一待定：singular/plural number(G2-Grammar)vs a number of（NA） |
| `weakness` | act 层 | 9 | 57 | 6.651 | 0.805 | act 层待定：反馈小标题"Weaknesses:"（元话语 NA）vs 负向评价（A2）；与 STRENGTH 同构处理 |
| `deserves` | act 层 | 9/11 | 57 | 4.943 | 0.676 | act 层待定：this point deserves more attention＝隐性建议（A3）vs 正向评价（A1） |
| `confusing` | 维度一 | 5/8/10 | 56 | 6.764 | 0.819 | 维度一待定（clear 系）；手册 A2 词族例明列 confusing |
| `reflection` | 维度一 | 9 | 55 | 5.149 | 0.709 | 维度一待定：your reflection on the topic(G1-Ideas)vs a reflection of（NA） |
| `narrow` | act 层 | 9 | 54 | 9.486 | 1.027 | 与本组 BROAD 构成论断范围对举，域固定于论断；act 层待定：narrow your claim(A3)vs too narrow(A2) |
| `confusion` | 维度一 | 7 | 53 | 6.403 | 0.818 | 维度一待定（clear 系）；负向评价 |
| `abstract` | 维度一 | 1/7 | 52 | 7.990 | 0.942 | 维度一待定：too abstract=缺具体支撑(G1-Dev)vs abstract language(G2) |
| `appropriate` | 维度一 | 7 | 52 | 4.238 | 0.653 | 维度一待定：appropriate tone(register)vs appropriate word choice(G2)；规范性框架词 |
| `imprecise` | 维度一 | 1 | 46 | 8.032 | 1.026 | 维度一待定：同 precision |
| `inaccurate` | 维度一 | 3/5 | 46 | 4.856 | 0.750 | 维度一待定：inaccurate wording(G2)vs inaccurate facts(G1-Development)；负向评价 |
| `tighten` | 维度一 | 1 | 44 | 24.264 | 2.251 | 维度一待定：tighten prose/sentences(G2)vs tighten argument(G1) |
| `basis` | 维度一 | 6/7 | 44 | 17.018 | 1.722 | 维度一待定：the basis of your claim(G1-Ideas)vs on a …basis（NA） |
| `loosely` | 维度一 | 1/9 | 40 | 6.277 | 0.962 | 维度一待定：loosely connected(G1 连贯)vs loosely worded(G2) |
