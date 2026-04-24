# Real Validation V9 — GSM8K Slice

## Dataset

- `examples/gsm8k_slice_omnia.jsonl`

## Model

- `google/flan-t5-large`

---

## Model Performance

- Correct: `1 / 20`
- Accuracy: `0.050`

The model shows systematic failure on basic arithmetic reasoning.

---

## OMNIA Gate Results (V9)

- GO: `1`
- NO_GO: `19`

---

## Alignment

- TP: `19`
- FN: `0`
- FP: `0`
- TN: `1`
- Precision: `1.000`
- Recall: `1.000`

---

## Interpretation

This test evaluates OMNIA on a GSM8K-style reasoning slice.

Observations:

- The model frequently produces:
  - incorrect arithmetic results
  - expressions instead of final answers
  - incomplete outputs

OMNIA V9:

- rejects all structurally invalid outputs
- accepts the only valid final answer

---

## Conclusion

On this slice:

> Structural validity filtering is perfectly aligned with correctness

However:

- the dataset is small
- the model performance is unusually low

Therefore:

- this demonstrates failure detection capability
- not general reasoning evaluation

---

## Status

- Reproducible
- Deterministic
- Strong structural filtering signal

Next step:

- larger GSM8K slice
- multiple models
- external benchmark comparison