#!/usr/bin/env python3
"""Scan Markdown files for common Chinese AI-flavor markers (去 AI 味 audit).

Usage:
    python scan_ai_markers.py <dir-or-file> [more paths ...]
    python scan_ai_markers.py D:/AI/project --top 6

Prints per-file totals with top markers (worst first), then global counts
per marker. Heuristics only — inspect hits in context and judge by the rules
of the humanizer-zh / de-ai-flavor skills; a hit is not automatically wrong,
and no match is not proof of anything.
"""
import argparse
import os
import re


PATTERNS = {
    "破折号——": r"——",
    "不是X而是Y": r"不是[^，。；]{2,20}，?而是",
    "值得(一试/关注/注意)": r"值得(一试|关注|注意)",
    "闭环/赋能/抓手/沉淀/打通/拆解/颗粒度/底层逻辑": r"闭环|赋能|抓手|沉淀|打通|拆解|颗粒度|底层逻辑",
    "综上/总而言之": r"综上|总而言之",
    "让我们": r"让我们",
    "首先/其次/最后": r"首先|其次|最后",
    "更X的是": r"更重要的是|更妙的是|更关键的是|更好的是",
    "堪称": r"堪称",
    "深入探讨": r"深入探讨",
    "全方位/无缝": r"全方位|无缝",
    "落地(动词用法)": r"落地",
}


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                files.extend(
                    os.path.join(root, n)
                    for n in names
                    if n.endswith(".md") and not n.startswith("_")
                )
        else:
            files.append(p)
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--top", type=int, default=5,
                    help="markers shown per file (default 5)")
    args = ap.parse_args()

    rows, global_counts = [], {}
    for f in collect(args.paths):
        text = open(f, encoding="utf-8").read()
        counts = {k: len(re.findall(p, text)) for k, p in PATTERNS.items()}
        for k, v in counts.items():
            global_counts[k] = global_counts.get(k, 0) + v
        top = sorted(((v, k) for k, v in counts.items() if v), reverse=True)
        rows.append((os.path.basename(f), sum(counts.values()), top[: args.top]))

    rows.sort(key=lambda r: r[1], reverse=True)
    width = max((len(r[0]) for r in rows), default=20)
    for name, total, top in rows:
        top_s = ", ".join(f"{k}×{v}" for v, k in top) or "-"
        print(f"{name:<{width}}  total={total:>4}  {top_s}")

    print()
    print("GLOBAL: " + " | ".join(
        f"{k}={v}"
        for k, v in sorted(global_counts.items(), key=lambda kv: -kv[1])
        if v
    ))


if __name__ == "__main__":
    main()
