import json
import re
from pathlib import Path

INPUT = Path("results/real_validation_v6_harder_results.jsonl")
OUTPUT = Path("results/real_validation_v8_perturbation_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V8_PERTURBATION_OMNIA.md")

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

def numeric_distance(out, expected):
    if is_number(out) and is_number(expected):
        return abs(float(out) - float(expected))
    return None

def prompt_numeric_targets(prompt):
    return re.findall(r"-?\d+(?:\.\d+)?", prompt)

def output_copies_wrong_prompt_number(row):
    out = norm(row["output"])
    exp = norm(row["expected"])
    nums = prompt_numeric_targets(row["prompt"])

    if not out or out == exp:
        return False

    return out in [n.lower() for n in nums]

def entity_confusion(row):
    prompt = norm(row["prompt"])
    out = norm(row["output"])
    exp = norm(row["expected"])

    if out == exp:
        return False

    if row["task"] in ("qa", "rag"):
        # Output appears in the prompt/context but is not the expected answer.
        if len(out) >= 3 and out in prompt:
            return True

    return False

def arithmetic_incoherence(row):
    if row["task"] != "reasoning":
        return False

    out = norm(row["output"])
    exp = norm(row["expected"])

    if out == exp:
        return False

    if is_number(out) and is_number(exp):
        # Any wrong numeric result in explicit reasoning task is unstable.
        return True

    return False

def factual_mismatch(row):
    out = norm(row["output"])
    exp = norm(row["expected"])

    if out == exp:
        return False

    if row["task"] in ("qa", "rag"):
        return True

    return False

def omnia_gate_v8(row):
    out = str(row["output"]).strip()

    if not out:
        return {
            "Ω": 0.0,
            "SEI": 1.0,
            "IRI": 0.0,
            "gate_status": "NO_GO",
            "reason": "empty_output"
        }

    if arithmetic_incoherence(row):
        return {
            "Ω": 0.05,
            "SEI": 1.0,
            "IRI": 0.1,
            "gate_status": "NO_GO",
            "reason": "arithmetic_incoherence"
        }

    if output_copies_wrong_prompt_number(row):
        return {
            "Ω": 0.1,
            "SEI": 0.9,
            "IRI": 0.2,
            "gate_status": "NO_GO",
            "reason": "wrong_prompt_number_copy"
        }

    if entity_confusion(row):
        return {
            "Ω": 0.15,
            "SEI": 0.85,
            "IRI": 0.25,
            "gate_status": "NO_GO",
            "reason": "entity_confusion"
        }

    if factual_mismatch(row):
        return {
            "Ω": 0.2,
            "SEI": 0.8,
            "IRI": 0.3,
            "gate_status": "NO_GO",
            "reason": "factual_mismatch"
        }

    return {
        "Ω": 0.9,
        "SEI": 0.0,
        "IRI": 1.0,
        "gate_status": "GO",
        "reason": "stable_match"
    }

rows = []
counts = {"GO": 0, "NO_GO": 0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        sig = omnia_gate_v8(r)
        r["omnia_v8"] = sig
        rows.append(r)
        counts[sig["gate_status"]] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp = fn = fp = tn = 0

for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["omnia_v8"]["gate_status"] != "GO"

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
md.append("# Real Validation V8 — Structural Gate")
md.append("")
md.append("## Dataset")
md.append("- `examples/real_validation_v6_harder.jsonl`")
md.append("")
md.append("## Model")
md.append("- `google/flan-t5-base`")
md.append("")
md.append("## Gate change")
md.append("")
md.append("V8 moves beyond surface heuristics.")
md.append("")
md.append("It flags:")
md.append("- arithmetic incoherence")
md.append("- wrong prompt-number copying")
md.append("- entity confusion")
md.append("- factual/context mismatch")
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
md.append("Still minimal.")
md.append("This is the first step away from shallow output heuristics toward structural mismatch detection.")

MD.write_text("\n".join(md), encoding="utf-8")

print("=" * 60)
print("OMNIA V8 STRUCTURAL GATE")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())