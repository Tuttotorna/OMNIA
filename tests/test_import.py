from omnia import OmniaResult, evaluate_structural_profile


def test_import_and_basic_execution() -> None:
    result = evaluate_structural_profile(
        omega_score=0.84,
        sei_score=0.77,
        iri_score=0.12,
        drift_score=0.15,
    )

    assert isinstance(result, OmniaResult)
    assert result.gate_status == "GO"
    assert result.reason_code == "stable"