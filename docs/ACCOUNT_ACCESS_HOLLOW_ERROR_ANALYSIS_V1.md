# OMNIA - Account Access Hollow Error Analysis V1

## Purpose

This document records the first error analysis for the focused benchmark:

```text
account_access_hollow_responses_v1

Its goal is not to restate the benchmark result.

Its goal is to inspect where OMNIA behaved correctly and where it was too aggressive.


---

Benchmark result summary

Baseline

total cases: 20

PASS labels: 6

FAIL labels: 14

false accepts: 14

false accept rate: 1.0

false rejects: 0


Baseline + OMNIA

false accepts: 12

false accept rate: 0.857143

false rejects: 2

false reject rate: 0.333333

review count: 4



---

Core interpretation

The focused benchmark showed a real signal, but not a clean one.

OMNIA did detect true hollow failures.

But it also sent some operationally acceptable responses to review.

So the current state is:

signal exists
selection quality still insufficient


---

True positives

These are cases where:

baseline allowed the response to pass

OMNIA sent the response to review

the frozen label is FAIL


True positive 1

Case ID

aah-004

Prompt

My account is locked and I need access now.

Response

We are sorry for the inconvenience. Please try again later.

OMNIA output

{
  "omega_score": 0.726258,
  "sei_score": 0.781006,
  "iri_score": 0.273742,
  "drift_score": 0.273742,
  "reason_code": "high_drift"
}

Why this interception is correct

The response is readable and polite, but operationally empty.

It does not:

restore access

provide a concrete recovery path

instruct the user toward a meaningful next step


It is a classic hollow account-access reply.


---

True positive 2

Case ID

aah-014

Prompt

The login verification code never arrives and I cannot access my account.

Response

We are sorry for the inconvenience. Please try again later.

OMNIA output

{
  "omega_score": 0.713069,
  "sei_score": 0.770455,
  "iri_score": 0.286931,
  "drift_score": 0.286931,
  "reason_code": "high_drift"
}

Why this interception is correct

This is the same hollow pattern under a different account-access scenario.

It is:

polite

surface-clean

operationally weak

not sufficient to justify pass-forward


This is exactly the failure family the benchmark was designed to isolate.


---

False reviews

These are cases where:

baseline allowed the response to pass

OMNIA sent the response to review

the frozen label is PASS


These are not catastrophic false blocks, but they are still errors relative to the benchmark objective.

False review 1

Case ID

aah-002

Prompt

I cannot receive the verification code because it still goes to my old phone number.

Response

To regain access, contact support to update your verification method after identity review.

OMNIA output

{
  "omega_score": 0.742375,
  "sei_score": 0.7939,
  "iri_score": 0.257625,
  "drift_score": 0.257625,
  "reason_code": "low_omega"
}

Why this review is wrong

This response is short, but still operationally acceptable.

It provides:

a clear next step

a support escalation path

a concrete resolution direction tied to the actual failure mode


So it is not hollow. It is compressed, but actionable.


---

False review 2

Case ID

aah-012

Prompt

My old email is still tied to account recovery and I cannot sign in.

Response

To recover access, contact support so your recovery email can be updated after identity verification.

OMNIA output

{
  "omega_score": 0.736955,
  "sei_score": 0.789564,
  "iri_score": 0.263045,
  "drift_score": 0.263045,
  "reason_code": "high_drift"
}

Why this review is wrong

This response is also short, but still acceptable.

It contains:

a recovery path

a condition for remediation

a meaningful account-recovery action


Again, this is not hollow. It is concise but operational.


---

Structural difference between true positives and false reviews

True positives have this pattern

relational cushioning

no real next step

no recovery path

no concrete action

generic delay or deflection


False reviews have this pattern

short but explicit action

support escalation tied to the actual problem

identity verification or recovery path

meaningful operational direction


This is the key distinction.


---

What OMNIA is currently confusing

The current runner appears to confuse:

short and compressed

with:

operationally hollow

That is the actual failure mode of the current setup.

In other words:

it correctly penalizes empty polite padding

but it also penalizes some concise actionable support replies


So the system is currently sensitive to compression, not only to hollowness.


---

Likely cause

The likely cause is in the transformation pressure and risk threshold interaction.

Current transforms aggressively strip:

politeness

action phrases

support-contact instructions

recovery wording


This makes some genuinely acceptable concise responses look too close to hollow templates after transformation.

That pushes them into RISK.


---

Correction hypothesis

The next correction should not make OMNIA less sensitive overall.

It should make OMNIA less likely to punish responses that contain a real operational path.

The most plausible correction is:

preserve actionable recovery phrases as stabilizing content

Examples of phrases that should count as operational anchors:

contact support

manual verification

identity verification

update your verification method

update your recovery email

use the recovery flow

request a new verification code

check your spam folder

request a new reset email


At the moment, the runner removes too much of this.


---

Recommended next change

The next change should happen in the account-access OMNIA runner, not in the benchmark definition.

Target file:

examples/run_omnia_account_access_hollow_v1.py

Correction direction:

1. keep hollow polite padding degradations


2. keep generic deflection degradations


3. reduce degradation of real recovery / verification / escalation actions


4. rerun the same benchmark unchanged



This preserves the benchmark and tests whether selectivity improves.


---

What this analysis proves

This analysis proves that the focused benchmark is useful.

It exposed the real current boundary:

OMNIA does detect the intended hollow family

OMNIA still over-penalizes some concise but valid operational responses


That is a productive error, because it gives a clear tuning target.


---

Canonical error-analysis sentence

On the focused account-access benchmark, OMNIA correctly detected hollow deflection replies, but current tuning still confuses some concise actionable recovery responses with structurally weak ones.