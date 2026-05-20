from omnia import (
    build_boundary_certificate,
    build_boundary_certificate_from_measurement,
)


def test_build_boundary_certificate_shape():
    cert = build_boundary_certificate(
        certificate_id="omnia-core-cert",
        timestamp="2026-05-20T20:00:00Z",
        target_repository="OMNIA",
        ast_deformation_index=0.42,
        perturbation_step=3,
        should_continue=False,
        saturation_detected=True,
        reason="Structural saturation reached",
    )

    assert cert["metadata"]["certificate_id"] == "omnia-core-cert"
    assert cert["metadata"]["timestamp"] == "2026-05-20T20:00:00Z"
    assert cert["metadata"]["target_repository"] == "OMNIA"
    assert cert["metrics"]["ast_deformation_index"] == 0.42
    assert cert["metrics"]["perturbation_step"] == 3
    assert cert["boundary_status"]["should_continue"] is False
    assert cert["boundary_status"]["saturation_detected"] is True
    assert cert["boundary_status"]["reason"] == "Structural saturation reached"


def test_build_boundary_certificate_from_measurement_stop_gate():
    measurement = {
        "drift_score": 0.91,
        "perturbation_step": 5,
        "gate_status": "STOP",
        "omega": 0.8,
        "sei": 0.01,
        "iri": 0.98,
    }

    cert = build_boundary_certificate_from_measurement(
        measurement,
        target_repository="OMNIA",
        certificate_id="from-measurement-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert cert["metadata"]["certificate_id"] == "from-measurement-cert"
    assert cert["metrics"]["ast_deformation_index"] == 0.91
    assert cert["metrics"]["perturbation_step"] == 5
    assert cert["metrics"]["omega"] == 0.8
    assert cert["metrics"]["sei"] == 0.01
    assert cert["metrics"]["iri"] == 0.98
    assert cert["boundary_status"]["should_continue"] is False
    assert cert["boundary_status"]["saturation_detected"] is True


def test_build_boundary_certificate_from_measurement_continue_gate():
    measurement = {
        "delta_omega": 0.12,
        "gate_status": "CONTINUE",
        "reason": "Measurement still productive",
    }

    cert = build_boundary_certificate_from_measurement(
        measurement,
        target_repository="OMNIA",
        perturbation_step=1,
        certificate_id="continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert cert["metrics"]["ast_deformation_index"] == 0.12
    assert cert["metrics"]["perturbation_step"] == 1
    assert cert["boundary_status"]["should_continue"] is True
    assert cert["boundary_status"]["saturation_detected"] is False
    assert cert["boundary_status"]["reason"] == "Measurement still productive"
