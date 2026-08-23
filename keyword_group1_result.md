# 关键词处理结果 · 第一组（L1 vs Generic）

## 1. 处理概览

| 项目 | 数值 |
|---|---|
| 目标语料 | L1.db |
| 参照语料 | Generic.db |
| 目标语料文档数 | 348 |
| 目标语料形符数 | 273,834 |
| 关键性measure | Log-Likelihood (4-term), p<0.05 (3.84) |
| 效应量measure | LogRatio |
| Range ≥ 35 对应比例 | ≥10.06% 文档 |

## 2. 筛选流程

| 阶段 | 规则 | 剩余词条 |
|---|---|---|
| 原始词表 | — | 530 |
| R1 | Freq_Tar ≥ 10 且 Range_Tar ≥ 35 | 157 |
| R2 | 排除冠词/介词/连词/关系词/指示词/非人称代词/系动词/助动词 | 141（−16） |
| R3 | 排除缩写切分碎片 | 138（−3） |
| R4 | 同族词归并（屈折变体） | **128**（−10 组） |

## 3. 入选词表（128 个词位，按 Freq_Tar 降序）

> Range 标注 `≥` 者为归并项：Freq 为组内求和，Range 取组内最大值作保守下界（同一文档可能同时含多个变体，Range 不可直接相加）。

