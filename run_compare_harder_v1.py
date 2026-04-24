import json
from pathlib import Path

OMNIA = Path("results/real_validation_v6_harder_omnia.jsonl")
BASE = Path("results/baseline_majority_v2_harder.jsonl")
MD = Path("docs/OMNIA_VS_BASELINE_HARDER_V1.md")

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

    return {
        "TP": tp,
        "FN": fn,
        "FP": fp,
        "TN": tn,
        "precision": precision,
        "recall": recall,
    }

omnia_rows = load_jsonl(OMNIA)
base_rows = load_jsonl(BASE)

omnia = metrics(omnia_rows, "omnia_v6_harder")
base = metrics(base_rows, "baseline_majority_v2_harder")

md = []
md.append("# OMNIA vs Baseline — Harder Validation V1")
md.append("")
md.append("## Setup")
md.append("")
md.append("- Dataset: `examples/real_validation_v6_harder.jsonl`")
md.append("- Model: `google/flan-t5-base`")
md.append("- Same gate rules as previous validation")
md.append("- No tuning after seeing harder dataset results")
md.append("")
md.append("## Results")
md.append("")
md.append("| Method | TP | FN | FP | TN | Precision | Recall |")
md.append("|---|---:|---:|---:|---:|---:|---:|")
md.append(f"| OMNIA harder gate | {omnia['TP']} | {omnia['FN']} | {omnia['FP']} | {omnia['TN']} | {omnia['precision']:.3f} | {omnia['recall']:.3f} |")
md.append(f"| Baseline Majority V2 harder | {base['TP']} | {base['FN']} | {base['FP']} | {base['TN']} | {base['precision']:.3f} | {base['recall']:.3f} |")
md.append("")
md.append("## Interpretation")
md.append("")
md.append("This test checks whether the previous gate logic survives a harder dataset without retuning.")
md.append("")
md.append("A useful result requires:")
md.append("")
md.append("- higher recall than the baseline")
md.append("- low false positives")
md.append("- no dependence on manually tuned cases")
md.append("")
md.append("## Status")
md.append("")
md.append("Still minimal validation.")
md.append("The next step is testing stronger models and public benchmark slices.")
md.append("")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA VS BASELINE HARDER V1")
print("=" * 60)
print("OMNIA:", omnia)
print("BASELINE:", base)
print("Saved:", MD.resolve())