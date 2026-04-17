# REPRODUCIBLE_RUNS.md

## Status

This document freezes the minimal reproducible run surface of OMNIA CORE v1.

Its purpose is to record the exact bounded commands and artifact flow currently supported by the repository.

This is not a roadmap.

This is not a benchmark protocol.

This is the minimal reproducible run layer.

---

## 1. Minimal reproducible root

All commands below are intended to be executed from the repository root.

Canonical assumption:

```text
repo root
-> pyproject.toml
-> omnia/
-> examples/
-> tests/
-> docs/


---

2. Installation

Install the package in editable mode:

pip install -e . -U --no-cache-dir

Optional import check:

python -c "from omnia import evaluate_structural_profile; print('OK import omnia')"


---

3. Canonical test run

Run the full canonical test suite:

pytest

Main test subsets:

pytest tests/test_gate.py
pytest tests/test_demo_profiles.py
pytest tests/test_import.py

Expected state:

all tests pass

At the current frozen minimal state, the expected total is:

11 passed


---

4. Minimal smoke run

Run the minimal smoke test:

python examples/quick_omnia_test.py

Expected output pattern:

one canonical result object

followed by:

OK: OMNIA core executed


This confirms:

import path works

core gate logic works

canonical output schema is emitted



---

5. Canonical JSONL runner

The canonical JSONL runner is:

examples/run_profiles_jsonl.py

Generic pattern:

python examples/run_profiles_jsonl.py <input.jsonl>
python examples/run_profiles_jsonl.py <input.jsonl> -o <output.jsonl>

The runner expects one JSON object per line containing at least:

omega_score

sei_score

iri_score

drift_score


Optional fields are preserved in the output.


---

6. Frozen minimal input/output runs

A. Demo profile run

Input:

examples/demo_profiles.jsonl

Command:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl -o examples/demo_profiles_results.jsonl

Output:

examples/demo_profiles_results.jsonl


---

B. Surface-ok run

Input:

examples/surface_ok_cases.jsonl

Command:

python examples/run_profiles_jsonl.py examples/surface_ok_cases.jsonl -o examples/surface_ok_results.jsonl

Output:

examples/surface_ok_results.jsonl


---

C. LLM surface run

Input:

examples/llm_surface_cases.jsonl

Command:

python examples/run_profiles_jsonl.py examples/llm_surface_cases.jsonl -o examples/llm_surface_results.jsonl

Output:

examples/llm_surface_results.jsonl


---

D. Support-response run

Input:

examples/support_response_cases.jsonl

Command:

python examples/run_profiles_jsonl.py examples/support_response_cases.jsonl -o examples/support_response_results.jsonl

Output:

examples/support_response_results.jsonl


---

7. Frozen analysis runs

Generic analyzer

Script:

examples/analyze_results.py

Command pattern:

python examples/analyze_results.py --input examples/surface_ok_results.jsonl
python examples/analyze_results.py --input examples/llm_surface_results.jsonl
python examples/analyze_results.py --input examples/support_response_results.jsonl
python examples/analyze_results.py --input examples/demo_profiles_results.jsonl

This prints:

total cases

surface_ok count

gate status counts

non-GO ratio

non-GO case list when case_id exists



---

LLM surface analyzer

Script:

examples/analyze_llm_surface_results.py

Command:

python examples/analyze_llm_surface_results.py

This prints the bounded LLM surface mini-result summary.


---

Support-response analyzer

Script:

examples/analyze_support_response_results.py

Command:

python examples/analyze_support_response_results.py

This prints the bounded support-response mini-result summary.


---

8. Rebuild all frozen result artifacts

The canonical rebuild script is:

examples/rebuild_all_results.py

Command:

python examples/rebuild_all_results.py

This script rebuilds all frozen result JSONL artifacts from their canonical input files:

examples/demo_profiles_results.jsonl

examples/surface_ok_results.jsonl

examples/llm_surface_results.jsonl

examples/support_response_results.jsonl


This is the shortest reproducible command for regenerating the current frozen mini-result artifact layer.


---

9. Rebuild and analyze all frozen artifacts

The canonical orchestration script is:

examples/rebuild_and_analyze_all.py

Command:

python examples/rebuild_and_analyze_all.py

This script performs, in one bounded run:

1. rebuild all frozen result JSONL artifacts


2. verify that all rebuilt result files exist


3. run the generic analyzer on all frozen result files


4. run the LLM-specific analyzer



This is the shortest end-to-end bounded reproducibility command currently supported by the repository.


---

10. Current reproducible artifact chain

The current canonical artifact chain is:

input JSONL
-> OMNIA JSONL runner
-> result JSONL
-> analysis script
-> mini-result summary document

This is the current reproducible run surface of OMNIA CORE v1.


---

11. What is reproducible now

The following are reproducible now:

package installation

package import

core smoke execution

canonical tests

JSONL batch processing

frozen mini-result regeneration

result analysis from frozen JSONL files

rebuild of all current frozen result artifacts

rebuild-and-analysis of the current frozen result surface


This is the current minimal reproducibility surface.


---

12. What is not yet part of reproducible runs

The following are not yet part of the current reproducible run layer:

real production data pipelines

external benchmark harnesses

live model integrations

hidden-state instrumentation

architecture-specific upstream probes

large-scale comparative evaluations


Those remain outside the current reproducible boundary.


---

13. Canonical one-line formula

The shortest correct formula is:

OMNIA CORE v1 currently supports reproducible install, test, smoke, JSONL run, frozen mini-result regeneration, full frozen artifact rebuild, and bounded result analysis from repository-local artifacts.


---

14. Final status

At the current state of the repository, OMNIA is no longer only readable.

It is reproducibly runnable in a bounded way.