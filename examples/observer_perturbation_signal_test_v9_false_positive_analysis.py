# ============================================================
# OMNIA — V9 FALSE POSITIVE ANALYSIS (COLAB-READY SCRIPT)
# ============================================================

import json
from dataclasses import asdict, is_dataclass

from omnia.lenses.observer_perturbation import (
    ObserverPerturbation,
    o_identity,
    o_add_explanation,
    o_optimize_for_clarity,
    o_reformat_bullets,
)

# ============================================================
# SAME DATASET AS V7 / V8
# ============================================================

def build_dataset():
    return [

        # --- STABLE (0) ---
        {"label": 0, "text": "The answer is 42."},
        {"label": 0, "text": "Final answer: 17."},
        {"label": 0, "text": "Result: 128."},
        {"label": 0, "text": "The correct output is 5."},
        {"label": 0, "text": "Answer: 64."},
        {"label": 0, "text": "Paris is the capital of France."},
        {"label": 0, "text": "Water freezes at 0°C."},
        {"label": 0, "text": "2 + 2 equals 4."},
        {"label": 0, "text": "A triangle has three sides."},
        {"label": 0, "text": "Jupiter is the largest planet."},

        # --- CONTRADICTIONS (1) ---
        {"label": 1, "text": "The answer is 42. The answer is 41."},
        {"label": 1, "text": "Final answer: 17. Final answer: 18."},
        {"label": 1, "text": "Result: 128. Result: 127."},
        {"label": 1, "text": "The correct output is 5. The correct output is 6."},
        {"label": 1, "text": "Answer: 64. Answer: 63."},
        {"label": 1, "text": "Paris is the capital of France. The capital of France is Lyon."},
        {"label": 1, "text": "Water freezes at 0°C. Water freezes at 10°C."},
        {"label": 1, "text": "2 + 2 equals 4. 2 + 2 equals 5."},
        {"label": 1, "text": "A triangle has three sides. A triangle has four sides."},
        {"label": 1, "text": "Jupiter is the largest planet. Saturn is the largest planet."},
    ]

# ============================================================
# OBSERVERS
# ============================================================

def get_observers():
    return [
        ("identity", o_identity),
        ("add_explanation", o_add_explanation()),
        ("optimize_for_clarity", o_optimize_for_clarity()),
        ("reformat_bullets", o_reformat_bullets()),
    ]

# ============================================================
# FEATURE EXTRACTION (WHY OPI IS HIGH)
# ============================================================

def extract_features(text):
    return {
        "length": len(text),
        "num_sentences": text.count("."),
        "has_numbers": any(c.isdigit() for c in text),
        "token_count": len(text.split()),
        "repeated_prefix": len(set(text.split("."))) < len(text.split(".")),
    }

# ============================================================
# RUN
# ============================================================

def run():
    lens = ObserverPerturbation()
    observers = get_observers()
    data = build_dataset()

    rows = []

    for item in data:
        text = item["text"]

        opi_vals = []
        ratio_vals = []

        for _, obs in observers:
            out = lens.measure(x=text, observer=obs)
            d = asdict(out) if is_dataclass(out) else vars(out)

            opi_vals.append(d.get("opi"))
            ratio_vals.append(d.get("ratio"))

        avg_opi = sum(opi_vals) / len(opi_vals)
        avg_ratio = sum(ratio_vals) / len(ratio_vals)

        features = extract_features(text)

        rows.append({
            "label": item["label"],
            "text": text,
            "avg_opi": avg_opi,
            "avg_ratio": avg_ratio,
            **features
        })

    return rows

# ============================================================
# ANALYSIS
# ============================================================

def analyze(rows):
    ranked = sorted(rows, key=lambda x: x["avg_opi"], reverse=True)

    false_positives = [
        r for r in ranked
        if r["label"] == 0
    ][:5]

    true_positives = [
        r for r in ranked
        if r["label"] == 1
    ][:5]

    return ranked, false_positives, true_positives

# ============================================================
# SAVE
# ============================================================

def save(ranked, fp, tp):
    with open("results_observer_perturbation_v9_ranked.json", "w") as f:
        json.dump(ranked, f, indent=2)

    with open("results_observer_perturbation_v9_analysis.json", "w") as f:
        json.dump({
            "top_false_positives": fp,
            "top_true_positives": tp
        }, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V9 FALSE POSITIVE ANALYSIS ===\n")

    rows = run()
    ranked, fp, tp = analyze(rows)

    print("\n=== TOP FALSE POSITIVES ===")
    for r in fp:
        print(f"{r['avg_opi']:.6f} | {r['text']}")

    print("\n=== TOP TRUE POSITIVES ===")
    for r in tp:
        print(f"{r['avg_opi']:.6f} | {r['text']}")

    save(ranked, fp, tp)

    print("\nSaved:")
    print("- results_observer_perturbation_v9_ranked.json")
    print("- results_observer_perturbation_v9_analysis.json")


if __name__ == "__main__":
    main()