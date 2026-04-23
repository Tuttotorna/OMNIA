# GSM Symbolic v1 — OMNIA Run 01

## Status

This document freezes the first OMNIA-style group scoring run for
GSM Symbolic v1.

This is an early structural scoring result built on top of the baseline pipeline.

It is NOT a general validation of OMNIA.
It is NOT a real-model benchmark.
It is a first bounded structural readout over controlled variants.

---

## Purpose

The purpose of this run is to verify that the GSM Symbolic v1 pipeline
can produce group-level structural distinctions across near-equivalent variants.

More precisely, this run tests whether the scoring layer can separate:

- robust groups
- fragile groups
- regime-shifted groups

using aggregate group behavior rather than single-case correctness alone.

---

## Input

Source file:

- `examples/gsm_symbolic_v1_model_outputs.jsonl`

Scoring script:

- `examples/run_gsm_symbolic_v1_omnia.py`

Output file:

- `examples/gsm_symbolic_v1_omnia_scores.jsonl`

---

## Aggregate Result

Total template groups:

- `5`

Group status distribution:

- `ROBUST`: `1`
- `FRAGILE`: `4`
- `COLLAPSED`: `0`

Regime shift flags:

- `True`: `4`
- `False`: `1`

---

## Per-Template Result

### `gsm_v1_t001`

- total variants: `5`
- correct count: `3`
- accuracy: `0.600`
- unique answers: `3`
- failure count: `2`
- most common answer: `14`
- regime shift flag: `True`
- group status: `FRAGILE`

### `gsm_v1_t002`

- total variants: `5`
- correct count: `5`
- accuracy: `1.000`
- unique answers: `2`
- failure count: `0`
- most common answer: `15`
- regime shift flag: `False`
- group status: `ROBUST`

### `gsm_v1_t003`

- total variants: `5`
- correct count: `4`
- accuracy: `0.800`
- unique answers: `3`
- failure count: `1`
- most common answer: `13`
- regime shift flag: `True`
- group status: `FRAGILE`

### `gsm_v1_t004`

- total variants: `5`
- correct count: `4`
- accuracy: `0.800`
- unique answers: `3`
- failure count: `1`
- most common answer: `31`
- regime shift flag: `True`
- group status: `FRAGILE`

### `gsm_v1_t005`

- total variants: `5`
- correct count: `4`
- accuracy: `0.800`
- unique answers: `3`
- failure count: `1`
- most common answer: `22`
- regime shift flag: `True`
- group status: `FRAGILE`

---

## Main Observation

The scoring layer does not treat all template groups as equivalent.

One group (`gsm_v1_t002`) appears structurally stable across all tested variants.

The other four groups show measurable instability through some combination of:

- reduced group accuracy
- increased answer dispersion
- non-zero failure count
- regime shift flag activation

This is the first bounded indication that group-level behavior under controlled perturbation
can reveal structural differences not captured by single-case correctness alone.

---

## Why This Matters

A simple accuracy view would say that several groups look "mostly fine":

- `0.800`
- `0.800`
- `0.800`

But the group-level readout shows that these are not equivalent to the `1.000` robust case.

This matters because the experiment is explicitly about **stability under controlled transformation**,
not only about isolated correctness.

In other words:

> similar average correctness does not imply similar structural stability.

---

## Interpretation Boundary

This result must be interpreted conservatively.

It does NOT show:

- general OMNIA superiority
- real-model reasoning evaluation
- semantic validation
- large-scale benchmark evidence

It shows only that:

- the scoring layer runs
- the protocol generates group-level separation
- controlled variants can expose fragile behavior patterns

---

## Limitation

This run is based on a mock baseline solver.

That means:

- the scoring signal is real within the pipeline
- but the benchmark is not yet externally meaningful

The next necessary step is to preserve the protocol and replace the mock solver
with a real model while keeping the same dataset and scoring logic.

---

## Conclusion

OMNIA Run 01 is successful as an early structural scoring freeze.

It establishes that:

- the pipeline is complete
- group-level scoring is possible
- robust vs fragile distinctions already emerge in a bounded setting

This is sufficient to justify the next phase:

- real-model execution
- fixed-protocol rerun
- direct comparison between baseline and model behavior