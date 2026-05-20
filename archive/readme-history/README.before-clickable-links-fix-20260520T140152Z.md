# OMNIA

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

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

---

## License

MIT.

