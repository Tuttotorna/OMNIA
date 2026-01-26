# OMNIA — Unified Structural Measurement Engine

Ω · SEI · IRI · SNRC  
**Author:** Massimiliano Brighindi

---

## Overview

**OMNIA** is a **post-hoc, model-agnostic structural measurement engine**.

It measures structural stability of representations under independent transformations:

- **invariance**
- **drift**
- **saturation**
- **irreversibility**
- **epistemic limits**

OMNIA is strictly a **measurement layer**.

It:

- does **not** interpret meaning  
- does **not** decide  
- does **not** optimize  
- does **not** learn  

OMNIA measures **what remains invariant when representation changes**.

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

OMNIA evaluates outputs by applying independent structural lenses and measuring the residual Ω.

---

## Quickstart (10 seconds)

```bash
git clone https://github.com/Tuttotorna/OMNIA.git
cd OMNIA

pip install -e .
python examples/quick_omnia_test.py

Expected output:

an Ω̂ estimate

OK: OMNIA core executed



---

Repository Layout

omnia/ — core measurement engine

examples/ — minimal runnable smoke tests

metrics/ — SEI, IRI, PBII modules (in progress)

limit/ — OMNIA-LIMIT boundary certificates (SNRC) (next step)



---

Structural Chain (non-negotiable)

Correct separation:

representation → OMNIA measure → OMNIA-LIMIT → STOP

Principle:

measurement ≠ cognition ≠ decision

confidence is signal reliability, not truth by authority

saturation is a formal stop condition, not escalation



---

Status

Current version: v0.1.0

Stable:

installable Python package

core Ω engine imported

smoke test runnable


Next milestones:

1. Integrate OMNIA-LIMIT (snrc.py)


2. Add one public benchmark pipeline (JSONL real-run)


3. Produce a single boundary certificate output (boundary.json)




---

License

MIT