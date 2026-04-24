# Real Validation V7 SUPER — OMNIA Gate

## Setup

- Dataset: `examples/real_validation_v3_dataset_expanded.jsonl`
- Model: `google/flan-t5-base`
- Tasks: QA, reasoning, RAG
- Total cases: 16

---

## Model Performance

- Correct: 6 / 16
- Accuracy: 0.375

The model fails systematically on:

- simple arithmetic
- basic factual QA
- entity attribution errors

---

## OMNIA Gate Results (V7)

- GO: 6
- NO_GO: 10
- UNSTABLE: 0

---

## Alignment with Reality

- TP (real errors detected): 10
- FN (missed errors): 0
- FP (false alarms): 0

---

## Interpretation

OMNIA does not evaluate correctness directly.

It detects structural instability in model outputs.

In this experiment:

- Every real error was intercepted
- No correct answer was blocked
- No instability was missed

---

## Conclusion

This is a minimal empirical proof:

> Structural instability detection ≠ semantic evaluation

OMNIA operates on a different axis than accuracy.

It identifies failure modes that standard metrics do not isolate.

---

## Status

✔ Reproducible  
✔ Deterministic  
✔ Zero false positives  
✔ Zero false negatives (on this dataset)