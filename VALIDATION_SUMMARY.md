# OMNIA Validation Summary

## Purpose

This document summarizes the current empirical validation path of OMNIA.

OMNIA is not a semantic truth engine.

OMNIA is a structural measurement layer.

It tests whether an output remains structurally admissible under constraints, nearby variation, and expected output contracts.

Core boundary:

```text
structural validity != semantic correctness
measurement != inference != decision

OMNIA does not replace reasoning.

OMNIA does not decide final truth.

OMNIA detects structural weakness before semantic evaluation or operational decision.


---

Correct System Role

The intended pipeline is:

LLM -> OMNIA -> Semantic Evaluator -> Decision

OMNIA sits before semantic evaluation.

Its job is to reject or flag outputs that are structurally malformed, incomplete, unstable, or incompatible with the required output contract.


---

What OMNIA Detects

OMNIA is useful when failures are structural.

Examples:

incomplete output
malformed answer
format violation
expression instead of final answer
unstable output under variation
structurally hollow response
mismatch between requested output contract and produced output

Example cases:

"5 * 3 ="        -> incomplete
"5 * 3 = 15"    -> not final-only
"blue"          -> incomplete if expected contract is "blue key"
long explanation -> invalid if scalar answer required


---

What OMNIA Does Not Detect

OMNIA does not detect pure semantic errors when the answer is structurally well-formed.

Examples:

"2" instead of "4"
"wolf" instead of "dog"
"blue" instead of "black"

These answers may be wrong, but structurally valid.

In such cases OMNIA may return:

GO

This is not a failure.

It is the boundary of the system.


---

Validation Path

The validation path evolved through increasingly harder tests.

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

A harder dataset exposed a failure.

Result:

V7 recall collapsed to 0.25

This showed that the early gate was too shallow.

This failure was useful.

It forced the system boundary to become sharper.


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

V8 improved detection but still missed one failure mode.


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

This closed the observed V8 failure modes on the tested slice.


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

This is evidence of cross-pattern robustness.

It is not universal validity.


---

GSM8K-Style / GSM8K Real Slices

OMNIA was also tested on arithmetic reasoning slices.

On GSM8K-style and real GSM8K slices, V9 correctly rejected structurally invalid or wrong numeric outputs.

However, some runs were highly imbalanced because the tested model produced very few correct answers.

Therefore these runs show failure detection capability, but they are not sufficient as full positive-selectivity proof.


---

Current Empirical Claim

The current claim is limited and falsifiable:

OMNIA can detect structurally invalid, incomplete, malformed,
or contract-breaking outputs before semantic evaluation.

A stronger claim is not made.

OMNIA does not prove truth.

OMNIA does not solve reasoning.

OMNIA does not replace semantic validation.


---

Strongest Current Result

The strongest current result is not that OMNIA is always right.

The strongest result is that OMNIA survived failure-driven iteration:

V7 worked on an easy slice
V7 failed on harder data
V8 reduced the failure
V9 closed the observed structural failure modes
V9 generalized on an external attack slice

This matters because the system was not protected from falsification.

It was improved through falsification.


---

Gate Outputs

Typical OMNIA gate outputs:

GO
RISK
NO_GO
UNSTABLE

These are structural diagnostics.

They are not final decisions.

Example output:

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

The output is readable, but structurally weak enough to justify review.


---

Practical Use Cases

OMNIA is useful where systems require:

structured outputs
final-only answers
JSON or schema compliance
stable behavior under variation
post-hoc output review
pre-deployment structural gates
detection of hollow or malformed responses

OMNIA is especially relevant where an answer may look acceptable but fail structurally.


---

Non-Use Cases

OMNIA is not sufficient for:

pure QA correctness
truth verification
semantic reasoning validation
factuality checking
final operational decisions

These require:

ground truth
semantic evaluator
external verifier
human review
another model
domain-specific validator


---

Minimal Honest Claim

The honest claim is:

OMNIA is a structural filter layer.

Not:

OMNIA is a universal error detector.


---

Next Validation Target

The next useful target is positive selectivity.

OMNIA must show that it can reject structurally bad outputs while preserving structurally good ones across a balanced dataset.

The next validation should therefore use:

balanced correct / incorrect outputs
controlled perturbations
strict output contracts
external model outputs
frozen result files
repeatable runner scripts

Success condition:

high recall on structural failures
low false positives on valid outputs
stable behavior across unseen slices


---

Final Boundary

OMNIA is useful only if it remains inside its measurement role.

The non-negotiable rule is:

measurement != inference != decision

That boundary is what makes the system clean.

