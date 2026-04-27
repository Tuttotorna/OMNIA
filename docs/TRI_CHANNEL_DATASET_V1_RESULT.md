# OMNIA — Tri-Channel Dataset V1 Result

## 1. Setup

Dataset:

```text
data/structural_dataset_v1.jsonl

Size:

300 samples

Classes:

- good   (structurally stable)
- atomic (atomic malformed)
- short  (short malformed)
- long   (long incoherent)

Important:

"good" is a structural label, not semantic correctness


---

2. Method

Tri-channel classification:

length <= 2   → atomic
length <= 8   → short
else          → long

Measurement:

OMNIA observer perturbation (multi-observer OPI averaging)


---

3. Results

Confusion Matrix

atomic -> { atomic: 74, short: 0,  long: 0 }
short  -> { atomic: 30, short: 41, long: 0 }
long   -> { atomic: 0,  short: 12, long: 61 }
good   -> { atomic: 0,  short: 82, long: 0 }


---

Structural Accuracy (excluding "good")

176 / 218 = 0.8073


---

4. Interpretation

Strong signals

atomic detection → very strong (74/74)
long detection   → strong (61/73)

Weak region

short class is unstable:

- 30 short → misclassified as atomic
- 12 long  → misclassified as short

This indicates:

short regime is structurally ambiguous


---

"Good" class behavior

good → mostly classified as short (82 cases)

This is expected because:

classification is length-based, not semantic


---

5. Key Insight

Structural failure is multi-regime,
but regime boundaries are not cleanly separable
with simple heuristics.


---

6. What Works

✔ atomic regime is well isolated
✔ long regime is mostly separable
✔ tri-channel decomposition is meaningful


---

7. What Fails

✘ short regime is unstable
✘ simple threshold classification is insufficient
✘ "good" cannot be separated without semantic layer


---

8. Conclusion

Tri-channel decomposition is valid.

However:

- it is a diagnostic structure
- not a reliable classifier with naive rules


---

9. Next Step

Required to progress:

- feature-based classification (not only length)
- statistical calibration
- larger datasets
- possible learned boundary (not manual thresholds)


---

10. Status

Dataset V1 → validated
Tri-channel → validated
Classifier  → not yet robust