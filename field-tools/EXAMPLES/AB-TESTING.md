# Example — A/B Testing

## Decision D

Roll out variant A or B.

## Object pi

Aggregate conversion rate.

## Field Omega

Segmented population:

- new users;
- returning users;
- device types;
- geography;
- traffic source;
- time;
- product state;
- acquisition channel.

## Failure mode

The aggregate may favour B while segments require different rollout decisions.

`pi(omega1) = pi(omega2)` or aggregate equivalence

but:

`D(segment1) != D(segment2)`

## Audit conclusion

The aggregate cannot ground the rollout if it collapses segment distinctions required by the decision.

## Correction

Use segment-preserving decision rules.

## Final sentence

An aggregate is valid only for the rollout decisions it preserves.\n

<!-- AB_TESTING_LOCAL_PROOF_LINK_START -->
## Local proof

A reproducible local counterexample is provided here:

[AB-TESTING-LOCAL-PROOF](AB-TESTING-LOCAL-PROOF/)

It shows:

`pi(omega_1) = pi(omega_2)`

but:

`D(omega_1) != D(omega_2)`

Therefore aggregate conversion rate cannot ground segment-preserving rollout decisions in general.
<!-- AB_TESTING_LOCAL_PROOF_LINK_END -->
