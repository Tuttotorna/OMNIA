# ============================================================
# OMNIA — REAL OUTPUTS DATASET GENERATOR V1
# ============================================================
#
# Purpose:
# Generate a dataset of REAL model outputs (not synthetic)
#
# Output:
# data/real_structural_dataset_v1.jsonl
#
# NOTE:
# - No labels
# - Raw outputs only
# - Structural analysis happens later
#
# ============================================================

import json
from pathlib import Path

from transformers import pipeline

OUTPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH.parent.mkdir(exist_ok=True)

# ------------------------------------------------------------
# PROMPTS (REAL TASKS)
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# MODEL
# ------------------------------------------------------------

def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small"
    )

# ------------------------------------------------------------
# GENERATION
# ------------------------------------------------------------

def generate_outputs(generator, n_per_prompt=5):
    rows = []
    idx = 0

    for prompt in PROMPTS:
        for _ in range(n_per_prompt):
            try:
                out = generator(prompt, max_length=64, do_sample=True)[0]["generated_text"]
            except Exception as e:
                out = f"ERROR: {str(e)}"

            rows.append({
                "id": f"{idx:04d}",
                "prompt": prompt,
                "text": out
            })

            idx += 1

    return rows

# ------------------------------------------------------------
# SAVE
# ------------------------------------------------------------

def save(rows):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

def main():
    print("Loading model...")
    generator = load_model()

    print("Generating outputs...")
    rows = generate_outputs(generator, n_per_prompt=5)

    save(rows)

    print("Saved:", OUTPUT_PATH)
    print("Total rows:", len(rows))


if __name__ == "__main__":
    main()