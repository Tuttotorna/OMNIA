# GSM Symbolic v1 — Local FLAN-T5 Small Run 01

## Status

This document freezes the first local instruction-model run for
GSM Symbolic v1 using `google/flan-t5-small`.

This is not a positive validation result.

It is a bounded collapse-control run.

---

## Purpose

The purpose of this run is to test whether the GSM Symbolic v1 protocol
and the OMNIA scoring layer can process a weak local instruction model
and detect large-scale structural failure.

This run is useful primarily as:

- pipeline validation
- local-model sanity check
- collapse-control reference

---

## Environment

Repository: `OMNIA`  
Model: `google/flan-t5-small`  
Execution mode: local CPU inference  
Core import: OK  
Core tests: passed

Observed core test result:

- `47 passed`

---

## Input

Question file:

- `examples/gsm_symbolic_v1_questions.jsonl`

Model runner:

- `examples/run_gsm_symbolic_v1_local_flan.py`

OMNIA scoring script:

- `examples/run_gsm_symbolic_v1_omnia.py`

Generated outputs:

- `examples/gsm_symbolic_v1_model_outputs.jsonl`
- `examples/gsm_symbolic_v1_omnia_scores.jsonl`

---

## Aggregate Result

Model accuracy:

- `0 / 25`
- `0.000`

Group status distribution:

- `ROBUST`: `0`
- `FRAGILE`: `0`
- `COLLAPSED`: `5`

Regime shift flags:

- `True`: `2`
- `False`: `3`

---

## Per-Template Result

### `gsm_v1_t001`

- total variants: `5`
- correct count: `0`
- accuracy: `0.000`
- unique answers: `2`
- failure count: `5`
- most common answer: `4`
- regime shift flag: `False`
- group status: `COLLAPSED`

### `gsm_v1_t002`

- total variants: `5`
- correct count: `0`
- accuracy: `0.000`
- unique answers: `4`
- failure count: `5`
- most common answer: `6`
- regime shift flag: `True`
- group status: `COLLAPSED`

### `gsm_v1_t003`

- total variants: `5`
- correct count: `0`
- accuracy: `0.000`
- unique answers: `2`
- failure count: `5`
- most common answer: `4`
- regime shift flag: `False`
- group status: `COLLAPSED`

### `gsm_v1_t004`

- total variants: `5`
- correct count: `0`
- accuracy: `0.000`
- unique answers: `2`
- failure count: `5`
- most common answer: `9`
- regime shift flag: `False`
- group status: `COLLAPSED`

### `gsm_v1_t005`

- total variants: `5`
- correct count: `0`
- accuracy: `0.000`
- unique answers: `3`
- failure count: `5`
- most common answer: `0`
- regime shift flag: `True`
- group status: `COLLAPSED`

---

## Main Observation

The local model does not show partial competence on this task.

Instead, it exhibits broad structural failure across all template groups.

This produces a full collapse profile under the current protocol.

However, the collapse is not identical across all groups.

Two distinct patterns appear:

### Pattern A — rigid collapse
Groups produce a narrow answer set and fail uniformly.

Observed in:

- `gsm_v1_t001`
- `gsm_v1_t003`
- `gsm_v1_t004`

### Pattern B — dispersed collapse
Groups fail uniformly but show higher answer dispersion and regime-shift activation.

Observed in:

- `gsm_v1_t002`
- `gsm_v1_t005`

This means the scoring layer still captures internal variation
inside an overall collapse regime.

---

## Interpretation Boundary

This run does NOT show:

- real benchmark strength
- meaningful arithmetic competence
- robust-vs-fragile separation in a competent model
- external validation of OMNIA

It shows only that:

- the local inference pipeline runs correctly
- valid output files are produced
- OMNIA scoring processes the run correctly
- total collapse is detectable and classifiable

---

## Why This Run Still Matters

This run is useful as a control.

It establishes a reference case where:

- correctness is absent
- collapse is global
- regime shift may still vary by group

This helps separate:

- **fine fragility**
from
- **total incompetence**

That distinction is important for later experiments.

---

## Limitation

`google/flan-t5-small` is too weak for this benchmark
to serve as an externally meaningful reasoning test.

Therefore this run should not be used as evidence of benchmark success.

It should be used only as:

- a negative control
- a collapse reference
- a local pipeline validation artifact

---

## Conclusion

Local FLAN-T5 Small Run 01 is successful only as a collapse-control run.

It confirms that the protocol and scoring layer can detect
full structural failure in a weak local model.

It does not yet provide the kind of partial-competence regime
needed to test fine separation between robust and fragile groups.

That requires a stronger model under the same frozen protocol.