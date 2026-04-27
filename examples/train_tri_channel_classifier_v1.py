# ============================================================
# OMNIA — TRI-CHANNEL CLASSIFIER TRAINING V1
# ============================================================
#
# Purpose:
# Train a simple classifier to distinguish structural regimes:
#
# - atomic
# - short
# - long
#
# NOTE:
# The "good" class is excluded from this classifier because it is not
# a structural failure regime.
#
# ============================================================

import json
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

INPUT_PATH = Path("data/structural_dataset_v1.jsonl")
RESULT_PATH = Path("results/tri_channel_classifier_v1_summary.json")


def extract_features(text):
    tokens = text.split()

    digit = sum(c.isdigit() for c in text)
    symbol = sum((not c.isalnum()) and (not c.isspace()) for c in text)

    malformed = 0
    for token in tokens:
        has_alpha = any(c.isalpha() for c in token)
        has_digit = any(c.isdigit() for c in token)
        has_symbol = any((not c.isalnum()) for c in token)

        if (has_alpha and has_digit) or (has_symbol and len(token) > 3):
            malformed += 1

    return [
        len(tokens),
        digit / max(1, len(text)),
        symbol / max(1, len(text)),
        malformed,
    ]


def load_data():
    x = []
    y = []

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            if item["label"] == "good":
                continue

            x.append(extract_features(item["text"]))
            y.append(item["label"])

    return x, y


def main():
    x, y = load_data()

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y,
    )

    clf = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    labels = ["atomic", "short", "long"]

    report = classification_report(
        y_test,
        y_pred,
        labels=labels,
        output_dict=True,
        zero_division=0,
    )

    matrix = confusion_matrix(y_test, y_pred, labels=labels)

    feature_names = [
        "length",
        "digit_density",
        "symbol_density",
        "malformed",
    ]

    importance = {
        name: float(score)
        for name, score in zip(feature_names, clf.feature_importances_)
    }

    summary = {
        "labels": labels,
        "classification_report": report,
        "confusion_matrix": matrix.tolist(),
        "feature_importance": importance,
        "train_size": len(x_train),
        "test_size": len(x_test),
    }

    RESULT_PATH.parent.mkdir(exist_ok=True)

    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("\n=== CLASSIFICATION REPORT ===\n")
    print(classification_report(y_test, y_pred, labels=labels, zero_division=0))

    print("\n=== CONFUSION MATRIX ===")
    print(labels)
    print(matrix)

    print("\n=== FEATURE IMPORTANCE ===")
    for name, score in importance.items():
        print(f"{name}: {score:.4f}")

    print("\nSaved:", RESULT_PATH)


if __name__ == "__main__":
    main()