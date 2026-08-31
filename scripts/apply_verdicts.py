#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 concordance 判定结果回填到 all_codes.tsv 的 PENDING 单元格。

判定表以（词形 × 语料）为键，总表以（组 × 词形）为键，语料→组为一对多：
  L1→1,12  Generic→2,4,8,10  Chinese→3,5  German→6,7  Baseline→9,11
判定表的取值有多种写法，本脚本统一解析后按层落位；只填当前为 PENDING 的单元格，
凡目标单元格不是 PENDING、或判定无法唯一落位者，一律不改动并列入报告。
"""
import csv, re, sys
from collections import defaultdict

VERDICTS = "data_concordance_verdicts.tsv"
ALL = "coding/all_codes.tsv"
CORPUS2G = {"L1": [1, 12], "Generic": [2, 4, 8, 10], "Chinese": [3, 5],
            "German": [6, 7], "Baseline": [9, 11]}
SUB = {"G1-Ideas": ("G1", "Ideas"), "G1-Development": ("G1", "Development"),
       "G1-Global Structure": ("G1", "Global Structure"),
       "G2-Wording": ("G2", "Wording"), "G2-Local Structure": ("G2", "Local Structure"),
       "G2-Correctness": ("G2", "Correctness"),
       "G2-Correctness-Grammar": ("G2", "Grammar"),
       "G2-Correctness-Mechanics": ("G2", "Mechanics")}
ACTS = {"A1", "A2", "A3"}
LAYER_OF = {"G": "d1", "A": "act", "M": "hedge", "C": "c"}
PREFIX = {"维度一": "d1", "维度二": "act?", "act": "act", "hedge": "hedge", "维度三": "c"}

def norm(s):
    return s.replace("；", ";").replace("，", ";").replace("　", " ").strip()

def strip_pct(tok):
    m = re.match(r"^(.*?)\s*\((\d+)%\)$", tok.strip())
    return (m.group(1).strip(), int(m.group(2))) if m else (tok.strip(), None)

def parse(v):
    """返回 (assignments, pct, problem)；assignments: [(layer|None, label)]。"""
    v = norm(v)
    if "/" in v and "%" in v:                       # 形如 A(50%) / B(50%)：并列，无主导
        return [], None, f"并列无主导：{v}"
    out, pcts = [], []
    for part in [p for p in v.split(";") if p.strip()]:
        part = part.strip()
        layer = None
        m = re.match(r"^(维度一|维度二|维度三|act|hedge)\s*=\s*(.*)$", part)
        if m:
            layer, part = PREFIX[m.group(1)], m.group(2).strip()
        lbl, pct = strip_pct(part)
        if pct is not None: pcts.append(pct)
        out.append((layer, lbl))
    return out, (min(pcts) if pcts else None), None

def label_layer(lbl):
    if lbl in SUB: return "d1"
    if lbl in ACTS: return "act"
    if lbl == "M1": return "hedge"
    if lbl.startswith("C1"): return "c"
    if lbl == "NA": return None
    return "?"

rows = list(csv.DictReader(open(ALL, encoding="utf-8"), delimiter="\t"))
pend = defaultdict(list)                      # (g, lower(type)) -> [layer,...]
real = {}                                     # (g, lower(type)) -> 原始 type
for r in rows:
    k = (int(r["group"]), r["type"].lower())
    real[k] = r["type"]
    for L in ("d1", "act", "hedge", "c"):
        if r[L] == "PENDING":
            pend[k].append(L)

# 判定表为 UTF-8 BOM + CRLF，须用 utf-8-sig 并清除行尾 \r
vs = list(csv.DictReader(open(VERDICTS, encoding="utf-8-sig", newline=""), delimiter="\t"))
for v in vs:
    for k in list(v):
        if isinstance(v.get(k), str): v[k] = v[k].replace("\r", "").strip()
vs = [v for v in vs if v.get("word") and v.get("corpus")]
print(f"判定表 {len(vs)} 行；总表 PENDING 单元格 "
      f"{sum(len(v) for v in pend.values())} 个\n")

def resolve(word, corpus, verdict):
    """把一条判定落位到具体的 (group, layer, label)；返回 (assign_list, problems)。"""
    parts, pct, prob = parse(verdict)
    if prob:
        return [], [prob]
    out, probs = [], []
    for g in CORPUS2G[corpus]:
        k = (g, word.lower())
        if k not in real:
            continue                      # 该组没有这个词形，正常（语料对一对多）
        P = list(pend.get(k, []))
        if not P:
            probs.append(f"组{g} `{real[k]}` 无 PENDING 单元格，判定无处落位")
            continue
        got, na_toks = [], []
        for layer, lbl in parts:
            if layer == "act?":           # 「维度二」需在 act / hedge 中择一
                layer = "act" if "act" in P else ("hedge" if "hedge" in P else None)
            if layer is None:
                layer = label_layer(lbl)
            if layer == "?":
                probs.append(f"组{g} `{real[k]}` 标签无法识别：{lbl}"); continue
            if layer is None:             # NA，层待推断
                na_toks.append(lbl); continue
            got.append((layer, lbl))
        # NA 按典型顺序填入尚未被占用的 PENDING 层
        free = [L for L in ("d1", "act", "hedge", "c") if L in P and L not in {x[0] for x in got}]
        if len(na_toks) > len(free):
            probs.append(f"组{g} `{real[k]}` NA 数({len(na_toks)}) 多于可落位的 PENDING 层({len(free)})")
        elif na_toks and len(na_toks) < len(free):
            probs.append(f"组{g} `{real[k]}` NA 数({len(na_toks)}) 少于 PENDING 层 {free}，落位不唯一")
        else:
            got += [(L, "NA") for L in free[:len(na_toks)]]
        for layer, lbl in got:
            if layer not in P:
                probs.append(f"组{g} `{real[k]}` 的 {layer} 层不是 PENDING（现值见总表），判定 {lbl} 未采用")
            else:
                out.append((g, real[k], layer, lbl, pct))
        miss = [L for L in P if L not in {x[0] for x in got}]
        if miss:
            probs.append(f"组{g} `{real[k]}` 判定未覆盖 PENDING 层 {miss}")
    return out, probs

# 逐条解析
by_key = defaultdict(list)
all_assign, all_probs = [], []
for i, v in enumerate(vs, 2):
    a, pr = resolve(v["word"], v["corpus"], v["主导判定"])
    by_key[(v["word"].lower(), v["corpus"])].append(frozenset((x[0], x[2], x[3]) for x in a))
    all_assign += [(i, v["word"], v["corpus"]) + x for x in a]
    all_probs += [(i, v["word"], v["corpus"], p) for p in pr]

real_dup = {k: x for k, x in by_key.items() if len(set(x)) > 1}
print(f"解析后仍互相冲突的（词形×语料）：{len(real_dup)} 处")
for k, x in real_dup.items():
    print(f"   ⚠ {k[0]} / {k[1]}：落位结果不一致 → {[sorted(y) for y in set(x)]}")
print()

# 同一目标单元格被多条判定指向且值不同
cell = defaultdict(set)
for _, w, c, g, t, L, lbl, pct in all_assign:
    cell[(g, t, L)].add(lbl)
clash = {k: v for k, v in cell.items() if len(v) > 1}
print(f"同一单元格收到互不相同的判定：{len(clash)} 处 {clash if clash else ''}\n")

print(f"可落位的赋值 {len({(x[3],x[4],x[5]) for x in all_assign})} 个单元格（判定行 {len({x[0] for x in all_assign})} 条）")
print(f"问题记录 {len(all_probs)} 条：")
from collections import Counter
kinds = Counter(re.sub(r"组\d+ `[^`]+` ", "", p[3]).split("：")[0].split("(")[0] for p in all_probs)
for k, n in kinds.most_common():
    print(f"   {n:>3}  {k}")


# ================= 三类分流 =================
# A 类：目标单元格现为 PENDING          → 本轮填充
# B 类：目标单元格已有标签且与判定一致  → 仅记录确认，不改动
# C 类：目标单元格已有标签且与判定不符  → 不擅自改动，单独报告待定夺
cur = {(int(r["group"]), r["type"], L): r[L] for r in rows for L in ("d1","act","hedge","c")}
sub_of = {(int(r["group"]), r["type"]): r["d1sub"] for r in rows}

def as_pair(lbl):
    if lbl in SUB: return SUB[lbl]
    if lbl.startswith("C1"): return ("C1", None)
    return (lbl, None)

A, B, C = [], [], []
for i, w, c, g, t, L, lbl, pct in all_assign:
    val, sub = as_pair(lbl)
    now = cur[(g, t, L)]
    if now == "PENDING":
        A.append((i, g, t, L, val, sub, lbl, pct))
    elif now == val and (sub is None or sub_of[(g, t)] == sub):
        B.append((i, g, t, L, val, lbl))
    else:
        C.append((i, g, t, L, now, sub_of[(g, t)], val, sub, lbl))

# 判定指向的词形在该组无任何 PENDING —— 同样按 B/C 分流
for i, w, cps, msg in all_probs:
    if "无 PENDING 单元格" not in msg: continue
    g = int(re.search(r"组(\d+)", msg).group(1)); t = re.search(r"`([^`]+)`", msg).group(1)
    parts, pct, prob = parse(vs[i-2]["主导判定"])
    for layer, lbl in parts:
        if layer in (None, "act?"):
            layer = label_layer(lbl)
            if layer is None:   # 裸 NA：无法确定针对哪一层，按「维持现状」处理
                B.append((i, g, t, "(未指明层)", "NA", lbl)); continue
        if layer == "?": continue
        val, sub = as_pair(lbl); now = cur[(g, t, layer)]
        if now == val and (sub is None or sub_of[(g, t)] == sub):
            B.append((i, g, t, layer, val, lbl))
        else:
            C.append((i, g, t, layer, now, sub_of[(g, t)], val, sub, lbl))

print(f"A 类（填充 PENDING）        {len({(x[1],x[2],x[3]) for x in A}):>4} 个单元格")
print(f"B 类（与现有标签一致，确认）{len(B):>4} 条")
print(f"C 类（与现有标签不符，待定夺）{len(C):>3} 条")
if C:
    print("\n===== C 类明细：判定与总表现有标签不符 =====")
    for i, g, t, L, now, nowsub, val, sub, lbl in C:
        nv = f"{val}/{sub}" if sub else val
        cv = f"{now}/{nowsub}" if now in ("G1","G2") else now
        print(f"  第{i:>3}行 组{g:<3}`{t}`  {L:<6} 现值 {cv:<22} → 判定 {nv}")
print("\n===== 仍无法落位 =====")
for i, w, c, msg in all_probs:
    if "无 PENDING 单元格" not in msg:
        print(f"  第{i:>3}行 {w}/{c}: {msg}")

# ================= 落盘 =================
# all_codes.tsv 由 12 个分组文件经 merge_codes.py 生成，故改动必须落在分组文件上，
# 再重新生成总表；否则下次重跑 merge_codes.py 会覆盖这里的改动。
APPLY = {}                                   # (g, type, layer) -> (值, 子类, 来源标签)
for i, g, t, L, val, sub, lbl, pct in A:
    APPLY[(g, t, L)] = (val, sub, lbl + (f"({pct}%)" if pct else ""))

# 裸 NA 且该词该组有多个 PENDING 层：按「该词主导用法在这些层上均不成立」处理，
# 即把全部剩余 PENDING 层一并判为 NA。此为本脚本的显式假设，已在报告中标出。
ASSUMED = []
for i, w, cps, msg in all_probs:
    m = re.match(r"组(\d+) `([^`]+)` NA 数\(1\) 少于 PENDING 层 \[([^\]]+)\]", msg)
    if not m: continue
    g, t = int(m.group(1)), m.group(2)
    for L in [x.strip().strip("'") for x in m.group(3).split(",")]:
        if cur[(g, t, L)] == "PENDING" and (g, t, L) not in APPLY:
            APPLY[(g, t, L)] = ("NA", None, "NA〔裸 NA 推定覆盖全部剩余 PENDING 层〕")
            ASSUMED.append((i, g, t, L))

changed = 0
for g in range(1, 13):
    fp = f"coding/group{g:02d}_codes.tsv"
    rs = list(csv.DictReader(open(fp, encoding="utf-8"), delimiter="\t"))
    fields = list(rs[0].keys())
    hit = False
    for r in rs:
        marks = []
        for L in ("d1", "act", "hedge", "c"):
            key = (g, r["type"], L)
            if key in APPLY and r[L] == "PENDING":
                val, sub, src = APPLY[key]
                r[L] = val
                if L == "d1":
                    r["d1sub"] = sub if val in ("G1", "G2") else "-"
                marks.append(f"{L}={src}")
                changed += 1; hit = True
        if marks:
            r["note"] = r["note"] + "〔concordance 判定：" + "，".join(marks) + "〕"
            r["conf"] = "C"
    if hit:
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            f.write("\t".join(fields) + "\n")
            for r in rs: f.write("\t".join(r[k] for k in fields) + "\n")

print(f"\n===== 落盘 =====")
print(f"已填充 {changed} 个 PENDING 单元格（其中 {len(ASSUMED)} 个来自裸 NA 推定）")
if ASSUMED:
    for i, g, t, L in ASSUMED:
        print(f"    推定：第{i}行 组{g} `{t}` {L} = NA")
