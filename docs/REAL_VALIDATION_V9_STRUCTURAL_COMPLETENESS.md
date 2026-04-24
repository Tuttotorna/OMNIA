# Real Validation V9 — Structural Completeness

## Dataset

- `examples/real_validation_v6_harder.jsonl`

## Model

- `google/flan-t5-large`

---

## Gate change

V9 extends V8 with structural completeness signals:

- final-answer enforcement
- expression detection
- answer completeness / granularity check

---

## Results

- GO: `8`
- NO_GO: `12`

---

## Alignment

- TP: `12`
- FN: `0`
- FP: `0`
- TN: `8`
- Precision: `1.000`
- Recall: `1.000`

---

## Interpretation

V8 failed on structural incompleteness:

- intermediate reasoning instead of final answer
- expressions instead of outputs
- partial answers

V9 introduces completeness constraints and eliminates all observed false negatives.

---

## Conclusion

This is the first closed loop:

test → failure → analysis → targeted correction → full recovery

---

## Status

Still minimal:

- small dataset
- single model

But now:

- structural mismatch detected (V8)
- structural completeness enforced (V9)

This moves OMNIA from error detection toward answer validation.