import json
from pathlib import Path

INPUT = Path("results/real_validation_v5_super.jsonl")
OUTPUT = Path("results/baseline_majority_v2.jsonl")
MD = Path("docs/BASELINE_MAJORITY_V2.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def baseline_gate(row):
    out = str(row["output"]).strip()

    # regole semplici ma meno banali
    if not out:
        return "NO_GO"

    if len(out) > 50:
        return "NO_GO"

    # numeri: evita "0" costante o valori sospetti per task aritmetici
    if row.get("task") == "reasoning":
        if out == "0":
            return "NO_GO"

    # QA/RAG: risposte in minuscolo su entità note spesso segnale di errore nel tuo set
    if row.get("task") in ("qa", "rag"):
        if out.islower() and len(out.split()) <= 2:
            return "NO_GO"

    return "GO"

rows = []
counts = {"GO": 0, "NO_GO": 0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        gate = baseline_gate(r)
        r["baseline_majority_v2"] = {"gate_status": gate}
        rows.append(r)
        counts[gate] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp = fn = fp = tn = 0

for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["baseline_majority_v2"]["gate_status"] != "GO"

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
md.append("# Baseline Majority V2")
md.append("")
md.append("## Rules")
md.append("- empty or very long outputs → NO_GO")
md.append("- reasoning outputs equal to '0' → NO_GO")
md.append("- QA/RAG short lowercase entities → NO_GO")
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
md.append("## Note")
md.append("Heuristic baseline stronger than trivial; still not semantic.")
MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("BASELINE MAJORITY V2")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())