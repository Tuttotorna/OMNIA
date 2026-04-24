import json
import re
from pathlib import Path

INPUT = Path("results/real_validation_v6_harder_flan_large_results.jsonl")
OUTPUT = Path("results/real_validation_v9_structural_completeness_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V9_STRUCTURAL_COMPLETENESS.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def norm(s):
    return str(s).strip().lower()

def is_number(s):
    try:
        float(str(s).strip())
        return True
    except Exception:
        return False

def is_pure_number(s):
    return bool(re.fullmatch(r"-?\d+(\.\d+)?", str(s).strip()))

def has_expression(s):
    return bool(re.search(r"\d+\s*[\+\-\*/]\s*\d+", str(s))) or "=" in str(s)

def token_set(s):
    return set(re.findall(r"[a-zA-Z0-9]+", norm(s)))

def same(out, exp):
    if is_number(out) and is_number(exp):
        return float(out) == float(exp)
    return norm(out) == norm(exp)

def arithmetic_incoherence(row):
    if row["task"] != "reasoning":
        return False

    out = row["output"]
    exp = row["expected"]

    if same(out, exp):
        return False

    # wrong pure numeric answer
    if is_pure_number(out) and is_number(exp):
        return True

    return False

def final_answer_violation(row):
    out = str(row["output"]).strip()

    if row["task"] == "reasoning":
        if has_expression(out):
            return True
        if not is_pure_number(out):
            return True

    return False

def factual_mismatch(row):
    if row["task"] not in ("qa", "rag"):
        return False

    if same(row["output"], row["expected"]):
        return False

    return True

def entity_confusion(row):
    if row["task"] not in ("qa", "rag"):
        return False

    prompt = norm(row["prompt"])
    out = norm(row["output"])
    exp = norm(row["expected"])

    if out == exp:
        return False

    if len(out) >= 3 and out in prompt:
        return True

    return False

def completeness_violation(row):
    out = norm(row["output"])
    exp = norm(row["expected"])

    if same(out, exp):
        return False

    out_tokens = token_set(out)
    exp_tokens = token_set(exp)

    if out_tokens and out_tokens < exp_tokens:
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

    if completeness_violation(row):
        return {"gate_status": "NO_GO", "reason": "completeness_violation"}

    if entity_confusion(row):
        return {"gate_status": "NO_GO", "reason": "entity_confusion"}

    if factual_mismatch(row):
        return {"gate_status": "NO_GO", "reason": "factual_mismatch"}

    return {"gate_status": "GO", "reason": "stable_complete_match"}

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
md.append("# Real Validation V9 — Structural Completeness")
md.append("")
md.append("## Dataset")
md.append("- `examples/real_validation_v6_harder.jsonl`")
md.append("")
md.append("## Model")
md.append("- `google/flan-t5-large`")
md.append("")
md.append("## Gate change")
md.append("")
md.append("V9 extends V8 with structural completeness signals:")
md.append("")
md.append("- final-answer enforcement")
md.append("- expression detection")
md.append("- answer completeness / granularity check")
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
md.append("## Interpretation")
md.append("")
md.append("V9 tests whether structural completeness closes the failure modes identified in V8.")
md.append("")
md.append("It is not a new benchmark.")
md.append("It is a targeted correction based on observed false negatives.")
md.append("")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA V9 STRUCTURAL COMPLETENESS")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())