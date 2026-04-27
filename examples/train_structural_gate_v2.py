# ============================================================
# OMNIA — STRUCTURAL GATE V2 (LEARNED)
# ============================================================
#
# Trains a simple classifier to replace rule-based gate
# using structural features only.
#
# Input:
# data/real_structural_dataset_v1.jsonl
#
# Output:
# models/structural_gate_v2.pkl
# results/structural_gate_v2_report.json
#
# ============================================================

import json
import pickle
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


INPUT_PATH = Path("data/real_structural_dataset_v1.jsonl")
MODEL_PATH = Path("models/structural_gate_v2.pkl")
REPORT_PATH = Path("results/structural_gate_v2_report.json")


# ------------------------------------------------------------
# FEATURES
# ------------------------------------------------------------
def features(text):
    tokens = text.split()
    length = len(tokens)

    digits = sum(c.isdigit() for c in text)
    symbols = sum(not c.isalnum() and not c.isspace() for c in text)

    total_chars = max(len(text), 1)

    digit_density = digits / total_chars
    symbol_density = symbols / total_chars
    malformed = sum(1 for t in tokens if not t.isalnum())

    return [
        length,
        digit_density,
        symbol_density,
        malformed,
    ]


# ------------------------------------------------------------
# LABEL (BOOTSTRAP FROM V1 LOGIC)
# ------------------------------------------------------------
def label_from_rules(f):
    length, digit_d, symbol_d, malformed = f

    if length <= 2:
        return "REJECT"

    if length <= 8:
        if malformed > 0 or symbol_d > 0.15:
            return "REVIEW"
        return "PASS"

    if digit_d > 0.20 or symbol_d > 0.20 or malformed > 3:
        return "REVIEW"

    return "PASS"


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------
def load():
    X = []
    y = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            text = item["text"]

            fts = features(text)
            label = label_from_rules(fts)

            X.append(fts)
            y.append(label)

    return X, y


# ------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------
def train():
    X, y = load()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    matrix = confusion_matrix(y_test, y_pred).tolist()

    return model, report, matrix


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    model, report, matrix = train()

    MODEL_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.parent.mkdir(exist_ok=True)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "classification_report": report,
            "confusion_matrix": matrix
        }, f, indent=2)

    print("\n=== STRUCTURAL GATE V2 TRAINED ===\n")
    print("Model saved:", MODEL_PATH)
    print("Report saved:", REPORT_PATH)


if __name__ == "__main__":
    main()