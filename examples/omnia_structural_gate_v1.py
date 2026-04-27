# ============================================================
# OMNIA — STRUCTURAL GATE V1
# ============================================================
#
# Purpose:
# Apply a minimal structural gate to real local-model outputs.
#
# Input:
# data/real_structural_dataset_v1.jsonl
#
# Output:
# results/omnia_structural_gate_v1.json
#
# Gate values:
# - PASS
# - REVIEW
# - REJECT
#
# ============================================================

import json
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH = Path("results/omnia_structural_gate_v1.json")


def features(text):
    tokens = text.split()
    length = len(tokens)

    digits = sum(c.isdigit() for c in text)
    symbols = sum(not c.isalnum() and not c.isspace() for c in text)

    total_chars = max(len(text), 1)

    digit_density = digits / total_chars
    symbol_density = symbols / total_chars
    malformed = sum(1 for token in tokens if not token.isalnum())

    return {
        "length": length,
        "digit_density": digit_density,
        "symbol_density": symbol_density,
        "malformed": malformed,
    }


def classify(feature_row):
    if feature_row["length"] <= 2:
        return "atomic"

    if feature_row["length"] <= 8:
        return "short"

    return "long"


def gate_decision(feature_row, structural_class):
    if structural_class == "atomic":
        return "REJECT"

    if structural_class == "short":
        if feature_row["malformed"] > 0 or feature_row["symbol_density"] > 0.15:
            return "REVIEW"
        return "PASS"

    if structural_class == "long":
        if (
            feature_row["digit_density"] > 0.20
            or feature_row["symbol_density"] > 0.20
            or feature_row["malformed"] > 3
        ):
            return "REVIEW"
        return "PASS"

    return "PASS"


def run():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(INPUT_PATH)

    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            text = item["text"]

            feature_row = features(text)
            structural_class = classify(feature_row)
            decision = gate_decision(feature_row, structural_class)

            rows.append({
                "id": item["id"],
                "prompt": item["prompt"],
                "text": text,
                "class": structural_class,
                "gate": decision,
                **feature_row,
            })

    return rows


def summarize(rows):
    gate_counts = {
        "PASS": 0,
        "REVIEW": 0,
        "REJECT": 0,
    }

    class_counts = {
        "atomic": 0,
        "short": 0,
        "long": 0,
    }

    for row in rows:
        gate_counts[row["gate"]] += 1
        class_counts[row["class"]] += 1

    total = len(rows)

    return {
        "total": total,
        "gate_counts": gate_counts,
        "gate_ratios": {
            key: value / total for key, value in gate_counts.items()
        },
        "class_counts": class_counts,
        "class_ratios": {
            key: value / total for key, value in class_counts.items()
        },
    }


def main():
    rows = run()
    summary = summarize(rows)

    print("\n=== OMNIA STRUCTURAL GATE V1 ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample decisions:")
    for row in rows[:15]:
        print(
            f"{row['gate']:6s} | "
            f"{row['class']:6s} | "
            f"len={row['length']:2d} "
            f"dig={row['digit_density']:.3f} "
            f"sym={row['symbol_density']:.3f} "
            f"mal={row['malformed']} | "
            f"{row['text'][:90]}"
        )

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "rows": rows,
        }, f, indent=2, ensure_ascii=False)

    print("\nSaved:")
    print("-", OUTPUT_PATH)


if __name__ == "__main__":
    main()