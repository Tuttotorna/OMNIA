File: README.md

# OMNIA - Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19657671.svg)](https://doi.org/10.5281/zenodo.19657671)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a bounded post-hoc structural measurement core.

It is not a model.  
It is not a reasoning system.  
It is not a semantic judge.  
It is not an autonomous decision-maker.

OMNIA measures structure only.

Its task is to evaluate what remains stable, what degrades, and what becomes fragile when an output is observed under controlled transformations.

The core architectural rule is non-negotiable:

```text
measurement != cognition != decision

OMNIA belongs to the measurement layer only.


---

Core principle

OMNIA starts from one bounded principle:

structural stability = what survives controlled representational variation

It does not ask:

is this semantically correct?

is this universally true?

does the model understand the task?


It asks:

how much does this output depend on its surface form?

how much structure survives under transformation?

how much degrades?

when does continuation stop being structurally admissible?


This makes OMNIA a structural sensor, not a content interpreter.


---

What OMNIA does

OMNIA measures a bounded structural profile through four core outputs:

omega_score

sei_score

iri_score

drift_score


and converts that profile into a bounded gate layer:

GO

RISK

NO_GO

UNSTABLE


Every valid OMNIA run also returns:

limit_triggered

reason_code


So the canonical minimal output surface is:

omega_score
sei_score
iri_score
drift_score
limit_triggered
gate_status
reason_code


---

What OMNIA does not do

OMNIA does not:

interpret semantics

replace reasoning

optimize a model

train a model

act as a truth oracle

certify safety in the general sense

function as a cognition system

function as a decision system


If a claim requires any of those, it is outside OMNIA core.


---

Focused proof

The strongest current public result is not a broad benchmark.

It is a focused bounded proof on one failure family:

account_access_hollow_responses_v1

Result:

On the focused account-access hollow benchmark,
OMNIA reduced false accepts from 14 to 7
with no observed increase in false rejects.

This is the current strongest narrow public claim.

It does not prove general support-domain superiority. It does prove that, in a focused benchmark, OMNIA added useful review pressure on a real hollow-response failure family.

For the compact proof, read:

docs/FOCUSED_PROOF.md


For the full result and case analysis, read:

docs/ACCOUNT_ACCESS_HOLLOW_RESULT_V1.md

docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md



---

Start here

If only one public entry point is needed, start here:

docs/FOCUSED_PROOF.md


If the goal is to see the benchmark result in more detail, then read:

docs/ACCOUNT_ACCESS_HOLLOW_RESULT_V1.md

docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md


If the goal is to understand how broader validation was structured, read:

docs/EXTERNAL_VALIDATION_PLAN.md

docs/BENCHMARK_V2_PLAN.md



---

Current public benchmark state

Broader support-style benchmarks

OMNIA has already been tested on broader support-style frozen sets.

Those runs showed:

a real signal

but weak generalization

and limited coverage


So the broad claim remains narrow.

Focused benchmark

OMNIA then moved to a focused benchmark on:

polite
readable
surface-acceptable
operationally hollow
account-access responses

That focused run produced the first clear bounded result.

This is why the focused proof now matters more than the broad benchmark summaries.


---

Canonical pipeline

The canonical pipeline is:

input
-> controlled structural transforms
-> omega / sei / iri / drift
-> limit check
-> gate status
-> bounded structural report

This is the canonical v1 software path.


---

Gate meanings

GO

The structural profile remains admissible under the tested bounded conditions.

RISK

The profile remains readable but shows enough fragility, drift, or weakness to justify review.

NO_GO

The profile is not structurally admissible under the tested bounded conditions.

UNSTABLE

The profile is degraded enough that it should not be treated as operationally reliable inside scope.

These gate values are bounded outputs of measurement. They are not independent decisions.


---

Core metrics

omega_score

Residual structural stability under admissible transformations.

sei_score

Remaining structural extractability. A lower SEI suggests exhaustion or weak remaining structure.

iri_score

Structural irreversibility. A higher IRI suggests non-recoverable degradation.

drift_score

Structural displacement under comparison and transformation.

These metrics are not semantic scores. They are structural diagnostics.


---

Limit logic

OMNIA includes a bounded limit layer.

A triggered limit means only this:

further structural continuation inside scope is not justified

It does not mean:

truth has been proven

the task is solved

the output is universally unsafe

the system has understood the problem


OMNIA-LIMIT is about structural stopping, not metaphysics.


---

Repository role

This repository is the canonical product repository for OMNIA core.

Its role is narrower than the broader ecosystem.

This repository exists to:

define the core

implement the core

test the core

document the core

validate bounded external behavior


Historical, conceptual, or ecosystem-level material may exist elsewhere.

OMNIA should be read as the core structural measurement layer, not as the whole ecosystem.


---

Repository structure

omnia/
examples/
docs/
tests/
pyproject.toml
README.md

Main areas:

omnia/ -> structural measurement logic

examples/ -> runnable benchmark scripts and result generators

docs/ -> scope, validation plans, results, focused proof

tests/ -> bounded core behavior tests



---

Installation

From repository root:

pip install -e . -U --no-cache-dir


---

Minimal smoke test

Run:

python examples/quick_omnia_test.py

Expected pattern:

{
  "omega_score": 0.594462,
  "sei_score": 0.67557,
  "iri_score": 0.405538,
  "drift_score": 0.405538,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "low_omega"
}

followed by:

OK: OMNIA core executed

This confirms that the minimal executable core is alive.


---

Tests

Run the test suite:

pytest -q tests

A recent verified run passed all tests:

47 passed

This is software validity only. It is not external benchmark proof by itself.


---

Focused benchmark artifacts

Dataset

data/account_access_hollow_responses_v1.jsonl


Baseline runner

examples/run_baseline_account_access_hollow_v1.py


OMNIA runner

examples/run_omnia_account_access_hollow_v1.py


Combined evaluation

examples/evaluate_baseline_plus_omnia_account_access_hollow_v1.py


Case inspection

examples/inspect_omnia_review_cases_account_access_hollow_v1.py


Documents

docs/FOCUSED_PROOF.md

docs/ACCOUNT_ACCESS_HOLLOW_RESULT_V1.md

docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md

docs/ACCOUNT_ACCESS_HOLLOW_ERROR_ANALYSIS_V1.md



---

Broader benchmark artifacts

Validation plans

docs/EXTERNAL_VALIDATION_PLAN.md

docs/EXTERNAL_DATASET_SPEC.md

docs/BASELINE_SPEC.md

docs/OMNIA_GATE_MAPPING.md

docs/LABELING_POLICY.md

docs/BENCHMARK_V2_PLAN.md


Broader support-style dataset family

data/support_screening_external_v1.jsonl

data/support_screening_external_v2.jsonl


Broader support-style runners

examples/run_baseline_support_screening.py

examples/run_omnia_support_screening.py

examples/evaluate_baseline_plus_omnia_support_screening.py

examples/inspect_omnia_review_cases.py


V2 runners

examples/run_baseline_support_screening_v2.py

examples/run_omnia_support_screening_v2.py

examples/evaluate_baseline_plus_omnia_support_screening_v2.py

examples/inspect_omnia_review_cases_v2.py



---

Intended use

OMNIA is designed to be:

post-hoc

bounded

deterministic

structural

composable

model-agnostic

non-semantic by design


Typical bounded uses include:

hollow-response detection

structural fragility sensing

post-hoc output review

admissibility screening

silent failure pressure

structural drift inspection


It is most useful where a response looks acceptable on the surface but may still be weak under transformation.


---

Reproducibility rule

OMNIA is only meaningful if the result can be reproduced.

That requires:

frozen dataset

frozen scripts

frozen labeling policy

frozen gate mapping

fixed metric interpretation

machine-readable outputs


If the setup is not reproducible, the claim is not valid core evidence.


---

What is currently proved

Currently proved:

the core runs

the core is testable

the core emits bounded structural outputs

broader benchmarks show a small real signal

focused account-access hollow benchmarking shows a stronger bounded signal

tuned transforms can improve selectivity within that narrow family


Not proved:

broad external validity

general support-domain superiority

cross-domain transfer

production readiness

universal filtering power



---

Minimal public claim

The current public claim should remain this narrow:

OMNIA is a bounded structural measurement core.
Its strongest current result is a focused benchmark where it reduced false accepts
on polite but operationally hollow account-access responses
from 14 to 7 with no observed increase in false rejects.

Anything broader than this is not yet justified.


---

License

MIT License