# OMNIA - Focused Proof

## Problem

Some support responses look acceptable on the surface:

- readable
- polite
- grammatically fine
- support-like in tone

But they are still operationally weak.

This is especially visible in account-access scenarios such as:

- locked account
- recovery blocked
- verification code not arriving
- outdated recovery contact
- failed login recovery

A weak surface baseline tends to let these responses pass because they are not broken text.

---

## Focused benchmark

The focused benchmark is:

```text
account_access_hollow_responses_v1

It contains account-access responses that can appear acceptable at surface level while remaining materially weak as recovery guidance.

The benchmark used in the public run contained:

total cases: 20
total FAIL labels: 14
total PASS labels: 6


---

What the baseline did

The baseline was intentionally weak.

It treated readable non-empty responses as acceptable.

Observed result:

false accepts: 14
false accept rate: 1.0
false rejects: 0
false reject rate: 0.0
review count: 0
review rate: 0.0
true accepts: 6
true rejects: 0

So the baseline passed every hollow failure.


---

What OMNIA did

Using the same dataset and the same baseline, adding OMNIA changed the result to:

false accepts: 7
false accept rate: 0.5
false rejects: 0
false reject rate: 0.0
review count: 7
review rate: 0.35
true accepts: 6
true rejects: 7

So OMNIA reduced false accepts by half without increasing false rejects.

More precisely, OMNIA intercepted 7 failure cases that the baseline would otherwise have allowed to pass automatically, shifting them into review.


---

Result table

Metric	Baseline	Baseline + OMNIA

Total cases	20	20
Total FAIL labels	14	14
Total PASS labels	6	6
False accepts	14	7
False accept rate	1.0	0.5
False rejects	0	0
False reject rate	0.0	0.0
Review count	0	7
Review rate	0.0	0.35
True accepts	6	6
True rejects	0	7



---

What OMNIA was catching

The intercepted cases were not junk.

They were:

readable

polite

apparently acceptable

operationally hollow


Typical pattern:

reassurance

delay language

passive review language

no real recovery path

no actionable access instruction


Example pattern:

> We are sorry for the inconvenience. Please try again later.



In an account-access scenario, that is surface-clean but materially weak.


---

Why this matters

This result is stronger than a generic demo because it shows:

a frozen dataset

a fixed baseline

a fixed evaluation mapping

a measurable delta

no false reject increase


It is not a claim about universal truth. It is a bounded operational result.


---

What this proves

It proves this narrow statement:

> On a focused benchmark of operationally hollow account-access responses, OMNIA reduced false accepts from 14 to 7 by shifting 7 failure cases from automatic pass to review, with no observed increase in false rejects.



That is the current proof.


---

What this does not prove

It does not prove:

general support-domain superiority

universal robustness

cross-domain transfer

semantic understanding

production readiness


This is a focused proof, not a general validation.


---

Minimal conclusion

OMNIA is not yet broadly validated.

But on the focused account-access hollow benchmark, it showed a clear bounded result:

false accepts cut in half

no false reject increase

7 failure cases intercepted before automatic acceptance


That is the first focused public proof that OMNIA can add operational value on a real failure family.