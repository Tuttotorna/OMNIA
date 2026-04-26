# OMNIA — Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19739481.svg)](https://doi.org/10.5281/zenodo.19739481)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a structural measurement core.

It does not judge meaning.  
It does not replace reasoning.  
It does not declare truth.

OMNIA measures whether an output remains structurally admissible under controlled transformations, constraints, or observer perturbations.

In one sentence:

> OMNIA measures how much structure survives when form, constraints, or nearby representation changes.

---

## Core Boundary

```text
structural validity != semantic correctness

OMNIA measures structural validity.
It does not measure semantic truth.

This boundary is intentional.

OMNIA is not a truth oracle.
OMNIA is not a semantic evaluator.
OMNIA is not a final decision system.


---

Non-Negotiable Rule

measurement != inference != decision

OMNIA stays inside the measurement layer.

That is what keeps it clean.


---

What OMNIA detects

OMNIA is strongest when failures are structural:

incomplete outputs

malformed answers

format violations

expression instead of final answer

unstable output under variation

structurally hollow responses

mismatch between requested output contract and produced output

instability under observer perturbation


Examples:

"5 * 3 ="        -> incomplete
"5 * 3 = 15"    -> not final-only
"blue"          -> incomplete if expected contract is "blue key"
long explanation -> invalid if scalar answer required


---

What OMNIA does not detect

OMNIA does not detect pure semantic errors when the answer is structurally well-formed.

Examples:

"2" instead of "4"
"wolf" instead of "dog"
"blue" instead of "black"

These answers may be wrong, but structurally valid.

OMNIA may return:

GO

This is not a bug.

It is the boundary of the system.


---

Correct System Role

The correct pipeline is:

LLM -> OMNIA -> Semantic Evaluator -> Decision

OMNIA removes structurally invalid, unstable, incomplete, or malformed outputs before semantic evaluation or operational decision.


---

Minimal External Signal

OMNIA now includes a minimal reproducible signal test for observer-induced structural instability.

See:

docs/OBSERVER_PERTURBATION_RESULT.md

Runner:

examples/observer_perturbation_signal_test.py

Result summary:

Stable avg OPI:    ~0.0016
Unstable avg OPI:  ~0.0062

Stable avg ratio:    ~0.089
Unstable avg ratio:  ~0.284

Interpretation:

> Internally unstable outputs change more under observer perturbation than stable outputs.



This is not a universal proof.
It is a minimal reproducible signal showing that a real OMNIA lens can separate stable from unstable structures.


---

Current Empirical Status

OMNIA has been tested across several controlled validation stages.

V7

Initial gate on controlled QA, reasoning, and RAG cases.

Result:

TP: 10
FN: 0
FP: 0
TN: 6

V7 performed well on the initial small dataset.


---

Harder Dataset

A harder dataset exposed a failure:

V7 recall collapsed to 0.25

This showed that the early gate was too shallow.


---

V8

V8 added structural mismatch detection.

Result on harder data:

TP: 11
FN: 1
FP: 0
TN: 8
Recall: 0.917
Precision: 1.000


---

V9

V9 added structural completeness detection:

final-answer enforcement

expression detection

answer completeness / granularity check


Result:

TP: 12
FN: 0
FP: 0
TN: 8
Recall: 1.000
Precision: 1.000

This closed the observed V8 failure modes.


---

External Attack Slice

A separate synthetic attack set tested whether V9 generalized beyond the previous dataset.

Result:

TP: 9
FN: 0
FP: 0
TN: 11
Recall: 1.000
Precision: 1.000

This is evidence of cross-pattern robustness, not universal validity.


---

GSM8K-style / GSM8K Real Slices

OMNIA was also tested on arithmetic reasoning slices.

On GSM8K-style and real GSM8K slices, V9 correctly rejected structurally invalid or wrong numeric outputs.

However, some runs were highly imbalanced because the tested model produced very few correct answers.

Therefore these runs show failure detection capability, but are not sufficient as full positive-selectivity proof.


---

Scope Boundary

Read:

docs/OMNIA_SCOPE_BOUNDARY_V1.md

Core conclusion:

> OMNIA is not a universal error detector.
OMNIA is a structural filter layer.




---

Where OMNIA is useful

OMNIA is useful when systems require:

structured outputs

final-only answers

JSON or schema compliance

stable behavior under variation

post-hoc output review

pre-deployment structural gates

detection of hollow or malformed responses

observer-perturbation analysis


OMNIA is especially relevant where an answer may look acceptable but fail structurally.


---

Where OMNIA is not sufficient

OMNIA is not sufficient for:

pure QA correctness

truth verification

semantic reasoning validation

factuality checking

final operational decisions


These require a semantic evaluator, another model, ground truth, or human review.


---

Canonical Outputs

OMNIA produces bounded structural diagnostics such as:

omega_score
sei_score
iri_score
drift_score
limit_triggered
gate_status
reason_code

Typical gate values:

GO
RISK
NO_GO
UNSTABLE

These are measurement outputs.

They are not final decisions.


---

Minimal Example Output

{
  "omega_score": 0.594462,
  "sei_score": 0.67557,
  "iri_score": 0.405538,
  "drift_score": 0.405538,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "low_omega"
}

Interpretation:

> The output is readable, but structurally weak enough to justify review.




---

Repository Structure

omnia/      -> structural measurement logic
examples/   -> validation datasets and runners
results/    -> frozen experimental outputs
docs/       -> reports, scope, validation notes
tests/      -> core behavior tests


---

Key Documents

docs/OMNIA_SCOPE_BOUNDARY_V1.md
docs/OBSERVER_PERTURBATION_RESULT.md
docs/REAL_VALIDATION_V9_STRUCTURAL_COMPLETENESS.md
docs/REAL_VALIDATION_V9_EXTERNAL_ATTACK.md
docs/REAL_VALIDATION_V9_GSM8K_SLICE.md
docs/REAL_VALIDATION_V9_GSM8K_REAL.md
docs/OMNIA_V8_FAILURE_ANALYSIS.md
docs/FOCUSED_PROOF.md


---

Installation

From repository root:

pip install -e . -U --no-cache-dir


---

Smoke Test

python examples/quick_omnia_test.py

Expected ending:

OK: OMNIA core executed


---

Observer Perturbation Signal Test

Run:

python examples/observer_perturbation_signal_test.py

Expected direction:

unstable avg OPI > stable avg OPI
unstable avg ratio > stable avg ratio

This test uses the real OMNIA ObserverPerturbation lens.

It does not use an external model.
It does not use semantic labels during measurement.
It measures structural change under observer transformations.


---

Tests

pytest -q tests

Recent verified run:

47 passed

This proves software consistency only.

It is not external scientific validation by itself.


---

Reproducibility Rule

An OMNIA claim is valid only if it includes:

frozen dataset

frozen runner

frozen result file

explicit metric interpretation

clear scope boundary


Without reproducibility, the claim is not evidence.


---

Current Public Claim

The correct public claim is narrow:

> OMNIA is a bounded structural measurement core. It detects structural invalidity, incompleteness, drift, malformed outputs, and observer-perturbation instability. It does not detect semantic truth. Current results show strong behavior on controlled structural validation tasks, while pure semantic QA remains outside its standalone scope.




---

One-Line Definition

OMNIA measures how much structure survives when form, constraints, or observer framing changes.


---

Final Boundary

OMNIA is strongest when it stays inside its real role:

structural measurement only

No hidden semantics.
No truth oracle.
No decision theater.
No claims beyond evidence.


---

License

MIT License