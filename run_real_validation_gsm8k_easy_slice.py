import json
import re
from pathlib import Path

from datasets import load_dataset
from transformers import pipeline

OUT_RESULTS = Path("results/real_validation_gsm8k_easy_slice_results.jsonl")
OUT_RESULTS.parent.mkdir(parents=True, exist_ok=True)

MODEL = "google/flan-t5-large"
TARGET = 20

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

def is_easy(q):
    # euristica: operazioni semplici senza condizioni complesse
    q = q.lower()
    keywords = ["total", "sum", "how many", "in total", "altogether"]
    ops = len(re.findall(r"\d+", q))
    return any(k in q for k in keywords) and ops <= 3

print("Loading GSM8K...")
ds = load_dataset("gsm8k", "main", split="test")

pipe = pipeline("text2text-generation", model=MODEL, max_new_tokens=96)

rows = []
correct = 0
count = 0

for item in ds:
    if count >= TARGET:
        break

    q = item["question"]
    if not is_easy(q):
        continue

    prompt = "Answer with only the final number. " + q
    expected = extract_expected(item["answer"])

    raw = pipe(prompt, do_sample=False)[0]["generated_text"]
    final = extract_final(raw)

    ok = same(final, expected)

    row = {
        "id": f"gsm8k_easy_{count:03d}",
        "model": MODEL,
        "prompt": prompt,
        "output": final,
        "expected": expected,
        "correct": ok,
        "verdict": "correct" if ok else "semantic_error"
    }

    rows.append(row)
    if ok:
        correct += 1

    print(row)
    count += 1

with open(OUT_RESULTS, "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

print("\n=== SUMMARY ===")
print(f"Correct: {correct}/{count}")
print(f"Accuracy: {correct/count:.3f}")