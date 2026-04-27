# ============================================================
# OMNIA — STRUCTURAL GATE V2 (USAGE)
# ============================================================
#
# Uses trained model instead of rule-based gate
#
# Input:
# data/real_structural_dataset_v1.jsonl
#
# Model:
# models/structural_gate_v2.pkl
#
# Output:
# results/omnia_structural_gate_v2.json
#
# ============================================================

import json
import pickle
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
MODEL_PATH = Path("models/structural_gate_v2.pkl")
OUTPUT_PATH = Path("results/omnia_structural_gate_v2.json")


# ------------------------------------------------------------
# FEATURES (must match training)
# ------------------------------------------------------------
def features(text):
    tokens = text.split()
    length = len(tokens)

    digits = sum(c.isdigit() for c in text)
    symbols = sum(not c.isalnum() and not c.isspace() for c in text)

    total_chars = max(len(text), 1)

    digit_density = digits / total_chars
    symbol_density = symbols / total_chars
    malformed = sum(1 for t in tokens if not t.isalnum())

    return [
        length,
        digit_density,
        symbol_density,
        malformed,
    ]


# ------------------------------------------------------------
# RUN
# ------------------------------------------------------------
def run():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Train V2 first.")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            text = item["text"]

            fts = features(text)
            decision = model.predict([fts])[0]

            rows.append({
                "id": item["id"],
                "prompt": item["prompt"],
                "text": text,
                "gate": decision,
                "features": {
                    "length": fts[0],
                    "digit_density": fts[1],
                    "symbol_density": fts[2],
                    "malformed": fts[3],
                }
            })

    return rows


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------
def summarize(rows):
    counts = {"PASS": 0, "REVIEW": 0, "REJECT": 0}

    for r in rows:
        counts[r["gate"]] += 1

    total = len(rows)

    return {
        "total": total,
        "counts": counts,
        "ratios": {
            k: v / total for k, v in counts.items()
        }
    }


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    rows = run()
    summary = summarize(rows)

    print("\n=== OMNIA STRUCTURAL GATE V2 ===\n")
    print(json.dumps(summary, indent=2))

    print("\nSample decisions:")
    for r in rows[:15]:
        print(
            f"{r['gate']:6s} | "
            f"len={r['features']['length']:2d} "
            f"dig={r['features']['digit_density']:.3f} "
            f"sym={r['features']['symbol_density']:.3f} "
            f"mal={r['features']['malformed']} | "
            f"{r['text'][:90]}"
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