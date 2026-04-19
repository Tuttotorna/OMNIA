from omnia.core import run_omnia


def evaluate_structural_profile(case):
    return run_omnia(case)


__all__ = ["run_omnia", "evaluate_structural_profile"]