import json
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent

df = pd.read_csv(BASE / "full_segmented_fields.csv")

df["rate"] = df["conversions"] / df["trials"]

agg = (
    df.groupby(["world", "variant"], as_index=False)
    .agg({"trials": "sum", "conversions": "sum"})
)
agg["aggregate_rate"] = agg["conversions"] / agg["trials"]

idx = df.groupby(["world", "segment"])["rate"].idxmax()
decisions = (
    df.loc[idx, ["world", "segment", "variant", "rate"]]
    .rename(columns={"variant": "chosen_variant", "rate": "chosen_rate"})
    .sort_values(["world", "segment"])
    .reset_index(drop=True)
)

pi_vectors = {}
for world in sorted(df["world"].unique()):
    rows = agg[agg["world"] == world].sort_values("variant")
    pi_vectors[world] = {
        row["variant"]: {
            "trials": int(row["trials"]),
            "conversions": int(row["conversions"]),
            "aggregate_rate": float(row["aggregate_rate"]),
        }
        for _, row in rows.iterrows()
    }

D_vectors = {}
for world in sorted(df["world"].unique()):
    rows = decisions[decisions["world"] == world].sort_values("segment")
    D_vectors[world] = {
        row["segment"]: row["chosen_variant"]
        for _, row in rows.iterrows()
    }

pi_equal = pi_vectors["omega_1"] == pi_vectors["omega_2"]
D_equal = D_vectors["omega_1"] == D_vectors["omega_2"]
factorization_failure = pi_equal and not D_equal

print("pi(omega_1) = pi(omega_2):", pi_equal)
print("D(omega_1) = D(omega_2):", D_equal)
print("factorization_failure:", factorization_failure)

assert pi_equal is True
assert D_equal is False
assert factorization_failure is True

print("Reproduction successful: D cannot factor through pi.")
