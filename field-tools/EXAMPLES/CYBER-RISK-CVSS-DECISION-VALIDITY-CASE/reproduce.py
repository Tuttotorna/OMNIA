import json
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent

df = pd.read_csv(BASE / "cyber_risk_field.csv")

omega_1 = df[df["cve"] == "CVE-2023-3519"].iloc[0].to_dict()
omega_2 = df[df["cve"] == "CVE-2019-17531"].iloc[0].to_dict()

pi_omega_1 = omega_1["cvss_base_score"]
pi_omega_2 = omega_2["cvss_base_score"]

D_omega_1 = omega_1["decision_D"]
D_omega_2 = omega_2["decision_D"]

pi_equal = pi_omega_1 == pi_omega_2
D_equal = D_omega_1 == D_omega_2
factorization_failure = pi_equal and not D_equal

print("pi(omega_1) = pi(omega_2):", pi_equal)
print("D(omega_1) = D(omega_2):", D_equal)
print("factorization_failure:", factorization_failure)

assert pi_equal is True
assert D_equal is False
assert factorization_failure is True

print("Reproduction successful: CVSS base score alone cannot ground this patch-priority decision.")
