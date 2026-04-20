File: docs/ACCOUNT_ACCESS_HOLLOW_CASE_ANALYSIS_V1.md

# OMNIA - Account Access Hollow Case Analysis V1

## Purpose

This document records the case-level analysis for the focused benchmark:

```text
account_access_hollow_responses_v1

Its goal is to inspect the specific responses that OMNIA intercepted after tuning, and to verify whether they belong to the intended failure family.

This is not a broad interpretation layer. It is a bounded inspection of the 7 reviewed cases that produced the observed gain.


---

Benchmark result context

In the focused benchmark:

baseline false accepts: 14

baseline + OMNIA false accepts: 7

false accept reduction: 7

false reject increase: 0


So the key question is:

> are the 7 intercepted cases genuinely hollow account-access responses, or is the improvement arbitrary?




---

Intercepted cases

Case 1

Case ID

aah-004

Prompt

My account is locked and I need access now.

Response

We are sorry for the inconvenience. Please try again later.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.702155,
  "sei_score": 0.761724,
  "iri_score": 0.297845,
  "drift_score": 0.297845,
  "reason_code": "high_drift"
}

Interpretation

This is a canonical hollow response:

polite

readable

no recovery path

no actionable access instruction

generic delay only


The interception is correct.


---

Case 2

Case ID

aah-006

Prompt

My password reset email never arrives and I still cannot log in.

Response

We appreciate your patience while we review this.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.747054,
  "sei_score": 0.797643,
  "iri_score": 0.252946,
  "drift_score": 0.252946,
  "reason_code": "low_omega"
}

Interpretation

The response contains no reset guidance, no fallback path, no operational action. It is pure reassurance plus delay. The interception is correct.


---

Case 3

Case ID

aah-007

Prompt

My account recovery request is still pending and I cannot sign in.

Response

Your request is important to us and we are reviewing it.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.740349,
  "sei_score": 0.792279,
  "iri_score": 0.259651,
  "drift_score": 0.259651,
  "reason_code": "low_omega"
}

Interpretation

Again:

readable

polite

no access-restoration path

no concrete next action

only review/deflection language


The interception is correct.


---

Case 4

Case ID

aah-014

Prompt

The login verification code never arrives and I cannot access my account.

Response

We are sorry for the inconvenience. Please try again later.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.688967,
  "sei_score": 0.751173,
  "iri_score": 0.311033,
  "drift_score": 0.311033,
  "reason_code": "high_drift"
}

Interpretation

This is structurally the same failure family as aah-004, under a verification-code scenario. No actionable recovery instruction is present. The interception is correct.


---

Case 5

Case ID

aah-016

Prompt

I am locked out after changing my password and now nothing works.

Response

We appreciate your patience while we review this.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.746349,
  "sei_score": 0.79708,
  "iri_score": 0.253651,
  "drift_score": 0.253651,
  "reason_code": "low_omega"
}

Interpretation

This response is empty in operational terms. It gives no recovery instruction and no concrete next step. The interception is correct.


---

Case 6

Case ID

aah-017

Prompt

My account unlock request is still pending and I have no update.

Response

Your request is important to us and we are looking into it.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.749866,
  "sei_score": 0.799893,
  "iri_score": 0.250134,
  "drift_score": 0.250134,
  "reason_code": "low_omega"
}

Interpretation

This is not action. It is status-padding. No verification path, no unlock path, no escalation instruction. The interception is correct.


---

Case 7

Case ID

aah-018

Prompt

I cannot remove the old phone number from two-factor authentication.

Response

We understand your concern and appreciate your patience.

Label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.750643,
  "sei_score": 0.800515,
  "iri_score": 0.249357,
  "drift_score": 0.249357,
  "reason_code": "low_omega"
}

Interpretation

This response contains no recovery mechanism at all. It is pure relational cushioning. The interception is correct.


---

Shared pattern across intercepted cases

The 7 intercepted cases share the same structural pattern:

readable

polite

surface-acceptable

no concrete recovery mechanism

no actionable escalation path

no operational path to regained access

dominated by reassurance, delay, or passive review language


This is exactly the benchmark target family.


---

What OMNIA is detecting here

OMNIA is not detecting semantics in the rich sense.

What it is detecting in practice is a bounded structural profile of hollow account-access replies:

polite shell
+
low operational anchor density
+
high degradation under action-preserving transforms

That is the current operational meaning of the signal.


---

Why this matters

This case analysis matters because the gain is not coming from trivial garbage filtering.

The intercepted cases are not:

corrupted strings

junk tokens

malformed text


They are the harder category:

human-readable

support-like

superficially acceptable

operationally hollow


That makes the result materially more interesting.


---

What this does not prove

This analysis does not prove:

general support-domain validity

semantic understanding

universal hollow-response detection

production readiness


It proves only that, in this focused benchmark, the reviewed cases are the intended kind of failures.


---

Current conclusion

The focused benchmark gain is not cosmetic.

The 7 reviewed cases belong to the exact failure family the benchmark was designed to isolate.

That supports the narrow conclusion:

OMNIA is now meaningfully detecting hollow account-access deflections inside a bounded benchmark.


---

Canonical analysis sentence

In the focused account-access benchmark, OMNIA's 7 reviewed cases were all polite, readable, but operationally hollow responses with no real recovery path or actionable access instruction.