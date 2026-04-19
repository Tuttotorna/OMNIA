from omnia import run_omnia


def test_import_and_basic_output_schema() -> None:
    case = {
        "case_id": "test-import-001",
        "text": "The answer is 4.",
        "variants": [
            "4",
            "The answer is 4",
            "Answer: 4",
        ],
    }

    result = run_omnia(case)

    required_fields = {
        "omega_score",
        "sei_score",
        "iri_score",
        "drift_score",
        "limit_triggered",
        "gate_status",
        "reason_code",
    }

    assert required_fields.issubset(result.keys())

    for field in ("omega_score", "sei_score", "iri_score", "drift_score"):
        assert isinstance(result[field], (int, float))
        assert 0.0 <= float(result[field]) <= 1.0

    assert isinstance(result["limit_triggered"], bool)
    assert result["gate_status"] in {"GO", "RISK", "NO_GO", "UNSTABLE"}
    assert isinstance(result["reason_code"], str)
    assert result["reason_code"].strip() != ""