# ============================================================
# OMNIA — REAL OUTPUTS DATASET GENERATOR V1
# ============================================================
#
# Purpose:
# Generate a dataset of real model outputs using a local model.
#
# Output:
# data/real_structural_dataset_v1.jsonl
#
# Notes:
# - No labels
# - Raw model outputs only
# - Structural analysis happens later
#
# ============================================================

import json
from pathlib import Path

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

OUTPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH.parent.mkdir(exist_ok=True)

PROMPTS = [
    "What is 2 + 2?",
    "Solve: 27 * 14.",
    "Explain why the sky is blue.",
    "Give a short answer: 100/4.",
    "Write a Python function that reverses a string.",
    "Return a valid JSON with keys name and age.",
    "What is the capital of France?",
    "Define entropy in one sentence.",
    "Sort this list: [5,2,9,1].",
    "What is the largest planet?",
    "Explain photosynthesis in two sentences.",
    "Write a one-line answer: 9*9.",
]


def main():
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    rows = []
    idx = 0

    print("Generating outputs...")

    for prompt in PROMPTS:
        for _ in range(5):
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(
                **inputs,
                max_new_tokens=64,
                do_sample=True,
                temperature=0.7,
            )

            text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            rows.append({
                "id": f"{idx:04d}",
                "prompt": prompt,
                "text": text,
            })

            idx += 1

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print("Saved:", OUTPUT_PATH)
    print("Total rows:", len(rows))

    print("\nPreview:")
    for row in rows[:10]:
        print(json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()