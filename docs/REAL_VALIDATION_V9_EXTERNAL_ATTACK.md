# Real Validation V9 — External Attack Dataset

## Dataset

- `examples/real_validation_v7_external_attack.jsonl`

## Model

- `google/flan-t5-large`

---

## Results

- GO: `11`
- NO_GO: `9`

---

## Alignment

- TP: `9`
- FN: `0`
- FP: `0`
- TN: `11`
- Precision: `1.000`
- Recall: `1.000`

---

## Interpretation

This dataset was constructed to break V9 by introducing:

- misleading arithmetic structures
- expression outputs instead of answers
- partial answers
- subtle entity mismatches

V9 successfully detects all observed failures without blocking correct outputs.

---

## Conclusion

This is a stronger result than previous validations:

- not the same dataset
- not the same failure patterns
- same gate logic

Yet:

- zero false negatives
- zero false positives

---

## Status

Still not fully external validation:

- dataset is synthetic
- not independently produced

But:

- different structure
- adversarial intent
- successful generalization

This is the first evidence of cross-pattern robustness.