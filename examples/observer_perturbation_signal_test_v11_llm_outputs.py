# ============================================================
# OMNIA — V11 REALISTIC LLM-LIKE OUTPUT TEST
# ============================================================
#
# Purpose:
# Compare raw OPI vs corrected OPI on realistic LLM-like outputs.
#
# The test evaluates whether corrected_opi improves top-k
# prioritization of contradiction-like outputs compared with raw OPI.
#
# This is not a semantic truth detector.
# It is a structural triage / ranking test.
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
# label = 0 -> structurally stable
# label = 1 -> contradiction / internal inconsistency
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

        # --- CONTRADICTION / INTERNAL INCONSISTENCY ---
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
# FEATURES / CORRECTION
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
    """
    Correction introduced after V9/V10 false-positive analysis.

    Raw OPI is sensitive to very short, rigid structures.
    This correction penalizes short / single-sentence cases and
    slightly boosts repeated structures.
    """

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

    rows = []

    for item in build_dataset():
        text = item["text"]
        opi_values = []

        for observer in observers:
            out = lens.measure(x=text, observer=observer)
            d = asdict(out) if is_dataclass(out) else vars(out)
            opi_values.append(d["opi"])

        raw_opi = sum(opi_values) / len(opi_values)
        features = extract_features(text)
        corr_opi = corrected_opi(raw_opi, features)

        rows.append({
            "label": item["label"],
            "text": text,
            "raw_opi": raw_opi,
            "corrected_opi": corr_opi,
            **features,
        })

    return rows


# ============================================================
# ANALYSIS
# ============================================================

def analyze(rows):
    ranked_raw = sorted(rows, key=lambda x: x["raw_opi"], reverse=True)
    ranked_corrected = sorted(rows, key=lambda x: x["corrected_opi"], reverse=True)

    def topk(ranked, k):
        top = ranked[:k]
        tp = sum(r["label"] for r in top)

        return {
            "tp": tp,
            "precision": tp / k,
            "recall": tp / 10,
        }

    summary = {
        "raw": {
            "top3": topk(ranked_raw, 3),
            "top5": topk(ranked_raw, 5),
            "top10": topk(ranked_raw, 10),
        },
        "corrected": {
            "top3": topk(ranked_corrected, 3),
            "top5": topk(ranked_corrected, 5),
            "top10": topk(ranked_corrected, 10),
        },
    }

    return ranked_raw, ranked_corrected, summary


# ============================================================
# SAVE
# ============================================================

def save(ranked_raw, ranked_corrected, summary):
    with open("results/observer_perturbation_v11_raw_ranked.json", "w", encoding="utf-8") as f:
        json.dump(ranked_raw, f, indent=2, ensure_ascii=False)

    with open("results/observer_perturbation_v11_corrected_ranked.json", "w", encoding="utf-8") as f:
        json.dump(ranked_corrected, f, indent=2, ensure_ascii=False)

    with open("results/observer_perturbation_v11_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V11 REALISTIC LLM-LIKE TEST ===\n")

    rows = run()
    ranked_raw, ranked_corrected, summary = analyze(rows)

    print(json.dumps(summary, indent=2))

    print("\n=== TOP 5 RAW ===")
    for r in ranked_raw[:5]:
        print(f"{r['raw_opi']:.6f} | label={r['label']} | {r['text']}")

    print("\n=== TOP 5 CORRECTED ===")
    for r in ranked_corrected[:5]:
        print(
            f"{r['corrected_opi']:.6f} | raw={r['raw_opi']:.6f} | "
            f"label={r['label']} | len={r['length']} | "
            f"sent={r['num_sentences']} | dup={r['has_duplication']} | "
            f"{r['text']}"
        )

    save(ranked_raw, ranked_corrected, summary)

    print("\nSaved:")
    print("- results/observer_perturbation_v11_raw_ranked.json")
    print("- results/observer_perturbation_v11_corrected_ranked.json")
    print("- results/observer_perturbation_v11_summary.json")


if __name__ == "__main__":
    main()