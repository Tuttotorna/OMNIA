# ============================================================
# OMNIA — V18 TRI-CHANNEL STRUCTURAL TRIAGE
# ============================================================
#
# Purpose:
# Test whether structural failures are better separated into
# multiple channels instead of one global suspicion score.
#
# Channels:
# 1. atomic_score  -> empty / near-empty / atomic malformed outputs
# 2. short_score   -> short malformed outputs
# 3. long_score    -> long incoherent outputs
#
# Conclusion:
# A single score is insufficient.
# Multi-channel triage is more interpretable.
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

DATA_PATH = Path("data/real_llm_outputs_v14_local_flan_t5_small.jsonl")


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
# FEATURES
# ============================================================

def extract_features(text):
    tokens = text.split()
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    return {
        "length": len(tokens),
        "num_sentences": len(sentences),
        "empty": len(text.strip()) == 0,
    }


# ============================================================
# TRI-CHANNEL SCORING
# ============================================================

def atomic_score(raw_opi, features):
    """
    Atomic malformed channel:
    captures empty / near-empty / single-token malformed outputs.
    """

    if features["empty"]:
        return 1.0

    if features["length"] <= 2:
        return raw_opi

    return 0.0


def short_score(raw_opi, features):
    """
    Short malformed channel:
    captures short, broken outputs that are not atomic.
    """

    if 2 < features["length"] <= 8:
        return raw_opi

    return 0.0


def long_score(raw_opi, features):
    """
    Long incoherent channel:
    captures longer outputs and multi-sentence incoherence.
    """

    if features["length"] > 8:
        if features["num_sentences"] > 1:
            return raw_opi * features["num_sentences"]
        return raw_opi * 0.5

    return 0.0


# ============================================================
# DATA
# ============================================================

def load_data():
    rows = []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
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

        raw_opi = sum(opi_values) / len(opi_values)
        features = extract_features(text)

        rows.append({
            "id": item.get("id", ""),
            "prompt": item.get("prompt", ""),
            "text": text,
            "raw_opi": raw_opi,
            "atomic_score": atomic_score(raw_opi, features),
            "short_score": short_score(raw_opi, features),
            "long_score": long_score(raw_opi, features),
            **features,
        })

    return rows


# ============================================================
# SAVE
# ============================================================

def save(summary):
    with open("results/observer_perturbation_v18_tri_channel_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V18 TRI-CHANNEL STRUCTURAL TRIAGE ===\n")

    rows = run()

    atomic_rank = sorted(rows, key=lambda x: x["atomic_score"], reverse=True)
    short_rank = sorted(rows, key=lambda x: x["short_score"], reverse=True)
    long_rank = sorted(rows, key=lambda x: x["long_score"], reverse=True)

    summary = {
        "atomic_top10": atomic_rank[:10],
        "short_top10": short_rank[:10],
        "long_top10": long_rank[:10],
    }

    print("\n=== ATOMIC MALFORMED ===")
    for r in summary["atomic_top10"]:
        print(f"{r['atomic_score']:.6f} | {r['text']}")

    print("\n=== SHORT MALFORMED ===")
    for r in summary["short_top10"]:
        print(f"{r['short_score']:.6f} | {r['text']}")

    print("\n=== LONG INCOHERENT ===")
    for r in summary["long_top10"]:
        print(f"{r['long_score']:.6f} | {r['text']}")

    save(summary)

    print("\nSaved:")
    print("- results/observer_perturbation_v18_tri_channel_summary.json")


if __name__ == "__main__":
    main()