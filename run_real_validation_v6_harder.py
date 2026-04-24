import json
from pathlib import Path
from transformers import pipeline

DATA = Path("examples/real_validation_v6_harder.jsonl")
OUT = Path("results/real_validation_v6_harder_results.jsonl")

OUT.parent.mkdir(parents=True, exist_ok=True)

pipe = pipeline("text2text-generation", model="google/flan-t5-base")

def extract_final(output):
    return output.strip().split("\n")[-1].strip()

rows = []
correct = 0
total = 0

with open(DATA, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        prompt = r["prompt"]

        res = pipe(prompt, max_new_tokens=32, do_sample=False)[0]["generated_text"]
        final = extract_final(res)

        expected = r["expected"]

        is_correct = final == expected
        verdict = "correct" if is_correct else "semantic_error"

        out_row = {
            "id": r["id"],
            "task": r["task"],
            "prompt": prompt,
            "output": final,
            "expected": expected,
            "verdict": verdict,
            "correct": is_correct
        }

        rows.append(out_row)

        total += 1
        if is_correct:
            correct += 1

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("=" * 60)
print("VALIDATION V6 HARDER")
print("=" * 60)
print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")
print("Saved:", OUT.resolve())