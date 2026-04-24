# Real Validation V8 — FLAN-T5-LARGE

## Dataset

- `examples/real_validation_v6_harder.jsonl`

## Model

- `google/flan-t5-large`

---

## Results

- GO: `11`
- NO_GO: `9`

---

## Alignment

- TP: `9`
- FN: `3`
- FP: `0`
- TN: `8`
- Precision: `1.000`
- Recall: `0.750`

---

## Interpretation

On a stronger model, OMNIA V8 still detects most failures while keeping zero false positives.

Compared to the smaller model:

- Recall decreases (0.917 → 0.750)
- Precision remains perfect (no correct outputs blocked)

This indicates:

- partial generalization across models
- remaining blind spots in structural detection

---

## Status

Still minimal:

- small dataset
- single alternative model

Next step: analyze missed failures (FN) and extend structural signals.