import json
from pathlib import Path

OMNIA = Path("results/real_validation_v7_super_omnia.jsonl")
BASE_V1 = Path("results/baseline_simple_v1.jsonl")
BASE_V2 = Path("results/baseline_majority_v2.jsonl")

MD = Path("docs/OMNIA_VS_BASELINES_V2.md")
MD.parent.mkdir(parents=True, exist_ok=True)

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def metrics(rows, key):
    tp = fn = fp = tn = 0

    for r in rows:
        is_err = r["verdict"] == "semantic_error"
        flagged = r[key]["gate_status"] != "GO"

        if is_err and flagged:
            tp += 1
        elif is_err and not flagged:
            fn += 1
        elif not is_err and flagged:
            fp += 1
        else:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0

    return tp, fn, fp, tn, precision, recall

# load
omnia_rows = load_jsonl(OMNIA)
b1_rows = load_jsonl(BASE_V1)
b2_rows = load_jsonl(BASE_V2)

omnia_m = metrics(omnia_rows, "omnia_v7")
b1_m = metrics(b1_rows, "baseline_simple_v1")
b2_m = metrics(b2_rows, "baseline_majority_v2")

def row(name, m):
    tp, fn, fp, tn, p, r = m
    return f"| {name} | {tp} | {fn} | {fp} | {tn} | {p:.3f} | {r:.3f} |"

md = []
md.append("# OMNIA vs Baselines V2")
md.append("")
md.append("## Results")
md.append("")
md.append("| Method | TP | FN | FP | TN | Precision | Recall |")
md.append("|---|---:|---:|---:|---:|---:|---:|")
md.append(row("OMNIA V7", omnia_m))
md.append(row("Baseline Simple V1", b1_m))
md.append(row("Baseline Majority V2", b2_m))
md.append("")
md.append("## Interpretation")
md.append("")
md.append("- OMNIA must outperform both baselines")
md.append("- Especially compared to V2 (non-trivial heuristic)")
md.append("")
md.append("## Status")
md.append("")
md.append("Still minimal validation.")
md.append("More datasets and stronger models required.")
md.append("")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA VS BASELINES V2")
print("=" * 60)
print("OMNIA:", omnia_m)
print("BASE V1:", b1_m)
print("BASE V2:", b2_m)
print("Saved:", MD.resolve())