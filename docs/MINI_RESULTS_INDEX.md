# MINI_RESULTS_INDEX.md

## Status

This document indexes the current bounded mini-results of OMNIA CORE v1.

Its purpose is to keep the minimal external-facing evidence surface readable and frozen.

It does not describe the whole ecosystem.

It only records the current small reproducible result chain already present in this repository.

---

## 1. Current mini-results

The repository currently contains three bounded result layers:

### A. Demo profile result
Input:
```text
examples/demo_profiles.jsonl

Output:

examples/demo_profiles_results.jsonl

Purpose: A canonical profile-level check of the four gate outcomes:

GO

RISK

NO_GO

UNSTABLE


This is the smallest synthetic sanity layer.


---

B. Surface-ok mini-result

Input:

examples/surface_ok_cases.jsonl

Output:

examples/surface_ok_results.jsonl

Summary:

docs/SURFACE_OK_MINI_RESULT.md

Purpose: Show that surface acceptability does not imply structural admissibility.

Canonical formula:

surface_ok != always_GO


---

C. LLM surface mini-result

Input:

examples/llm_surface_cases.jsonl

Output:

examples/llm_surface_results.jsonl

Summary:

docs/LLM_SURFACE_MINI_RESULT.md

Purpose: Show that readable LLM-like outputs can remain structurally non-admissible.

Canonical formula:

surface-readable LLM-like output != always structurally admissible


---

2. Current analysis tools

The repository currently contains two lightweight result analyzers.

Generic analyzer

examples/analyze_results.py

Purpose: Analyze any OMNIA JSONL results file that follows the canonical output schema.


---

LLM surface-specific analyzer

examples/analyze_llm_surface_results.py

Purpose: Produce a short report specifically for the LLM surface mini-result.


---

3. Canonical reproducible flow

The minimal reproducible result flow is:

input JSONL
-> OMNIA JSONL runner
-> results JSONL
-> short analysis report
-> frozen mini-result document

This is now the canonical bounded externalization path of OMNIA CORE v1.


---

4. Why this index exists

Without an index, the mini-results remain scattered across:

examples

docs

analysis scripts


This file keeps the current result surface small and navigable.


---

5. What this index does not claim

This index does not claim:

broad external validation

benchmark superiority

production readiness

semantic correctness

general LLM evaluation coverage


It only records the current bounded mini-result surface.


---

6. Current minimal evidence surface

The current evidence surface is:

internal runnable core
+ canonical tests
+ demo profile result
+ surface-ok divergence
+ LLM-like surface divergence

This is the current state of external-readable validation.


---

7. Final formula

The shortest correct formula for the current state is:

OMNIA now has a runnable core, frozen mini-result artifacts, and a small reproducible divergence surface beyond pure internal architecture.