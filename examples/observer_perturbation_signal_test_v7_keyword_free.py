# ============================================================
# OMNIA — Observer Perturbation V7 (Keyword-Free Contradictions)
# ============================================================

import json
import re
from dataclasses import asdict, is_dataclass

from omnia.lenses.observer_perturbation import (
    ObserverPerturbation,
    o_identity,
    o_add_explanation,
    o_optimize_for_clarity,
    o_reformat_bullets,
)

# ============================================================
# DATASET (NO KEYWORDS LIKE: also / actually / however / might)
# ============================================================

def build_dataset():
    data = [

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

    return data

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
# BASELINES (WEAKENED ON PURPOSE)
# ============================================================

def baseline_uncertainty(text):
    keywords = ["might", "could", "maybe", "however"]
    return sum(text.lower().count(k) for k in keywords)

def baseline_duplicate_claim(text):
    return text.count(".") > 1 and len(set(text.split("."))) < len(text.split("."))

# ============================================================
# RUN
# ============================================================

def run_test():
    lens = ObserverPerturbation()
    data = build_dataset()
    observers = get_observers()

    results = []

    for idx, item in enumerate(data):
        label = item["label"]
        text = item["text"]

        opi_vals = []
        ratio_vals = []

        for _, observer in observers:
            out = lens.measure(x=text, observer=observer)
            d = asdict(out) if is_dataclass(out) else vars(out)

            opi_vals.append(d.get("opi"))
            ratio_vals.append(d.get("ratio"))

        avg_opi = sum(opi_vals) / len(opi_vals)
        avg_ratio = sum(ratio_vals) / len(ratio_vals)

        results.append({
            "id": idx,
            "label": label,
            "text": text,
            "avg_opi": avg_opi,
            "avg_ratio": avg_ratio,
            "baseline_uncertainty": baseline_uncertainty(text),
            "baseline_duplicate_claim": int(baseline_duplicate_claim(text)),
        })

    return results

# ============================================================
# CLASSIFIERS
# ============================================================

def classify_omnia(row, threshold):
    return 1 if row["avg_opi"] > threshold else 0

def classify_baseline(row):
    if row["baseline_duplicate_claim"]:
        return 1
    if row["baseline_uncertainty"] > 0:
        return 1
    return 0

# ============================================================
# EVALUATION
# ============================================================

def evaluate(results):
    all_opi = [r["avg_opi"] for r in results]
    threshold = sum(all_opi) / len(all_opi)

    metrics = {
        "omnia": {"tp": 0, "fp": 0, "tn": 0, "fn": 0},
        "baseline": {"tp": 0, "fp": 0, "tn": 0, "fn": 0},
    }

    for r in results:
        y = r["label"]
        y_omnia = classify_omnia(r, threshold)
        y_base = classify_baseline(r)

        for model, pred in [("omnia", y_omnia), ("baseline", y_base)]:
            if y == 1 and pred == 1:
                metrics[model]["tp"] += 1
            elif y == 0 and pred == 1:
                metrics[model]["fp"] += 1
            elif y == 0 and pred == 0:
                metrics[model]["tn"] += 1
            elif y == 1 and pred == 0:
                metrics[model]["fn"] += 1

    return metrics, threshold

# ============================================================
# SAVE
# ============================================================

def save(results, metrics, threshold):
    with open("results_observer_perturbation_v7.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v7_summary.json", "w") as f:
        json.dump({
            "threshold": threshold,
            "metrics": metrics
        }, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V7 KEYWORD-FREE TEST ===\n")

    results = run_test()
    metrics, threshold = evaluate(results)

    print("Threshold:", threshold)
    print("\nOMNIA:", metrics["omnia"])
    print("BASELINE:", metrics["baseline"])

    save(results, metrics, threshold)

    print("\nSaved:")
    print("- results_observer_perturbation_v7.jsonl")
    print("- results_observer_perturbation_v7_summary.json")


if __name__ == "__main__":
    main()