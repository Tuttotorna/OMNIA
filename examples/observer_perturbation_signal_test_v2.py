# ============================================================
# OMNIA — Observer Perturbation Signal Test V2
# ============================================================
#
# Goal:
# Strengthen the initial signal with:
# - 60 cases
# - 3 classes: stable / ambiguous / contradictory
# - OMNIA metrics vs simple baselines
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
    data = []

    # --- STABLE (20) ---
    for i in range(1, 21):
        data.append({
            "label": "stable",
            "text": f"The answer is {i}. The calculation is direct and complete."
        })

    # --- AMBIGUOUS (20) ---
    for i in range(1, 21):
        data.append({
            "label": "ambiguous",
            "text": (
                f"The answer is {i}. It could also be {i+1}. "
                f"Depending on interpretation it might vary."
            )
        })

    # --- CONTRADICTORY (20) ---
    for i in range(1, 21):
        data.append({
            "label": "contradictory",
            "text": (
                f"The answer is {i}. The answer is actually {i+1}. "
                f"Both values are presented as correct."
            )
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
# BASELINE METRICS
# ============================================================

def baseline_length(text):
    return len(text.split())

def baseline_uncertainty(text):
    keywords = ["maybe", "could", "depending", "might"]
    return sum(text.lower().count(k) for k in keywords)

def baseline_numbers(text):
    import re
    return len(re.findall(r"\d+", text))

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

            results.append({
                "id": idx,
                "label": label,
                "observer": obs_name,
                "opi": d.get("opi"),
                "ratio": d.get("ratio"),
                "baseline_length": baseline_length(text),
                "baseline_uncertainty": baseline_uncertainty(text),
                "baseline_numbers": baseline_numbers(text),
            })

    return results

# ============================================================
# ANALYSIS
# ============================================================

def avg(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None

def analyze(results):
    groups = {
        "stable": [r for r in results if r["label"] == "stable"],
        "ambiguous": [r for r in results if r["label"] == "ambiguous"],
        "contradictory": [r for r in results if r["label"] == "contradictory"],
    }

    report = {}

    for name, group in groups.items():
        report[name] = {
            "avg_opi": avg([r["opi"] for r in group]),
            "avg_ratio": avg([r["ratio"] for r in group]),
            "avg_len": avg([r["baseline_length"] for r in group]),
            "avg_uncertainty": avg([r["baseline_uncertainty"] for r in group]),
            "avg_numbers": avg([r["baseline_numbers"] for r in group]),
        }

    return report

# ============================================================
# SAVE
# ============================================================

def save(results, report):
    with open("results_observer_perturbation_v2.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v2_summary.json", "w") as f:
        json.dump(report, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V2 SIGNAL TEST ===\n")

    results = run_test()
    report = analyze(results)

    for k, v in report.items():
        print("\n", k.upper())
        for m, val in v.items():
            print(f"  {m}: {val}")

    save(results, report)

    print("\nSaved:")
    print("- results_observer_perturbation_v2.jsonl")
    print("- results_observer_perturbation_v2_summary.json")


if __name__ == "__main__":
    main()