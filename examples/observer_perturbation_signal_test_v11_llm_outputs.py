# ============================================================
# OMNIA — V11 REALISTIC LLM-LIKE OUTPUT TEST (COLAB-READY)
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
# REALISTIC LLM-LIKE DATASET (manually curated)
# label = 1 → contradiction / internal inconsistency
# label = 0 → structurally stable
# ============================================================

def build_dataset():
    return [

        # --- STABLE ---
        {"label": 0, "text": "The result is 42."},
        {"label": 0, "text": "Paris is the capital of France."},
        {"label": 0, "text": "2 + 2 equals 4."},
        {"label": 0, "text": "Water freezes at 0°C."},
        {"label": 0, "text": "A triangle has three sides."},
        {"label": 0, "text": "The largest planet is Jupiter."},
        {"label": 0, "text": "The function returns a sorted list."},
        {"label": 0, "text": "The answer is 17."},
        {"label": 0, "text": "Python is a programming language."},
        {"label": 0, "text": "The output is a valid JSON object."},

        # --- CONTRADICTORY / DRIFT ---
        {"label": 1, "text": "The result is 42. The result is 41."},
        {"label": 1, "text": "Paris is the capital of France. The capital is Lyon."},
        {"label": 1, "text": "2 + 2 equals 4. 2 + 2 equals 5."},
        {"label": 1, "text": "Water freezes at 0°C. It freezes at 10°C."},
        {"label": 1, "text": "A triangle has three sides. It has four sides."},
        {"label": 1, "text": "The largest planet is Jupiter. The largest planet is Saturn."},
        {"label": 1, "text": "The function returns a sorted list. It returns unsorted data."},
        {"label": 1, "text": "The answer is 17. The answer is 18."},
        {"label": 1, "text": "Python is a programming language. It is not a programming language."},
        {"label": 1, "text": "The output is valid JSON. The output is not valid JSON."},
    ]

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
# FEATURES (same logic as V10)
# ============================================================

def extract_features(text):
    tokens = text.split()
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    return {
        "length": len(tokens),
        "num_sentences": len(sentences),
        "has_duplication": len(set(sentences)) < len(sentences),
    }

def corrected_opi(opi, features):
    length_factor = min(1.0, features["length"] / 8.0)
    structure_factor = min(1.0, features["num_sentences"] / 2.0)
    duplication_factor = 1.2 if features["has_duplication"] else 0.8
    return opi * length_factor * structure_factor * duplication_factor

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

        for obs in observers:
            out = lens.measure(x=text, observer=obs)
            d = asdict(out) if is_dataclass(out) else vars(out)
            opi_vals.append(d["opi"])

        raw_opi = sum(opi_vals) / len(opi_vals)
        features = extract_features(text)
        corr = corrected_opi(raw_opi, features)

        rows.append({
            "label": item["label"],
            "text": text,
            "raw_opi": raw_opi,
            "corrected_opi": corr,
            **features
        })

    return rows

# ============================================================
# ANALYSIS
# ============================================================

def analyze(rows):
    ranked_raw = sorted(rows, key=lambda x: x["raw_opi"], reverse=True)
    ranked_corr = sorted(rows, key=lambda x: x["corrected_opi"], reverse=True)

    def topk(ranked, k):
        top = ranked[:k]
        tp = sum(r["label"] for r in top)
        return {"tp": tp, "precision": tp / k, "recall": tp / 10}

    summary = {
        "raw": {
            "top3": topk(ranked_raw, 3),
            "top5": topk(ranked_raw, 5),
        },
        "corrected": {
            "top3": topk(ranked_corr, 3),
            "top5": topk(ranked_corr, 5),
        }
    }

    return ranked_raw, ranked_corr, summary

# ============================================================
# SAVE
# ============================================================

def save(ranked_raw, ranked_corr, summary):
    with open("results_observer_perturbation_v11_raw_ranked.json", "w") as f:
        json.dump(ranked_raw, f, indent=2)

    with open("results_observer_perturbation_v11_corrected_ranked.json", "w") as f:
        json.dump(ranked_corr, f, indent=2)

    with open("results_observer_perturbation_v11_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V11 REALISTIC TEST ===\n")

    rows = run()
    raw, corr, summary = analyze(rows)

    print(json.dumps(summary, indent=2))

    print("\n=== TOP 5 RAW ===")
    for r in raw[:5]:
        print(f"{r['raw_opi']:.6f} | label={r['label']} | {r['text']}")

    print("\n=== TOP 5 CORRECTED ===")
    for r in corr[:5]:
        print(f"{r['corrected_opi']:.6f} | label={r['label']} | {r['text']}")

    save(raw, corr, summary)

    print("\nSaved:")
    print("- results_observer_perturbation_v11_raw_ranked.json")
    print("- results_observer_perturbation_v11_corrected_ranked.json")
    print("- results_observer_perturbation_v11_summary.json")


if __name__ == "__main__":
    main()