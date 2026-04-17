"""
OMNIA CORE v1
Post-hoc structural measurement and gating system.
"""

from .gate import OmniaResult, evaluate_structural_profile

__all__ = [
    "__version__",
    "OmniaResult",
    "evaluate_structural_profile",
]

__version__ = "0.1.0"