# OMNIA V8 — Failure Analysis (FLAN-T5-LARGE)

## Context

- Dataset: `examples/real_validation_v6_harder.jsonl`
- Model: `google/flan-t5-large`
- OMNIA version: V8 (structural signals)

Result summary:

- TP: 9
- FN: 3
- FP: 0
- TN: 8
- Recall: 0.750

---

## Goal

Identify why 3 errors were **not detected** (FN) and what structural signals are missing.

---

## FN Case 1

### Input
Task: reasoning  
Prompt:
> If 3 notebooks cost 18 dollars total, how much do 5 notebooks cost at the same price each?

### Output

18 * 3 = 54

### Expected

30

### Problem

- Output contains a **calculation expression**, not a final answer
- Violates instruction: "Answer with only the final number"
- Arithmetic reasoning is also incorrect

### Why V8 failed

Current rule:

```text
if is_number(out) and is_number(expected) → detect error

But here:

output is NOT a pure number

→ rule not triggered

Missing signal

format violation detection
+
non-final expression detection


---

FN Case 2

Input

Task: reasoning
Prompt:

> A farmer has 30 apples. He gives away half, then buys 6 more. How many apples does he have?



Output

30 / 2 = 15 apples.

Expected

21

Problem

Output is intermediate step, not final result

Contains reasoning trace, not answer

Incorrect final reasoning


Why V8 failed

Not numeric-only → arithmetic rule skipped

No entity confusion

No factual mismatch triggered


Missing signal

final-answer enforcement
+
intermediate-step detection


---

FN Case 3

Input

Task: rag
Prompt:

> which key opens the office?



Output

blue

Expected

blue key

Problem

Output is semantically correct but incomplete

Partial answer instead of exact expected format


Why V8 failed

blue is not considered:

entity confusion (it is correct entity)

factual mismatch (semantically aligned)


No rule for partial completeness


Missing signal

answer completeness / granularity check


---

Pattern Summary

All FN share one property:

NOT wrong in a simple way
BUT structurally incomplete or malformed

Categories:

1. Format violation (expression instead of answer)


2. Intermediate reasoning instead of final output


3. Partial answer (loss of specificity)




---

Structural Gap

Current V8 detects:

- wrong numbers
- entity confusion
- factual mismatch

But misses:

- output format correctness
- completion of reasoning
- answer granularity


---

Required Extensions (V9 direction)

Introduce new signals:

1. Final Answer Constraint

output must satisfy:
- numeric-only (reasoning)
- concise entity (qa/rag)

2. Expression Detection

detect patterns:
- "="
- arithmetic symbols
→ flag as non-final output

3. Completeness Check

expected vs output token containment
→ penalize truncated answers


---

Conclusion

V8 captures structural inconsistency
but not structural incompleteness

Next step:

extend OMNIA to detect:
structure completeness, not only mismatch

This is the transition from:

error detection
→ answer validation structure