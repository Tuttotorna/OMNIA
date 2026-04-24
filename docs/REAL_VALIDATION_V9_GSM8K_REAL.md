# Real Validation V9 — GSM8K Real Slice

## Dataset

- Source: `gsm8k`
- Split: `test[:20]`
- Saved slice: `examples/gsm8k_real_slice.jsonl`

## Model

- `google/flan-t5-large`

---

## Model Performance

- Correct: `0 / 20`
- Accuracy: `0.000`

---

## OMNIA Gate Results

- GO: `0`
- NO_GO: `20`

---

## Alignment

- TP: `20`
- FN: `0`
- FP: `0`
- TN: `0`
- Precision: `1.000`
- Recall: `1.000`

---

## Interpretation

OMNIA V9 correctly rejects all observed incorrect outputs on this real GSM8K slice.

However, the model produced no correct answers in this run.

Therefore, this test confirms failure detection, but does not test positive selectivity because there are no true negatives.

---

## Status

Useful result:

- real public dataset
- all observed failures rejected
- no missed failures

Limitation:

- no correct model outputs
- no false-positive stress test

Next step:

- run the same slice with a stronger model that produces at least some correct answers