from pathlib import Path

import joblib
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data" / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

PREPROCESSING_DIR = MODEL_DIR / "preprocessing"

TRAINED_MODELS_DIR = MODEL_DIR / "trained_models"

df = pd.read_csv(
    DATA_DIR / "churn_features.csv"
)

print("=" * 60)
print("EXPORT PREDICTIONS")
print("=" * 60)

print(f"\nInput Shape: {df.shape}")

# --------------------------------------------------
# Keep Business Columns
# --------------------------------------------------

business_columns = df[[
    "CustomerID",
    "Contract",
    "Internet Service",
    "Payment Method",
    "Tenure Months",
    "Monthly Charges"
]].copy()

drop_columns = [

    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",

    "Churn Label",
    "Churn Value",
    "Churn Score",
    "Churn Reason",
    "CLTV"

]

X = df.drop(columns=drop_columns)

X = pd.get_dummies(
    X,
    drop_first=True
)

redundant_features = [

    "tenure_band_Growing",
    "tenure_band_Loyal",
    "tenure_band_New",

    "customer_lifecycle_Growing Customer",
    "customer_lifecycle_Loyal Customer",
    "customer_lifecycle_New Customer"

]

X = X.drop(
    columns=redundant_features,
    errors="ignore"
)

imputer = joblib.load(
    PREPROCESSING_DIR / "imputer.pkl"
)

X = pd.DataFrame(imputer.transform(X), columns=X.columns)

model = joblib.load(TRAINED_MODELS_DIR / "random_forest_model.pkl")

probability = model.predict_proba(X)[:,1]

prediction = model.predict(X)

risk = []

for p in probability:
    if p >= 0.75:
        risk.append("High")

    elif p >= 0.40:
        risk.append("Medium")

    else:
        risk.append("Low")

predictions = business_columns.copy()
predictions["Churn Probability"] = probability
predictions["Predicted Churn"] = prediction
predictions["Risk Category"] = risk

predictions["Predicted Churn"] = predictions[
    "Predicted Churn"
].map({
    1:"Yes",
    0:"No"
})

predictions["Churn Probability"] = predictions[
    "Churn Probability"
].round(4)

predictions.to_csv(DATA_DIR / "customer_predictions.csv", index=False)

print("\nPrediction Summary")

print(
    predictions["Risk Category"].value_counts()
)

print("\nTop 10 Highest Risk Customers")

print(
    predictions.sort_values(
        by="Churn Probability",
        ascending=False
    ).head(10)
)

print("\nPredictions exported successfully!")