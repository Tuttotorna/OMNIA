# OMNIA — Tri-Channel Classifier V1 Result

## 1. Objective

Train a classifier to distinguish structural regimes:

```text
atomic
short
long

The "good" class is excluded because it is not a failure regime.


---

2. Dataset

Source:

data/structural_dataset_v1.jsonl

Size:

300 samples

Training setup:

train: 152
test:  66

Only non-good samples used.


---

3. Features

The classifier uses simple structural features:

- length
- digit density
- symbol density
- malformed tokens

No semantic information is used.


---

4. Results

Classification Report

precision = 1.00
recall    = 1.00
f1-score  = 1.00
accuracy  = 1.00

Confusion Matrix

[22  0  0]
[ 0 22  0]
[ 0  0 22]

Perfect separation across all classes.


---

5. Feature Importance

length           → 0.4573
digit_density    → 0.2724
symbol_density   → 0.2452
malformed        → 0.0251

Key observation:

length is the dominant structural signal


---

6. Interpretation

This result confirms:

structural regimes are separable

Specifically:

atomic, short, long form distinct regions
in feature space


---

7. Important Limitation

dataset is synthetic

Implications:

- patterns are clean
- class boundaries are simplified
- real-world noise is not fully represented

Therefore:

this is not proof of real-world performance


---

8. Correct Claim

On a controlled synthetic structural dataset,
tri-channel regimes are perfectly separable
using simple structural features.


---

9. Relation to Previous Results

V18 → discovered tri-channel structure
V19–V21 → failed manual gating
V1 classifier → succeeds with learned boundary

Key shift:

from rules → to learned separation


---

10. Conclusion

OMNIA structural regimes are real and learnable.

However, reliable deployment requires:

- real-world datasets
- richer features
- proper calibration

Current status:

diagnostic → validated
classifier → promising (synthetic only)
deployment → not yet

