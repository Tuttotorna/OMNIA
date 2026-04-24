import json
from transformers import pipeline

DATA_PATH = "examples/gsm8k_balanced_v1.jsonl"
OUT_PATH = "results/real_validation_balanced_v1_results.jsonl"

pipe = pipeline("text2text-generation", model="google/flan-t5-large")

def extract_number(text):
    import re
    nums = re.findall(r"-?\d+\.?\d*", text)
    return nums[-1] if nums else text.strip()

results = []

with open(DATA_PATH, "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)

        out = pipe(item["prompt"], max_new_tokens=50)[0]["generated_text"]
        pred = extract_number(out)

        correct = (pred == item["expected"])

        res = {
            "id": item["id"],
            "task": item["task"],
            "difficulty": item["difficulty"],
            "model": "google/flan-t5-large",
            "prompt": item["prompt"],
            "raw_output": out,
            "output": pred,
            "expected": item["expected"],
            "correct": correct,
            "verdict": "correct" if correct else "semantic_error"
        }

        print(res)
        results.append(res)

with open(OUT_PATH, "w", encoding="utf-8") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

acc = sum(r["correct"] for r in results)
print("\n=== SUMMARY ===")
print(f"Correct: {acc}/20")
print(f"Accuracy: {acc/20:.3f}")