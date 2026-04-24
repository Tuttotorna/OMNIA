import json
from pathlib import Path
from transformers import pipeline

DATASET = Path("examples/real_validation_v3_dataset_expanded.jsonl")
OUT = Path("results/real_validation_v4_super.jsonl")

OUT.parent.mkdir(parents=True, exist_ok=True)

# modello robusto (istruzione)
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=32
)

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

        verdict = "correct" if out == expected else "semantic_error"

        if verdict == "correct":
            correct += 1
        total += 1

        row = {
            "id": r["id"],
            "task": r["task"],
            "prompt": prompt,
            "output": out,
            "expected": expected,
            "verdict": verdict,
            "correct": verdict == "correct"
        }

        rows.append(row)
        print(row)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("="*60)
print("VALIDATION V4 SUPER")
print("="*60)
print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")
print("Saved:", OUT.resolve())