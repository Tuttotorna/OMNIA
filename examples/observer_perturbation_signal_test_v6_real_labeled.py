# ============================================================
# OMNIA — Observer Perturbation V6 (Real Labeled + Baselines)
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
# DATASET (REALISTIC + MANUAL LABELS)
# label = 1 → contradiction present
# label = 0 → stable
# ============================================================

def build_dataset():
    data = [

        # --- STABLE (0) ---
        {"label": 0, "text": "The answer is 42."},
        {"label": 0, "text": "Final answer: 17."},
        {"label": 0, "text": "Result: 128."},
        {"label": 0, "text": "The correct output is 5."},
        {"label": 0, "text": "Answer: 64."},
        {"label": 0, "text": "The capital of France is Paris."},
        {"label": 0, "text": "Water freezes at 0°C under standard conditions."},
        {"label": 0, "text": "The sum of 2 and 2 is 4."},
        {"label": 0, "text": "A triangle has three sides."},
        {"label": 0, "text": "The largest planet in the solar system is Jupiter."},

        # --- CONTRADICTIONS (1) ---
        {"label": 1, "text": "The answer is 42. Actually, the answer is 41."},
        {"label": 1, "text": "Final answer: 17. However, it might be 18."},
        {"label": 1, "text": "The result is 128. The result is also 127."},
        {"label": 1, "text": "The correct output is 5. The correct output is also 6."},
        {"label": 1, "text": "Answer: 64. On second thought, it is 63."},
        {"label": 1, "text": "Paris is the capital of France. The capital is also Lyon."},
        {"label": 1, "text": "Water freezes at 0°C. It also freezes at 10°C."},
        {"label": 1, "text": "2 + 2 = 4. Actually, 2 + 2 = 5."},
        {"label": 1, "text": "A triangle has three sides. It also has four sides."},
        {"label": 1, "text": "Jupiter is the largest planet. The largest planet is Saturn."},
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
# BASELINES
# ============================================================

def baseline_uncertainty(text):
    keywords = ["might", "could", "maybe", "however"]
    return sum(text.lower().count(k) for k in keywords)

def baseline_conflict_numbers(text):
    nums = re.findall(r"\d+", text)
    return len(set(nums)) > 1

def baseline_duplicate_claim(text):
    return "also" in text.lower() or "actually" in text.lower()

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
            "baseline_conflict_numbers": int(baseline_conflict_numbers(text)),
            "baseline_duplicate_claim": int(baseline_duplicate_claim(text)),
        })

    return results

# ============================================================
# SIMPLE CLASSIFIERS
# ============================================================

def classify_omnia(row, threshold):
    return 1 if row["avg_opi"] > threshold else 0

def classify_baseline(row):
    if row["baseline_conflict_numbers"]:
        return 1
    if row["baseline_duplicate_claim"]:
        return 1
    if row["baseline_uncertainty"] > 0:
        return 1
    return 0

# ============================================================
# EVALUATION
# ============================================================

def evaluate(results):
    # threshold = mean of all OPI
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

        # OMNIA
        if y == 1 and y_omnia == 1:
            metrics["omnia"]["tp"] += 1
        elif y == 0 and y_omnia == 1:
            metrics["omnia"]["fp"] += 1
        elif y == 0 and y_omnia == 0:
            metrics["omnia"]["tn"] += 1
        elif y == 1 and y_omnia == 0:
            metrics["omnia"]["fn"] += 1

        # BASELINE
        if y == 1 and y_base == 1:
            metrics["baseline"]["tp"] += 1
        elif y == 0 and y_base == 1:
            metrics["baseline"]["fp"] += 1
        elif y == 0 and y_base == 0:
            metrics["baseline"]["tn"] += 1
        elif y == 1 and y_base == 0:
            metrics["baseline"]["fn"] += 1

    return metrics, threshold

# ============================================================
# SAVE
# ============================================================

def save(results, metrics, threshold):
    with open("results_observer_perturbation_v6.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v6_summary.json", "w") as f:
        json.dump({
            "threshold": threshold,
            "metrics": metrics
        }, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V6 REAL LABELED TEST ===\n")

    results = run_test()
    metrics, threshold = evaluate(results)

    print("Threshold:", threshold)
    print("\nOMNIA:", metrics["omnia"])
    print("BASELINE:", metrics["baseline"])

    save(results, metrics, threshold)

    print("\nSaved:")
    print("- results_observer_perturbation_v6.jsonl")
    print("- results_observer_perturbation_v6_summary.json")


if __name__ == "__main__":
    main()