import json
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent

df = pd.read_csv(BASE / "stone_size_conditioned_field.csv")

df["success_rate"] = df["successes"] / df["total"]

aggregate = (
    df.groupby("treatment", as_index=False)
    .agg({"successes": "sum", "total": "sum", "failures": "sum"})
)
aggregate["success_rate"] = aggregate["successes"] / aggregate["total"]

aggregate_decision = str(aggregate.loc[aggregate["success_rate"].idxmax(), "treatment"])

idx_stratified = df.groupby("stone_size")["success_rate"].idxmax()
stratified_decisions = (
    df.loc[idx_stratified, ["stone_size", "treatment", "success_rate", "successes", "total"]]
    .rename(columns={"treatment": "chosen_treatment"})
    .sort_values("stone_size")
    .reset_index(drop=True)
)

stratified_policy = {
    row["stone_size"]: row["chosen_treatment"]
    for _, row in stratified_decisions.iterrows()
}

all_strata_choose_same = len(set(stratified_policy.values())) == 1
stratified_common_decision = list(set(stratified_policy.values()))[0] if all_strata_choose_same else None

aggregate_vs_stratified_conflict = (
    all_strata_choose_same and aggregate_decision != stratified_common_decision
)

print("Aggregate decision from pi:", aggregate_decision)
print("Stone-size-conditioned policy from Omega:", stratified_policy)
print("aggregate_vs_stratified_conflict:", aggregate_vs_stratified_conflict)

assert aggregate_decision == "B"
assert stratified_policy == {"large": "A", "small": "A"}
assert aggregate_vs_stratified_conflict is True

print("Reproduction successful: aggregate success rate is the wrong object for the stone-size-conditioned decision.")
