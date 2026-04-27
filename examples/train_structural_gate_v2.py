import json
import pickle
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
MODEL_PATH = Path("models/structural_gate_v2.pkl")
REPORT_PATH = Path("results/structural_gate_v2_report.json")


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


def label_from_v1_rules(f):
    length, digit_density, symbol_density, malformed = f

    if length <= 2:
        return "REJECT"

    if length <= 8:
        if malformed > 0 or symbol_density > 0.15:
            return "REVIEW"
        return "PASS"

    if digit_density > 0.20 or symbol_density > 0.20 or malformed > 3:
        return "REVIEW"

    return "PASS"


def main():
    x = []
    y = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            fts = features(item["text"])
            label = label_from_v1_rules(fts)

            x.append(fts)
            y.append(label)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    report = classification_report(
        y_test,
        y_pred,
        output_dict=True,
        zero_division=0
    )

    matrix = confusion_matrix(y_test, y_pred).tolist()

    MODEL_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.parent.mkdir(exist_ok=True)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "classification_report": report,
            "confusion_matrix": matrix,
            "train_size": len(x_train),
            "test_size": len(x_test),
        }, f, indent=2)

    print("Model saved:", MODEL_PATH)
    print("Report saved:", REPORT_PATH)
    print(classification_report(y_test, y_pred, zero_division=0))


if __name__ == "__main__":
    main()