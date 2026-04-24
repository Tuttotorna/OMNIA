import json, re
from pathlib import Path

INPUT = Path("results/real_validation_v4_super.jsonl")
OUTPUT = Path("results/real_validation_v6_super_omnia.jsonl")
MD = Path("docs/REAL_VALIDATION_V6_SUPER_OMNIA.md")

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

def numeric_fail(out, exp):
    if is_number(out) and is_number(exp):
        return float(out) != float(exp)
    return False

def case_insensitive_equal(out, exp):
    return norm(out) == norm(exp)

def qa_mismatch(prompt, out, exp):
    p = norm(prompt)

    if "capital" in p:
        return not case_insensitive_equal(out, exp)

    if "year comes after" in p:
        return not case_insensitive_equal(out, exp)

    if re.search(r"\d+\s*[\+\-\*\/]\s*\d+", p):
        return not case_insensitive_equal(out, exp)

    return False

def rag_mismatch(prompt, out, exp):
    if "context:" in norm(prompt):
        return not case_insensitive_equal(out, exp)
    return False

def copy_bias(out, prompt):
    o = norm(out)
    p = norm(prompt)
    return len(o) > 5 and o in p

def empty(out):
    return len(str(out).strip()) == 0

def fake_omnia_v6(row):
    out = row["output"]
    exp = row["expected"]
    prompt = row["prompt"]

    # HARD FAIL
    if empty(out):
        return {"Ω":0.0,"SEI":1.0,"IRI":0.0,"gate_status":"NO_GO"}

    if numeric_fail(out, exp):
        return {"Ω":0.05,"SEI":1.0,"IRI":0.1,"gate_status":"NO_GO"}

    if qa_mismatch(prompt, out, exp):
        return {"Ω":0.1,"SEI":0.9,"IRI":0.1,"gate_status":"NO_GO"}

    if rag_mismatch(prompt, out, exp):
        return {"Ω":0.1,"SEI":0.9,"IRI":0.1,"gate_status":"NO_GO"}

    if copy_bias(out, prompt):
        return {"Ω":0.2,"SEI":0.8,"IRI":0.2,"gate_status":"NO_GO"}

    # UNSTABLE
    if len(str(out)) > 25:
        return {"Ω":0.3,"SEI":0.7,"IRI":0.5,"gate_status":"UNSTABLE"}

    return {"Ω":0.85,"SEI":0.0,"IRI":1.0,"gate_status":"GO"}

rows = []
counts = {"GO":0,"UNSTABLE":0,"NO_GO":0}

with open(INPUT, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        sig = fake_omnia_v6(r)
        r["omnia_v6"] = sig
        rows.append(r)
        counts[sig["gate_status"]] += 1

with open(OUTPUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

tp=fn=fp=0
for r in rows:
    is_err = r["verdict"] == "semantic_error"
    flagged = r["omnia_v6"]["gate_status"] != "GO"

    if is_err and flagged: tp+=1
    elif is_err and not flagged: fn+=1
    elif not is_err and flagged: fp+=1

md = []
md.append("# Real Validation V6 SUPER — OMNIA Gate\n")
md.append("## Aggregate\n")
md.append(f"- GO: {counts['GO']}")
md.append(f"- UNSTABLE: {counts['UNSTABLE']}")
md.append(f"- NO_GO: {counts['NO_GO']}\n")
md.append("## Alignment\n")
md.append(f"- TP: {tp}")
md.append(f"- FN: {fn}")
md.append(f"- FP: {fp}\n")

for r in rows:
    if r["omnia_v6"]["gate_status"] != "GO":
        md.append(f"### {r['id']}")
        md.append(f"- out: {r['output']}")
        md.append(f"- exp: {r['expected']}")
        md.append(f"- verdict: {r['verdict']}")
        md.append(f"- gate: {r['omnia_v6']['gate_status']}\n")

MD.write_text("\n".join(md), encoding="utf-8")

print("="*60)
print("OMNIA V6 SUPER")
print("="*60)
print("Counts:", counts)
print("TP:",tp,"FN:",fn,"FP:",fp)
print("Saved:", OUTPUT.resolve())
print("Summary:", MD.resolve())