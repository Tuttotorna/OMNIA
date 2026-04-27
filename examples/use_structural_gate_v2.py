import json
import pickle
from pathlib import Path

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
MODEL_PATH = Path("models/structural_gate_v2.pkl")
OUTPUT_PATH = Path("results/omnia_structural_gate_v2.json")


def features(text):
    tokens = text.split()
    length = len(tokens)
    digits = sum(c.isdigit() for c in text)
    symbols = sum(not c.isalnum() and not c.isspace() for c in text)
    total_chars = max(len(text), 1)

    return [
        length,
        digits / total_chars,
        symbols / total_chars,
        sum(1 for token in tokens if not token.isalnum()),
    ]


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Missing model. Run examples/train_structural_gate_v2.py first."
        )

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    rows = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            fts = features(item["text"])
            gate = model.predict([fts])[0]

            rows.append({
                "id": item["id"],
                "prompt": item["prompt"],
                "text": item["text"],
                "gate": gate,
                "features": {
                    "length": fts[0],
                    "digit_density": fts[1],
                    "symbol_density": fts[2],
                    "malformed": fts[3],
                },
            })

    counts = {
        "PASS": 0,
        "REVIEW": 0,
        "REJECT": 0,
    }

    for row in rows:
        counts[row["gate"]] += 1

    total = len(rows)

    summary = {
        "total": total,
        "counts": counts,
        "ratios": {
            key: value / total for key, value in counts.items()
        },
    }

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "rows": rows,
        }, f, indent=2, ensure_ascii=False)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()