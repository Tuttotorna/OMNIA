# OMNIA - Account Access Hollow Result V1

## Status

This document records the first focused benchmark result for OMNIA on the account-access hollow response family.

This is not a general-domain validation.

It is a bounded result on a narrow failure family where earlier broader benchmarks had already shown a small signal.

---

## Benchmark identity

Benchmark:

```text
account_access_hollow_responses_v1

Task family:

account access / account recovery / verification / login blockage

Dataset:

data/account_access_hollow_responses_v1.jsonl

Dataset size:

total cases: 20

PASS labels: 6

FAIL labels: 14



---

Baseline result

{
  "false_accept_rate": 1.0,
  "false_accepts": 14,
  "false_reject_rate": 0.0,
  "false_rejects": 0,
  "review_count": 0,
  "review_rate": 0.0,
  "total_cases": 20,
  "total_fail_labels": 14,
  "total_pass_labels": 6,
  "true_accepts": 6,
  "true_rejects": 0
}

Interpretation:

The weak surface baseline allowed every FAIL case to pass.


---

Baseline + OMNIA result

{
  "false_accept_rate": 0.5,
  "false_accepts": 7,
  "false_reject_rate": 0.0,
  "false_rejects": 0,
  "review_count": 7,
  "review_rate": 0.35,
  "total_cases": 20,
  "total_fail_labels": 14,
  "total_pass_labels": 6,
  "true_accepts": 6,
  "true_rejects": 7
}

Interpretation:

OMNIA reduced the false-accept surface by sending 7 hollow FAIL cases to review, without introducing any false reject on PASS cases.


---

Observed delta

False accepts

baseline: 14

baseline + OMNIA: 7


Absolute reduction:

7 fewer false accepts

False accept rate

baseline: 1.0

baseline + OMNIA: 0.5


Absolute FAR reduction:

0.5

Relative reduction:

50%

False rejects

baseline: 0

baseline + OMNIA: 0


No false reject increase was observed.

Review rate

baseline: 0.0

baseline + OMNIA: 0.35


OMNIA introduced review on 7 cases out of 20.


---

Minimal conclusion

On the focused account-access hollow benchmark, OMNIA showed a materially stronger signal than in the broader support benchmarks:

false accepts dropped from 14 to 7

false reject rate remained 0.0

the intercepted cases belonged to the intended hollow-response family


This is the first benchmark where OMNIA shows not only a real signal, but also a useful signal-to-cost profile inside a narrow task family.


---

What this result means

This result supports the following narrow claim:

> on a focused benchmark of polite but operationally hollow account-access responses, baseline + OMNIA reduced false accepts by 50% without increasing false rejects



This is a bounded empirical result.


---

What this result does not mean

This result does not prove:

general support-domain validity

cross-domain robustness

production readiness

universal structural filtering

semantic understanding

broad benchmark superiority


The result is still narrow and benchmark-specific.


---

Current interpretation

The correct interpretation is:

OMNIA shows strong bounded value on the focused account-access hollow response family.

This is stronger than the earlier broad-benchmark signal. It is still much narrower than general external validation.


---

Why this result matters

Earlier broader benchmarks showed:

a real signal

but weak coverage

and limited selectivity


This focused benchmark shows:

stronger signal magnitude

improved selectivity

correct preservation of operational PASS cases

consistent interception of hollow account-access deflections


So the current evidence suggests that OMNIA is not yet broad, but is becoming meaningful in a specific operational niche.


---

Next required step

The next step is not more tuning inside the same benchmark.

The next step is one of:

1. record case-level analysis of the 7 intercepted cases


2. replicate the same focused benchmark with a second frozen set


3. test whether the same tuned runner transfers to a nearby access/recovery dataset




---

Canonical result sentence

On the focused account-access hollow benchmark, OMNIA reduced false accepts from 14 to 7 with no observed increase in false rejects.