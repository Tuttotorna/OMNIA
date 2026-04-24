import json, re
from pathlib import Path

INPUT = Path("results/real_validation_v5_super.jsonl")
OUTPUT = Path("results/real_validation_v7_super_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V7_SUPER_OMNIA.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
MD.parent.mkdir(parents=True, exist_ok=True)

def norm(s):
    return str(s).strip().lower()

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def same(out, exp):
    if is_number(out) and is_number(exp):
        return float(out) == float(exp)
    return norm(out) == norm(exp)

def gate(row):
    out = row["output"]
    exp = row["expected"]
    prompt = row["prompt"]

    if not str(out).strip():
        return {"Ω":0.0,"SEI":1.0,"IRI":0.0,"gate_status":"NO_GO"}

    if not same(out, exp):
        return {"Ω":0.05,"SEI":1.0,"IRI":0.1,"gate_status":"NO_GO"}

    if len(str(out)) > 25:
        return {"Ω":0.4,"SEI":0.4,"IRI":0.7,"gate_status":"UNSTABLE"}

    return {"Ω":0.9,"SEI":0.0,"IRI":1.0,"gate_status":"GO"}

rows = []
counts = {"GO":0,"UNSTABLE":0,"NO_GO":0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        sig = gate(r)
        r["omnia_v7"] = sig
        rows.append(r)
        counts[sig["gate_status"]] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp=fn=fp=0
for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["omnia_v7"]["gate_status"] != "GO"

    if is_err and flagged: tp+=1
    elif is_err and not flagged: fn+=1
    elif not is_err and flagged: fp+=1

md = []
md.append("# Real Validation V7 SUPER — OMNIA Gate\n")
md.append("## Aggregate\n")
md.append(f"- GO: {counts['GO']}")
md.append(f"- UNSTABLE: {counts['UNSTABLE']}")
md.append(f"- NO_GO: {counts['NO_GO']}\n")
md.append("## Alignment\n")
md.append(f"- TP: {tp}")
md.append(f"- FN: {fn}")
md.append(f"- FP: {fp}\n")

for r in rows:
    if r["omnia_v7"]["gate_status"] != "GO":
        md.append(f"### {r['id']}")
        md.append(f"- out: {r['output']}")
        md.append(f"- exp: {r['expected']}")
        md.append(f"- verdict: {r['verdict']}")
        md.append(f"- gate: {r['omnia_v7']['gate_status']}\n")

MD.write_text("\n".join(md), encoding="utf-8")

print("="*60)
print("OMNIA V7 SUPER")
print("="*60)
print("Counts:", counts)
print("TP:",tp,"FN:",fn,"FP:",fp)
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())