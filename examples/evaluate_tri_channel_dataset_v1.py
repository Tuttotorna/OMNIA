# ============================================================
# OMNIA — TRI-CHANNEL DATASET EVALUATION V1
# ============================================================
#
# Purpose:
# Evaluate tri-channel structural classification on dataset V1
#
# NOTE:
# - "good" is NOT a semantic correctness label
# - accuracy is computed excluding "good"
#
# ============================================================

import json
from pathlib import Path
from dataclasses import asdict, is_dataclass

from omnia.lenses.observer_perturbation import (
    ObserverPerturbation,
    o_identity,
    o_add_explanation,
    o_optimize_for_clarity,
    o_reformat_bullets,
)

INPUT_PATH = Path("data/structural_dataset_v1.jsonl")
RESULT_PATH = Path("results/tri_channel_dataset_v1_summary.json")


def observers():
    return [
        o_identity,
        o_add_explanation(),
        o_optimize_for_clarity(),
        o_reformat_bullets(),
    ]


def features(text):
    tokens = text.split()
    return {
        "length": len(tokens)
    }


def classify_channel(f):
    if f["length"] <= 2:
        return "atomic"
    elif f["length"] <= 8:
        return "short"
    else:
        return "long"


def run():
    lens = ObserverPerturbation()
    obs = observers()
    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            opis = []
            for o in obs:
                out = lens.measure(x=item["text"], observer=o)
                d = asdict(out) if is_dataclass(out) else vars(out)
                opis.append(d["opi"])

            raw = sum(opis) / len(opis)
            fts = features(item["text"])
            pred = classify_channel(fts)

            rows.append({
                "id": item["id"],
                "label": item["label"],
                "pred": pred,
                "raw_opi": raw,
                "text": item["text"],
                **fts
            })

    return rows


def evaluate(rows):
    labels = ["atomic", "short", "long", "good"]
    preds = ["atomic", "short", "long"]

    matrix = {l: {p: 0 for p in preds} for l in labels}

    for r in rows:
        matrix[r["label"]][r["pred"]] += 1

    correct = 0
    total = 0

    for r in rows:
        if r["label"] == "good":
            continue
        total += 1
        if r["label"] == r["pred"]:
            correct += 1

    summary = {
        "total": len(rows),
        "non_good_total": total,
        "non_good_correct": correct,
        "structural_accuracy_excluding_good": correct / total if total else 0,
        "confusion_matrix": matrix
    }

    return summary


def main():
    rows = run()
    summary = evaluate(rows)

    RESULT_PATH.parent.mkdir(exist_ok=True)

    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("\n=== CONFUSION MATRIX ===")
    for label, preds in summary["confusion_matrix"].items():
        print(label, "->", preds)

    print("\n=== STRUCTURAL ACCURACY EXCLUDING GOOD ===")
    print(
        summary["non_good_correct"],
        "/",
        summary["non_good_total"],
        "=",
        summary["structural_accuracy_excluding_good"]
    )

    print("\nSaved:", RESULT_PATH)


if __name__ == "__main__":
    main()