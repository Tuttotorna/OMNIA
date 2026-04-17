"""
Minimal OMNIA CORE v1 batch demo.

Run:
  python examples/silent_failure_demo.py
"""

from __future__ import annotations

import json

from omnia import evaluate_structural_profile


def main() -> None:
    cases = [
        {
            "case_id": "clean_admissible",
            "omega_score": 0.84,
            "sei_score": 0.77,
            "iri_score": 0.12,
            "drift_score": 0.15,
        },
        {
            "case_id": "surface_ok_but_fragile",
            "omega_score": 0.58,
            "sei_score": 0.55,
            "iri_score": 0.31,
            "drift_score": 0.57,
        },
        {
            "case_id": "continuation_not_admissible",
            "omega_score": 0.43,
            "sei_score": 0.16,
            "iri_score": 0.44,
            "drift_score": 0.49,
        },
        {
            "case_id": "collapsed_profile",
            "omega_score": 0.18,
            "sei_score": 0.09,
            "iri_score": 0.87,
            "drift_score": 0.82,
        },
        {
            "case_id": "high_drift_block",
            "omega_score": 0.47,
            "sei_score": 0.45,
            "iri_score": 0.28,
            "drift_score": 0.74,
        },
        {
            "case_id": "extractability_exhausted",
            "omega_score": 0.52,
            "sei_score": 0.12,
            "iri_score": 0.33,
            "drift_score": 0.34,
        },
    ]

    results = []

    for case in cases:
        result = evaluate_structural_profile(
            omega_score=case["omega_score"],
            sei_score=case["sei_score"],
            iri_score=case["iri_score"],
            drift_score=case["drift_score"],
        )

        row = {
            "case_id": case["case_id"],
            **result.to_dict(),
        }
        results.append(row)

    print("OMNIA CORE v1 silent failure demo")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()