# ============================================================
# OMNIA — TRI-CHANNEL CLASSIFIER TRAINING V1
# ============================================================

import json
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

INPUT_PATH = Path("data/structural_dataset_v1.jsonl")

# ------------------------------------------------------------
# FEATURE EXTRACTION
# ------------------------------------------------------------

def extract_features(text):
    tokens = text.split()

    digit = sum(c.isdigit() for c in text)
    symbol = sum((not c.isalnum()) and (not c.isspace()) for c in text)

    malformed = 0
    for t in tokens:
        if any(c.isdigit() for c in t) and any(c.isalpha() for c in t):
            malformed += 1

    return [
        len(tokens),                 # length
        digit / max(1, len(text)),   # digit density
        symbol / max(1, len(text)),  # symbol density
        malformed                   # malformed tokens
    ]

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

X = []
y = []

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)

        if item["label"] == "good":
            continue  # exclude

        X.append(extract_features(item["text"]))
        y.append(item["label"])

# ------------------------------------------------------------
# SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# ------------------------------------------------------------
# EVALUATE
# ------------------------------------------------------------

y_pred = clf.predict(X_test)

print("\n=== CLASSIFICATION REPORT ===\n")
print(classification_report(y_test, y_pred))

# ------------------------------------------------------------
# FEATURE IMPORTANCE
# ------------------------------------------------------------

features = ["length", "digit_density", "symbol_density", "malformed"]

print("\n=== FEATURE IMPORTANCE ===\n")
for name, score in zip(features, clf.feature_importances_):
    print(f"{name}: {score:.4f}")