# OMNIA — Structural Measurement and Gating Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18379486.svg)](https://doi.org/10.5281/zenodo.18379486)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

**OMNIA** is a **post-hoc structural measurement and gating system**.

Its task is to detect **structural fragility** in outputs that may appear acceptable on the surface, measure whether structural continuation remains admissible under controlled transformations, and convert the result into a bounded operational gate output.

OMNIA operates **after inference**.

It does **not**:

- interpret meaning
- replace reasoning
- optimize a model
- train a model
- act as a semantic judge
- function as a truth oracle

OMNIA measures structure only.

---

## 10-second quick start

Install from the repository root:

```bash
pip install -e . -U --no-cache-dir

Run the minimal smoke test:

python examples/quick_omnia_test.py

Expected output pattern:

{
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}

followed by:

OK: OMNIA core executed


---

Minimal JSONL batch demo

Canonical demo input is provided in:

examples/demo_profiles.jsonl

Run the batch demo:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl

Save the results to file:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl -o examples/demo_profiles_results.jsonl

Minimal input example:

{"case_id":"clean_admissible","omega_score":0.84,"sei_score":0.77,"iri_score":0.12,"drift_score":0.15}
{"case_id":"surface_ok_but_fragile","omega_score":0.58,"sei_score":0.55,"iri_score":0.31,"drift_score":0.57}

Example enriched output shape:

{
  "case_id": "clean_admissible",
  "omega_score": 0.84,
  "sei_score": 0.77,
  "iri_score": 0.12,
  "drift_score": 0.15,
  "limit_triggered": false,
  "gate_status": "GO",
  "reason_code": "stable"
}


---

Current mini-results

The repository now includes a small bounded result surface beyond pure internal architecture.

Demo profile result

input: examples/demo_profiles.jsonl

output: examples/demo_profiles_results.jsonl


Surface-ok mini-result

input: examples/surface_ok_cases.jsonl

output: examples/surface_ok_results.jsonl

summary: docs/SURFACE_OK_MINI_RESULT.md


Canonical formula:

surface_ok != always_GO

LLM surface mini-result

input: examples/llm_surface_cases.jsonl

output: examples/llm_surface_results.jsonl

summary: docs/LLM_SURFACE_MINI_RESULT.md


Canonical formula:

surface-readable LLM-like output != always structurally admissible

Support-response mini-result

input: examples/support_response_cases.jsonl

output: examples/support_response_results.jsonl

summary: docs/SUPPORT_RESPONSE_MINI_RESULT.md


Canonical formula:

support-readable output != always structurally admissible

Retrieval-augmented answer mini-result

input: examples/rag_answer_cases.jsonl

output: examples/rag_answer_results.jsonl

summary: docs/RAG_ANSWER_MINI_RESULT.md


Canonical formula:

retrieval-grounded readable output != always structurally admissible

Index of current mini-results:

docs/MINI_RESULTS_INDEX.md


---

Core claim

The canonical claim of OMNIA is:

> A post-hoc structural measurement layer can detect silent fragility in outputs that appear superficially acceptable, detect when structural continuation becomes unjustified, and convert that result into a bounded operational gate output.



Anything broader than this is outside scope.


---

Core principle

> Structural stability is what survives controlled representational variation.



OMNIA does not begin from semantic interpretation.

OMNIA begins from structural behavior under transformation.

It asks:

what remains structurally stable?

what drifts?

what degrades?

what becomes irrecoverable?

when does further continuation stop being admissible?


The result is a bounded structural report, not a semantic verdict.


---

Non-negotiable architectural rule

measurement != cognition != decision

This separation is mandatory.

Measurement asks what remains, what drifts, what saturates, and what collapses.

Cognition asks what those measurements mean inside a model, task, or domain.

Decision asks what action should follow.


OMNIA belongs to the measurement layer.

Its gate is a bounded operational conversion layer attached to the measurement result.

OMNIA is not a cognition system and not an autonomous decision-maker.


---

Canonical pipeline

input
-> optional framing normalization
-> structural lenses
-> omega / sei / iri / drift
-> limit check
-> gate decision
-> report

This is the canonical v1 pipeline.


---

Core outputs

Every valid OMNIA run must produce these core outputs:

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code


These outputs define the minimal readable structural profile of a case.


---

Gate outputs

OMNIA allows only these bounded gate outcomes:

GO

RISK

NO_GO

UNSTABLE


GO

Structural behavior remains admissible under the tested conditions.

RISK

The case remains admissible, but structural fragility or elevated drift is present.

NO_GO

Structural continuation is not admissible under the tested conditions.

UNSTABLE

The structural profile is sufficiently degraded, inconsistent, or collapsed that the case cannot be treated as operationally reliable inside scope.


---

Core metrics

OMNIA is built around a bounded structural metric family:

omega_score — structural residue or stability under admissible transformations

sei_score — remaining structural extractability / degree of non-exhaustion

iri_score — structural irreversibility / non-recoverable degradation

drift_score — structural displacement, instability, or change across compared states or variants


OMNIA may internally use multiple lenses, but the canonical output layer remains bounded by these metric roles.


---

Limit layer

OMNIA includes a formal limit layer.

The limit layer exists to detect when further structural continuation becomes unjustified inside the admissible transformation space.

A triggered limit does not mean:

truth has been proven

the task is solved

the output is universally safe

the system has understood the problem


A triggered limit means only:

further structural continuation inside scope is not justified

the bounded structural analysis has reached exhaustion, collapse, or non-admissibility


This is a structural boundary, not a metaphysical claim.


---

What OMNIA includes

Inside the canonical scope of OMNIA:

post-hoc structural measurement

structural drift detection

structural exhaustion / saturation detection

formal limit triggering

bounded gate conversion

reproducible report generation

controlled structural transformations

deterministic or reproducible scoring logic

machine-readable structured output



---

What OMNIA excludes

Outside the canonical scope of OMNIA:

semantic reasoning

general truth adjudication

training-time optimization

hidden-state introspection as a requirement

architecture-specific instrumentation as a requirement

human-AI compatibility protocols

Dual-Echo perception theory

octal logic systems

latent carrier compression

translator/export subsystems beyond core reporting

manifesto or identity layers

universal cognition claims

total theories of reality

safety certification in the broad sense


If a component depends on one of these, it is not part of OMNIA core.


---

Optional upstream components

Some modules may exist upstream of OMNIA, but they are not required parts of the canonical runtime.

Examples include:

framing normalization layers

observer-framing reduction layers

candidate-distribution instrumentation

OMNIAMIND-style pre-output split / bifurcation probes


These may be useful, but OMNIA must remain valid and runnable without them.

OMNIAMIND

OMNIAMIND is an optional upstream instrumentation module.

It is not part of the required OMNIA runtime.

If present, it may contribute additional pre-output structural signals.
If absent, OMNIA must still remain complete as a post-hoc structural measurement and gating system.


---

Repository role

This repository is the canonical product repository for OMNIA core.

Its function is narrower than the broader ecosystem.

This repository exists to:

define the canonical core

implement the canonical core

demonstrate the canonical core

document the canonical core


Historical experiments, side branches, exploratory prototypes, and genealogical material may exist elsewhere.

For broader ecosystem history and related branches, see:

lon-mirror

OMNIABASE


OMNIA should be read as the canonical structural measurement and gating core, not as the entire ecosystem.


---

Repository structure

omnia/
examples/
docs/
tests/
pyproject.toml
README.md

Main areas:

omnia/ -> core structural measurement and gating logic

examples/ -> runnable minimal examples, runners, analyzers, rebuild scripts, and frozen result artifacts

docs/ -> canonical scope, architecture, thresholds, output schema, reproducibility, work-state, phase-state, and mini-result summaries

tests/ -> canonical gate and profile tests



---

Installation

From the repository root:

pip install -e . -U --no-cache-dir

Verify import:

python -c "from omnia import evaluate_structural_profile; print('OK import omnia')"


---

Quick smoke test

Run:

python examples/quick_omnia_test.py

Expected output pattern:

{
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}

followed by:

OK: OMNIA core executed

This confirms that:

the package imports correctly

the core gate logic executes

the canonical output schema is emitted



---

Result analysis

Run the generic analyzer on any OMNIA results file:

python examples/analyze_results.py --input examples/llm_surface_results.jsonl
python examples/analyze_results.py --input examples/surface_ok_results.jsonl
python examples/analyze_results.py --input examples/support_response_results.jsonl
python examples/analyze_results.py --input examples/rag_answer_results.jsonl
python examples/analyze_results.py --input examples/demo_profiles_results.jsonl

Run the LLM surface-specific analyzer:

python examples/analyze_llm_surface_results.py

Run the support-response-specific analyzer:

python examples/analyze_support_response_results.py


---

Rebuild frozen result artifacts

Rebuild all currently frozen result JSONL artifacts in one command:

python examples/rebuild_all_results.py

This regenerates:

examples/demo_profiles_results.jsonl

examples/surface_ok_results.jsonl

examples/llm_surface_results.jsonl

examples/support_response_results.jsonl

examples/rag_answer_results.jsonl


Rebuild and analyze the current frozen result surface in one command:

python examples/rebuild_and_analyze_all.py


---

JSONL batch demo

Run the canonical batch demo:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl

Save the results to file:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl -o examples/demo_profiles_results.jsonl

This processes one JSON object per line and emits canonical OMNIA results for each record.


---

Tests

Run the full test suite:

pytest

Or run the main subsets individually:

pytest tests/test_gate.py
pytest tests/test_demo_profiles.py
pytest tests/test_import.py


---

Intended use

OMNIA is designed to be:

post-hoc

model-agnostic

composable

bounded

structural

non-semantic by design


Typical bounded use cases include:

silent fragility detection in superficially acceptable outputs

post-hoc auditing of model outputs

structural consistency checks

structural drift detection

structural exhaustion / collapse detection

bounded release gating

representation-dependent fragility sensing


OMNIA is most useful where an output may look acceptable on the surface but remain structurally weak under controlled variation.


---

Reproducibility requirement

OMNIA must be reproducible.

This means:

the same input and same configuration must produce the same structural report

transformation logic must be explicit

thresholds must be documented

outputs must be serializable

the reporting layer must be inspectable


If a result cannot be reproduced, it is not valid core behavior.


---

Bounded-use principle

OMNIA is valid only inside bounded use.

This means:

bounded inputs

bounded transformations

bounded metrics

bounded gate outputs

bounded claims


Any attempt to expand OMNIA into an unbounded general theory breaks the scope of the system.


---

Strong non-claims

OMNIA does not prove truth in the universal sense.

OMNIA does not solve reasoning.

OMNIA does not replace task evaluation.

OMNIA does not certify safety in the general sense.

OMNIA does not explain meaning.

OMNIA does not function as an autonomous decision-maker.

OMNIA does not require belief in any broader theoretical framework to remain valid inside scope.


---

Status

Current intended status of the repository:

canonical core: active

structural measurement: in scope

limit logic: in scope

bounded gate output: in scope

frozen mini-results: present

rebuildable frozen result artifacts: present

training loop: absent by design

semantic interpretation: excluded by design


OMNIA is intended to remain bounded, readable, and structurally disciplined.


---

License

MIT License