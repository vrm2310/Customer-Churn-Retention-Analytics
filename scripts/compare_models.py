from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EVALUATION_DIR = (
    PROJECT_ROOT
    / "models"
    / "evaluation"
)

# --------------------------------------------------
# Load Evaluation Metrics
# --------------------------------------------------

logistic = pd.read_csv(
    EVALUATION_DIR / "logistic_metrics.csv"
)

random_forest = pd.read_csv(
    EVALUATION_DIR / "random_forest_metrics.csv"
)

logistic = logistic.rename(
    columns={"Value": "Logistic Regression"}
)

random_forest = random_forest.rename(
    columns={"Value": "Random Forest"}
)

comparison = logistic.merge(

    random_forest,

    on="Metric"

)

comparison["Best Model"] = comparison.apply(

    lambda row:
    "Logistic Regression"

    if row["Logistic Regression"] >= row["Random Forest"]

    else "Random Forest",

    axis=1

)

comparison.to_csv(

    EVALUATION_DIR / "model_comparison.csv",

    index=False

)

print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print()

print(comparison)

wins = comparison["Best Model"].value_counts()

print("\nMetric Wins")

print(wins)

best_model = comparison.loc[
    comparison["Metric"] == "ROC-AUC",
    "Best Model"
].iloc[0]

print("\nRecommended Production Model")

print(best_model)

print("\nComparison report saved successfully!")