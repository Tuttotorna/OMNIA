import json
from pathlib import Path

INPUT = Path("results/real_validation_v6_harder_results.jsonl")
OUTPUT = Path("results/real_validation_v6_harder_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V6_HARDER_OMNIA.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def omnia_gate(row):
    out = str(row["output"]).strip()

    # stesse regole V7 (nessun tuning)
    if not out:
        return "NO_GO"

    if len(out) > 50:
        return "NO_GO"

    if row["task"] == "reasoning":
        if out == "0":
            return "NO_GO"

    if row["task"] in ("qa", "rag"):
        if out.islower() and len(out.split()) <= 2:
            return "NO_GO"

    return "GO"

rows = []
counts = {"GO": 0, "NO_GO": 0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        gate = omnia_gate(r)
        r["omnia_v6_harder"] = {"gate_status": gate}
        rows.append(r)
        counts[gate] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp = fn = fp = tn = 0

for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["omnia_v6_harder"]["gate_status"] != "GO"

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

md = []
md.append("# Real Validation V6 HARDER — OMNIA Gate")
md.append("")
md.append("## Results")
md.append(f"- GO: `{counts['GO']}`")
md.append(f"- NO_GO: `{counts['NO_GO']}`")
md.append("")
md.append("## Alignment")
md.append(f"- TP: `{tp}`")
md.append(f"- FN: `{fn}`")
md.append(f"- FP: `{fp}`")
md.append(f"- TN: `{tn}`")
md.append(f"- Precision: `{precision:.3f}`")
md.append(f"- Recall: `{recall:.3f}`")
md.append("")
md.append("## Status")
md.append("Same rules as V7. No tuning.")
MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA V6 HARDER")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())