# Engine Overview

OMNIA is the core structural measurement engine of the MB-X.01 / OMNIA ecosystem.

It is designed to measure whether structure remains admissible or stable under controlled transformation.

Canonical boundary:

    measurement != inference != decision

---

## Engine pipeline

The core pipeline is:

    input -> transformation -> measurement -> output -> boundary

Meaning:

| Stage | Role |
|---|---|
| input | Object, output, trace, representation, or trajectory being measured |
| transformation | Perturbation, rewrite, representation shift, temporal drift, or controlled variant |
| measurement | Structural scoring or diagnostic process |
| output | Score, signal, report, or artifact |
| boundary | Declared limit of what the output means |

---

## What makes OMNIA different

OMNIA is not optimized to answer:

    Is this semantically true?

It is optimized to ask:

    Does the measured structure survive transformation?

This is a narrower claim.

That narrowness is intentional.

---

## Correct use

Correct use:

    use OMNIA to measure structural stability
    inspect the output
    validate artifacts externally
    make decisions outside the engine

Incorrect use:

    treat OMNIA as a measurement layer
    treat a score as truth
    treat structural stability as semantic correctness
    treat measurement as decision

---

## Relation to validation

OMNIA produces or supports measurement artifacts.

OMNIA-VALIDATION exists to make those artifacts inspectable, reproducible, and falsifiable.

