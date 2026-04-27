# ============================================================
# OMNIA — REAL OUTPUTS STRUCTURAL EVALUATION V1
# ============================================================

import json
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH = Path("results/real_structural_analysis_v1.json")


def features(text):
    tokens = text.split()
    length = len(tokens)

    digits = sum(c.isdigit() for c in text)
    symbols = sum(not c.isalnum() and not c.isspace() for c in text)

    total_chars = max(len(text), 1)

    digit_density = digits / total_chars
    symbol_density = symbols / total_chars

    malformed = sum(1 for t in tokens if not t.isalnum())

    return {
        "length": length,
        "digit_density": digit_density,
        "symbol_density": symbol_density,
        "malformed": malformed,
    }


def classify(f):
    if f["length"] <= 2:
        return "atomic"

    if f["length"] <= 8:
        return "short"

    return "long"


def run():
    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            text = item["text"]

            fts = features(text)
            label = classify(fts)

            rows.append({
                "id": item["id"],
                "prompt": item["prompt"],
                "text": text,
                "label": label,
                **fts
            })

    return rows


def summarize(rows):
    counts = {"atomic": 0, "short": 0, "long": 0}

    for r in rows:
        counts[r["label"]] += 1

    total = len(rows)

    ratios = {k: v / total for k, v in counts.items()}

    return {
        "total": total,
        "counts": counts,
        "ratios": ratios
    }


def main():
    rows = run()
    summary = summarize(rows)

    print("\n=== REAL STRUCTURAL ANALYSIS ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample rows:")
    for r in rows[:10]:
        print(
            f"{r['label']:6s} | "
            f"len={r['length']:2d} "
            f"dig={r['digit_density']:.3f} "
            f"sym={r['symbol_density']:.3f} "
            f"mal={r['malformed']} | "
            f"{r['text'][:80]}"
        )

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "rows": rows
        }, f, indent=2, ensure_ascii=False)

    print("\nSaved:")
    print("-", OUTPUT_PATH)


if __name__ == "__main__":
    main()

