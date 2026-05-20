from omnia import build_boundary_certificate
from omnia_limit import BoundaryCertificate, validate_certificate


def test_omnia_emitted_boundary_certificate_validates_against_omnia_limit():
    raw = build_boundary_certificate(
        certificate_id="omnia-to-limit-contract",
        timestamp="2026-05-20T20:00:00Z",
        target_repository="OMNIA",
        ast_deformation_index=0.42,
        perturbation_step=3,
        should_continue=False,
        saturation_detected=True,
        reason="Structural saturation reached",
    )

    cert = validate_certificate(raw)

    assert isinstance(cert, BoundaryCertificate)
    assert cert.certificate_id == "omnia-to-limit-contract"
    assert cert.target_repository == "OMNIA"
    assert cert.ast_deformation_index == 0.42
    assert cert.perturbation_step == 3
    assert cert.should_continue is False
    assert cert.saturation_detected is True
