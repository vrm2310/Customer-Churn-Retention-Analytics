from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_DATA = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "churn_features.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "data"
    / "processed"
)

MODEL_DIR = PROJECT_ROOT / "models"

PREPROCESSING_DIR = MODEL_DIR / "preprocessing"

TRAINED_MODELS_DIR = MODEL_DIR / "trained_models"

EVALUATION_DIR = MODEL_DIR / "evaluation"

PREPROCESSING_DIR.mkdir(parents=True, exist_ok=True)
TRAINED_MODELS_DIR.mkdir(parents=True, exist_ok=True)
EVALUATION_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Feature Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_DATA)

print("=" * 60)
print("MODEL PREPROCESSING")
print("=" * 60)

print(f"\nInput Shape: {df.shape}")

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

    "Churn Value",
    "Churn Score",
    "Churn Reason",
    "CLTV"

]

df = df.drop(columns=drop_columns)

y = (
    df["Churn Label"]
    .map({"Yes": 1, "No": 0})
)

X = df.drop(columns=["Churn Label"])

X = pd.get_dummies(
    X,
    drop_first=True
)

# --------------------------------------------------
# Train / Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# Handle Missing Values
# --------------------------------------------------

imputer = SimpleImputer(strategy="median")

X_train = pd.DataFrame(
    imputer.fit_transform(X_train),
    columns=X_train.columns,
    index=X_train.index
)

X_test = pd.DataFrame(
    imputer.transform(X_test),
    columns=X_test.columns,
    index=X_test.index
)

print("\nMissing Values After Imputation")

print(X_train.isna().sum().sum())
print(X_test.isna().sum().sum())

X_train_unscaled = X_train.copy()
X_test_unscaled = X_test.copy()

# --------------------------------------------------
# Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train = pd.DataFrame(
    scaler.fit_transform(X_train),
    columns=X_train.columns,
    index=X_train.index
)

X_test = pd.DataFrame(
    scaler.transform(X_test),
    columns=X_test.columns,
    index=X_test.index
)

joblib.dump(
    scaler,
    PREPROCESSING_DIR / "scaler.pkl"
)

joblib.dump(
    imputer,
    PREPROCESSING_DIR / "imputer.pkl"
)

# --------------------------------------------------
# Validation
# --------------------------------------------------

print("\nNumber of Features:", X_train.shape[1])

print("\nTarget Distribution")

print(y.value_counts(normalize=True).round(3))

print("\nTraining Target Distribution")

print(y_train.value_counts(normalize=True).round(3))

print("\nFirst 15 Features")

print(X_train.columns[:15].tolist())

X_train.to_csv(OUTPUT_DIR / "X_train_scaled.csv", index=False)
X_test.to_csv(OUTPUT_DIR / "X_test_scaled.csv", index=False)
X_train_unscaled.to_csv(OUTPUT_DIR / "X_train_unscaled.csv", index=False)
X_test_unscaled.to_csv(OUTPUT_DIR / "X_test_unscaled.csv", index=False)
y_train.to_csv(OUTPUT_DIR / "y_train.csv", index=False)
y_test.to_csv(OUTPUT_DIR / "y_test.csv", index=False)

# --------------------------------------------------
# Save Feature Names
# --------------------------------------------------

pd.Series(X_train.columns).to_csv(
    OUTPUT_DIR / "feature_names.csv",
    index=False,
    header=["feature_name"]
)

print("\nTrain/Test datasets saved successfully!")

print(f"\nTraining Shape : {X_train.shape}")
print(f"Testing Shape  : {X_test.shape}")

print("\nModel preprocessing completed successfully!")