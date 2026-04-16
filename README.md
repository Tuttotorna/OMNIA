# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18379486.svg)](https://doi.org/10.5281/zenodo.18379486)

## Canonical Ecosystem Map

This repository is part of the **MB-X.01 / OMNIABASE / OMNIA** ecosystem.

Canonical architecture and broader ecosystem map:  
**[lon-mirror / ECOSYSTEM.md](https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md)**

**[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** defines the general multirepresentational framework.  
**OMNIA** is its most mature **Diagnostics / Structural Measurement** branch.

Ω · Ω̂ · SEI · IRI · OMNIA-LIMIT  
**MB-X.01**

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## Overview

**OMNIA** is a **post-hoc structural measurement engine**.

It measures **what remains structurally stable when representations change**.

OMNIA:

- does **not** interpret meaning
- does **not** decide
- does **not** optimize
- does **not** learn

OMNIA operates **after inference**, as a **measurement layer**, not as a model.

It is designed to evaluate whether apparent stability survives beyond a single representation.

---

## Position Inside OMNIABASE

**[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** is the general framework.

It begins from one principle:

> a phenomenon should not be treated as exhausted by a single representation.

From that principle, multiple branches follow.

**OMNIA** is the branch focused on one narrower question:

> when something looks stable in one representation, does that stability survive when representation changes?

In that sense, OMNIA is not the whole framework.  
It is the **Diagnostics / Structural Measurement** branch of OMNIABASE.

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

OMNIA evaluates outputs by applying **independent structural transformations** and measuring what remains stable.

The result is **a measured boundary**, not a semantic judgment.

OMNIA does not ask first:

- what does this mean?
- what should be done?

OMNIA asks first:

- what remains?
- what drifts?
- what saturates?
- what collapses?
- what becomes irrecoverable under further transformation?

---

## What OMNIA Measures

OMNIA computes structural metrics such as:

- **Ω (Omega)** — invariant residual under transformation
- **Ω̂ (Omega-set)** — Omega under multiple lenses
- **ΔΩ / ΔC** — structural drift
- **SEI** — saturation / exhaustion index
- **IRI** — irreversibility
- **OMNIA-LIMIT** — declared boundary where further transformation is structurally futile

No semantic labels are required.  
No narrative interpretation is required.  
The output is **measurement only**.

---

## Architectural Rule

**Measurement ≠ cognition ≠ decision**

This separation is non-negotiable.

- **Measurement** asks what remains invariant, what drifts, what saturates, and what collapses.
- **Cognition** asks what those measurements mean inside a model or domain.
- **Decision** asks what action should follow.

OMNIA belongs to the first layer only.

---

## Architecture (High Level)

```text
Input / Model Output
        ↓
OMNIA lenses
(base, time, causality, token, constraints, compression, permutation, ...)
        ↓
Ω / Ω̂
        ↓
SEI · IRI
        ↓
OMNIA-LIMIT (STOP)

OMNIA is therefore:

post-hoc

model-agnostic

composable

structural

non-semantic by design



---

Repository Structure

OMNIA/
├─ omnia/                     # Core engine
│  ├─ engine/
│  ├─ lenses/
│  ├─ omega.py
│  └─ __init__.py
├─ examples/
│  └─ quick_omnia_test.py     # ~10s smoke test
├─ docs/
├─ pyproject.toml
├─ README.md
└─ .gitignore

Main areas:

omnia/ -> core structural measurement engine

examples/ -> runnable examples and smoke tests

docs/ -> architectural and methodological notes



---

Installation (Editable)

From the repository root:

pip install -e . -U

Verify import:

python -c "import omnia; print('OK import omnia', omnia.__version__)"


---

Quick Smoke Test

Run:

python examples/quick_omnia_test.py

Expected output (example):

Ω̂ estimate: <value>
OK: OMNIA core executed

This confirms that:

the engine loads correctly

the Omega pipeline executes

no external runtime coupling is required



---

Intended Use

OMNIA is designed to be:

model-agnostic

post-hoc

composable

institution-agnostic


Typical use cases include:

hallucination boundary detection

structural consistency checks

saturation / collapse detection

evaluation of irreducible residuals

research on invariance and structural limits

post-hoc auditing of model outputs

representation-dependent fragility sensing


OMNIA is especially useful where outputs look acceptable on the surface but may remain structurally weak under transformation.


---

What OMNIA Is Not

OMNIA is not:

a classifier

a judge

an alignment system

a training loop

a semantic interpreter

a truth oracle

a replacement for domain-specific models


OMNIA measures structure only.

It does not replace reasoning.
It does not replace interpretation.
It does not replace decision.

It measures structural behavior after an output already exists.


---

Scope and Boundary

OMNIA operates on structural traces.

It does not directly measure:

pure meaning in itself

pure interiority in itself

final causation in itself

metaphysical truth in itself


It works on what can be rendered into comparable structural residues under controlled representational variation.

Its boundary is not a weakness.

It is what keeps the engine coherent.


---

Relationship to the Broader Ecosystem

At a high level:

OMNIABASE -> umbrella framework

OMNIA -> Diagnostics / Structural Measurement branch

omniabase-coordinate-discovery -> Coordinate Discovery branch

omega-translator and related repos -> Cross-Representation Translation branch

observer-suspension -> epistemic pre-layer


OMNIA should therefore be read not as an isolated universal system, but as one operational branch inside a broader multirepresentational architecture.


---

Related Repositories

For the shortest functional path through the broader ecosystem:

OMNIABASE — umbrella framework

lon-mirror — deep operational and historical core of the diagnostics lineage

observer-suspension — epistemic pre-layer

omniabase-coordinate-discovery — Coordinate Discovery branch

omega-translator — Cross-Representation Translation branch

OMNIA-RADAR — residual structural opportunity detection

omnia-limit — structural boundary / saturation layer



---

Status

Core engine: stable

Smoke test: present

Architecture: frozen

OMNIA-LIMIT: defined

Training loop: absent by design


OMNIA is intended to remain bounded and structurally disciplined.


---

Author & Origin

OMNIA / MB-X.01
Massimiliano Brighindi

Logical Origin Node (L.O.N.)
Structural measurement without narrative.


---

License

MIT License
