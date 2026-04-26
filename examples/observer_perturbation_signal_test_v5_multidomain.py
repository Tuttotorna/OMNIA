# ============================================================
# OMNIA — Observer Perturbation V5 (Multi-Domain Controlled)
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
# DATASET (MULTI-DOMAIN, CONTROLLED STRUCTURE)
# ============================================================

def build_dataset():
    data = []

    domains = ["math", "qa", "reasoning", "instruction"]

    templates = {
        "math": (
            "We compute the result step by step. "
            "All operations are verified. "
            "The reasoning is consistent. "
            "Final answer is {a}."
        ),
        "qa": (
            "We analyze the question carefully. "
            "Relevant facts are considered. "
            "The reasoning is consistent. "
            "Final answer is {a}."
        ),
        "reasoning": (
            "We follow the logical steps carefully. "
            "Each inference is verified. "
            "The reasoning is consistent. "
            "Final answer is {a}."
        ),
        "instruction": (
            "We follow the instructions precisely. "
            "Each step is executed correctly. "
            "The reasoning is consistent. "
            "Final answer is {a}."
        ),
    }

    templates_contradictory = {
        k: v + " However the final answer is {b}."
        for k, v in templates.items()
    }

    for domain in domains:
        for i in range(1, 11):
            data.append({
                "label": "stable",
                "domain": domain,
                "text": templates[domain].format(a=i)
            })

        for i in range(1, 11):
            data.append({
                "label": "contradictory",
                "domain": domain,
                "text": templates_contradictory[domain].format(a=i, b=i+1)
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
                "domain": item["domain"],
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
    summary = {}

    for domain in ["math", "qa", "reasoning", "instruction"]:
        stable = [r for r in results if r["label"] == "stable" and r["domain"] == domain]
        contradictory = [r for r in results if r["label"] == "contradictory" and r["domain"] == domain]

        summary[domain] = {
            "stable_avg_opi": avg([r["opi"] for r in stable]),
            "contradictory_avg_opi": avg([r["opi"] for r in contradictory]),
            "stable_avg_ratio": avg([r["ratio"] for r in stable]),
            "contradictory_avg_ratio": avg([r["ratio"] for r in contradictory]),
            "opi_gap": (
                avg([r["opi"] for r in contradictory]) -
                avg([r["opi"] for r in stable])
            ),
            "ratio_gap": (
                avg([r["ratio"] for r in contradictory]) -
                avg([r["ratio"] for r in stable])
            ),
        }

    return summary

# ============================================================
# SAVE
# ============================================================

def save(results, report):
    with open("results_observer_perturbation_v5.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    with open("results_observer_perturbation_v5_summary.json", "w") as f:
        json.dump(report, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V5 MULTI-DOMAIN TEST ===\n")

    results = run_test()
    report = analyze(results)

    for domain, metrics in report.items():
        print(f"\n--- {domain.upper()} ---")
        for k, v in metrics.items():
            print(f"{k}: {v}")

    save(results, report)

    print("\nSaved:")
    print("- results_observer_perturbation_v5.jsonl")
    print("- results_observer_perturbation_v5_summary.json")


if __name__ == "__main__":
    main()