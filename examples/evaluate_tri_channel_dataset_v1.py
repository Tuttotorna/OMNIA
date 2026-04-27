# ============================================================
# OMNIA — TRI-CHANNEL DATASET EVALUATION V1
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

def observers():
    return [
        o_identity,
        o_add_explanation(),
        o_optimize_for_clarity(),
        o_reformat_bullets(),
    ]

def features(text):
    tokens = text.split()
    digit = sum(c.isdigit() for c in text)
    symbol = sum((not c.isalnum()) and (not c.isspace()) for c in text)

    malformed = 0
    for t in tokens:
        if any(c.isdigit() for c in t) and any(c.isalpha() for c in t):
            malformed += 1

    return {
        "length": len(tokens),
        "digit_density": digit / max(1, len(text)),
        "symbol_density": symbol / max(1, len(text)),
        "malformed": malformed
    }

def classify_channel(raw, f):
    if f["length"] <= 2:
        return "atomic"
    elif f["length"] <= 8:
        return "short"
    else:
        return "long"

def run():
    lens = ObserverPerturbation()
    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            opis = []
            for o in observers():
                out = lens.measure(x=item["text"], observer=o)
                d = asdict(out) if is_dataclass(out) else vars(out)
                opis.append(d["opi"])

            raw = sum(opis) / len(opis)
            fts = features(item["text"])
            pred = classify_channel(raw, fts)

            rows.append({
                "label": item["label"],
                "pred": pred,
                "raw": raw,
                **fts
            })

    return rows

def evaluate(rows):
    labels = ["atomic", "short", "long", "good"]
    matrix = {l: {p: 0 for p in ["atomic", "short", "long"]} for l in labels}

    for r in rows:
        matrix[r["label"]][r["pred"]] += 1

    print("\n=== CONFUSION MATRIX ===")
    for l in labels:
        print(l, "->", matrix[l])

    # Accuracy excluding "good"
    correct = 0
    total = 0

    for r in rows:
        if r["label"] == "good":
            continue
        total += 1
        if r["label"] == r["pred"]:
            correct += 1

    print("\n=== STRUCTURAL ACCURACY ===")
    print(correct, "/", total, "=", correct / total if total else 0)

def main():
    rows = run()
    evaluate(rows)

if __name__ == "__main__":
    main()