# OMNIA — Where It Works (V1)

## Core Idea

OMNIA is not universal.

Its value emerges where structure fails before semantics.

---

## Case 1 — Incomplete Answer

Prompt:
"Answer with only the final number. 5 * 3 = ?"

Model output:
"5 * 3 ="

- Semantically: undefined
- Structurally: incomplete

OMNIA:

NO_GO

Without OMNIA:
→ passes silently

---

## Case 2 — Expression Instead of Answer

Output:
"5 * 3 = 15"

Expected:
"15"

OMNIA detects:

- format violation
- structural mismatch

---

## Case 3 — Drift Under Perturbation

Two equivalent prompts:

A: "5 * 3"
B: "3 * 5"

Model outputs:

A → 15  
B → 12

OMNIA detects:

- instability across equivalent inputs

---

## Case 4 — RAG Structural Failure

Context:
"A → B → C"

Question:
"who is C?"

Model output:
"because A leads to..."

OMNIA detects:

- answer not aligned with output contract

---

## Summary

OMNIA is strongest when:

- output format matters
- stability matters
- consistency matters
- systems require reliability under transformation

OMNIA is weakest when:

- only semantic correctness matters
- output is short and structurally valid

---

## Final Position

OMNIA is a structural safety layer.

Not a truth engine.