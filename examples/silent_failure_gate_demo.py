#!/usr/bin/env python3
"""
OMNIA — Silent Failure Gate Demo

Purpose
-------
This demo shows the core OMNIA distinction:

    surface-valid output != structurally stable output

The script creates a minimal set of outputs that all pass basic surface checks,
then applies a simple structural stability gate.

It demonstrates three cases:

    1. stable_output    -> surface PASS + structural GO
    2. fragile_output   -> surface PASS + structural RISK
    3. collapsed_output -> surface FAIL/PASS boundary + structural STOP

This is not a semantic evaluator.
This is not a truth detector.
This is not a production-grade gate.

It is a minimal, readable demonstration of post-hoc structural measurement.

Core boundary:

    measurement != inference != decision
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
import json
from typing import Dict, List, Literal


GateStatus = Literal["GO", "RISK", "STOP"]


@dataclass(frozen=True)
class DemoCase:
    case_id: str
    label: str
    prompt: str
    output: str
    perturbed_outputs: List[str]
    expected_contract: str


@dataclass(frozen=True)
class SurfaceCheckResult:
    non_empty: bool
    has_final_answer_marker: bool
    has_minimum_length: bool
    surface_status: str


@dataclass(frozen=True)
class StructuralMetrics:
    omega: float
    iri: float
    sei: float
    average_similarity: float
    min_similarity: float
    max_degradation: float


@dataclass(frozen=True)
class GateResult:
    case_id: str
    label: str
    surface_status: str
    omnia_status: GateStatus
    metrics: StructuralMetrics
    reason: str
    boundary: str


def surface_check(output: str) -> SurfaceCheckResult:
    """
    Minimal surface check.

    This intentionally checks only shallow properties:

    - output is not empty
    - output contains a final answer marker
    - output has minimal length

    A fragile output may still pass this check.
    That is the point of the demo.
    """

    normalized = output.strip()

    non_empty = bool(normalized)
    has_final_answer_marker = "final answer:" in normalized.lower()
    has_minimum_length = len(normalized) >= 20

    passed = non_empty and has_final_answer_marker and has_minimum_length

    return SurfaceCheckResult(
        non_empty=non_empty,
        has_final_answer_marker=has_final_answer_marker,
        has_minimum_length=has_minimum_length,
        surface_status="PASS" if passed else "FAIL",
    )


def similarity(a: str, b: str) -> float:
    """
    String-level structural similarity.

    This is intentionally simple and transparent.
    It is not semantic similarity.
    It is not correctness.
    It is only a structural comparison proxy.
    """

    return SequenceMatcher(None, a.strip().lower(), b.strip().lower()).ratio()


def compute_structural_metrics(reference: str, variants: List[str]) -> StructuralMetrics:
    """
    Compute simplified structural metrics.

    omega:
        Residual structural coherence.
        Higher means more structural stability.

    iri:
        Irreversibility / degradation proxy.
        Higher means greater divergence from the reference.

    sei:
        Structural exhaustion index.
        Lower means less remaining structural opportunity.

    These simplified formulas are for demonstration only.
    """

    if not variants:
        return StructuralMetrics(
            omega=0.0,
            iri=1.0,
            sei=0.0,
            average_similarity=0.0,
            min_similarity=0.0,
            max_degradation=1.0,
        )

    similarities = [similarity(reference, variant) for variant in variants]

    average_similarity = sum(similarities) / len(similarities)
    min_similarity = min(similarities)
    max_degradation = 1.0 - min_similarity

    omega = round(average_similarity, 4)
    iri = round(max_degradation, 4)

    reference_length = max(len(reference.strip()), 1)
    length_ratios = [
        min(len(variant.strip()) / reference_length, 1.0)
        for variant in variants
    ]

    average_length_ratio = sum(length_ratios) / len(length_ratios)
    sei = round(min(average_similarity, average_length_ratio), 4)

    return StructuralMetrics(
        omega=omega,
        iri=round(iri, 4),
        sei=sei,
        average_similarity=round(average_similarity, 4),
        min_similarity=round(min_similarity, 4),
        max_degradation=round(max_degradation, 4),
    )


def gate_decision(surface: SurfaceCheckResult, metrics: StructuralMetrics) -> tuple[GateStatus, str]:
    """
    Minimal structural gate.

    The thresholds are explicit and intentionally simple.

    GO:
        Surface check passes and structural stability is high.

    RISK:
        Surface check passes but structural stability is degraded.

    STOP:
        Surface check fails or structural collapse is severe.

    This gate does not decide truth.
    It emits a structural signal only.
    """

    if surface.surface_status == "FAIL":
        return (
            "STOP",
            "surface output failed minimal admissibility checks",
        )

    if metrics.omega < 0.35 or metrics.sei < 0.25 or metrics.iri > 0.75:
        return (
            "STOP",
            "structural collapse detected under controlled perturbation",
        )

    if metrics.omega < 0.75 or metrics.sei < 0.60 or metrics.iri > 0.40:
        return (
            "RISK",
            "surface-valid output degraded under controlled perturbation",
        )

    return (
        "GO",
        "output remained structurally stable under tested perturbations",
    )


def evaluate_case(case: DemoCase) -> GateResult:
    surface = surface_check(case.output)
    metrics = compute_structural_metrics(case.output, case.perturbed_outputs)
    status, reason = gate_decision(surface, metrics)

    return GateResult(
        case_id=case.case_id,
        label=case.label,
        surface_status=surface.surface_status,
        omnia_status=status,
        metrics=metrics,
        reason=reason,
        boundary="measurement != inference != decision",
    )


def build_demo_cases() -> List[DemoCase]:
    """
    Build three minimal cases.

    stable_output:
        Output keeps the same structure under nearby transformations.

    fragile_output:
        Output passes surface checks but becomes inconsistent or degraded
        under nearby transformations.

    collapsed_output:
        Output is malformed or collapses structurally.
    """

    return [
        DemoCase(
            case_id="case_001",
            label="stable_output",
            prompt="Answer the arithmetic question with a final answer.",
            output=(
                "Reasoning: 5 groups of 3 items gives 15 items. "
                "Final answer: 15."
            ),
            perturbed_outputs=[
                (
                    "Reasoning: 5 groups of 3 items gives 15 items. "
                    "Final answer: 15."
                ),
                (
                    "Reasoning: 3 items repeated 5 times gives 15 items. "
                    "Final answer: 15."
                ),
                (
                    "Reasoning: 5 multiplied by 3 equals 15. "
                    "Final answer: 15."
                ),
            ],
            expected_contract="final answer with short reasoning",
        ),
        DemoCase(
            case_id="case_002",
            label="fragile_output",
            prompt="Answer the arithmetic question with a final answer.",
            output=(
                "Reasoning: the quantities combine into a stable result. "
                "Final answer: 15."
            ),
            perturbed_outputs=[
                (
                    "Reasoning: the quantities combine into something close. "
                    "Final answer: 15."
                ),
                (
                    "Reasoning: the result depends on how the quantities are read. "
                    "Final answer: maybe 15."
                ),
                (
                    "Reasoning: the structure is not fully determined by the question. "
                    "Final answer: uncertain."
                ),
            ],
            expected_contract="final answer with short reasoning",
        ),
        DemoCase(
            case_id="case_003",
            label="collapsed_output",
            prompt="Answer the arithmetic question with a final answer.",
            output="Final answer: LDL",
            perturbed_outputs=[
                "LDL",
                "",
                "Final:",
            ],
            expected_contract="final answer with short reasoning",
        ),
    ]


def result_to_dict(result: GateResult) -> Dict[str, object]:
    return asdict(result)


def main() -> None:
    cases = build_demo_cases()
    results = [evaluate_case(case) for case in cases]

    print("=" * 80)
    print("OMNIA — Silent Failure Gate Demo")
    print("=" * 80)
    print()
    print("Core distinction:")
    print()
    print("    surface-valid output != structurally stable output")
    print()
    print("Boundary:")
    print()
    print("    measurement != inference != decision")
    print()
    print("=" * 80)
    print()

    for result in results:
        print(f"Case: {result.case_id} — {result.label}")
        print(f"Surface check: {result.surface_status}")
        print(f"OMNIA structural gate: {result.omnia_status}")
        print(f"Reason: {result.reason}")
        print(
            "Metrics: "
            f"omega={result.metrics.omega}, "
            f"iri={result.metrics.iri}, "
            f"sei={result.metrics.sei}"
        )
        print("-" * 80)

    print()
    print("Machine-readable results:")
    print()
    print(json.dumps([result_to_dict(result) for result in results], indent=2))


if __name__ == "__main__":
    main()
