# Real Validation V9 — GSM8K Easy Slice

## Model

- `google/flan-t5-large`

## Model Performance

- Correct: `1 / 20`
- Accuracy: `0.050`

## OMNIA Gate Results

- GO: `1`
- NO_GO: `19`

## Alignment

- TP: `19`
- FN: `0`
- FP: `0`
- TN: `1`
- Precision: `1.000`
- Recall: `1.000`

## Interpretation

OMNIA V9 rejected all observed incorrect outputs and allowed the only correct output.

This gives a minimal positive-selectivity signal, but the slice remains highly imbalanced.

## Limitation

The test is still dominated by incorrect model outputs.

Next target:

- 5–8 correct outputs out of 20
- preserve FN = 0
- preserve FP near 0