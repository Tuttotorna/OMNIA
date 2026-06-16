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