# ============================================================
# OMNIA — REAL OUTPUTS EVALUATION V1
# ============================================================
#
# Purpose:
# Apply tri-channel structural analysis to real outputs
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
        1 for t in tokens if any(c.isdigit() for c in t) and any(c.isalpha() for c in t)
    )

    return {
        "length": len(tokens),
        "digit_density": digits / max(len(text), 1),
        "symbol_density": symbols / max(len(text), 1),
        "malformed": malformed_tokens,
    }


def classify(f):
    if f["length"] <= 2:
        return "atomic"

    if f["length"] <= 8:
        return "short"

    return "long"


def main():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(INPUT_PATH)

    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))

    results = []
    counts = {"atomic": 0, "short": 0, "long": 0}

    for r in rows:
        f = features(r["text"])
        cls = classify(f)

        counts[cls] += 1

        results.append({
            "id": r["id"],
            "prompt": r["prompt"],
            "text": r["text"],
            "class": cls,
            **f
        })

    total = len(results)

    summary = {
        "total": total,
        "counts": counts,
        "ratios": {k: v / total for k, v in counts.items()}
    }

    print("\n=== REAL STRUCTURAL ANALYSIS ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample rows:")
    for r in results[:10]:
        print(
            f"{r['class']:6s} | "
            f"len={r['length']:2d} "
            f"dig={r['digit_density']:.3f} "
            f"sym={r['symbol_density']:.3f} "
            f"mal={r['malformed']} | "
            f"{r['text'][:80]}"
        )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "results": results
        }, f, indent=2, ensure_ascii=False)

    print("\nSaved:", OUTPUT_PATH)


if __name__ == "__main__":
    main()