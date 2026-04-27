# ============================================================
# OMNIA — REAL OUTPUTS EVALUATION V1
# ============================================================
#
# Purpose:
# Apply tri-channel structural analysis to real local-model outputs.
#
# Input:
# data/real_structural_dataset_v1.jsonl
#
# Output:
# results/real_structural_analysis_v1.json
#
# ============================================================

import json
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH = Path("results/real_structural_analysis_v1.json")
OUTPUT_PATH.parent.mkdir(exist_ok=True)


def features(text):
    tokens = text.split()

    digits = sum(c.isdigit() for c in text)
    symbols = sum((not c.isalnum() and not c.isspace()) for c in text)

    malformed_tokens = sum(
        1
        for token in tokens
        if any(c.isdigit() for c in token) and any(c.isalpha() for c in token)
    )

    return {
        "length": len(tokens),
        "digit_density": digits / max(len(text), 1),
        "symbol_density": symbols / max(len(text), 1),
        "malformed": malformed_tokens,
    }


def classify(feature_row):
    if feature_row["length"] <= 2:
        return "atomic"

    if feature_row["length"] <= 8:
        return "short"

    return "long"


def main():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(INPUT_PATH)

    rows = [
        json.loads(line)
        for line in INPUT_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    results = []
    counts = {
        "atomic": 0,
        "short": 0,
        "long": 0,
    }

    for row in rows:
        feature_row = features(row["text"])
        structural_class = classify(feature_row)

        counts[structural_class] += 1

        results.append({
            "id": row["id"],
            "prompt": row["prompt"],
            "text": row["text"],
            "class": structural_class,
            **feature_row,
        })

    total = len(results)

    summary = {
        "total": total,
        "counts": counts,
        "ratios": {
            key: value / total for key, value in counts.items()
        },
    }

    print("\n=== REAL STRUCTURAL ANALYSIS ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample rows:")
    for row in results[:10]:
        print(
            f"{row['class']:6s} | "
            f"len={row['length']:2d} "
            f"dig={row['digit_density']:.3f} "
            f"sym={row['symbol_density']:.3f} "
            f"mal={row['malformed']} | "
            f"{row['text'][:80]}"
        )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(
            {
                "summary": summary,
                "results": results,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("\nSaved:", OUTPUT_PATH)


if __name__ == "__main__":
    main()