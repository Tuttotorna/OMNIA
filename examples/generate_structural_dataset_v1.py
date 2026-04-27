# ============================================================
# OMNIA — STRUCTURAL DATASET GENERATOR V1
# ============================================================

import json
import random
from pathlib import Path

OUTPUT_PATH = Path("data/structural_dataset_v1.jsonl")
OUTPUT_PATH.parent.mkdir(exist_ok=True)

# -------------------------
# BASE PROMPTS
# -------------------------

PROMPTS = [
    "Solve: 27 * 14.",
    "What is 2 + 2?",
    "Return a valid JSON with keys name and age.",
    "Explain why the sky is blue.",
    "Give a short answer: 100/4.",
    "Write a Python function that reverses a string.",
    "What is the capital of France?",
    "Define entropy in one sentence.",
    "Sort this list: [5,2,9,1].",
]

# -------------------------
# GENERATORS
# -------------------------

def good_answer(prompt):
    return {
        "type": "good",
        "text": "The answer is 42."
    }

def atomic_bad():
    tokens = ["LDL", "B", "X9Z", "K", "A12B"]
    return {
        "type": "atomic",
        "text": random.choice(tokens)
    }

def short_bad():
    patterns = [
        "6 * 16 * 11* 9) *",
        "15 numbers! (Courp 0!",
        "1532 cut. S",
        "9 = 25",
        "3// + 1-"
    ]
    return {
        "type": "short",
        "text": random.choice(patterns)
    }

def long_bad():
    patterns = [
        "120 (23.36). 1035 [16.59+112], 17.51-635 181 912 1927.",
        "No 3 or None 7, but 1/1 or 2 * No 2. So who says two is 3/2?",
        "This system generates numbers 1 2 3 4 and continues in patterns that do not converge.",
        "The output may contain inconsistencies where 5 becomes 7 and later returns to 3."
    ]
    return {
        "type": "long",
        "text": random.choice(patterns)
    }

# -------------------------
# MAIN
# -------------------------

def generate(n=200):
    rows = []

    for i in range(n):
        prompt = random.choice(PROMPTS)

        mode = random.choice(["good", "atomic", "short", "long"])

        if mode == "good":
            sample = good_answer(prompt)
        elif mode == "atomic":
            sample = atomic_bad()
        elif mode == "short":
            sample = short_bad()
        else:
            sample = long_bad()

        rows.append({
            "id": f"{i:04d}",
            "prompt": prompt,
            "label": sample["type"],
            "text": sample["text"]
        })

    return rows

def save(rows):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def main():
    rows = generate(300)
    save(rows)

    print("Saved:", OUTPUT_PATH)
    print("Total rows:", len(rows))

if __name__ == "__main__":
    main()