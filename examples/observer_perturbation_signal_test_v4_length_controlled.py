# ============================================================
# OMNIA — Observer Perturbation V4 (Length Controlled)
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
# DATASET (CONTROLLED)
# ============================================================

def build_dataset():
    data = []

    # Template identico
    template_stable = (
        "We compute the result carefully. "
        "Intermediate values are checked. "
        "The reasoning is consistent. "
        "Final answer is {a}."
    )

    template_contradictory = (
        "We compute the result carefully. "
        "Intermediate values are checked. "
        "The reasoning is consistent. "
        "Final answer is {a}. "
        "However the final answer is {b}."
    )

    for i in range(1, 21):
        data.append({
            "label": "stable",
            "text": template_stable.format(a=i)
        })

    for i in range(1, 21):
        data.append({
            "label": "contradictory",
            "text": template_contradictory.format(a=i, b=i+1)
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
# RUN
# ============================================================

def run_test():
    lens = ObserverPerturbation()
    data = build_dataset()
    observers = get_observers()

    results = []

    for idx, item in enumerate(data):
        for obs_name, observer in observers:
            out = lens.measure(x=item["text"], observer=observer)

            d = asdict(out) if is_dataclass(out) else vars(out)

            results.append({
                "label": item["label"],
                "observer": obs_name,
                "opi": d.get("opi"),
                "ratio": d.get("ratio"),
            })

    return results

# ============================================================
# ANALYSIS
# ============================================================

def avg(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None

def analyze(results):
    stable = [r for r in results if r["label"] == "stable"]
    contradictory = [r for r in results if r["label"] == "contradictory"]

    return {
        "stable": {
            "avg_opi": avg([r["opi"] for r in stable]),
            "avg_ratio": avg([r["ratio"] for r in stable]),
        },
        "contradictory": {
            "avg_opi": avg([r["opi"] for r in contradictory]),
            "avg_ratio": avg([r["ratio"] for r in contradictory]),
        }
    }

# ============================================================
# SAVE
# ============================================================

def save(results, report):
    with open("results_observer_perturbation_v4.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v4_summary.json", "w") as f:
        json.dump(report, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V4 LENGTH-CONTROLLED TEST ===\n")

    results = run_test()
    report = analyze(results)

    for k, v in report.items():
        print("\n", k.upper())
        for m, val in v.items():
            print(f"  {m}: {val}")

    save(results, report)

    print("\nSaved:")
    print("- results_observer_perturbation_v4.jsonl")
    print("- results_observer_perturbation_v4_summary.json")


if __name__ == "__main__":
    main()