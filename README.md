# OMNIA - Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19657671.svg)](https://doi.org/10.5281/zenodo.19657671)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a structural measurement core.

It does not try to act like a human judge.  
It does not try to replace reasoning.  
It does not try to declare absolute truth.

OMNIA does one thing only:

**it checks whether an output still holds together when its form is changed in controlled ways.**

That is the whole idea.

---

## Why OMNIA exists

Many outputs look good once.

They may be:

- polite
- readable
- well formatted
- plausible
- confident
- apparently coherent

and still be weak.

A response can look fine on the surface and still fall apart when you rewrite it, perturb it slightly, or compare it with a nearby version.

OMNIA exists to detect that hidden weakness.

---

## A real result

OMNIA is not just a theory.

In one focused benchmark on **polite but operationally hollow account-access responses**, OMNIA reduced false accepts from **14 to 7**, with **no observed increase in false rejects**.

This is a narrow result, not a universal claim.  
But it shows the practical point:

**a response can look acceptable and still be structurally weak.**

For the compact proof, read:

- `docs/FOCUSED_PROOF.md`

---

## The shortest possible explanation

OMNIA does not ask:

> "Does this look right?"

OMNIA asks:

> "Does this still hold when I touch it?"

If it still holds, that is a good sign.  
If it starts drifting, weakening, or collapsing, that is a structural warning.

OMNIA measures that warning.

---

## A simple example

Imagine a model gives an answer that sounds correct.

Now do something small:

- rewrite the same request
- change the wording
- apply a nearby variation
- compare the new response to the original one

If the answer still behaves coherently, the structure is likely stronger.

If it starts contradicting itself, losing force, or becoming hollow, the structure is weak.

OMNIA is built to measure that difference.

---

## What you see when you use OMNIA

In practice, OMNIA works like this:

- you take an output
- you apply controlled variation
- you compare the structural response
- OMNIA returns scores and a gate result
- the result tells you whether the output looks structurally solid, weak, drifting, or unstable

OMNIA does **not** tell you absolute truth.  
It tells you whether structural review is justified.

---

## The minimal universal protocol

OMNIA can be understood in four steps:

### 1. Take an output
An answer, response, representation, or structured object.

### 2. Apply controlled transformation
Change the form in a bounded way.

### 3. Observe the response
Check what remains stable, what drifts, and what breaks.

### 4. Measure the structural profile
Return bounded structural scores and a bounded gate result.

That is OMNIA in its simplest universal form.

---

## What OMNIA measures

OMNIA measures structure only.

It does not measure semantic truth directly.  
It does not decide what a model "really understands."  
It does not replace human judgment.

It measures things like:

- how much structure remains stable
- how much structure becomes fragile
- how much drift appears under variation
- when further continuation stops being structurally justified

In short:

**OMNIA measures how much an output depends on its surface form, and how much structure survives when that form is changed.**

---

## A concrete output example

A minimal OMNIA run may return something like this:

```json
{
  "omega_score": 0.594462,
  "sei_score": 0.67557,
  "iri_score": 0.405538,
  "drift_score": 0.405538,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "low_omega"
}

A human-readable interpretation would be:

omega_score is not strong enough -> the structure is weaker than desired

sei_score is still decent -> some usable structure remains

iri_score is moderate -> some degradation is not easily recoverable

drift_score is moderate -> the output moves too much under comparison

limit_triggered = false -> structural continuation is still allowed

gate_status = RISK -> the output is still readable, but weak enough to justify review


This is the role of OMNIA:

not to say "true" or "false", but to say whether the structure looks solid, weak, drifting, or unreliable under controlled variation.


---

The non-negotiable rule

OMNIA is built on one strict boundary:

measurement != cognition != decision

In practical terms:

measurement = OMNIA says what the structural profile looks like

cognition = another model or a human reasons about what that profile means

decision = another layer decides whether to accept, review, retry, or block


So OMNIA does not do everything.

It stays inside the measurement layer.

That is not a weakness.
It is what keeps OMNIA clean.


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

function as an autonomous decision-maker


If a claim depends on any of the above, it is outside OMNIA core.


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

when does continuation stop being structurally justified?


That makes OMNIA a structural sensor, not a content interpreter.


---

What OMNIA is really checking

OMNIA is not checking whether something sounds good.

It is checking whether the output depends too much on the exact form in which it appears.

That is the key distinction.

A system can be:

correct but fragile

wrong but stable

stable and useful

unstable and misleading


OMNIA does not collapse these into one number.

It keeps structural behavior separate from semantic claims.


---

Canonical outputs

OMNIA measures a bounded structural profile through four core outputs:

omega_score

sei_score

iri_score

drift_score


It then maps that profile into a bounded gate layer:

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

These are structural outputs only.

They are not truth labels.
They are not semantic judgments.
They are not autonomous decisions.


---

What the scores mean

omega_score

How much structure still holds together under admissible transformation.

sei_score

How much usable structure remains before the output becomes exhausted or hollow.

iri_score

How much degradation is structurally irreversible.

drift_score

How far the output has moved away from its reference structural profile.

These scores are structural diagnostics.
They are not semantic scores.


---

What the gate values mean

GO

The structural profile remains admissible under the tested bounded conditions.

RISK

The output is still readable, but shows enough weakness or drift to justify review.

NO_GO

The output is not structurally admissible under the tested bounded conditions.

UNSTABLE

The output is degraded enough that it should not be treated as operationally reliable inside scope.

These gate values are measurement outputs.
They are not final decisions by themselves.


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

Why this matters in practice

Many failures are not immediately visible.

A system can:

pass formatting checks

look coherent

sound helpful

satisfy superficial evaluation

appear acceptable at first glance


and still be structurally weak.

OMNIA is designed to expose that hidden weakness.

It is most useful where an output looks acceptable on the surface but may still be hollow, unstable, or operationally weak under transformation.


---

Start here

If you want only one entry point, start here:

docs/FOCUSED_PROOF.md


If you want the focused result in more detail, read:

docs/ACCOUNT_ACCESS_HOLLOW_RESULT_V1.md

docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md


If you want broader validation planning, read:

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

This is why the focused proof currently matters more than the broad benchmark summaries.


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

This proves software validity only.
It is not external benchmark proof by itself.


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

The public claim should remain narrow:

OMNIA is a bounded structural measurement core.
Its strongest current result is a focused benchmark where it reduced false accepts on polite but operationally hollow account-access responses from 14 to 7 with no observed increase in false rejects.

Anything broader than this is not yet justified.


---

One-line definition

OMNIA measures how much structure survives when form is changed in a controlled way.


---

Final boundary

OMNIA is strongest when it stays inside its real role:

measurement only

no hidden semantics

no fake omniscience

no collapse into decision theater

no claims beyond evidence


That boundary is not a weakness.

It is what keeps OMNIA clean.


---

License

MIT License
