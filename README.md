# OMNIA - Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18379486.svg)](https://doi.org/10.5281/zenodo.18379486)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a bounded post-hoc structural measurement core.

It measures whether an output remains structurally admissible under controlled transformation and converts that measurement into a bounded gate result.

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

- [`docs/MINIMAL_PROOF.md`](./docs/MINIMAL_PROOF.md)
- [`docs/CORE_STATUS.md`](./docs/CORE_STATUS.md)
- [`docs/FIRST_PUBLIC_CASE.md`](./docs/FIRST_PUBLIC_CASE.md)

These are the shortest entry points into the repository.

---

## Current validated state

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

OK: OMNIA core executed

This is software-level proof that the minimal core exists.
It is not proof of scientific closure or benchmark superiority.


---

Core claim

OMNIA makes one bounded claim:

> A post-hoc structural measurement layer can detect silent fragility in outputs that appear superficially acceptable, detect when structural continuation becomes unjustified under controlled transformations, and convert that result into a bounded operational gate output.



Anything broader is outside scope.


---

Non-negotiable boundary

measurement != cognition != decision

This is a hard architectural constraint.

Measurement computes structural stability, fragility, saturation, irreversibility, and drift.

Cognition interprets what those measurements mean in a task or model context.

Decision chooses what action should follow.


OMNIA belongs strictly to the measurement layer.


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


---

Quick start

Install from repository root:

pip install -e . -U --no-cache-dir

Run tests:

pytest -q tests

Run minimal smoke test:

python examples/quick_omnia_test.py


---

Canonical output contract

Every valid OMNIA core run must return at least:

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

Allowed gate outcomes:

GO

RISK

NO_GO

UNSTABLE


GO means structural behavior remains admissible under tested conditions.
RISK means the case remains admissible, but fragility or drift is elevated.
NO_GO means structural continuation is not admissible under tested conditions.
UNSTABLE means the structural profile is degraded enough that operational reliability cannot be assumed inside scope.

The gate is a bounded conversion of measurement, not autonomous decision.


---

Core metrics

OMNIA uses a bounded structural metric family:

omega_score - structural residue or stability under admissible transformations

sei_score - remaining structural extractability / non-exhaustion

iri_score - structural irreversibility / non-recoverable degradation

drift_score - structural displacement or instability across variants



---

Limit layer

OMNIA includes a formal limit layer.

A triggered limit does not mean:

truth has been proven

the task is solved

the output is universally safe

the system understood the problem


It means only that further structural continuation inside scope is not justified.


---

Scope

OMNIA includes:

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


OMNIA excludes:

semantic reasoning

universal truth adjudication

training-time optimization

model fine-tuning

hidden-state introspection as a requirement

architecture-specific instrumentation as a requirement

autonomous decision systems

general safety certification

manifesto layers

total theories of reality



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

examples/ -> runnable examples and bounded result artifacts

docs/ -> architecture, scope, output schema, proof, status, public case

tests/ -> executable validation of core behavior



---

Key documents

docs/MINIMAL_PROOF.md

docs/CORE_STATUS.md

docs/FIRST_PUBLIC_CASE.md

docs/ARCHITECTURE.md

docs/SCOPE.md

docs/OUTPUT_SCHEMA.md

docs/POSITIONING.md



---

Current examples

Core examples and artifacts include:

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



---

Reproducibility

OMNIA must remain reproducible.

This means:

the same input under the same configuration must produce the same report

transformation logic must be explicit

thresholds must be documented

outputs must be serializable

scoring logic must be inspectable


If a result cannot be reproduced, it is not valid OMNIA core evidence.


---

Strong non-claims

OMNIA does not:

prove truth in the universal sense

solve reasoning

replace task evaluation

certify safety in the broad sense

explain meaning

function as an autonomous decision-maker



---

Repository role

This repository is the canonical implementation repository for OMNIA core.

Its function is narrow:

define the core

implement the core

document the core

demonstrate the core

validate the core


OMNIA should be read as a bounded structural measurement core, not as the entire ecosystem.


---

Broader context

For broader ecosystem context, see:

OMNIABASE

lon-mirror



---

Status sentence

OMNIA is now a real minimal executable structural measurement core.


---

License

MIT License