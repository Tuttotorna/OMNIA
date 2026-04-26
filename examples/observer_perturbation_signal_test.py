# ============================================================
# OMNIA — Observer Perturbation Signal Test
# ============================================================
#
# Purpose:
# Demonstrate that OMNIA's ObserverPerturbation lens detects
# structural instability in text under observer transformations.
#
# This script:
# - builds 20 cases (10 stable, 10 unstable)
# - applies multiple observers
# - computes OPI (Observer Perturbation Index)
# - shows separation between stable vs unstable
#
# Expected result:
# unstable avg OPI > stable avg OPI
#
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
# DATASET
# ============================================================

def build_dataset():
    stable_cases = [
        f"The answer is {i}. The calculation is direct and complete."
        for i in range(1, 11)
    ]

    unstable_cases = [
        f"The answer is {i}. Actually it could be {i+1}. "
        f"Depending on interpretation it might be {i} or {i+1}."
        for i in range(1, 11)
    ]

    data = []

    for t in stable_cases:
        data.append({"label": "stable", "text": t})

    for t in unstable_cases:
        data.append({"label": "unstable", "text": t})

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
# RUN TEST
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

            row = {
                "id": idx,
                "label": label,
                "observer": obs_name,
                "opi": d.get("opi"),
                "ratio": d.get("ratio"),
            }

            results.append(row)

    return results

# ============================================================
# ANALYSIS
# ============================================================

def avg(values):
    vals = [v for v in values if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None

def analyze(results):
    stable = [r for r in results if r["label"] == "stable"]
    unstable = [r for r in results if r["label"] == "unstable"]

    stable_opi = avg([r["opi"] for r in stable])
    unstable_opi = avg([r["opi"] for r in unstable])

    stable_ratio = avg([r["ratio"] for r in stable])
    unstable_ratio = avg([r["ratio"] for r in unstable])

    report = {
        "stable_avg_opi": stable_opi,
        "unstable_avg_opi": unstable_opi,
        "stable_avg_ratio": stable_ratio,
        "unstable_avg_ratio": unstable_ratio,
        "opi_gap": (unstable_opi - stable_opi) if stable_opi and unstable_opi else None,
        "ratio_gap": (unstable_ratio - stable_ratio) if stable_ratio and unstable_ratio else None,
        "signal": unstable_opi > stable_opi if (stable_opi and unstable_opi) else None,
    }

    return report

# ============================================================
# SAVE
# ============================================================

def save_results(results, report):
    with open("results_observer_perturbation.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_summary.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== RUNNING OBSERVER PERTURBATION TEST ===\n")

    results = run_test()
    report = analyze(results)

    print("Stable avg OPI   :", report["stable_avg_opi"])
    print("Unstable avg OPI :", report["unstable_avg_opi"])
    print("OPI gap          :", report["opi_gap"])

    print("\nStable avg ratio   :", report["stable_avg_ratio"])
    print("Unstable avg ratio :", report["unstable_avg_ratio"])
    print("Ratio gap          :", report["ratio_gap"])

    print("\nSignal detected:", report["signal"])

    save_results(results, report)

    print("\nResults saved:")
    print("- results_observer_perturbation.jsonl")
    print("- results_observer_perturbation_summary.json")


if __name__ == "__main__":
    main()