import json
from pathlib import Path

INPUT = Path("results/real_validation_v5_super.jsonl")
OUTPUT = Path("results/baseline_simple_v1.jsonl")
MD = Path("docs/BASELINE_SIMPLE_V1.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def baseline_gate(row):
    out = str(row["output"]).strip()

    if not out:
        return "NO_GO"

    if len(out) > 50:
        return "NO_GO"

    return "GO"

rows = []
counts = {"GO": 0, "NO_GO": 0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        gate = baseline_gate(r)
        r["baseline_simple_v1"] = {"gate_status": gate}
        rows.append(r)
        counts[gate] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp = fn = fp = 0

for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["baseline_simple_v1"]["gate_status"] != "GO"

    if is_err and flagged:
        tp += 1
    elif is_err and not flagged:
        fn += 1
    elif not is_err and flagged:
        fp += 1

md = []
md.append("# Baseline Simple V1")
md.append("")
md.append("## Purpose")
md.append("")
md.append("This is a deliberately simple baseline gate.")
md.append("")
md.append("It flags only:")
md.append("")
md.append("- empty outputs")
md.append("- outputs longer than 50 characters")
md.append("")
md.append("It does not evaluate semantics, arithmetic, factuality, or structural compatibility.")
md.append("")
md.append("## Aggregate")
md.append("")
md.append(f"- GO: `{counts['GO']}`")
md.append(f"- NO_GO: `{counts['NO_GO']}`")
md.append("")
md.append("## Alignment with observed errors")
md.append("")
md.append(f"- TP: `{tp}`")
md.append(f"- FN: `{fn}`")
md.append(f"- FP: `{fp}`")
md.append("")
md.append("## Interpretation")
md.append("")
md.append("This baseline is intentionally weak.")
md.append("")
md.append("Its purpose is to test whether OMNIA performs better than a trivial heuristic.")
md.append("")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("BASELINE SIMPLE V1")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp)
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())