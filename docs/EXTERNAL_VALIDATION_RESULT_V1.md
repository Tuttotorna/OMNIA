# OMNIA - External Validation Result V1

## Status

This document records the first bounded external validation result for OMNIA core on the support-response screening task.

This is not a general validation.

It is a small frozen comparison between:

- baseline alone
- baseline + OMNIA

using the frozen dataset, baseline specification, gate mapping, and labeling policy defined in the repository.

---

## Validation setup

### Task
Support-response screening.

### Dataset
`data/support_screening_external_v1.jsonl`

### Dataset size
- total cases: `20`
- PASS labels: `9`
- FAIL labels: `11`

### Baseline
Frozen surface-level support-response filter.

### OMNIA operational mapping
- `GO -> PASS`
- `RISK -> REVIEW`
- `NO_GO -> BLOCK`
- `UNSTABLE -> BLOCK`

### Combination rule
Final outcome is the stricter result between baseline and mapped OMNIA output.

---

## Baseline result

```json
{
  "false_accept_rate": 0.818182,
  "false_accepts": 9,
  "false_reject_rate": 0.0,
  "false_rejects": 0,
  "review_count": 0,
  "review_rate": 0.0,
  "total_cases": 20,
  "total_fail_labels": 11,
  "total_pass_labels": 9,
  "true_accepts": 9,
  "true_rejects": 2
}


---

Baseline + OMNIA result

{
  "false_accept_rate": 0.636364,
  "false_accepts": 7,
  "false_reject_rate": 0.0,
  "false_rejects": 0,
  "review_count": 2,
  "review_rate": 0.1,
  "total_cases": 20,
  "total_fail_labels": 11,
  "total_pass_labels": 9,
  "true_accepts": 9,
  "true_rejects": 4
}


---

Observed delta

False accepts

baseline: 9

baseline + OMNIA: 7


Absolute reduction:

2 fewer false accepts

False accept rate

baseline: 0.818182

baseline + OMNIA: 0.636364


Absolute FAR reduction:

0.181818

False rejects

baseline: 0

baseline + OMNIA: 0


No false reject increase was observed in this run.

Review rate

baseline: 0.0

baseline + OMNIA: 0.1


OMNIA introduced review on 2 cases out of 20.


---

Minimal conclusion

On this small frozen support-response dataset, OMNIA improved the bounded decision surface relative to the baseline:

false accepts decreased

false rejects did not increase

the cost was a limited review rate


This is the first bounded external signal that OMNIA may add operational value on superficially acceptable but fragile support-style outputs.


---

What this result means

This result supports the following narrow claim:

> on a small frozen external support-response screening set, baseline + OMNIA performed better than baseline alone on false accepts without increasing false rejects



This is a bounded empirical result.


---

What this result does not mean

This result does not prove:

general superiority of OMNIA

production readiness

broad external validity

semantic understanding

universal truth measurement

benchmark-scale effectiveness


The dataset is too small and the evaluation too narrow for those claims.


---

Current interpretation

The correct interpretation is:

OMNIA shows bounded external value on a small frozen support-screening set.

This is stronger than internal self-description. It is much weaker than broad validation.


---

Next required step

The next step is not theoretical expansion.

The next step is one of the following:

1. inspect the reviewed cases to verify they are meaningfully fragile


2. expand the frozen dataset beyond 20 items


3. repeat the same protocol on a second bounded external set




---

Canonical result sentence

OMNIA reduced false accepts from 9 to 7 on the first frozen external support-screening dataset, with no observed increase in false rejects and a review rate of 10%.