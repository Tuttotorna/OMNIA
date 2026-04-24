import json
import re
from pathlib import Path

from datasets import load_dataset
from transformers import pipeline

OUT_DATA = Path("examples/gsm8k_real_slice.jsonl")
OUT_RESULTS = Path("results/real_validation_gsm8k_real_stronger_results.jsonl")

OUT_DATA.parent.mkdir(parents=True, exist_ok=True)
OUT_RESULTS.parent.mkdir(parents=True, exist_ok=True)

MODEL = "google/flan-t5-xl"
N = 20

def extract_expected(answer):
    m = re.search(r"####\s*(-?\d+(?:\.\d+)?)", answer)
    if m:
        return m.group(1).strip()
    nums = re.findall(r"-?\d+(?:\.\d+)?", answer)
    return nums[-1].strip() if nums else ""

def norm(s):
    return str(s).strip().lower()

def clean_number(s):
    return str(s).strip().replace(",", "")

def is_number(s):
    try:
        float(clean_number(s))
        return True
    except Exception:
        return False

def correct_match(out, exp):
    if is_number(out) and is_number(exp):
        return float(clean_number(out)) == float(clean_number(exp))
    return norm(out) == norm(exp)

def extract_final(output):
    text = str(output).strip()
    nums = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    if nums:
        return nums[-1]
    return text.split("\n")[-1].strip()

print("Loading GSM8K real dataset...")
ds = load_dataset("gsm8k", "main", split=f"test[:{N}]")

dataset_rows = []
for i, item in enumerate(ds):
    expected = extract_expected(item["answer"])
    prompt = "Answer with only the final number. " + item["question"]

    dataset_rows.append({
        "id": f"gsm8k_real_{i:03d}",
        "task": "reasoning",
        "source": "gsm8k",
        "prompt": prompt,
        "expected": expected,
    })

with open(OUT_DATA, "w", encoding="utf-8") as f:
    for r in dataset_rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("Saved dataset:", OUT_DATA.resolve())

pipe = pipeline(
    "text2text-generation",
    model=MODEL,
    max_new_tokens=96,
)

rows = []
correct = 0
total = 0

for r in dataset_rows:
    prompt = r["prompt"]
    expected = r["expected"]

    try:
        raw = pipe(prompt, do_sample=False)[0]["generated_text"]
        final = extract_final(raw)
    except Exception as e:
        raw = f"ERROR: {e}"
        final = ""

    is_correct = correct_match(final, expected)
    verdict = "correct" if is_correct else "semantic_error"

    row = {
        "id": r["id"],
        "task": r["task"],
        "source": r["source"],
        "model": MODEL,
        "prompt": prompt,
        "raw_output": raw,
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

with open(OUT_RESULTS, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("=" * 60)
print("GSM8K REAL SLICE — STRONGER MODEL")
print("=" * 60)
print("Model:", MODEL)
print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total:.3f}")
print("Saved:", OUT_RESULTS.resolve())