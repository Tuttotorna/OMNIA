# GSM Symbolic v1 — Baseline Run 01

## Status

This document freezes the first successful pipeline validation run for
GSM Symbolic v1.

This is NOT an OMNIA result.
This is a baseline pipeline result.

The purpose of this run is:

- verify dataset integrity
- verify runner integrity
- verify strict extraction flow
- confirm that controlled variants can expose instability

---

## Environment

Repository: `OMNIA`  
Install mode: editable  
Import status: OK  
Core test suite: passed

Observed test result:

- `47 passed`

---

## Run Target

Script:

- `examples/run_gsm_symbolic_v1_baseline.py`

Input:

- `examples/gsm_symbolic_v1_questions.jsonl`

Output:

- `examples/gsm_symbolic_v1_model_outputs.jsonl`

---

## Aggregate Result

- total cases: `25`
- correct: `20`
- accuracy: `0.800`

---

## Per-Template Summary

- `gsm_v1_t001`: `3/5 = 0.600`
- `gsm_v1_t002`: `5/5 = 1.000`
- `gsm_v1_t003`: `4/5 = 0.800`
- `gsm_v1_t004`: `4/5 = 0.800`
- `gsm_v1_t005`: `4/5 = 0.800`

---

## Observed Pattern

The baseline runner is not uniformly stable across near-equivalent variants.

Observed instability appears especially in:

- `redundant_rephrase`
- `order_shifted`

This confirms that the dataset is capable of exposing variant-sensitive behavior.

---

## Notable Failures

### `gsm_v1_t001`
Incorrect on:

- `redundant_rephrase`
- `order_shifted`

### `gsm_v1_t003`
Incorrect on:

- `order_shifted`

Observed extracted output:

- `-17`

### `gsm_v1_t004`
Incorrect on:

- `order_shifted`

Observed extracted output:

- `37`

### `gsm_v1_t005`
Incorrect on:

- `order_shifted`

Observed extracted output:

- `17`

---

## Interpretation Boundary

This result does NOT validate OMNIA.

This result validates only that:

- the pipeline runs correctly
- strict extraction works
- controlled variants produce measurable instability

---

## Conclusion

Baseline Run 01 is successful as a pipeline freeze.

It provides a stable checkpoint before adding:

- group-level baseline aggregation
- OMNIA fragility scoring
- real model execution
- larger-scale expansion