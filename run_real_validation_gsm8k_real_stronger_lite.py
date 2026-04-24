import json
import re
from pathlib import Path

from datasets import load_dataset
from transformers import pipeline

OUT_RESULTS = Path("results/real_validation_gsm8k_real_stronger_lite_results.jsonl")
OUT_RESULTS.parent.mkdir(parents=True, exist_ok=True)

MODEL = "google/flan-t5-large"
N = 20

def extract_expected(answer):
    m = re.search(r"####\s*(-?\d+(?:\.\d+)?)", answer)
    if m:
        return m.group(1).strip()
    nums = re.findall(r"-?\d+(?:\.\d+)?", answer)
    return nums[-1].strip() if nums else ""

def extract_final(output):
    text = str(output).strip()
    nums = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    if nums:
        return nums[-1]
    return text.split("\n")[-1].strip()

def is_number(s):
    try:
        float(str(s).replace(",", ""))
        return True
    except:
        return False

def same(a, b):
    if is_number(a) and is_number(b):
        return float(a) == float(b)
    return str(a).strip().lower() == str(b).strip().lower()

print("Loading GSM8K...")
ds = load_dataset("gsm8k", "main", split=f"test[:{N}]")

pipe = pipeline("text2text-generation", model=MODEL, max_new_tokens=96)

rows = []
correct = 0

for i, item in enumerate(ds):
    prompt = "Answer with only the final number. " + item["question"]
    expected = extract_expected(item["answer"])

    raw = pipe(prompt, do_sample=False)[0]["generated_text"]
    final = extract_final(raw)

    ok = same(final, expected)

    row = {
        "id": f"gsm8k_real_{i:03d}",
        "model": MODEL,
        "prompt": prompt,
        "raw_output": raw,
        "output": final,
        "expected": expected,
        "correct": ok,
        "verdict": "correct" if ok else "semantic_error"
    }

    rows.append(row)
    if ok:
        correct += 1

    print(row)

with open(OUT_RESULTS, "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

print("\n=== SUMMARY ===")
print(f"Correct: {correct}/{N}")
print(f"Accuracy: {correct/N:.3f}")