# OMNIA - External Validation Plan

## Purpose

This document defines the first external validation path for OMNIA core.

Its purpose is not to prove universal value.

Its purpose is narrower:

to test whether OMNIA adds measurable value over a simple baseline on an external bounded task.

---

## Validation principle

OMNIA must not be validated by internal description alone.

The relevant question is:

> does baseline + OMNIA perform better than baseline alone on a bounded external task?

This comparison must be made with:

- a fixed task
- a fixed baseline
- explicit labels
- fixed metrics
- claims declared in advance

---

## First validation task

### Task
Support-response screening.

### Reason for choosing it

This task is suitable because:

- outputs are short and readable
- plausibility errors are common
- many weak outputs look acceptable on the surface
- false accepts are easy to understand operationally
- OMNIA is structurally aligned with this failure mode

This task is bounded enough for a first external validation pass.

---

## Target behavior under test

The specific behavior under test is:

> detection of superficially acceptable but structurally fragile support-style outputs

This is the narrowest external task that matches OMNIA's current design.

---

## Validation setup

The comparison will use two systems:

### Baseline
A simple screening rule or baseline acceptance policy without OMNIA.

### Baseline + OMNIA
The same baseline followed by OMNIA structural screening.

The baseline must be intentionally simple and explicit.

Examples of admissible baselines:

- accept all outputs that meet a minimal readability threshold
- accept all outputs that are grammatical and non-empty
- accept all outputs that pass a fixed surface heuristic
- accept all outputs not rejected by a predefined hard filter

The exact baseline must be frozen before evaluation.

---

## Unit of evaluation

Each evaluation item is a single support-style response.

Each item must have:

- a response text
- a reference label
- a baseline decision
- an OMNIA structural report
- a final combined decision under the baseline + OMNIA condition

---

## Labeling objective

Each item must be labeled according to whether it is operationally acceptable or not inside the bounded task.

The external label must answer this question:

> should this response be allowed to pass forward?

This is a bounded acceptability label, not a universal truth label.

---

## Primary hypothesis

The primary hypothesis is:

> baseline + OMNIA reduces false accepts relative to baseline alone

This is the main value claim under test.

---

## Secondary hypothesis

The secondary hypothesis is:

> baseline + OMNIA does not increase false rejects so much that the gain in false accept reduction becomes operationally useless

This prevents trivial "block everything" behavior from being counted as success.

---

## Primary metric

### False Accept Rate (FAR)

Definition:

- an item is a false accept when it is not operationally acceptable by label
- but the evaluated system allows it to pass forward

Primary comparison:

- FAR of baseline alone
- FAR of baseline + OMNIA

Success direction:

- lower is better

---

## Secondary metric

### False Reject Rate (FRR)

Definition:

- an item is a false reject when it is operationally acceptable by label
- but the evaluated system blocks or escalates it

Secondary comparison:

- FRR of baseline alone
- FRR of baseline + OMNIA

Success direction:

- lower is better, but small increases may be acceptable if FAR decreases materially

---

## Additional metric

### Review Rate

Because OMNIA uses bounded gate outcomes, it is useful to track how often items are sent to review.

Definition:

- proportion of items mapped to non-pass states such as `RISK`, `NO_GO`, or `UNSTABLE`
- depending on the frozen operational mapping used in the experiment

This metric helps detect whether performance gains are caused by excessive blocking.

---

## Operational mapping

A frozen mapping from OMNIA gate outputs to operational outcomes must be defined before evaluation.

Example mapping:

- `GO` -> pass
- `RISK` -> review
- `NO_GO` -> block
- `UNSTABLE` -> block

This mapping may be changed only before the experiment starts.

It must not be changed after observing results.

---

## Success criterion

OMNIA will be considered to show bounded external value if:

1. baseline + OMNIA produces a lower false accept rate than baseline alone
2. the false reject increase remains operationally tolerable
3. the result is reproducible on the frozen evaluation set

This is the only success criterion for this first validation pass.

---

## Failure criterion

OMNIA fails this validation pass if any of the following occurs:

- false accept rate does not improve over baseline
- false accept rate improves only by causing unacceptable false reject explosion
- results depend on unstable ad hoc thresholds
- results are not reproducible

---

## Data requirement

The evaluation set must be external to OMNIA's internal descriptive material.

It may be:

- a publicly available support-response dataset
- a bounded external corpus manually labeled for this task
- a frozen set of externally sourced responses collected under explicit rules

The set must be frozen before final scoring.

---

## Reproducibility requirement

The validation must be reproducible.

This requires:

- frozen dataset
- frozen baseline
- frozen OMNIA version
- frozen gate mapping
- frozen metric definitions
- machine-readable outputs

If these are not fixed, the validation is not valid.

---

## What this validation does not claim

This validation does not claim:

- universal superiority of OMNIA
- semantic understanding
- general truth measurement
- production readiness
- safety certification
- cross-domain dominance

It claims only a bounded result on one external task if success criteria are met.

---

## Minimal experiment summary

```text
task: support-response screening
comparison: baseline vs baseline + OMNIA
primary metric: false accept rate
secondary metric: false reject rate
goal: reduce false accepts without making the system operationally useless


---

Canonical validation sentence

OMNIA must show value by improving a bounded external decision surface, not by describing itself better.