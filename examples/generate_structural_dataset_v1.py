# ============================================================
# OMNIA — STRUCTURAL DATASET GENERATOR V1
# ============================================================
#
# Purpose:
# Generate a synthetic structural dataset for tri-channel evaluation.
#
# Labels are structural classes, not semantic correctness labels.
#
# Classes:
# - good   -> structurally stable / well-formed output
# - atomic -> atomic malformed / near-empty / token-level collapse
# - short  -> short malformed output
# - long   -> long incoherent / extended structural degradation
#
# ============================================================

import json
import random
from pathlib import Path

OUTPUT_PATH = Path("data/structural_dataset_v1.jsonl")
OUTPUT_PATH.parent.mkdir(exist_ok=True)


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


def good_answer():
    return random.choice([
        "The answer is 42.",
        "Paris is the capital of France.",
        "The output is valid JSON.",
        "The list is [1, 2, 5, 9].",
        "Entropy is a measure of uncertainty or disorder.",
    ])


def atomic_bad():
    return random.choice([
        "LDL",
        "B",
        "X9Z",
        "K",
        "A12B",
        "VEPSEINET",
        "leukdd1g9Aef",
        "inorganization",
    ])


def short_bad():
    return random.choice([
        "6 * 16 * 11* 9) *",
        "15 numbers! (Courp 0!",
        "1532 cut. S",
        "9 = 25",
        "3// + 1-",
        "25-208'ing 8",
        "15A",
        "23!",
    ])


def long_bad():
    return random.choice([
        "120 (23.36). 1035 [16.59+112], 17.51-635 181 912 1927.",
        "No 3 or None 7, but 1/1 or 2 * No 2. So who says two is 3/2?",
        "This system generates numbers 1 2 3 4 and continues in patterns that do not converge.",
        "The output may contain inconsistencies where 5 becomes 7 and later returns to 3.",
        "4.74 73.6 67.2 224.4 1.57 16.99 324.1.11 16.48 30.",
        "The sky is blue because numbers rotate through 17 and syntax dissolves into unrelated fragments.",
    ])


def generate(n=300, seed=42):
    random.seed(seed)
    rows = []

    for i in range(n):
        prompt = random.choice(PROMPTS)
        label = random.choice(["good", "atomic", "short", "long"])

        if label == "good":
            text = good_answer()
        elif label == "atomic":
            text = atomic_bad()
        elif label == "short":
            text = short_bad()
        else:
            text = long_bad()

        rows.append({
            "id": f"{i:04d}",
            "prompt": prompt,
            "label": label,
            "text": text,
        })

    return rows


def main():
    rows = generate()

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    counts = {}
    for row in rows:
        counts[row["label"]] = counts.get(row["label"], 0) + 1

    print("Saved:", OUTPUT_PATH)
    print("Total:", len(rows))
    print("Counts:", counts)


if __name__ == "__main__":
    main()