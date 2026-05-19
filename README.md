# OMNIA — Post-Hoc Structural Stability Gate for AI Outputs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19820729.svg)](https://doi.org/10.5281/zenodo.19820729)

**OMNIA** is a post-hoc structural stability gate for AI outputs.

It measures whether an output, answer, trajectory, or representation remains structurally stable after it has already been produced and before it is evaluated semantically or used in an operational decision.

Core thesis:

```text
Before evaluating whether an AI output is semantically correct,
we should verify whether it is structurally stable enough to be evaluated.
```

OMNIA is not a model.

OMNIA is not a semantic judge.

OMNIA is not a truth oracle.

OMNIA is not a final decision system.

OMNIA measures structural admissibility, coherence, fragility, invariance, instability, irreversibility, saturation, and degradation under controlled transformations or perturbations.

Core boundary:

```text
measurement != inference != decision
```

---

## Start here

If this is your first contact with OMNIA, start with:

- [`docs/REVIEWER_ENTRYPOINT.md`](docs/REVIEWER_ENTRYPOINT.md)
- [`docs/OMNIA_POST_HOC_STRUCTURAL_GATE.md`](docs/OMNIA_POST_HOC_STRUCTURAL_GATE.md)
- [`CORE_SCOPE.md`](CORE_SCOPE.md)
- [`MASTER_POSITION.md`](MASTER_POSITION.md)
- [`VALIDATION_SUMMARY.md`](VALIDATION_SUMMARY.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

The shortest correct reading is:

```text
OMNIA is a post-hoc structural stability gate for AI outputs.
```

The shortest incorrect reading is:

```text
OMNIA decides whether an output is true.
```

OMNIA does not decide truth.

OMNIA measures structural behavior.

---

## Reviewer path

For external reviewers, use:

```text
README.md
  -> docs/REVIEWER_ENTRYPOINT.md
  -> examples/silent_failure_gate_demo.py
  -> docs/SILENT_FAILURE_GATE_DEMO.md
  -> VALIDATION_SUMMARY.md
```

Minimal run:

```bash
python examples/silent_failure_gate_demo.py
python -m pytest -q
```

Expected pattern:

```text
stable_output    -> Surface PASS -> OMNIA GO
fragile_output   -> Surface PASS -> OMNIA RISK
collapsed_output -> Surface FAIL -> OMNIA STOP
```

Core boundary:

```text
measurement != inference != decision
```

---

## Why OMNIA exists

Modern AI systems can produce outputs that are fluent, plausible, well-formatted, and superficially acceptable.

However:

```text
surface-valid output != structurally stable output
```

An output can pass normal checks while still being structurally fragile.

It can appear acceptable while collapsing under small changes in prompt, constraint, representation, observer frame, or nearby input.

OMNIA targets this failure mode.

It introduces a prior question before semantic evaluation:

```text
Is this output structurally stable enough to be evaluated?
```

This is the core operational role of OMNIA.

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
- structural degradation
- residual structural stability

In one sentence:

```text
OMNIA measures how much structure survives when form, constraints,
observer frame, or nearby representation changes.
```

---

## What OMNIA is not

OMNIA is not:

- a semantic correctness evaluator
- a truth engine
- a reasoning engine
- a contradiction detector by itself
- a hallucination detector by itself
- a benchmark replacement
- a safety certificate
- a replacement for domain expertise
- a final decision system
- a claim that structural validity equals truth

A structurally valid output can still be semantically wrong.

A semantically correct output can still be structurally fragile.

This distinction is intentional.

---

## Core boundary

OMNIA is defined by a strict boundary:

```text
structural validity != semantic correctness
measurement          != inference          != decision
signal               != judgment           != action
```

OMNIA stays inside the measurement layer.

It can produce structural signals.

It can expose fragility.

It can flag instability.

It can show when an output should not proceed blindly into semantic evaluation or deployment.

But OMNIA does not decide final truth.

Decision remains external.

---

## Correct system role

The correct pipeline is:

```text
Input / output / trajectory
  ↓
OMNIA structural measurement
  ↓
Structural signal
  ↓
External semantic evaluator or domain layer
  ↓
External decision layer
```

More explicitly:

```text
AI output
  ↓
controlled transformation or perturbation
  ↓
structural measurement
  ↓
GO / RISK / STOP / ESCALATE signal
  ↓
external semantic evaluation
  ↓
external decision
```

OMNIA can remove or flag structurally invalid, unstable, incomplete, collapsed, or malformed outputs before semantic evaluation or operational decision.

It does not replace those later layers.

---

## Main operational claim

The safest and strongest public claim is:

```text
OMNIA detects when an output is structurally unstable under controlled transformation,
before that output is evaluated semantically or used in deployment decisions.
```

This claim is bounded.

It is testable.

It does not require OMNIA to understand meaning.

It does not require OMNIA to prove truth.

It only requires OMNIA to measure structural behavior under defined transformations.

---

## Silent failure target

The central failure mode is silent structural failure.

A silent failure occurs when an output passes surface checks but fails structural stability checks.

Typical pattern:

```text
surface check:        PASS
format check:         PASS
basic plausibility:   PASS
structural stability: RISK or FAIL
```

This matters because the output appears acceptable while hiding structural fragility.

OMNIA is designed to expose this class of failure.

Key distinction:

```text
visible failure = easy to reject
silent failure  = appears acceptable but collapses under pressure
```

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
- structurally unstable reasoning traces
- surface-valid outputs that degrade under controlled perturbation

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

OMNIA measures structural admissibility.

It does not judge semantic correctness.

---

## Output states

OMNIA may expose structural states such as:

```text
GO
RISK
STOP
ESCALATE
```

These states must be interpreted as structural signals only.

### GO

```text
No structural instability was detected inside the tested regime.
```

GO does not mean:

```text
true
correct
safe
complete
deployable
```

### RISK

```text
The output shows measurable structural fragility or instability.
```

RISK does not mean:

```text
false
dangerous
invalid in all contexts
```

It means that semantic evaluation or deployment should not proceed blindly.

### STOP

```text
The structural process reached a boundary where continuation is non-informative
or structurally illegitimate inside the same admissible space.
```

STOP does not mean global failure.

It means the current diagnostic path has reached its structural limit.

### ESCALATE

```text
The structural signal should be routed to an external evaluator,
human reviewer, domain expert, or separate diagnostic space.
```

ESCALATE is not a final decision by OMNIA.

It is a routing signal for an external layer.

---

## Structural truth

The OMNIA ecosystem uses the thesis:

```text
Structural truth = invariance under transformation
```

This must be read strictly.

It does not mean:

```text
structural truth = semantic truth
structural truth = factual truth
structural truth = moral truth
structural truth = final correctness
```

It means:

```text
a structural property has stronger status when it survives controlled transformation
```

Therefore:

```text
structural validity != semantic correctness
structural signal   != final judgment
measurement         != decision
```

OMNIA does not claim that invariance proves truth in the semantic, factual, or philosophical sense.

OMNIA only treats invariance as evidence of structural stability.

---

## Relation to benchmarks

OMNIA does not replace benchmarks.

Benchmarks usually ask:

```text
Did the model answer correctly?
Did the output match the expected label?
Did the model satisfy the task?
Did humans prefer the output?
```

OMNIA asks:

```text
Did the output remain structurally stable under controlled transformation?
```

Correct relationship:

```text
OMNIA             -> structural admissibility
benchmark         -> task performance
semantic evaluator -> meaning / correctness
decision layer    -> action
```

Incorrect relationship:

```text
OMNIA replaces benchmarks
OMNIA proves semantic correctness
OMNIA decides deployment
```

OMNIA should be understood as a pre-semantic or parallel structural gate.

---

## Silent Failure Gate demo

OMNIA includes a minimal demo showing the core distinction:

```text
surface-valid output != structurally stable output
```

Demo file:

- [`examples/silent_failure_gate_demo.py`](examples/silent_failure_gate_demo.py)

Documentation:

- [`docs/SILENT_FAILURE_GATE_DEMO.md`](docs/SILENT_FAILURE_GATE_DEMO.md)

Run from the repository root:

```bash
python examples/silent_failure_gate_demo.py
```

Expected conceptual pattern:

```text
stable_output    -> Surface PASS -> OMNIA GO
fragile_output   -> Surface PASS -> OMNIA RISK
collapsed_output -> Surface FAIL -> OMNIA STOP
```

The central case is:

```text
fragile_output -> Surface PASS -> OMNIA RISK
```

This demonstrates the silent failure pattern: an output can pass surface checks while degrading under controlled structural perturbation.

The demo does not prove semantic correctness.

It emits structural signal only.

The boundary remains:

```text
measurement != inference != decision
```

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

Expected package sanity pattern:

```text
import omnia        OK
pip install -e .    OK
pytest              passed
```

The repository contains executable validation and diagnostic material.

A clean test run means the current package, tests, and examples are operational.

It does not mean OMNIA is universally valid.

---

## Validation status

The current package sanity check recorded for this repository is:

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

## Reproducibility principle

OMNIA should not require trust.

It should be inspectable, runnable, and falsifiable.

Correct attitude:

```text
Do not trust the claim.
Run the test.
Inspect the artifacts.
Change the thresholds.
Check the failures.
Try to falsify the result.
```

The goal is not to protect OMNIA from failure.

The goal is to expose exactly where it works, where it fails, and where its boundary begins.

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

Core positioning:

- [`docs/OMNIA_POST_HOC_STRUCTURAL_GATE.md`](docs/OMNIA_POST_HOC_STRUCTURAL_GATE.md)
- [`MASTER_POSITION.md`](MASTER_POSITION.md)
- [`CORE_SCOPE.md`](CORE_SCOPE.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/SCOPE.md`](docs/SCOPE.md)
- [`docs/CORE_STATUS.md`](docs/CORE_STATUS.md)
- [`docs/OMNIA_SCOPE_BOUNDARY_V1.md`](docs/OMNIA_SCOPE_BOUNDARY_V1.md)
- [`docs/OMNIA_WHERE_IT_WORKS_V1.md`](docs/OMNIA_WHERE_IT_WORKS_V1.md)

Validation and results:

- [`VALIDATION_SUMMARY.md`](VALIDATION_SUMMARY.md)
- [`README_REAL_VALIDATION_V7.md`](README_REAL_VALIDATION_V7.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)
- [`docs/REPRODUCIBLE_RUNS.md`](docs/REPRODUCIBLE_RUNS.md)
- [`docs/RESULTS_STATUS.md`](docs/RESULTS_STATUS.md)

---

## Relation to the MB-X.01 / L.O.N. ecosystem

OMNIA is the structural measurement core inside the MB-X.01 / L.O.N. ecosystem.

A clean ecosystem reading is:

```text
lon-mirror       = public ecosystem hub
OMNIABASE        = representation / multi-base observation layer
OMNIA            = structural measurement core
OMNIA-RADAR      = structural detection / drift surfacing layer
OMNIA-INVARIANCE = invariance / trajectory-space analysis layer
OMNIAMIND        = orchestration of cognitive / reasoning flow
OMNIA-LIMIT      = terminal boundary / stop condition layer
OMNIA-VALIDATION = evidence / reproducibility layer
Decision         = external human or system layer
```

OMNIA must remain measurement-only.

It does not absorb the other layers.

It does not become the decision layer.

---

## Public boundary

OMNIA is a post-hoc structural measurement engine.

OMNIA is not a truth oracle.

OMNIA is not a semantic judge.

OMNIA is not a decision engine.

OMNIA does not infer meaning.

OMNIA does not decide truth.

OMNIA does not replace external review.

The public boundary is:

```text
measurement != inference != decision
decision remains external
```

This boundary does not weaken OMNIA.

It defines its correct role.

---

## Claims to avoid

Avoid claiming:

```text
OMNIA proves truth
OMNIA detects all hallucinations
OMNIA replaces human judgment
OMNIA proves semantic correctness
OMNIA guarantees safety
OMNIA is artificial consciousness
OMNIA is a universal intelligence layer
OMNIA solves reasoning
```

These claims are unnecessary and too broad.

The strong claim is narrower:

```text
OMNIA measures structural stability under controlled transformation.
```

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

OMNIA is a post-hoc structural stability gate for AI outputs.

It measures structural behavior after an output already exists.

It does not infer truth.

It does not replace semantic evaluation.

It does not make final decisions.

Its strongest operational role is:

```text
Before semantic correctness, check structural admissibility.
Before deployment decision, check structural stability.
Before trusting fluent output, test invariance under transformation.
```

The final boundary remains:

```text
OMNIA measures.
External systems evaluate.
External agents decide.
```

Core boundary:

```text
measurement != inference != decision
```