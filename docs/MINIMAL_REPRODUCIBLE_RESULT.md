# OMNIA — Minimal Reproducible Result

## Purpose

This document records the minimal reproducible result currently demonstrated by OMNIA.

It refers to the executable demo:

```text
examples/silent_failure_gate_demo.py
```

and its documentation:

```text
docs/SILENT_FAILURE_GATE_DEMO.md
```

The purpose is to preserve a clear, testable, reviewer-facing result:

```text
surface-valid output != structurally stable output
```

---

## Core result

The minimal reproducible result is:

```text
stable_output    -> Surface PASS -> OMNIA GO
fragile_output   -> Surface PASS -> OMNIA RISK
collapsed_output -> Surface FAIL -> OMNIA STOP
```

The central case is:

```text
fragile_output -> Surface PASS -> OMNIA RISK
```

This is the silent failure pattern.

It shows that an output can pass surface-level checks while still being structurally fragile under controlled perturbation.

---

## Boundary

This result follows the OMNIA boundary:

```text
measurement != inference != decision
```

The result does not claim semantic truth.

The result does not claim factual correctness.

The result does not claim safety.

The result does not make deployment decisions.

It records a structural measurement outcome only.

---

## What was run

From the repository root:

```bash
python examples/silent_failure_gate_demo.py
```

The repository test suite was also run:

```bash
python -m pytest -q
```

Observed test result:

```text
47 passed
```

---

## Expected demo output pattern

A successful run should show this pattern:

```text
Case: case_001 — stable_output
Surface check: PASS
OMNIA structural gate: GO

Case: case_002 — fragile_output
Surface check: PASS
OMNIA structural gate: RISK

Case: case_003 — collapsed_output
Surface check: FAIL
OMNIA structural gate: STOP
```

The exact numeric values may change if the demo is modified.

The structural pattern should remain the same for the current version.

---

## Recorded metric pattern

The current demo produces the following conceptual metric profile:

```text
stable_output
  omega: high
  iri: low / moderate
  sei: high
  gate: GO

fragile_output
  omega: degraded
  iri: elevated
  sei: degraded
  gate: RISK

collapsed_output
  omega: low
  iri: high
  sei: low
  gate: STOP
```

The important point is not the absolute number.

The important point is the separation:

```text
surface PASS + structural GO
surface PASS + structural RISK
surface FAIL + structural STOP
```

---

## Why this result matters

Ordinary checks often detect visible failure:

```text
empty output
missing answer
wrong format
obvious malformed response
```

The important failure mode is different:

```text
surface check: PASS
structural gate: RISK
```

This means the output appears acceptable at the surface level but degrades under controlled structural perturbation.

That is the minimal operational value of OMNIA.

---

## What this result demonstrates

This result demonstrates:

```text
a surface-valid output can be structurally fragile
```

It also demonstrates that structural evaluation can be separated from semantic evaluation.

The demo does not need to decide whether the answer is true.

It only needs to expose structural instability.

---

## What this result does not demonstrate

This result does not demonstrate:

```text
semantic correctness
factual truth
universal AI safety
deployment readiness
complete hallucination detection
benchmark replacement
production-grade reliability
```

It is a minimal structural measurement result.

It should be read narrowly.

---

## Correct interpretation

Correct reading:

```text
OMNIA can flag a surface-valid output as structurally risky under controlled perturbation.
```

Incorrect reading:

```text
OMNIA proves the output is false.
OMNIA proves the output is unsafe.
OMNIA replaces semantic evaluation.
OMNIA decides deployment.
```

OMNIA does none of those things.

The final decision remains external.

---

## Minimal reviewer check

A reviewer can reproduce the result by running:

```bash
python examples/silent_failure_gate_demo.py
python -m pytest -q
```

The reviewer should verify:

```text
[ ] stable_output returns GO
[ ] fragile_output returns RISK
[ ] collapsed_output returns STOP
[ ] fragile_output passes the surface check
[ ] fragile_output still receives structural RISK
[ ] pytest passes
[ ] the boundary measurement != inference != decision is preserved
```

The most important check is:

```text
fragile_output:
  Surface check: PASS
  OMNIA structural gate: RISK
```

---

## Falsification path

A reviewer should try to modify:

```text
surface checks
perturbations
similarity function
thresholds
case definitions
expected contracts
metric formulas
```

Useful falsification questions:

```text
Does the fragile case remain weaker than the stable case?
Does RISK disappear under reasonable threshold changes?
Can a better structural metric improve separation?
Can real model outputs reproduce the same pattern?
Where does the gate fail?
Where does it overflag?
Where does it underflag?
```

Failure cases are useful.

They define the boundary of the system.

---

## Relationship to OMNIA position

This result supports the main OMNIA position:

```text
Before semantic correctness, check structural admissibility.
Before deployment decision, check structural stability.
Before trusting fluent output, test invariance under transformation.
```

The result is intentionally minimal.

It exists so that the central claim can be inspected without trusting the author.

---

## Current status

Current minimal public chain:

```text
README.md
  -> docs/REVIEWER_ENTRYPOINT.md
  -> docs/OMNIA_POST_HOC_STRUCTURAL_GATE.md
  -> examples/silent_failure_gate_demo.py
  -> docs/SILENT_FAILURE_GATE_DEMO.md
  -> docs/MINIMAL_REPRODUCIBLE_RESULT.md
```

Current executable result:

```text
stable_output    -> Surface PASS -> OMNIA GO
fragile_output   -> Surface PASS -> OMNIA RISK
collapsed_output -> Surface FAIL -> OMNIA STOP
pytest           -> 47 passed
```

---

## Summary

The minimal reproducible result is:

```text
surface check: PASS
OMNIA structural gate: RISK
```

on the `fragile_output` case.

That is the smallest useful demonstration of OMNIA as a post-hoc structural stability gate.

The final boundary remains:

```text
measurement != inference != decision
```