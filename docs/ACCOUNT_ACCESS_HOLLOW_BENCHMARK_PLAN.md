# OMNIA - Account Access Hollow Benchmark Plan

## Purpose

This document defines a focused benchmark for the failure family that OMNIA actually showed signs of detecting.

The goal is not to broaden claims.

The goal is to test whether OMNIA performs better on the specific response class where V1 and V2 already showed a narrow signal.

---

## Benchmark identity

Benchmark name:

```text
account_access_hollow_responses_v1

Task family:

account access / account recovery / verification / login blockage

Failure family under test:

polite
readable
surface-acceptable
operationally hollow responses


---

Why this benchmark exists

The first two support-screening validations showed a narrow but repeatable pattern:

OMNIA did not broadly discriminate across all support-style FAIL cases

OMNIA did show bounded review pressure on a specific class of cases

the recurring class was account-access style hollow deflection


So the correct next move is not to pretend generality.

It is to test the family where signal actually appeared.


---

Core question

The benchmark asks only this:

> can OMNIA reliably detect polite but operationally hollow responses in account-access and recovery scenarios better than a naive surface baseline?




---

Scope

Included prompts:

locked account

account recovery

failed verification

old phone or email bound to verification

password reset failure

login blocked after repeated attempts

recovery code not arriving

2FA migration issues


Included response type under interest:

polite but empty reassurance

delay-without-resolution replies

generic “please try again later”

generic “we understand your concern”

generic “we are reviewing this”

readable but operationally weak replies


Excluded:

unrelated shipping-only prompts

refund-only prompts

invoice-only prompts

long multi-turn thread contexts

cases needing hidden context



---

Benchmark size

Target size:

30 items

This is enough for a narrow focused benchmark without becoming noisy.


---

Composition rule

Target composition:

10 PASS operationally acceptable
20 FAIL surface-ok but hollow

This is intentionally asymmetric.

The benchmark is not intended to be balanced for its own sake. It is intended to pressure-test the narrow failure family OMNIA appears to detect.


---

Labeling rule

Labeling question remains unchanged:

> should this response be allowed to pass forward?



Labels remain:

PASS

FAIL


No new label types are introduced.


---

Baseline rule

Use the same weak surface-level baseline philosophy:

readable + non-empty -> usually PASS

obvious corruption -> BLOCK

no semantic or structural measurement


This preserves continuity with prior benchmarks.


---

OMNIA rule

Use the current OMNIA runner and gate mapping in force when the benchmark is frozen.

Operational mapping remains:

GO -> PASS
RISK -> REVIEW
NO_GO -> BLOCK
UNSTABLE -> BLOCK


---

Primary metric

Primary metric:

false accept rate

The benchmark is successful only if baseline + OMNIA reduces false accepts versus baseline alone.


---

Secondary metrics

Secondary metrics:

false reject rate

review rate

number of intercepted hollow account-access cases



---

Success criterion

This benchmark counts as successful only if:

1. OMNIA reduces false accepts relative to baseline


2. no unacceptable false reject increase appears


3. intercepted cases are genuinely hollow account-access responses, not arbitrary noise


4. the result is reproducible




---

Failure criterion

The benchmark fails if:

OMNIA does not improve over baseline

OMNIA only catches trivial garbage

OMNIA introduces unacceptable false rejects

the V1/V2 signal disappears even inside this focused family



---

Output artifacts

Suggested artifacts:

data/account_access_hollow_responses_v1.jsonl
examples/account_access_hollow_v1_baseline_results.jsonl
examples/account_access_hollow_v1_omnia_results.jsonl
docs/ACCOUNT_ACCESS_HOLLOW_RESULT_V1.md
docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md


---

What this benchmark does not claim

This benchmark does not claim:

general support-domain validation

cross-domain validity

broad external superiority

semantic understanding

production readiness


It is only a focused test of the failure family where OMNIA has already shown a narrow signal.


---

Minimal benchmark summary

benchmark: account_access_hollow_responses_v1
size: 30
task: account access / recovery hollow responses
comparison: baseline vs baseline + OMNIA
primary metric: false accept rate
goal: verify whether OMNIA's observed narrow signal is real inside its apparent target family


---

Canonical benchmark sentence

This benchmark tests whether OMNIA's small observed signal becomes stronger when evaluation is restricted to polite but operationally hollow account-access responses.