| # | 词位 | Freq_Tar | Range_Tar | 归并形式 |
|---:|---|---:|---:|---|
| 1 | claim | 1663 | ≥332 | claim+claims |
| 2 | evidence | 1389 | 321 | — |
| 3 | should | 1312 | 333 | — |
| 4 | need | 1069 | ≥281 | need+needs |
| 5 | rather | 833 | 295 | — |
| 6 | would | 786 | 298 | — |
| 7 | now | 594 | 320 | — |
| 8 | right | 548 | 316 | — |
| 9 | strengthen | 476 | ≥291 | strengthening+strengthen |
| 10 | then | 382 | 225 | — |
| 11 | reader | 327 | 183 | readers |
| 12 | carefully | 324 | 237 | — |
| 13 | analysis | 319 | 153 | — |
| 14 | proofread | 317 | ≥181 | proofreading+proofread |
| 15 | level | 298 | 232 | — |
| 16 | give | 296 | ≥178 | gives+given |
| 17 | reasoning | 281 | 168 | — |
| 18 | public | 275 | 114 | — |
| 19 | clarify | 272 | ≥197 | clarifying+clarify |
| 20 | case | 269 | 137 | — |
| 21 | address | 264 | 177 | — |
| 22 | just | 263 | 182 | — |
| 23 | currently | 259 | 182 | — |
| 24 | credibility | 243 | 190 | — |
| 25 | matter | 235 | ≥123 | matters+matter |
| 26 | even | 232 | 158 | — |
| 27 | phrasing | 229 | 176 | — |
| 28 | paper | 216 | 105 | — |
| 29 | instance | 202 | 184 | — |
| 30 | might | 187 | 150 | — |
| 31 | read | 180 | 164 | reads |
| 32 | strong | 180 | 137 | strongest |
| 33 | actual | 176 | 126 | — |
| 34 | open | 176 | 133 | opening |
| 35 | mechanics | 175 | 148 | — |
| 36 | develop | 169 | 144 | — |
| 37 | material | 166 | 118 | — |
| 38 | replace | 166 | 128 | — |
| 39 | section | 164 | 98 | — |
| 40 | draft | 164 | 127 | — |
| 41 | something | 157 | 130 | — |
| 42 | actually | 154 | 115 | — |
| 43 | analytical | 153 | 112 | — |
| 44 | significant | 149 | 111 | — |
| 45 | make | 147 | 113 | making |
| 46 | wording | 144 | 108 | — |
| 47 | want | 144 | 107 | — |
| 48 | move | 142 | 117 | — |
| 49 | policy | 139 | 68 | — |
| 50 | sharpen | 138 | ≥94 | sharpen+sharpening |
| 51 | power | 132 | 55 | — |
| 52 | vague | 126 | 107 | — |
| 53 | credible | 125 | 100 | — |
| 54 | rely | 125 | ≥63 | relies+rely |
| 55 | counterargument | 125 | 96 | counterarguments |
| 56 | piece | 123 | 95 | — |
| 57 | edit | 122 | 109 | — |
| 58 | sense | 114 | 97 | — |
| 59 | reorganize | 109 | 108 | — |
| 60 | acknowledge | 106 | 93 | — |
| 61 | weaken | 103 | 100 | — |
| 62 | broad | 103 | 87 | broader |
| 63 | precision | 99 | 81 | — |
| 64 | assert | 99 | ≥48 | assert+asserted |
| 65 | genuine | 99 | 82 | — |
| 66 | specifically | 96 | 81 | — |
| 67 | argue | 95 | 82 | arguing |
| 68 | single | 95 | 71 | — |
| 69 | define | 94 | 62 | — |
| 70 | financial | 93 | 43 | — |
| 71 | aim | 92 | 89 | — |
| 72 | structural | 92 | 70 | — |
| 73 | cut | 90 | 77 | — |
| 74 | line | 86 | 70 | — |
| 75 | shift | 82 | 75 | shifts |
| 76 | distinct | 82 | 64 | — |
| 77 | anecdote | 82 | 52 | — |
| 78 | cultural | 80 | 52 | — |
| 79 | term | 79 | 62 | terms |
| 80 | concern | 78 | 65 | concerns |
| 81 | mechanical | 77 | 63 | — |
| 82 | arguable | 76 | 68 | — |
| 83 | come | 73 | 60 | — |
| 84 | big | 72 | 70 | biggest |
| 85 | typo | 71 | 57 | typos |
| 86 | placeholder | 70 | 62 | — |
| 87 | inconsistent | 68 | 58 | — |
| 88 | similarly | 67 | 66 | — |
| 89 | tackle | 66 | 66 | tackles |
| 90 | authority | 65 | 48 | — |
| 91 | measure | 65 | 59 | measured |
| 92 | underdeveloped | 65 | 63 | — |
| 93 | improve | 64 | 62 | improving |
| 94 | risk | 64 | 48 | — |
| 95 | complexity | 63 | 56 | — |
| 96 | core | 63 | 60 | — |
| 97 | casual | 63 | 43 | — |
| 98 | polish | 61 | 59 | polished |
| 99 | correctness | 60 | 54 | — |
| 100 | alone | 60 | 51 | — |
| 101 | fairly | 59 | 50 | — |
| 102 | distract | 58 | 55 | — |
| 103 | assertion | 58 | 53 | — |
| 104 | sharp | 57 | 54 | sharper |
| 105 | sweeping | 56 | 49 | — |
| 106 | defensible | 53 | 43 | — |
| 107 | contain | 53 | 48 | contains |
| 108 | turn | 51 | 49 | — |
| 109 | frame | 51 | 41 | framing |
| 110 | four | 49 | 39 | — |
| 111 | build | 48 | 44 | building |
| 112 | abstract | 48 | 42 | — |
| 113 | write | 47 | 40 | written |
| 114 | imprecise | 46 | 46 | — |
| 115 | entirely | 46 | 45 | — |
| 116 | heavily | 46 | 45 | — |
| 117 | engage | 45 | 41 | — |
| 118 | tighten | 44 | 41 | — |
| 119 | detail | 43 | 36 | — |
| 120 | prose | 42 | 37 | — |
| 121 | precisely | 41 | 37 | — |
| 122 | distinguish | 41 | 39 | — |
| 123 | loosely | 40 | 38 | — |
| 124 | serve | 40 | 37 | — |
| 125 | integrate | 39 | 39 | — |
| 126 | overly | 39 | 36 | — |
| 127 | skeptical | 38 | 37 | — |
| 128 | take | 37 | 36 | takes |

## 4. R2 排除项（16 项，均已通过 R1）

