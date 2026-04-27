# ============================================================
# OMNIA — STRUCTURAL GATE V1
# ============================================================

import json
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
OUTPUT_PATH = Path("results/omnia_structural_gate_v1.json")


# -----------------------------
# FEATURE EXTRACTION
# -----------------------------
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


# -----------------------------
# STRUCTURAL CLASS
# -----------------------------
def classify(f):
    if f["length"] <= 2:
        return "atomic"
    if f["length"] <= 8:
        return "short"
    return "long"


# -----------------------------
# GATE LOGIC
# -----------------------------
def gate_decision(f, cls):
    # HARD FAIL
    if cls == "atomic":
        return "REJECT"

    # SHORT instability
    if cls == "short":
        if f["malformed"] > 0 or f["symbol_density"] > 0.15:
            return "REVIEW"
        return "PASS"

    # LONG drift detection
    if cls == "long":
        if (
            f["digit_density"] > 0.20
            or f["symbol_density"] > 0.20
            or f["malformed"] > 3
        ):
            return "REVIEW"
        return "PASS"

    return "PASS"


# -----------------------------
# RUN
# -----------------------------
def run():
    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            text = item["text"]

            fts = features(text)
            cls = classify(fts)
            decision = gate_decision(fts, cls)

            rows.append({
                "id": item["id"],
                "prompt": item["prompt"],
                "text": text,
                "class": cls,
                "gate": decision,
                **fts
            })

    return rows


# -----------------------------
# SUMMARY
# -----------------------------
def summarize(rows):
    counts = {"PASS": 0, "REVIEW": 0, "REJECT": 0}
    class_counts = {"atomic": 0, "short": 0, "long": 0}

    for r in rows:
        counts[r["gate"]] += 1
        class_counts[r["class"]] += 1

    total = len(rows)

    return {
        "total": total,
        "gate_counts": counts,
        "class_counts": class_counts
    }


# -----------------------------
# MAIN
# -----------------------------
def main():
    rows = run()
    summary = summarize(rows)

    print("\n=== OMNIA STRUCTURAL GATE V1 ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample decisions:")
    for r in rows[:10]:
        print(
            f"{r['gate']:6s} | {r['class']:6s} | "
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