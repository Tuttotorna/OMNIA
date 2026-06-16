# Example — AI Benchmarks

## Decision D

Select or deploy a model.

## Object pi

Benchmark score or leaderboard rank.

## Field Omega

Real deployment field:

- task distribution;
- environment;
- latency;
- cost;
- reliability;
- failure modes;
- safety;
- recoverability;
- tool-use constraints;
- verifier quality;
- infrastructure.

## Failure mode

Two models may have the same benchmark score but require different deployment decisions.

`pi(model1) = pi(model2)`

but:

`D(model1) != D(model2)`

## Audit conclusion

If the score collapses deployment-relevant distinctions, the benchmark cannot ground the deployment decision.

## Correction

Use a deployment-conditioned evaluation object, not only a scalar benchmark score.

## Final sentence

A benchmark is valid only for the deployment decisions it preserves.\n