| 词形 | Freq_Tar | Range_Tar | 排除理由 |
|---|---:|---:|---|
| that | 2935 | 348 | 关系词/连词/指示词 |
| than | 1199 | 324 | 连词(比较)/介词 |
| what | 885 | 309 | 疑问词/关系词 |
| the | 10478 | 348 | 冠词 |
| into | 477 | 256 | 介词 |
| around | 220 | 160 | 介词 |
| from | 857 | 312 | 介词 |
| toward | 122 | 100 | 介词 |
| without | 439 | 245 | 介词 |
| up | 174 | 123 | 介词/动词小品词 |
| as | 1367 | 341 | 介词/连词 |
| if | 667 | 285 | 从属连词 |
| those | 109 | 86 | 指示词 |
| it | 2719 | 348 | 非人称代词(虚指/形式主语为主) |
| does | 417 | 223 | 助动词do |
| either | 124 | 97 | 并列连词(either...or)/限定词 |

## 5. R3 排除项（3 项）

| 词形 | Freq_Tar | Range_Tar | 排除理由 |
|---|---:|---:|---|
| t | 550 | 205 | not/is/has 缩写残片 |
| doesn | 170 | 102 | does not 残片 |
| ll | 47 | 42 | will 残片 |

## 6. R4 归并明细（10 组）

| 词位 | 归并形式 | Freq 合计 | Range 下界 |
|---|---|---:|---:|
| claim | claim + claims | 1663 | ≥332 |
| need | need + needs | 1069 | ≥281 |
| strengthen | strengthening + strengthen | 476 | ≥291 |
| proofread | proofreading + proofread | 317 | ≥181 |
| give | gives + given | 296 | ≥178 |
| clarify | clarifying + clarify | 272 | ≥197 |
| matter | matters + matter | 235 | ≥123 |
| sharpen | sharpen + sharpening | 138 | ≥94 |
| rely | relies + rely | 125 | ≥63 |
| assert | assert + asserted | 99 | ≥48 |

### 未归并的对照项（派生变体 / 否定对立项，按 R4 保持独立）

- `assert` ／ `assertion`（动词 → 名词派生）
- `analysis` ／ `analytical`（名词 → 形容词派生）
- `mechanics` ／ `mechanical`（名词 → 形容词派生）
- `credible` ／ `credibility`（形容词 → 名词派生）
- `precision` ／ `precisely` ／ `imprecise`（派生 + 否定对立）
- `develop` ／ `underdeveloped`（派生 + 否定对立）
- `sharp`(sharper) ／ `sharpen`(sharpening)（形容词 → 动词派生）
- `actual` ／ `actually`（形容词 → 副词派生）
- `broad`(broader) ／ `loosely`、`cultural`、`structural` 等派生形容词/副词各自独立

## 7. 待确认的判断

| # | 词形 | 本次判定 | 说明 |
|---:|---|---|---|
| 1 | `it` | R2 排除 | 该语料中多为 "it reads as…/it would help" 形式主语，但含指代实义用法；能否细分需回原语料，词表层面无法判定 |
| 2 | `either` | R2 排除 | 按 either…or 并列连词/限定词处理；若视为量词则应保留 |
| 3 | `rather` | 保留 | 按副词保留；但语料中大量出现于 rather than 结构（than freq 1199，量级相近），若按结构判定应排除 |
| 4 | `then` | 保留 | 按副词保留；若视为连接词则排除 |
| 5 | `four`、`single` | 保留 | 按量词/数词保留 |

## 8. 口径说明与边界个案

**归并时点：R1 先行、R4 后置。** 原因：Range 无法从词表层面合并——同一文档可能同时含 `claim` 与 `claims`，相加会系统性高估分布。因此只在已通过 R1 的形式之间归并，Freq 求和、Range 取组内最大值。

按此口径被拒、但若改用「先合并再判 R1」则可能入选的家族如下，真实合并 Range 落在「最大值」与「上限和」之间，需回 AntConc 以 lemma 检索核实：

| 家族 | Freq 合计 | Range 最大值 | Range 上限和 | 门槛 |
|---|---:|---:|---:|---|
| objection + objections | 77 | 34 | 59 | 35 |
| gesture + gestures | 51 | 25 | 46 | 35 |
| stake + stakes | 47 | 30 | 43 | 35 |

