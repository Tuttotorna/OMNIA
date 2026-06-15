<!-- TOTALITY_FIELD_ALIGNMENT_START -->
## Totality Field Alignment

This repository is not an independent fragment.

It is a local operational appearance of the same total field formalized in [LAW OF TOTALITY](https://github.com/Tuttotorna/LAW-OF-TOTALITY).

Public threshold release: [v0.1.2](https://github.com/Tuttotorna/LAW-OF-TOTALITY/releases/tag/v0.1.2)

DOI: [10.5281/zenodo.20700914](https://doi.org/10.5281/zenodo.20700914)

See: [TOTALITY-FIELD.md](TOTALITY-FIELD.md)
<!-- TOTALITY_FIELD_ALIGNMENT_END -->

<!-- DOI OWNERSHIP AUDIT:START -->

## DOI ownership audit

This repository uses strict DOI ownership by exact repository identity.

OMNIA != OMNIA-VALIDATION
OMNIA DOI != OMNIA-VALIDATION DOI
repo_name substring match is forbidden for DOI ownership
exact repository identity is required for DOI ownership
this_repository: Tuttotorna/OMNIA
this_repository_doi: 10.5281/zenodo.20322683
other_repository: Tuttotorna/OMNIA-VALIDATION
other_repository_doi: 10.5281/zenodo.20322696

<!-- DOI OWNERSHIP AUDIT:END -->

<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIA
Release tag: v2026.05.21
Release commit: 335ea50
Release DOI: 10.5281/zenodo.20322683

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement
DOI ownership != substring match
OMNIA != OMNIA-VALIDATION

<!-- MB-X.01 LON RELEASE:END -->

# OMNIA

<!-- ZENODO DOI:START -->

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281%2Fzenodo.20322683.svg)](https://doi.org/10.5281/zenodo.20322683)

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA
GitHub repository id: 1142595417
Release tag: v2026.05.21
Release commit: 335ea50
Latest release DOI: 10.5281/zenodo.20322683

Ownership rule:

exact repository identity is required for DOI ownership
repo_name substring match is forbidden for DOI ownership
OMNIA != OMNIA-VALIDATION
OMNIA DOI != OMNIA-VALIDATION DOI

<!-- ZENODO DOI:END -->


## DOI

[![DOI](https://zenodo.org/badge/1142595417.svg)](https://zenodo.org/badge/latestdoi/1142595417)

Release DOI: [10.5281/zenodo.19820729](https://doi.org/10.5281/zenodo.19820729)

GitHub release: [OMNIA v1.0.0 release](https://github.com/Tuttotorna/OMNIA/releases/tag/v1.0.0)

## Start here

From a clean environment:

    git clone [OMNIA.git](https://github.com/Tuttotorna/OMNIA.git)
    cd OMNIA
    python -m pip install -e .
    pytest

If example scripts are available, run the smallest smoke test after tests pass.

The goal is to see the engine as a pipeline, not as a manifesto.

---

## What OMNIA does

OMNIA measures structural behavior.

It can be used to observe whether an output, trace, representation, transformation, or trajectory remains structurally admissible under controlled changes.

The core engine path is:

    input
      -> transformation
      -> measurement
      -> structural output
      -> boundary signal

OMNIA may expose signals such as stability, drift, irreversibility, saturation, compatibility, or structural fragility depending on the implemented measurement path.

---

## What OMNIA does not do

OMNIA does not:

- infer semantic truth;
- decide correctness;
- replace external judgment;
- claim consciousness;
- perform security scanning;
- perform cryptographic attacks;
- recover keys;
- prove physical truth;
- turn structural stability into final meaning.

OMNIA stops at measurement.

Interpretation and decision remain external.

---

## Public mental model

    Surface correctness can pass.
    Structural stability can fail.
    OMNIA measures the structural side.

---

## Engine contract

Every serious OMNIA measurement should make clear:

| Component | Meaning |
|---|---|
| input | What object, trace, output, or representation enters the engine |
| transformation | What controlled change is applied or observed |
| measurement | What structural property is measured |
| output | What signal, score, report, or artifact is produced |
| boundary | What the result does and does not claim |

---

## Minimal output discipline

A useful OMNIA output should distinguish:

    measured signal
    structural interpretation
    external decision

The engine may produce the first.

The second must be explicit.

The third is outside OMNIA.

---

## Recommended reading order

1. [docs/QUICKSTART_ENGINE.md](docs/QUICKSTART_ENGINE.md)
2. [docs/ENGINE_OVERVIEW.md](docs/ENGINE_OVERVIEW.md)
3. [docs/INPUT_OUTPUT_CONTRACT.md](docs/INPUT_OUTPUT_CONTRACT.md)
4. [docs/MEASUREMENT_BOUNDARY.md](docs/MEASUREMENT_BOUNDARY.md)
5. [docs/METRICS_GLOSSARY.md](docs/METRICS_GLOSSARY.md)
6. [docs/ENGINE_MANIFEST.json](docs/ENGINE_MANIFEST.json)

---

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

---

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    measurement != inference != decision

---

## License

MIT.

<!-- OMNIA_ECOSYSTEM_BOUNDARY_V1 -->

## Ecosystem Boundary

```text
measurement != inference != decision
```

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs must be read as structural measurement, validation, detection, orchestration or adapter artifacts according to the repository role. They are not autonomous semantic truth claims and they do not make external decisions.

<!-- OMNIA_PUBLIC_CLAIM_BOUNDARY_V1 -->

## Public Claim Boundary

~~~text
measurement != inference != decision
~~~

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs are structural measurement or validation artifacts, not semantic truth claims or autonomous decisions.

<!-- STRUCTURAL_OBSERVABILITY_ROLE_START -->
## Structural Observability role

This repository is one bounded measurement role inside **Structural Observability**.

Role:

~~~text
core post-hoc structural measurement engine
~~~

Boundary:

~~~text
OMNIA measures structural behavior after an output, trace, or artifact already exists. It does not infer meaning, learn, or decide.
~~~

Structural Observability foundation:

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- Foundation release: https://github.com/Tuttotorna/lon-mirror/releases/tag/v0.2.2
- DOI: https://doi.org/10.5281/zenodo.20379374

Role document:

- [Structural Observability Role](docs/STRUCTURAL_OBSERVABILITY_ROLE.md)
<!-- STRUCTURAL_OBSERVABILITY_ROLE_END -->

## Foundational Principle

OMNIA is an output-level application of the L.O.N. Multi-Form Invariance Principle:

> No single form is sovereign.

In OMNIA, this becomes:

> No output form is sovereign.

A response is not trusted because it appears correct once. It must preserve structural compatibility under independent transformations of form.

See:

- https://github.com/Tuttotorna/lon-mirror/tree/main/foundation

<!-- OMNIA_ZENODO_CITATION_BLOCK_START -->

## Citation and archival

This repository is prepared for GitHub-Zenodo archival.

Repository:
https://github.com/Tuttotorna/OMNIA

Latest GitHub release: v2026.05.21 (https://github.com/Tuttotorna/OMNIA/releases/tag/v2026.05.21)

Detected Zenodo DOI(s):
- https://doi.org/10.5281/zenodo.20322683
- https://doi.org/10.5281/zenodo.20322696
- https://doi.org/10.5281/zenodo.19820729
- https://doi.org/10.5281/zenodo.20379374

Metadata files used for archival/citation:

- .zenodo.json
- CITATION.cff

Zenodo note:

GitHub-Zenodo archiving works after the repository is enabled in Zenodo GitHub settings and a GitHub release is created.

<!-- OMNIA_ZENODO_CITATION_BLOCK_END -->
