# OMNIA Scope Boundary — V1

## Core Principle

OMNIA is a structural measurement system.

It evaluates:

- coherence
- completeness
- structural consistency
- representation stability

OMNIA does **not** evaluate semantic truth.

---

## What OMNIA Detects

OMNIA is effective at detecting:

- incomplete outputs
- malformed answers
- inconsistent representations
- structural contradictions
- output drift under perturbation
- instability across equivalent formulations

Examples:

- missing final answer
- expression instead of result (`"5 * 3 ="`)
- long incoherent text where a scalar is required
- inconsistent formatting across variants

---

## What OMNIA Does NOT Detect

OMNIA does not detect:

- pure semantic errors
- logically incorrect but well-formed answers
- wrong answers that are structurally valid

Examples:

- `"2"` instead of `"4"`
- `"wolf"` instead of `"dog"`
- `"blue"` instead of `"black"`

These outputs are structurally correct.

OMNIA will classify them as:

```text
GO (structurally valid)


---

Empirical Evidence

Arithmetic / Structural Tasks

OMNIA performs strongly:

high TP

near-zero FP

low FN


These tasks expose structural weaknesses clearly.


---

QA / RAG Tasks

OMNIA shows limitation:

fails to detect semantic-only errors

high FN when structure is valid but answer is wrong


Example result:

TP: 0
FN: 6
FP: 0
TN: 14

Interpretation:

OMNIA correctly passes structurally valid outputs, but cannot identify semantic incorrectness.


---

Interpretation

OMNIA is not a universal error detector.

It is a structural filter layer.

Correct system design:

LLM → OMNIA → Semantic Evaluator → Decision

Where:

OMNIA removes structurally invalid outputs

semantic layer evaluates correctness



---

Positioning

OMNIA should be used as:

pre-deployment structural gate

robustness validator

instability detector


OMNIA should NOT be used as:

truth verifier

reasoning correctness evaluator

standalone judge



---

Final Statement

Structural validity ≠ semantic correctness.

OMNIA measures the first, not the second.

This boundary is intentional and required for system integrity.
