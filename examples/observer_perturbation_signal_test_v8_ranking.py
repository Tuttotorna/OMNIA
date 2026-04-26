# ============================================================
# OMNIA — Observer Perturbation V8 (Ranking / Distribution)
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
# DATASET (same as V7, keyword-free)
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
        o_identity,
        o_add_explanation(),
        o_optimize_for_clarity(),
        o_reformat_bullets(),
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
        text = item["text"]

        opi_vals = []
        ratio_vals = []

        for observer in observers:
            out = lens.measure(x=text, observer=observer)
            d = asdict(out) if is_dataclass(out) else vars(out)

            opi_vals.append(d.get("opi"))
            ratio_vals.append(d.get("ratio"))

        avg_opi = sum(opi_vals) / len(opi_vals)
        avg_ratio = sum(ratio_vals) / len(ratio_vals)

        results.append({
            "id": idx,
            "label": item["label"],
            "text": text,
            "avg_opi": avg_opi,
            "avg_ratio": avg_ratio,
        })

    return results

# ============================================================
# ANALYSIS
# ============================================================

def analyze(results):
    # sort by descending OPI
    ranked = sorted(results, key=lambda x: x["avg_opi"], reverse=True)

    total = len(ranked)
    positives = sum(r["label"] for r in ranked)

    # Top-K evaluation
    ks = [3, 5, 10]

    topk_stats = {}
    for k in ks:
        top = ranked[:k]
        tp = sum(r["label"] for r in top)
        precision_at_k = tp / k
        recall_at_k = tp / positives if positives > 0 else 0

        topk_stats[k] = {
            "tp": tp,
            "precision": precision_at_k,
            "recall": recall_at_k,
        }

    # Mean separation
    stable = [r["avg_opi"] for r in results if r["label"] == 0]
    contradictory = [r["avg_opi"] for r in results if r["label"] == 1]

    mean_stats = {
        "stable_mean_opi": sum(stable) / len(stable),
        "contradictory_mean_opi": sum(contradictory) / len(contradictory),
    }

    return ranked, topk_stats, mean_stats

# ============================================================
# SAVE
# ============================================================

def save(ranked, topk, mean):
    with open("results_observer_perturbation_v8_ranked.json", "w") as f:
        json.dump(ranked, f, indent=2)

    with open("results_observer_perturbation_v8_summary.json", "w") as f:
        json.dump({
            "topk": topk,
            "means": mean
        }, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V8 RANKING TEST ===\n")

    results = run_test()
    ranked, topk, mean = analyze(results)

    print("=== MEAN SEPARATION ===")
    print(json.dumps(mean, indent=2))

    print("\n=== TOP-K ===")
    print(json.dumps(topk, indent=2))

    print("\n=== TOP 10 RANKED ===")
    for r in ranked[:10]:
        print(f"{r['avg_opi']:.6f} | label={r['label']} | {r['text']}")

    save(ranked, topk, mean)

    print("\nSaved:")
    print("- results_observer_perturbation_v8_ranked.json")
    print("- results_observer_perturbation_v8_summary.json")


if __name__ == "__main__":
    main()