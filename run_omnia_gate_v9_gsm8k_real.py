import json
import re
from pathlib import Path

INPUT = Path("results/real_validation_gsm8k_real_results.jsonl")
OUTPUT = Path("results/real_validation_v9_gsm8k_real_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V9_GSM8K_REAL.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def norm(s):
    return str(s).strip().lower()

def is_number(s):
    try:
        float(str(s).strip().replace(",", ""))
        return True
    except Exception:
        return False

def clean_number(s):
    return str(s).strip().replace(",", "")

def is_pure_number(s):
    return bool(re.fullmatch(r"-?\d+(\.\d+)?", clean_number(s)))

def has_expression(s):
    return bool(re.search(r"\d+\s*[\+\-\*/]\s*\d+", str(s))) or "=" in str(s)

def same(out, exp):
    if is_number(out) and is_number(exp):
        return float(clean_number(out)) == float(clean_number(exp))
    return norm(out) == norm(exp)

def final_answer_violation(row):
    out = str(row["output"]).strip()

    if has_expression(out):
        return True
    if not is_pure_number(out):
        return True

    return False

def arithmetic_incoherence(row):
    out = row["output"]
    exp = row["expected"]

    if same(out, exp):
        return False

    if is_pure_number(out) and is_number(exp):
        return True

    return False

def omnia_gate_v9(row):
    out = str(row["output"]).strip()

    if not out:
        return {"gate_status": "NO_GO", "reason": "empty_output"}

    if final_answer_violation(row):
        return {"gate_status": "NO_GO", "reason": "final_answer_violation"}

    if arithmetic_incoherence(row):
        return {"gate_status": "NO_GO", "reason": "arithmetic_incoherence"}

    return {"gate_status": "GO", "reason": "valid_numeric_answer"}

rows = []
counts = {"GO": 0, "NO_GO": 0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        sig = omnia_gate_v9(r)
        r["omnia_v9"] = sig
        rows.append(r)
        counts[sig["gate_status"]] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp = fn = fp = tn = 0

for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["omnia_v9"]["gate_status"] != "GO"

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
md.append("# V9 — GSM8K Real Slice")
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

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA V9 — GSM8K REAL")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())