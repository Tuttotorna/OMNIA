# OMNIA Repository Status

Generated / updated: 2026-05-08T16:37:05.119479+00:00

## Status

OMNIA is currently a working Python repository with package metadata, examples, documentation, stored results, and tests.

Clean-environment checks performed during the public documentation cleanup:

```text
import omnia        OK
pip install -e .    OK
pytest              47 passed
```

## Core role

OMNIA is the structural measurement core.

It measures structural behavior after an output, answer, trajectory, or representation already exists.

It is not a model.

It is not a truth oracle.

It is not a final decision system.

## Boundary

```text
measurement != inference != decision
```

## What was cleaned

This cleanup does not modify the Python core.

It does not modify the test suite.

It does not modify validation scripts.

It only improves public-facing repository clarity:

- README.md cleaned and shortened
- DOI badge corrected
- CITATION.cff added
- repository status document added
- GitHub About / Description / Homepage / Topics aligned
- GitHub Release updated or created

## Current DOI

```text
10.5281/zenodo.19820729
https://doi.org/10.5281/zenodo.19820729
```

## License status

No LICENSE file was added automatically.

This is intentional.

A license should only be added after an explicit choice.

Common options:

- MIT for maximum openness
- Apache-2.0 for openness with patent language
- no license if reuse should remain legally restricted by default

## Interpretation

OMNIA should be read as a measurement layer, not as a reasoning or decision layer.

The correct system boundary is:

```text
OMNIA measures.
External layers infer.
External layers decide.
```
