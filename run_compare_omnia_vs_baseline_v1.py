import json
from pathlib import Path

OMNIA = Path("results/real_validation_v7_super_omnia.jsonl")
BASELINE = Path("results/baseline_simple_v1.jsonl")
MD = Path("docs/OMNIA_VS_BASELINE_V1.md")

MD.parent.mkdir(parents=True, exist_ok=True)

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

omnia_rows = load_jsonl(OMNIA)
baseline_rows = load_jsonl(BASELINE)

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
        elif not is_err and not flagged:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0

    return {
        "TP": tp,
        "FN": fn,
        "FP": fp,
        "TN": tn,
        "precision": precision,
        "recall": recall,
    }

omnia_m = metrics(omnia_rows, "omnia_v7")
base_m = metrics(baseline_rows, "baseline_simple_v1")

md = []
md.append("# OMNIA V7 vs Baseline Simple V1")
md.append("")
md.append("## Purpose")
md.append("")
md.append("This report compares OMNIA Gate V7 against a trivial baseline gate.")
md.append("")
md.append("The baseline only flags:")
md.append("")
md.append("- empty outputs")
md.append("- outputs longer than 50 characters")
md.append("")
md.append("The goal is to verify whether OMNIA performs better than a naive heuristic.")
md.append("")
md.append("## Results")
md.append("")
md.append("| Method | TP | FN | FP | TN | Precision | Recall |")
md.append("|---|---:|---:|---:|---:|---:|---:|")
md.append(
    f"| OMNIA V7 | {omnia_m['TP']} | {omnia_m['FN']} | {omnia_m['FP']} | {omnia_m['TN']} | {omnia_m['precision']:.3f} | {omnia_m['recall']:.3f} |"
)
md.append(
    f"| Baseline Simple V1 | {base_m['TP']} | {base_m['FN']} | {base_m['FP']} | {base_m['TN']} | {base_m['precision']:.3f} | {base_m['recall']:.3f} |"
)
md.append("")
md.append("## Interpretation")
md.append("")
md.append("OMNIA is useful only if it detects failures that the trivial baseline misses.")
md.append("")
md.append("A strong result is:")
md.append("")
md.append("- higher TP")
md.append("- lower FN")
md.append("- low or zero FP")
md.append("")
md.append("## Status")
md.append("")
md.append("This is still a minimal validation.")
md.append("")
md.append("It does not prove generality.")
md.append("It tests whether OMNIA provides a measurable advantage over a simple heuristic on this controlled dataset.")
md.append("")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA VS BASELINE V1")
print("=" * 60)
print("OMNIA:", omnia_m)
print("BASELINE:", base_m)
print("Saved:", MD.resolve())