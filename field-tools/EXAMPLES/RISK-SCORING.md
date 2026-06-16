# Example — Risk Scoring

## Decision D

Prioritize remediation, patching, review, intervention, or resource allocation.

## Object pi

Risk score.

## Field Omega

Risk field:

- exposure;
- exploitability;
- asset criticality;
- active exploitation;
- compensating controls;
- business impact;
- blast radius;
- remediation cost;
- time sensitivity.

## Failure mode

Two risks can have the same score but require different actions.

`pi(omega1) = pi(omega2)`

but:

`D(omega1) != D(omega2)`

## Audit conclusion

If the score collapses action-relevant distinctions, the score cannot ground the prioritization decision.

## Correction

Use a decision-specific risk vector or policy-conditioned scoring object.

## Final sentence

A risk score is valid only for the actions it preserves.\n