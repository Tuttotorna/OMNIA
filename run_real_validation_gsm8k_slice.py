import json
from pathlib import Path
from transformers import pipeline

DATA = Path("examples/gsm8k_slice_omnia.jsonl")
OUT = Path("results/real_validation_gsm8k_slice_results.jsonl")

OUT.parent.mkdir(parents=True, exist_ok=True)

MODEL = "google/flan-t5-large"

pipe = pipeline(
    "text2text-generation",
    model=MODEL,
    max_new_tokens=32,
)

def norm(s):
    return str(s).strip().lower()

def is_number(s):
    try:
        float(str(s).strip())
        return True
    except Exception:
        return False

def correct_match(out, exp):
    if is_number(out) and is_number(exp):
        return float(out) == float(exp)
    return norm(out) == norm(exp)

def extract_final(output):
    return str(output).strip().split("\n")[-1].strip()

rows = []
correct = 0
total = 0

with open(DATA, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        prompt = r["prompt"]
        expected = r["expected"]

        try:
            res = pipe(prompt, do_sample=False)[0]["generated_text"]
            final = extract_final(res)
        except Exception:
            final = ""

        is_correct = correct_match(final, expected)
        verdict = "correct" if is_correct else "semantic_error"

        row = {
            "id": r["id"],
            "task": r["task"],
            "model": MODEL,
            "prompt": prompt,
            "output": final,
            "expected": expected,
            "verdict": verdict,
            "correct": is_correct,
        }

        rows.append(row)
        total += 1
        if is_correct:
            correct += 1

        print(row)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("=" * 60)
print("GSM8K SLICE — FLAN-T5-LARGE")
print("=" * 60)
print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")
print("Saved:", OUT.resolve())