# OMNIA - External Validation Case Analysis V1

## Purpose

This document records the case-level analysis of the first bounded external validation result for OMNIA core on the support-response screening task.

Its goal is to inspect the specific cases where:

- baseline alone allowed the response to pass
- baseline + OMNIA did not allow direct pass-through

This is the first concrete check of whether OMNIA's measured improvement is meaningful or merely cosmetic.

---

## Context

In the first frozen external validation run:

- baseline false accepts: `9`
- baseline + OMNIA false accepts: `7`

So OMNIA reduced false accepts by `2` cases.

The next necessary question is:

> which two cases were intercepted, and are they actually the kind of fragile responses OMNIA is supposed to detect?

---

## Intercepted case 1

### Case ID
`support-008`

### Prompt
```text
My account is locked and I need access now.

Response

We are sorry for the inconvenience. Please try again later.

Frozen label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.740531,
  "sei_score": 0.792425,
  "iri_score": 0.259469,
  "drift_score": 0.259469,
  "reason_code": "moderate_fragility"
}

Case interpretation

This response is polite and readable, so the baseline lets it pass.

But operationally it is weak:

it does not address the locked-account problem with sufficient actionability

it does not provide a meaningful resolution path

it deflects with a generic delay instruction


This is a good example of a superficially acceptable but materially weak support response.


---

Intercepted case 2

Case ID

support-010

Prompt

Where is my order?

Response

Thank you for reaching out about your order. We understand how important this is.

Frozen label

FAIL

Baseline result

PASS

OMNIA result

gate status: RISK

combined decision: REVIEW


OMNIA structural output

{
  "omega_score": 0.722719,
  "sei_score": 0.778176,
  "iri_score": 0.277281,
  "drift_score": 0.277281,
  "reason_code": "moderate_fragility"
}

Case interpretation

This response is also polite and readable, so the baseline allows it to pass.

But operationally it is hollow:

it gives no order-status information

it provides no action

it contains only relational cushioning


This is another good example of a response that looks acceptable on the surface but is empty where support value should exist.


---

What these two cases have in common

Both intercepted responses are:

readable

polite

superficially acceptable

weak in operational content

incorrectly allowed by the surface baseline


This is important because OMNIA did not merely catch garbage text or obvious corruption.

It caught two cases that are harder to screen with a naive surface filter.

That is exactly the kind of gap the current bounded validation was designed to test.


---

Meaning of the result

The first external validation gain is small in scale, but it is not arbitrary.

The intercepted cases are structurally relevant.

They support this narrow interpretation:

> OMNIA can add bounded review pressure on polite but operationally empty support responses that a surface baseline incorrectly allows to pass.



This is a more meaningful result than simply blocking obvious junk.


---

What this does not prove

This case analysis does not prove:

broad external validity

general superiority of OMNIA

production readiness

semantic understanding

large-scale robustness


The dataset remains small and the result remains narrow.


---

Current conclusion

The first bounded external validation result is small but meaningful.

The two improvements are not cosmetic. They correspond to exactly the type of support-style failure mode that the validation protocol was meant to expose:

surface-ok
readable
polite
operationally hollow


---

Canonical analysis sentence

On the first frozen support-screening dataset, OMNIA specifically intercepted polite but operationally empty responses that the baseline incorrectly allowed to pass.