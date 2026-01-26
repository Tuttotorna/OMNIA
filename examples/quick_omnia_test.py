"""
Quick OMNIA smoke test (10 seconds).

Run:
  python examples/quick_omnia_test.py
"""

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator


def main():
    texts = [
        "OMNIA measures invariance under transformation.",
        "OMNIA measures structural drift and residual Ω.",
        "This is a simple smoke test.",
    ]

    kernel = SuperpositionKernel()
    est = OmegaEstimator(kernel=kernel)

    omega_hat = est.estimate(texts)

    print("Ω̂ estimate:", omega_hat)
    print("OK: OMNIA core executed")


if __name__ == "__main__":
    main()
