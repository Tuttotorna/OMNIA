# OMNIA V7 vs Baseline Simple V1

## Setup

- Dataset: 16 mixed cases (QA, reasoning, RAG)
- Model: google/flan-t5-base

---

## Results

| Method               | TP | FN | FP | TN | Precision | Recall |
|---------------------|---:|---:|---:|---:|----------:|-------:|
| OMNIA V7            | 10 |  0 |  0 |  6 |     1.000 |  1.000 |
| Baseline Simple V1  |  0 | 10 |  0 |  6 |     0.000 |  0.000 |

---

## Interpretation

- OMNIA detects all observed errors (TP = 10, FN = 0)
- OMNIA does not block correct outputs (FP = 0)

- Baseline detects no errors (TP = 0, FN = 10)

---

## Key Point

OMNIA provides measurable value over a trivial heuristic.

It captures failure modes that simple rules completely miss.

---

## Status

- Minimal comparison
- Single dataset
- Single model

No claim of generality.

Further validation required.