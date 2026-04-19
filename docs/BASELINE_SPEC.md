# OMNIA - Baseline Specification

## Purpose

This document defines the baseline system for the first external validation pass of OMNIA core.

Its purpose is to freeze the comparison target before scoring.

OMNIA must be evaluated against a simple explicit baseline, not against an undefined or moving reference.

---

## Validation role

The baseline is the control condition in the first bounded external comparison:

- baseline alone
- baseline + OMNIA

The baseline must be:

- simple
- explicit
- reproducible
- bounded
- weaker than a full review system
- strong enough to be non-trivial

---

## Baseline type

The baseline is a surface-level acceptability filter.

It does not use structural measurement.

It does not use hidden states.

It does not use semantic adjudication beyond simple explicit surface rules.

It is intended to simulate a plausible lightweight screening layer that might exist before deeper review.

---

## Baseline objective

The baseline answers one bounded operational question:

> should this response pass forward based only on simple explicit surface rules?

This is not a truth judgment.
It is a minimal screening decision.

---

## Baseline decision space

The baseline must return one of these operational outcomes:

- `PASS`
- `REVIEW`
- `BLOCK`

These are baseline outcomes only.
They are not OMNIA gate values.

---

## Baseline rules

A support-style response is processed by the baseline using only explicit surface rules.

### Rule 1 - Non-empty response
If the response is empty or whitespace only:

- outcome = `BLOCK`

### Rule 2 - Minimal readability
If the response is non-empty but not readable as a basic support-style sentence:

- outcome = `REVIEW`

Examples:
- broken fragments
- severely malformed text
- obvious corruption

### Rule 3 - Minimal grammatical pass
If the response is readable, grammatical enough at surface level, and non-empty:

- continue baseline screening

This rule does not check whether the response is structurally strong.
It checks only whether it looks minimally acceptable on the surface.

### Rule 4 - Hard failure markers
If the response contains obvious hard-failure characteristics, outcome = `BLOCK`.

Examples may include:
- placeholder-only outputs
- visible generation artifacts
- repeated junk tokens
- explicit corruption strings
- empty-template shells with no operational content

The exact marker list must be frozen before scoring.

### Rule 5 - Surface-readable default
If the response is readable, non-empty, and does not trigger a hard failure marker:

- outcome = `PASS`

This is the main baseline behavior.

---

## Baseline design principle

The baseline is intentionally weak.

It is allowed to pass responses that look superficially acceptable.

That weakness is necessary, because the first OMNIA validation is specifically testing whether OMNIA can reduce false accepts on superficially acceptable but structurally fragile outputs.

If the baseline is too strong, the experiment becomes trivial or redundant.

---

## What the baseline does not use

The baseline must not use:

- OMNIA metrics
- OMNIA gate outputs
- structural transforms
- hidden-state access
- semantic scoring models
- learned classifiers
- post-hoc threshold tuning after observing results
- human reinterpretation after baseline scoring

If any of these are introduced, it is no longer the frozen baseline.

---

## Baseline operational mapping

The baseline outcomes have this meaning:

### PASS
The response is allowed to pass forward under baseline-only screening.

### REVIEW
The response is held for manual or secondary review.

### BLOCK
The response is not allowed to pass forward.

---

## Baseline decision logic summary

Minimal frozen logic:

```text
empty -> BLOCK
surface-corrupted -> BLOCK
not clearly readable -> REVIEW
readable and non-empty with no hard-failure marker -> PASS

This is the canonical baseline for the first validation pass.


---

Relationship to OMNIA

The baseline alone operates without structural measurement.

In the combined condition:

baseline + OMNIA

the same baseline decision surface is followed by OMNIA screening according to a separately frozen operational mapping.

This separation must remain explicit.


---

Why this baseline is acceptable

This baseline is acceptable because it is:

simple

explicit

reproducible

plausible as a lightweight operational filter

weak enough to leave room for OMNIA to demonstrate value


It is not intended to be optimal.

It is intended to be a fair minimal comparison target.


---

Freeze rule

Once the baseline is declared frozen:

the decision rules may not change

the hard-failure marker list may not change

the pass/review/block logic may not change

no threshold or rule may be adjusted after observing final results


If the baseline changes, a new version must be declared.


---

Versioning rule

The baseline must be versioned.

Example:

baseline_support_screening_v1

If rules change materially, the version must change.

No silent mutation is allowed.


---

What this baseline does not claim

This baseline does not claim:

strong operational intelligence

semantic correctness evaluation

structural insight

production adequacy

benchmark quality by itself


It is only a frozen comparison condition for the first OMNIA validation pass.


---

Minimal baseline summary

type: surface-level support-response filter
decision space: PASS / REVIEW / BLOCK
strength: intentionally simple and weak
purpose: comparison target for baseline vs baseline + OMNIA
freeze rule: no rule changes after evaluation begins


---

Canonical baseline sentence

The first OMNIA external validation baseline is a frozen surface-level support-response filter that allows superficially acceptable outputs to pass unless explicit hard failure markers are present.