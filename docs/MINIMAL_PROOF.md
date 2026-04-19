# OMNIA - Minimal Proof

## Claim

OMNIA is a minimal executable structural measurement core.

This claim is narrow.

It does not claim scientific closure.
It does not claim benchmark superiority.
It does not claim universal validity.

It claims only that a bounded OMNIA core now exists as working software.

---

## What is proved here

The repository now provides a core that is:

- installable
- importable
- runnable
- testable
- bounded by a canonical output schema

---

## Install

From repository root:

```bash
pip install -e . -U --no-cache-dir


---

Run tests

pytest -q tests

Verified result:

47 passed in 0.14s


---

Run minimal smoke test

python examples/quick_omnia_test.py

Verified output:

{
  "case_id": "quick-smoke-001",
  "drift_score": 0.405538,
  "gate_status": "RISK",
  "iri_score": 0.405538,
  "limit_triggered": false,
  "omega_score": 0.594462,
  "reason_code": "low_omega",
  "sei_score": 0.67557
}

Terminal confirmation:

OK: OMNIA core executed


---

Canonical output contract

A valid OMNIA core run returns at minimum:

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code


This is the bounded structural report surface of OMNIA core.


---

What this means

This proves that OMNIA now exists as a real minimal executable system.

More precisely:

the package installs

the canonical imports resolve

the core run executes

the output schema is material

the test suite passes


This is a software-level proof of existence.


---

What this does not mean

This does not prove:

large-scale external validation

scientific finality

production maturity

superiority over other systems

universal truth measurement


Those are separate questions.


---

Minimal status sentence

OMNIA is now a real minimal executable structural measurement core.