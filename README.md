# OMNIA - Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18379486.svg)](https://doi.org/10.5281/zenodo.18379486)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a bounded post-hoc structural measurement core.

Its task is to measure whether an output remains structurally admissible under controlled transformations and convert that measurement into a bounded gate result.

OMNIA operates after inference.

It does not:

- interpret semantics
- replace reasoning
- train a model
- optimize a model
- act as a truth oracle
- function as an autonomous decision-maker

OMNIA measures structure only.

---

## Start here

If only one entry point is needed, start here:

- [`docs/MINIMAL_PROOF.md`](./docs/MINIMAL_PROOF.md)

If the goal is to check the validated current state of the repository, read:

- [`docs/CORE_STATUS.md`](./docs/CORE_STATUS.md)

If the goal is to understand the primary public-facing case, read:

- [`docs/FIRST_PUBLIC_CASE.md`](./docs/FIRST_PUBLIC_CASE.md)

These three files are the shortest path through the repository.

---

## Current validated status

Minimal OMNIA core is materially executable.

Validated state:

- editable install works
- canonical imports work
- canonical output schema works
- smoke test works
- tests pass

Verified test result:

```text
47 passed in 0.14s

Verified smoke test output:

{
  "case_id": "quick-smoke-001",
  "drift_score": 0.405538,
  "gate_status": "RISK",
  "iri_score": 0.405538,
  "limit_triggered": false,
  "omega_score": 0.594462,
  "reason_code": "low_omega",
  "sei_score": 0.67557
}

Terminal confirmation:

OK: OMNIA core executed

This proves software-level existence of a minimal OMNIA core.
It does not prove scientific closure or benchmark superiority.


---

Core claim

The canonical claim of OMNIA is narrow:

> A bounded post-hoc structural measurement layer can detect silent fragility in outputs that appear superficially acceptable, detect when structural continuation becomes unjustified under controlled transformations, and convert that result into a bounded operational gate output.



Anything broader than this is outside scope.


---

Core principle

Structural stability is what survives controlled representational variation.

OMNIA does not begin from semantic interpretation.

OMNIA begins from structural behavior under transformation.

It asks:

what remains stable

what drifts

what degrades

what becomes irrecoverable

when continuation stops being admissible


The result is a bounded structural report, not a semantic verdict.


---

Non-negotiable boundary

measurement != cognition != decision

This is a hard architectural constraint.

Measurement computes structural stability, fragility, saturation, irreversibility, and drift.

Cognition interprets what those measurements mean in a task or model context.

Decision chooses what action should follow.


OMNIA belongs strictly to the measurement layer.

Its gate is a bounded operational conversion of measurement, not an autonomous decision layer.


---

Canonical pipeline

input
-> optional framing normalization
-> controlled structural transformations
-> structural comparison
-> omega / sei / iri / drift
-> limit check
-> gate status
-> bounded structural report

This is the canonical minimal pipeline of OMNIA core.


---

10-second quick start

Install from repository root:

pip install -e . -U --no-cache-dir

Run tests:

pytest -q tests

Run minimal smoke test:

python examples/quick_omnia_test.py


---

Canonical output contract

Every valid OMNIA core run must return at least these fields:

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code


This is the bounded structural report surface of OMNIA core.


---

Gate outputs

OMNIA allows only these bounded gate outcomes:

GO

RISK

NO_GO

UNSTABLE


GO

Structural behavior remains admissible under tested conditions.

RISK

The case remains admissible, but fragility or drift is elevated.

NO_GO

Structural continuation is not admissible under tested conditions.

UNSTABLE

The structural profile is sufficiently degraded or inconsistent that operational reliability cannot be assumed inside scope.


---

Core metrics

OMNIA uses a bounded structural metric family:

omega_score - structural residue or stability under admissible transformations

sei_score - remaining structural extractability / non-exhaustion

iri_score - structural irreversibility / non-recoverable degradation

drift_score - structural displacement or instability across variants


These metrics define the minimal readable structural profile of a case.


---

Limit layer

OMNIA includes a formal limit layer.

Its role is to detect when further structural continuation inside the admissible transformation space is no longer justified.

A triggered limit does not mean:

truth has been proven

the task is solved

the output is universally safe

the system understood the problem


A triggered limit means only:

further structural continuation inside scope is not justified

the analysis has reached exhaustion, collapse, or non-admissibility


This is a structural stop condition, not a metaphysical claim.


---

What OMNIA includes

Inside canonical OMNIA scope:

post-hoc structural measurement

controlled structural transformations

structural comparison across bounded variants

structural fragility detection

structural drift detection

structural exhaustion detection

structural irreversibility detection

formal limit triggering

bounded gate conversion

machine-readable report generation

deterministic or reproducible scoring logic

rebuildable executable examples

testable bounded behavior



---

What OMNIA excludes

Outside canonical OMNIA scope:

semantic reasoning

universal truth adjudication

training-time optimization

model fine-tuning

hidden-state introspection as a requirement

architecture-specific instrumentation as a requirement

autonomous decision systems

general safety certification

broad ecosystem ideology

manifesto layers

cognition frameworks

total theories of reality


If a component depends on one of these, it is not OMNIA core.


---

Repository structure

omnia/
examples/
docs/
tests/
pyproject.toml
README.md

Main areas:

omnia/ -> core structural measurement logic

examples/ -> runnable examples and frozen result artifacts

docs/ -> architecture, scope, output schema, proof, status, public case

tests/ -> executable validation of core behavior



---

Key repository documents

docs/MINIMAL_PROOF.md
shortest proof that the minimal core exists as working software

docs/CORE_STATUS.md
validated repository status and current execution result

docs/FIRST_PUBLIC_CASE.md
current primary public-facing case

docs/ARCHITECTURE.md
architectural boundary and pipeline

docs/SCOPE.md
canonical scope and exclusion rules

docs/OUTPUT_SCHEMA.md
canonical output contract



---

Current examples

The repository includes bounded runnable examples and result artifacts, including:

examples/quick_omnia_test.py

examples/demo_profiles.jsonl

examples/demo_profiles_results.jsonl

examples/llm_surface_cases.jsonl

examples/llm_surface_results.jsonl

examples/support_response_cases.jsonl

examples/support_response_results.jsonl

examples/rag_answer_cases.jsonl

examples/rag_answer_results.jsonl

examples/surface_ok_cases.jsonl

examples/surface_ok_results.jsonl

examples/omnia_inevitability_case_v0/



---

Result analysis

Generic analyzer:

python examples/analyze_results.py --input examples/llm_surface_results.jsonl
python examples/analyze_results.py --input examples/surface_ok_results.jsonl
python examples/analyze_results.py --input examples/support_response_results.jsonl
python examples/analyze_results.py --input examples/rag_answer_results.jsonl
python examples/analyze_results.py --input examples/demo_profiles_results.jsonl

Domain-specific analyzers:

python examples/analyze_surface_ok_results.py
python examples/analyze_llm_surface_results.py
python examples/analyze_support_response_results.py
python examples/analyze_rag_answer_results.py

Rebuild artifacts:

python examples/rebuild_all_results.py
python examples/rebuild_and_analyze_all.py


---

Tests

Run the full core test suite:

pytest -q tests

The repository currently validates passing bounded core behavior through the test suite.


---

Intended use

OMNIA is designed to be:

post-hoc

bounded

structural

model-agnostic

reproducible

non-semantic by design


Typical bounded use cases include:

silent fragility detection in superficially acceptable outputs

post-hoc auditing of generated outputs

structural consistency checks

structural drift detection

structural exhaustion detection

bounded release gating

representation-dependent fragility sensing


OMNIA is useful where an output may look acceptable on the surface but remain structurally weak under controlled variation.


---

Reproducibility requirement

OMNIA must remain reproducible.

This means:

the same input under the same configuration must produce the same report

transformation logic must be explicit

thresholds must be documented

outputs must be serializable

scoring logic must be inspectable


If a result cannot be reproduced, it is not valid OMNIA core evidence.


---

Bounded-use principle

OMNIA is valid only under bounded use.

This requires:

bounded inputs

bounded transformations

bounded metrics

bounded outputs

bounded claims


Any attempt to expand OMNIA into an unbounded general theory breaks the scope of the system.


---

Strong non-claims

OMNIA does not prove truth in the universal sense.

OMNIA does not solve reasoning.

OMNIA does not replace task evaluation.

OMNIA does not certify safety in the broad sense.

OMNIA does not explain meaning.

OMNIA does not function as an autonomous decision-maker.

OMNIA does not require belief in any broader theoretical framework to remain valid inside scope.


---

Repository role

This repository is the canonical implementation repository for OMNIA core.

Its function is narrow:

define the core

implement the core

document the core

demonstrate the core

validate the core


Historical branches, exploratory prototypes, and broader ecosystem material belong elsewhere.

For broader context and neighboring branches, see:

OMNIABASE

lon-mirror


OMNIA should be read as the canonical structural measurement core, not as the entire ecosystem.


---

Status sentence

OMNIA is now a real minimal executable structural measurement core.


---

License

MIT License