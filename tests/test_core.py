from omnia import run_omnia


def test_run_omnia_returns_canonical_schema() -> None:
    case = {
        "case_id": "core-001",
        "text": "The answer is 4.",
        "variants": [
            "4",
            "The answer is 4",
            "Answer: 4",
        ],
    }

    result = run_omnia(case)

    assert set(result.keys()) >= {
        "omega_score",
        "sei_score",
        "iri_score",
        "drift_score",
        "limit_triggered",
        "gate_status",
        "reason_code",
    }

    assert isinstance(result["omega_score"], (int, float))
    assert isinstance(result["sei_score"], (int, float))
    assert isinstance(result["iri_score"], (int, float))
    assert isinstance(result["drift_score"], (int, float))
    assert isinstance(result["limit_triggered"], bool)
    assert isinstance(result["gate_status"], str)
    assert isinstance(result["reason_code"], str)


def test_run_omnia_scores_are_bounded() -> None:
    case = {
        "text": "Answer: 4",
        "variants": [
            "4",
            "The answer is 4",
            "Result: 4",
        ],
    }

    result = run_omnia(case)

    for field in ("omega_score", "sei_score", "iri_score", "drift_score"):
        value = float(result[field])
        assert 0.0 <= value <= 1.0


def test_run_omnia_gate_status_is_valid() -> None:
    case = {
        "text": "The answer is 4.",
        "variants": [
            "4",
            "Answer: 4",
        ],
    }

    result = run_omnia(case)

    assert result["gate_status"] in {"GO", "RISK", "NO_GO", "UNSTABLE"}


def test_run_omnia_reason_code_is_non_empty() -> None:
    case = {
        "text": "The answer is 4.",
        "variants": [
            "4",
            "Answer: 4",
        ],
    }

    result = run_omnia(case)

    assert result["reason_code"].strip() != ""


def test_run_omnia_preserves_case_id_when_present() -> None:
    case = {
        "case_id": "preserve-001",
        "text": "The answer is 4.",
        "variants": ["4"],
    }

    result = run_omnia(case)

    assert result["case_id"] == "preserve-001"