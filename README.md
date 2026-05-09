# OMNIA — Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19820729.svg)](https://doi.org/10.5281/zenodo.19820729)

**OMNIA** is a post-hoc structural measurement core.

It measures structural behavior after an output, answer, trajectory, or representation already exists.

It is not a model.
It is not a semantic judge.
It is not a truth oracle.
It is not a final decision system.

OMNIA measures structural admissibility, coherence, fragility, invariance, instability, and degradation under controlled transformations or perturbations.

Core boundary:

```text
measurement != inference != decision
```

---

## What OMNIA is

OMNIA is a structural measurement layer.

It evaluates whether a produced structure remains stable, admissible, or degraded under structural pressure.

It can measure signals such as:

- structural coherence
- fragility
- invariance under transformation
- instability under perturbation
- irreversibility
- saturation or exhaustion
- compatibility with an expected output contract
- observer-induced structural drift

In one sentence:

> OMNIA measures how much structure survives when form, constraints, observer frame, or nearby representation changes.

---

## What OMNIA is not

OMNIA is not:

- a semantic correctness evaluator
- a truth engine
- a reasoning engine
- a contradiction detector by itself
- a replacement for domain expertise
- a final decision system
- a claim that structural validity equals truth

A structurally valid output can still be semantically wrong.

A semantically correct output can still be structurally fragile.

This distinction is intentional.

---

## Core boundary

```text
structural validity != semantic correctness
measurement != inference != decision
```

OMNIA stays inside the measurement layer.

It can produce signals.

It can expose fragility.

It can recommend that a pipeline stop, continue, retry, or escalate through an external gate.

But OMNIA does not decide final truth.

---

## Correct system role

The correct pipeline is:

```text
Input / output / trajectory
  ↓
OMNIA structural measurement
  ↓
External semantic evaluator or domain layer
  ↓
External decision layer
```

OMNIA removes or flags structurally invalid, unstable, incomplete, collapsed, or malformed outputs before semantic evaluation or operational decision.

---

## What OMNIA detects well

OMNIA is strongest when failures are structural.

Examples:

- incomplete outputs
- malformed answers
- format violations
- expression instead of final answer
- unstable output under variation
- structurally hollow responses
- mismatch between requested output contract and produced output
- instability under observer perturbation
- atomic collapse
- short malformed output
- long incoherent drift

Examples of structural failures:

```text
"5 * 3 ="       -> incomplete
"5 * 3 = 15"   -> not final-only if scalar final answer was required
"blue"         -> incomplete if expected contract is "blue key"
"LDL"          -> atomic malformed output
```

---

## What OMNIA does not detect by itself

OMNIA does not reliably detect pure semantic errors when the answer is structurally well-formed.

Examples:

```text
"2" instead of "4"
"wolf" instead of "dog"
"blue" instead of "black"
```

These answers may be wrong, but structurally admissible.

OMNIA may return:

```text
GO
```

This is not a bug.

It is the boundary of the system.

---

## Validation status

The repository contains executable validation and diagnostic material.

Current package sanity check:

```text
import omnia        OK
pip install -e .    OK
pytest              47 passed
```

This means the repository is technically executable in a clean environment.

It does not mean OMNIA is universally valid.

It means the current package, tests, and examples are operational.

See:

- [`VALIDATION_SUMMARY.md`](VALIDATION_SUMMARY.md)
- [`README_REAL_VALIDATION_V7.md`](README_REAL_VALIDATION_V7.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)
- [`docs/REPRODUCIBLE_RUNS.md`](docs/REPRODUCIBLE_RUNS.md)
- [`docs/RESULTS_STATUS.md`](docs/RESULTS_STATUS.md)

---

## Minimal usage

Clone and test:

```bash
git clone https://github.com/Tuttotorna/OMNIA.git
cd OMNIA
python -m pip install -e .
python -m pytest -q
```

Run a minimal example:

```bash
python examples/quick_omnia_test.py
```

---

## Repository structure

```text
omnia/       core package
docs/        documentation and validation reports
examples/    runnable experiments and result builders
tests/       test suite
results/     stored validation outputs
data/        datasets and input records
```

---

## Main documentation

- [`MASTER_POSITION.md`](MASTER_POSITION.md)
- [`CORE_SCOPE.md`](CORE_SCOPE.md)
- [`VALIDATION_SUMMARY.md`](VALIDATION_SUMMARY.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/SCOPE.md`](docs/SCOPE.md)
- [`docs/CORE_STATUS.md`](docs/CORE_STATUS.md)
- [`docs/OMNIA_SCOPE_BOUNDARY_V1.md`](docs/OMNIA_SCOPE_BOUNDARY_V1.md)
- [`docs/OMNIA_WHERE_IT_WORKS_V1.md`](docs/OMNIA_WHERE_IT_WORKS_V1.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

---

## Relation to the MB-X.01 / L.O.N. ecosystem

OMNIA is the structural measurement core inside the MB-X.01 / L.O.N. ecosystem.

A clean ecosystem reading is:

```text
OMNIAMIND  = orchestration of cognitive / reasoning flow
OMNIA      = structural measurement core
OMNIA-LIMIT = stop / continue / retry / escalate boundary
Decision   = external human or system layer
```

OMNIA must remain measurement-only.

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19820729
https://doi.org/10.5281/zenodo.19820729
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA is a structural measurement core.

It measures structural behavior after the fact.

It does not infer truth.

It does not replace semantic evaluation.

It does not make final decisions.

Its central boundary is:

```text
measurement != inference != decision
```

---

## OMNIA — Public Boundary

- OMNIA is a post-hoc structural measurement engine.
- OMNIA is not a truth oracle.
- OMNIA is not a semantic judge.
- OMNIA is not a decision engine.
- OMNIA does not infer meaning.
- OMNIA does not decide truth.
- OMNIA does not replace external review.
- measurement != inference != decision
- decision remains external

This section is a public boundary clarification. It does not change the repository core logic.
