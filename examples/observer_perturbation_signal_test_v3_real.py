# ============================================================
# OMNIA — Observer Perturbation Signal Test V3 (Realistic)
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
# DATASET (LLM-LIKE)
# ============================================================

def build_dataset():
    data = []

    # --- STABLE (20) ---
    stable = [
        "The answer is 42.",
        "Final answer: 17.",
        "Result: 128.",
        "The correct output is 5.",
        "Answer: 64.",
    ]

    for i in range(20):
        data.append({
            "label": "stable",
            "text": stable[i % len(stable)]
        })

    # --- CONTRADICTORY (20) ---
    contradictory = [
        "The answer is 42. Actually the answer is 41.",
        "Final answer: 17. But it could also be 18.",
        "Result: 128. However, 127 might also be correct.",
        "The correct output is 5. The correct output is also 6.",
        "Answer: 64. On second thought, it may be 63.",
    ]

    for i in range(20):
        data.append({
            "label": "contradictory",
            "text": contradictory[i % len(contradictory)]
        })

    # --- DRIFT (20) ---
    drift = [
        "The answer is 42. First we compute 40, then 41, then 42.",
        "Final answer: 17. The reasoning initially suggested 15 and 16.",
        "Result: 128. Intermediate results were 120 and 124.",
        "Answer: 64. Earlier estimate was 60.",
        "The output is 5. Earlier we had 3 and 4.",
    ]

    for i in range(20):
        data.append({
            "label": "drift",
            "text": drift[i % len(drift)]
        })

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
# BASELINE
# ============================================================

def baseline_uncertainty(text):
    keywords = ["could", "might", "however", "maybe"]
    return sum(text.lower().count(k) for k in keywords)

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

        for obs_name, observer in observers:
            out = lens.measure(x=text, observer=observer)

            d = asdict(out) if is_dataclass(out) else vars(out)

            results.append({
                "id": idx,
                "label": label,
                "observer": obs_name,
                "opi": d.get("opi"),
                "ratio": d.get("ratio"),
                "baseline_uncertainty": baseline_uncertainty(text),
            })

    return results

# ============================================================
# ANALYSIS
# ============================================================

def avg(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None

def analyze(results):
    groups = {}
    for label in ["stable", "contradictory", "drift"]:
        group = [r for r in results if r["label"] == label]
        groups[label] = {
            "avg_opi": avg([r["opi"] for r in group]),
            "avg_ratio": avg([r["ratio"] for r in group]),
            "avg_uncertainty": avg([r["baseline_uncertainty"] for r in group]),
        }
    return groups

# ============================================================
# SAVE
# ============================================================

def save(results, report):
    with open("results_observer_perturbation_v3.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v3_summary.json", "w") as f:
        json.dump(report, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V3 REALISTIC TEST ===\n")

    results = run_test()
    report = analyze(results)

    for k, v in report.items():
        print("\n", k.upper())
        for m, val in v.items():
            print(f"  {m}: {val}")

    save(results, report)

    print("\nSaved:")
    print("- results_observer_perturbation_v3.jsonl")
    print("- results_observer_perturbation_v3_summary.json")


if __name__ == "__main__":
    main()