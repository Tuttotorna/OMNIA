# BoundaryCertificate emission bridge

This document defines the software bridge from OMNIA core measurements to the ecosystem boundary contract.

Flow:

OMNIA measurement
  -> build_boundary_certificate(...)
  -> BoundaryCertificate
  -> omnia_limit.validate_certificate(...)
  -> OMNIA-VALIDATION ValidationEnvelope

Boundary:

OMNIA emits a machine-readable measurement artifact.

OMNIA does not decide semantic truth.

OMNIA does not own the continuation policy.

The BoundaryCertificate is consumed by omnia-limit, which validates the contract and exposes the boundary state to downstream control-plane layers such as OMNIA-VALIDATION.

Public API:

from omnia import build_boundary_certificate
from omnia import build_boundary_certificate_from_measurement

Minimal example:

from omnia import build_boundary_certificate
from omnia_limit import validate_certificate

raw = build_boundary_certificate(
    target_repository="OMNIA",
    ast_deformation_index=0.42,
    perturbation_step=3,
    should_continue=False,
    saturation_detected=True,
    reason="Structural saturation reached",
)

cert = validate_certificate(raw)
