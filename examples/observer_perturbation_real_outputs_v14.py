# ============================================================
# OMNIA — V14 REAL OUTPUTS STRESS TEST
# ============================================================
#
# Purpose:
# Apply OMNIA to real LLM outputs (no synthetic labels).
#
# Output:
# ranked list by corrected_opi
#
# Evaluation:
# human inspects top-k only
#
# ============================================================

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

from omnia.lenses.observer_perturbation import (
    ObserverPerturbation,
    o_identity,
    o_add_explanation,
    o_optimize_for_clarity,
    o_reformat_bullets,
)

DATA_PATH = Path("data/real_llm_outputs.jsonl")


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
# LOAD
# ============================================================

def load_data():
    rows = []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


# ============================================================
# RUN
# ============================================================

def run():
    lens = ObserverPerturbation()
    observers = get_observers()
    data = load_data()

    rows = []

    for item in data:
        text = item["text"]

        opi_values = []

        for observer in observers:
            out = lens.measure(x=text, observer=observer)
            d = asdict(out) if is_dataclass(out) else vars(out)
            opi_values.append(d["opi"])

        raw = sum(opi_values) / len(opi_values)
        f = extract_features(text)
        corr = corrected_opi(raw, f)

        rows.append({
            "id": item.get("id", ""),
            "text": text,
            "raw_opi": raw,
            "corrected_opi": corr,
            **f,
        })

    return rows


# ============================================================
# SAVE
# ============================================================

def save(ranked):
    with open("results/observer_perturbation_v14_ranked.json", "w", encoding="utf-8") as f:
        json.dump(ranked, f, indent=2, ensure_ascii=False)


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V14 REAL OUTPUT STRESS TEST ===\n")

    rows = run()
    ranked = sorted(rows, key=lambda x: x["corrected_opi"], reverse=True)

    print("=== TOP 10 ===")
    for i, r in enumerate(ranked[:10]):
        print(
            f"{i+1:02d} | {r['corrected_opi']:.6f} | "
            f"len={r['length']} | sent={r['num_sentences']} | "
            f"{r['text']}"
        )

    print("\n=== TOP 20 ===")
    for i, r in enumerate(ranked[:20]):
        print(
            f"{i+1:02d} | {r['corrected_opi']:.6f} | "
            f"{r['text']}"
        )

    save(ranked)

    print("\nSaved:")
    print("- results/observer_perturbation_v14_ranked.json")

    print("\nManual step:")
    print("Inspect top 10–20 and mark issues manually.")


if __name__ == "__main__":
    main()