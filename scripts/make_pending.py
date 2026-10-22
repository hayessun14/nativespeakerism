#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从合并总表抽出全部待 concordance 判定的词形，按词形聚合并排定优先级。

单位是**词形**而非词位：concordance 是对某个词形在语料中的用法作一次判定，
判定结果回填到它出现的所有组，因此同一词形在多组的 PENDING 合并为一行。

输出：
  coding/pending_worklist.tsv   机读版，一行一个词形
  coding/pending_worklist.md    人读版，按优先级分节，含判定规则
"""
import csv
from collections import defaultdict

ALL = "coding/all_codes.tsv"
LAYER = {"d1": "维度一", "act": "act 层", "hedge": "hedge 层", "c": "维度三"}

# v3 强制查询清单已知条目及其同族形式（清单全文尚未获得，见各组报告）
MANDATORY = {"address", "strong", "strongest", "stronger", "strengths", "strength", "STRENGTH",
             "STRENGTHEN", "strengthen"}
# 手册指定的共享情态项
SHARED_MODAL = {"could", "would", "might", "can"}
# 内容动词类：本身不构成言语行为，act 归属取决于所嵌框架（待统一规则）
CONTENT_VERB = {"explain", "EXPLAIN", "discuss", "discussing", "say", "saying", "mention",
                "write", "use", "USE", "using", "used", "focus", "FOCUS", "create", "read",
                "choose", "check", "raise", "raises", "offer", "state", "vary", "double"}
BIG = 400          # 高体量阈值（单组 Freq_Tar）

rows = list(csv.DictReader(open(ALL, encoding="utf-8"), delimiter="\t"))

agg = defaultdict(lambda: dict(layers=set(), groups=set(), pend_groups=set(),
                               freq={}, ll=0.0, lr=0.0, notes=[], conf_l=False))
for r in rows:
    a = agg[r["type"]]
    a["groups"].add(int(r["group"]))
    a["freq"][int(r["group"])] = int(r["freq_tar"])
    for k in ("d1", "act", "hedge", "c"):
        if r[k] == "PENDING":
            a["layers"].add(k); a["pend_groups"].add(int(r["group"]))
    if r["conf"] == "L":
        a["conf_l"] = True; a["pend_groups"].add(int(r["group"]))
    if r["note"] not in a["notes"]:
        a["notes"].append(r["note"])
    a["ll"] = max(a["ll"], float(r["ll"])); a["lr"] = max(a["lr"], float(r["lr"]))

# 非 PENDING 但仍须 concordance 的两项特殊情况
SPECIAL = {
    "chinese": ("C1 子类判定", "已定 C1，但 Identity marking 与 Transfer framing 的子类归属未定；"
                              "决定中文条件的 C1 是纯身份命名还是含迁移归因"),
    "tackles": ("跨组一致性回填", "组 1 编为 A1、组 9 编为 PENDING（有意保留的唯一跨组不一致）；"
                                 "须与组 4 raises 并案判定后统一回填组 1、4、9"),
}

def priority(t, a):
    # 同一批须用同一套协议处理的词必须归在一起，不因体量被拆散——
    # 故 MANDATORY／SHARED_MODAL／CONTENT_VERB 三个成组类别先于高体量规则判定。
    if "c" in a["layers"] or t in SPECIAL:            return 1   # 维度三，决定核心结论
    if t in MANDATORY or t in SHARED_MODAL:            return 2   # 强制查询清单＋手册指定共享项
    if t in CONTENT_VERB:                              return 4   # 待统一规则后整批处理
    if "act" in a["layers"] and max(a["freq"].values()) >= BIG: return 2
    if "d1" in a["layers"] and max(a["freq"].values()) >= BIG: return 3
    if any("疑似议题" in n for n in a["notes"]):        return 5   # 议题残留统一判定
    if not a["layers"] and not a["conf_l"]:            return 5   # note 标记待核，无 PENDING 层
    if a["conf_l"] and not a["layers"]:                 return 6   # 仅低信度复核
    return 6

PRIO_NAME = {1: "P1 维度三候选（决定 RQ1／RQ2 核心结论）",
             2: "P2 强制查询清单、共享情态项与高体量 act",
             3: "P3 高体量维度一待定项",
             4: "P4 内容动词类（待统一规则后整批处理）",
             5: "P5 note 标记的待核项（议题残留疑似、子类边界、其他）",
             6: "P6 其余待定与低信度复核"}

work = []
for t, a in agg.items():
    flagged = any(("疑似" in n) or ("待核" in n) for n in a["notes"])
    # 强制查询清单条目无条件纳入：即便本轮已给出标签，按规则也不得凭词形定
    if (not a["layers"] and not a["conf_l"] and not flagged
            and t not in SPECIAL and t not in MANDATORY):
        continue
    layers = [LAYER[k] for k in ("d1", "act", "hedge", "c") if k in a["layers"]]
    if a["conf_l"]: layers.append("低信度复核")
    if t in SPECIAL: layers.append(SPECIAL[t][0])
    if t in MANDATORY and "act" not in a["layers"]:
        layers.append("强制查询清单项（本轮已给标签，须复核）")
    if not layers:
        n0 = " ".join(a["notes"])
        layers.append("议题残留待核" if "疑似议题" in n0
                      else "子类边界待核" if "子类" in n0 else "其他待核")
    pg = sorted(a["pend_groups"] or a["groups"])
    work.append(dict(
        type=t, priority=priority(t, a), layers="＋".join(layers),
        n_layers=len(layers), groups="/".join(map(str, pg)), n_groups=len(pg),
        max_freq_tar=max(a["freq"].values()),
        freq_by_group="; ".join(f"组{g}:{a['freq'][g]}" for g in sorted(a["freq"])),
        max_ll=f"{a['ll']:.3f}", max_lr=f"{a['lr']:.3f}",
        note=SPECIAL[t][1] if t in SPECIAL else a["notes"][0]))

work.sort(key=lambda r: (r["priority"], -r["max_freq_tar"]))
FIELDS = ["priority", "type", "layers", "n_layers", "groups", "n_groups",
          "max_freq_tar", "freq_by_group", "max_ll", "max_lr", "note"]
with open("coding/pending_worklist.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("\t".join(FIELDS) + "\n")
    for r in work:
        f.write("\t".join(str(r[k]) for k in FIELDS) + "\n")

# 核对：机读版覆盖的 PENDING 词位数应等于总表 PENDING 词位数
tot_pend_cells = sum(1 for r in rows for k in ("d1", "act", "hedge", "c") if r[k] == "PENDING")
covered = sum(1 for r in rows for k in ("d1", "act", "hedge", "c")
              if r[k] == "PENDING" and r["type"] in {w["type"] for w in work})
assert tot_pend_cells == covered, f"覆盖不全：{covered}/{tot_pend_cells}"
print(f"总表 PENDING 单元格 {tot_pend_cells} 个 → 聚合为 {len(work)} 个待判定词形（覆盖率 100%）")
for p in sorted(PRIO_NAME):
    sel = [w for w in work if w["priority"] == p]
    print(f"  {PRIO_NAME[p]}：{len(sel)} 个")

# ---------- 人读版 ----------
md = []
W = md.append
W("# concordance 待判定词形总表\n")
W(f"> 由 `scripts/make_pending.py` 从 `coding/all_codes.tsv` 生成。")
W(f"> **单位是词形，不是词位**：concordance 对一个词形在语料中的用法作一次判定，"
  f"结果回填到它出现的所有组，因此同一词形在多组的 PENDING 合并为一行。")
W(f"> 总表共 {tot_pend_cells} 个 PENDING 单元格，聚合为 **{len(work)} 个待判定词形**；"
  f"另含 note 标记待核项与两项特殊情况（见 P1、P5）。\n")
W("## 优先级与判定规则\n")
W("| 优先级 | 含义 | 数量 | 判定规则 |")
W("|---|---|---:|---|")
RULE = {
 1: "先做。决定 RQ1／RQ2 的核心结论。`false` 只需查右搭配是否为 friends，成本最低、回报最高；"
    "`natural`／`unnatural`／`sounds` 判定唯一可能的「规范型」C1；`chinese` 只判子类，范畴已定",
 2: "三类合并于此。① 手册 v3 强制查询清单已知条目，一律不得凭词形归类；"
    "② `could`／`would`／`might`／`can` 按手册各随机抽 50 行，**在 v3 共存规则下须分别判 act 层与 hedge 层**，不是二选一；"
    "③ 其余高体量 act 项（单组 Freq_Tar ≥ 400），其归属直接决定 A1／A3 的量级，进而决定 act 层能否跨组解读",
 3: "单组 Freq_Tar ≥ 400 的维度一待定项。它们决定各组敏感性区间能否收窄，"
    "尤其是组 1／组 2——十二组中唯一仍存在实质重叠区 [56.0, 68.9] 的一对",
 4: "**先定统一规则再逐词判**，勿因体量拆散（本级含 `use` 897、`EXPLAIN` 603 等高频项）。建议：抽 50 行，统计该动词是否出现在祈使句、"
    "`you should/need to/can/could + V`、`try/consider V-ing` 等补救框架中；"
    "≥60% 判 A3，≤40% 判 NA，中间区间报不可判定并在敏感性分析中双向计算",
 5: "第三人称代词群（`she`／`he`／`her`／`people`）建议一次性判定后统一处理，不要逐组单判；"
    "子类边界项只影响子类占比，不影响主类",
 6: "其余维度一／act／hedge 待定与低信度复核。可在前五级完成后批量处理",
}
for p in sorted(PRIO_NAME):
    n = sum(1 for w in work if w["priority"] == p)
    W(f"| **P{p}** | {PRIO_NAME[p][3:]} | {n} | {RULE[p]} |")
W("")
for p in sorted(PRIO_NAME):
    sel = [w for w in work if w["priority"] == p]
    if not sel: continue
    W(f"## {PRIO_NAME[p]}（{len(sel)} 个）\n")
    W("| 词形 | 待定层 | 出现组 | 单组最高 Freq_Tar | 最高 LL | 最高 LR | 竞争读法／依据 |")
    W("|---|---|---|---:|---:|---:|---|")
    for w in sel:
        W(f"| `{w['type']}` | {w['layers']} | {w['groups']} | {w['max_freq_tar']} | "
          f"{w['max_ll']} | {w['max_lr']} | {w['note']} |")
    W("")
open("coding/pending_worklist.md", "w", encoding="utf-8").write("\n".join(md))
print(f"\n写出 coding/pending_worklist.md（{len(md)} 行）")
