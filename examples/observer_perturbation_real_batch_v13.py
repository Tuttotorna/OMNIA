# ============================================================
# OMNIA — V13 REAL-LIKE BATCH TRIAGE
# ============================================================
#
# Purpose:
# Evaluate corrected ObserverPerturbation on a larger batch of
# LLM-like outputs.
#
# OMNIA does not decide correctness.
# OMNIA ranks structurally suspicious outputs for review.
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

DATA_PATH = Path("data/v13_real_batch.jsonl")


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
    length_factor = min(1.0, features["length"] / 8.0)
    structure_factor = min(1.0, features["num_sentences"] / 2.0)
    duplication_factor = 1.2 if features["has_duplication"] else 0.8

    return opi * length_factor * structure_factor * duplication_factor


# ============================================================
# DATA
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

        raw_opi = sum(opi_values) / len(opi_values)
        features = extract_features(text)
        corr_opi = corrected_opi(raw_opi, features)

        rows.append({
            "id": item["id"],
            "text": text,
            "raw_opi": raw_opi,
            "corrected_opi": corr_opi,
            **features,
        })

    return rows


# ============================================================
# TRIAGE SUMMARY
# ============================================================

def is_likely_issue(row):
    """
    Proxy label used for this generated batch:
    problematic records have ids starting with 'p_'.
    """

    return str(row["id"]).startswith("p_")


def summarize(ranked, k_values=(5, 10, 20)):
    total = sum(1 for r in ranked if is_likely_issue(r))
    out = {}

    for k in k_values:
        top = ranked[:k]
        found = sum(1 for r in top if is_likely_issue(r))

        out[f"top{k}"] = {
            "found_in_top_k": found,
            "total_proxy_issues": total,
            "recall_proxy": found / total if total else 0.0,
            "precision_proxy": found / k,
        }

    return out


# ============================================================
# SAVE
# ============================================================

def save(raw_ranked, corrected_ranked, summary):
    with open("results/observer_perturbation_v13_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open("results/observer_perturbation_v13_raw_ranked.json", "w", encoding="utf-8") as f:
        json.dump(raw_ranked, f, indent=2, ensure_ascii=False)

    with open("results/observer_perturbation_v13_corrected_ranked.json", "w", encoding="utf-8") as f:
        json.dump(corrected_ranked, f, indent=2, ensure_ascii=False)


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n=== OMNIA V13 REAL-LIKE BATCH TRIAGE ===\n")

    rows = run()

    raw_ranked = sorted(rows, key=lambda x: x["raw_opi"], reverse=True)
    corrected_ranked = sorted(rows, key=lambda x: x["corrected_opi"], reverse=True)

    summary = {
        "raw": summarize(raw_ranked),
        "corrected": summarize(corrected_ranked),
    }

    print(json.dumps(summary, indent=2))

    print("\n=== TOP 10 CORRECTED ===")
    for r in corrected_ranked[:10]:
        print(
            f"{r['corrected_opi']:.6f} | raw={r['raw_opi']:.6f} | "
            f"len={r['length']} | sent={r['num_sentences']} | {r['text']}"
        )

    save(raw_ranked, corrected_ranked, summary)

    print("\nSaved:")
    print("- results/observer_perturbation_v13_summary.json")
    print("- results/observer_perturbation_v13_raw_ranked.json")
    print("- results/observer_perturbation_v13_corrected_ranked.json")


if __name__ == "__main__":
    main()