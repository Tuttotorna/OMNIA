import json
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DATA = Path("examples/real_validation_v3_dataset_expanded.jsonl")
OUT = Path("results/real_validation_v3_expanded_results.jsonl")

OUT.parent.mkdir(parents=True, exist_ok=True)

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    ids = model.generate(
        **inputs,
        max_new_tokens=16,
        do_sample=False,
    )
    return tokenizer.decode(ids[0], skip_special_tokens=True).strip()

rows = []
with DATA.open(encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        r = json.loads(line)
        out = generate(r["prompt"])
        correct = out == r["expected"]
        verdict = "correct" if correct else "semantic_error"

        rows.append({
            "id": r["id"],
            "task": r["task"],
            "prompt": r["prompt"],
            "output": out,
            "expected": r["expected"],
            "verdict": verdict,
            "correct": correct,
        })

with OUT.open("w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("="*60)
print("VALIDATION V3 EXPANDED")
print("="*60)

correct = sum(1 for r in rows if r["correct"])
total = len(rows)

print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")

print("\nSample:")
for r in rows[:10]:
    print(r)

print("\nSaved:", OUT)