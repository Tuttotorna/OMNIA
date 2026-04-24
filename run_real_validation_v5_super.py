import json
from pathlib import Path
from transformers import pipeline

DATASET = Path("examples/real_validation_v3_dataset_expanded.jsonl")
OUT = Path("results/real_validation_v5_super.jsonl")

OUT.parent.mkdir(parents=True, exist_ok=True)

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=32
)

def norm(s):
    return str(s).strip().lower()

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def correct_match(out, exp):
    # numerico → confronto numerico
    if is_number(out) and is_number(exp):
        return float(out) == float(exp)

    # testuale → case insensitive
    return norm(out) == norm(exp)

rows = []
correct = 0
total = 0

with open(DATASET, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)

        prompt = r["prompt"]
        expected = r["expected"]

        try:
            out = pipe(prompt)[0]["generated_text"].strip()
        except Exception:
            out = ""

        is_ok = correct_match(out, expected)
        verdict = "correct" if is_ok else "semantic_error"

        if is_ok:
            correct += 1
        total += 1

        row = {
            "id": r["id"],
            "task": r["task"],
            "prompt": prompt,
            "output": out,
            "expected": expected,
            "verdict": verdict,
            "correct": is_ok
        }

        rows.append(row)
        print(row)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("="*60)
print("VALIDATION V5 SUPER (FIXED)")
print("="*60)
print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")
print("Saved:", OUT.resolve())