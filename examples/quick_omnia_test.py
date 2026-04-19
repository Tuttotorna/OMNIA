import json

from omnia.core import run_omnia


def main() -> None:
    """
    Minimal smoke test for OMNIA core.

    This script verifies that the canonical core:
    - imports correctly
    - executes on a bounded sample input
    - returns the required output schema
    """

    sample_case = {
        "case_id": "quick-smoke-001",
        "text": "The answer is 4.",
        "variants": [
            "4",
            "The answer is 4",
            "Answer: 4"
        ]
    }

    result = run_omnia(sample_case)

    required_fields = {
        "omega_score",
        "sei_score",
        "iri_score",
        "drift_score",
        "limit_triggered",
        "gate_status",
        "reason_code",
    }

    missing = required_fields - set(result.keys())
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"OMNIA output missing required fields: {missing_list}")

    numeric_fields = ("omega_score", "sei_score", "iri_score", "drift_score")
    for field in numeric_fields:
        value = result[field]
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field} must be numeric, got {type(value).__name__}")
        if not (0.0 <= float(value) <= 1.0):
            raise ValueError(f"{field} must be in [0.0, 1.0], got {value}")

    if not isinstance(result["limit_triggered"], bool):
        raise TypeError("limit_triggered must be boolean")

    allowed_gate_status = {"GO", "RISK", "NO_GO", "UNSTABLE"}
    if result["gate_status"] not in allowed_gate_status:
        raise ValueError(
            f"gate_status must be one of {sorted(allowed_gate_status)}, got {result['gate_status']}"
        )

    if not isinstance(result["reason_code"], str) or not result["reason_code"].strip():
        raise ValueError("reason_code must be a non-empty string")

    print(json.dumps(result, indent=2, sort_keys=True))
    print("OK: OMNIA core executed")


if __name__ == "__main__":
    main()