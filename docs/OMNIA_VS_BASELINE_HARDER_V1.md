# OMNIA vs Baseline — Harder Validation V1

## Setup

- Dataset: `examples/real_validation_v6_harder.jsonl`
- Model: `google/flan-t5-base`
- Same rules (no tuning between V7 and V8 except structural logic change)

---

## Results

| Method | TP | FN | FP | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| OMNIA V8 | 11 | 1 | 0 | 8 | 1.000 | 0.917 |
| Baseline Majority V2 | 3 | 9 | 0 | 8 | 1.000 | 0.250 |

---

## Interpretation

The previous gate (V7) collapsed on this dataset.

V8 introduces structural mismatch detection and restores performance:

- Recall improves from 0.25 → 0.917
- False positives remain zero

The baseline fails to generalize beyond simple heuristics.

---

## Conclusion

This is the first evidence that:

> structural signals can recover failure detection where surface heuristics fail

---

## Status

Still limited:

- small dataset
- single model

But now:

- failure mode identified
- improvement demonstrated
- direction validated