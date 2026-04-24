import json
from pathlib import Path

INPUT = Path("results/real_validation_v6_harder_flan_large_results.jsonl")
OUTPUT = Path("results/real_validation_v8_flan_large_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V8_FLAN_LARGE_OMNIA.md")

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

def entity_confusion(row):
    prompt = norm(row["prompt"])
    out = norm(row["output"])
    exp = norm(row["expected"])

    if out == exp:
        return False

    if row["task"] in ("qa", "rag"):
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
        return {"gate_status": "NO_GO", "reason": "empty_output"}

    if arithmetic_incoherence(row):
        return {"gate_status": "NO_GO", "reason": "arithmetic_incoherence"}

    if entity_confusion(row):
        return {"gate_status": "NO_GO", "reason": "entity_confusion"}

    if factual_mismatch(row):
        return {"gate_status": "NO_GO", "reason": "factual_mismatch"}

    return {"gate_status": "GO", "reason": "stable_match"}

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
md.append("# V8 — FLAN-T5-LARGE")
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
print("OMNIA V8 — FLAN LARGE")
print("=" * 60)
print("Counts:", counts)
print("TP:", tp, "FN:", fn, "FP:", fp, "TN:", tn)
print("Precision:", round(precision, 3), "Recall:", round(recall, 3))
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())