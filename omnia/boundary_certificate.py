from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class BoundaryCertificateBuildInput:
    """Input adapter for building a BoundaryCertificate from OMNIA measurements."""

    target_repository: str
    ast_deformation_index: float
    perturbation_step: int
    should_continue: bool
    saturation_detected: bool
    reason: str
    certificate_id: str | None = None
    timestamp: str | None = None
    extra_metrics: dict[str, Any] | None = None


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def build_boundary_certificate(
    *,
    target_repository: str,
    ast_deformation_index: float,
    perturbation_step: int,
    should_continue: bool,
    saturation_detected: bool,
    reason: str,
    certificate_id: str | None = None,
    timestamp: str | None = None,
    extra_metrics: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a schema-compatible BoundaryCertificate artifact.

    OMNIA emits a machine-readable artifact only.
    OMNIA does not infer, decide, or validate continuation policy here.
    """

    metrics: dict[str, Any] = {
        "ast_deformation_index": float(ast_deformation_index),
        "perturbation_step": int(perturbation_step),
    }

    if extra_metrics:
        for key, value in extra_metrics.items():
            if key not in metrics:
                metrics[key] = value

    return {
        "metadata": {
            "certificate_id": certificate_id or str(uuid4()),
            "timestamp": timestamp or _utc_timestamp(),
            "target_repository": str(target_repository),
        },
        "metrics": metrics,
        "boundary_status": {
            "should_continue": bool(should_continue),
            "saturation_detected": bool(saturation_detected),
            "reason": str(reason),
        },
    }


def build_boundary_certificate_from_measurement(
    measurement: dict[str, Any],
    *,
    target_repository: str,
    perturbation_step: int = 0,
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Normalize a generic OMNIA measurement dict into a BoundaryCertificate."""

    ast_deformation_index = measurement.get(
        "ast_deformation_index",
        measurement.get(
            "deformation_index",
            measurement.get(
                "drift_score",
                measurement.get("delta_omega", measurement.get("delta", 0.0)),
            ),
        ),
    )

    raw_step = measurement.get("perturbation_step", perturbation_step)

    should_continue = measurement.get("should_continue")
    saturation_detected = measurement.get("saturation_detected")

    if should_continue is None:
        gate = str(
            measurement.get(
                "gate",
                measurement.get("gate_status", measurement.get("status", "")),
            )
        ).upper()

        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            should_continue = False
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            should_continue = True
        else:
            should_continue = not bool(saturation_detected)

    if saturation_detected is None:
        saturation_detected = not bool(should_continue)

    reason = measurement.get("reason")
    if reason is None:
        reason = (
            "Structural saturation reached"
            if bool(saturation_detected)
            else "Additional measurement still yields structural information"
        )

    known_keys = {
        "ast_deformation_index",
        "deformation_index",
        "drift_score",
        "delta_omega",
        "delta",
        "perturbation_step",
        "should_continue",
        "saturation_detected",
        "gate",
        "gate_status",
        "status",
        "reason",
    }

    extra_metrics = {
        key: value
        for key, value in measurement.items()
        if key not in known_keys and isinstance(value, (int, float, str, bool, type(None)))
    }

    return build_boundary_certificate(
        target_repository=target_repository,
        ast_deformation_index=float(ast_deformation_index),
        perturbation_step=int(raw_step),
        should_continue=bool(should_continue),
        saturation_detected=bool(saturation_detected),
        reason=str(reason),
        certificate_id=certificate_id,
        timestamp=timestamp,
        extra_metrics=extra_metrics,
    )
