# ============================================================
# OMNIA — V12 TRIAGE DEMO (REAL USE-CASE)
# ============================================================
#
# Goal:
# Show practical value of OMNIA as a triage layer.
#
# Instead of detecting all errors, OMNIA ranks outputs
# so that reviewing top-k finds more inconsistencies.
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
# DATASET (30 LLM-like outputs)
# label = 1 → problematic (contradiction / drift / inconsistency)
# label = 0 → stable
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
        {"label": 0, "text": "The output is valid JSON."},
        {"label": 0, "text": "The sky appears blue due to scattering."},
        {"label": 0, "text": "A square has four equal sides."},
        {"label": 0, "text": "The API returns status code 200."},
        {"label": 0, "text": "The function runs in linear time."},
        {"label": 0, "text": "Earth orbits the Sun."},

        # --- PROBLEMATIC ---
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
        {"label": 1, "text": "The API returns 200. It returns 500."},
        {"label": 1, "text": "The algorithm is O(n). It is O(n^2)."},
        {"label": 1, "text": "The sky is blue. The sky is green."},
        {"label": 1, "text": "A square has four sides. It has five sides."},
        {"label": 1, "text": "Earth orbits the Sun. The Sun orbits the Earth."},
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
# FEATURES + CORRECTION
# ============================================================

def extract_features(text):
    tokens = text.split()
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    return {
        "length": len(tokens),
        "num_sentences": len(sentences),
        "has_duplication": len(set(sentences)) < len(sentences),
    }

def corrected_opi(opi, f):
    length_factor = min(1.0, f["length"] / 8.0)
    structure_factor = min(1.0, f["num_sentences"] / 2.0)
    duplication_factor = 1.2 if f["has_duplication"] else 0.8
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

        opi_vals = []
        for obs in observers:
            out = lens.measure(x=text, observer=obs)
            d = asdict(out) if is_dataclass(out) else vars(out)
            opi_vals.append(d["opi"])

        raw = sum(opi_vals) / len(opi_vals)
        f = extract_features(text)
        corr = corrected_opi(raw, f)

        rows.append({
            "label": item["label"],
            "text": text,
            "raw_opi": raw,
            "corrected_opi": corr,
        })

    return rows

# ============================================================
# TRIAGE METRIC
# ============================================================

def triage_score(ranked, k):
    top = ranked[:k]
    found = sum(r["label"] for r in top)
    total = sum(r["label"] for r in ranked)

    return {
        "found_in_top_k": found,
        "total_issues": total,
        "recall": found / total,
        "precision": found / k,
    }

# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V12 TRIAGE DEMO ===\n")

    rows = run()

    raw_ranked = sorted(rows, key=lambda x: x["raw_opi"], reverse=True)
    corr_ranked = sorted(rows, key=lambda x: x["corrected_opi"], reverse=True)

    print("RAW TRIAGE:")
    for k in [5, 10]:
        print(f"top{k}:", triage_score(raw_ranked, k))

    print("\nCORRECTED TRIAGE:")
    for k in [5, 10]:
        print(f"top{k}:", triage_score(corr_ranked, k))

    print("\nTOP 5 CORRECTED:")
    for r in corr_ranked[:5]:
        print(f"{r['corrected_opi']:.6f} | label={r['label']} | {r['text']}")

    with open("results_observer_perturbation_v12_summary.json", "w") as f:
        json.dump({
            "raw_top5": triage_score(raw_ranked, 5),
            "raw_top10": triage_score(raw_ranked, 10),
            "corrected_top5": triage_score(corr_ranked, 5),
            "corrected_top10": triage_score(corr_ranked, 10),
        }, f, indent=2)

if __name__ == "__main__":
    main()