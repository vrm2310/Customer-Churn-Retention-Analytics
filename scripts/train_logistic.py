from pathlib import Path

import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data" / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

MODEL_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

X_train = pd.read_csv(DATA_DIR / "X_train.csv")

y_train = pd.read_csv(DATA_DIR / "y_train.csv").squeeze()

print("=" * 60)
print("LOGISTIC REGRESSION")
print("=" * 60)

print(f"\nTraining Shape: {X_train.shape}")

model = LogisticRegression(max_iter=1000, random_state=42)

model.fit(X_train, y_train)

joblib.dump(model, MODEL_DIR / "logistic_model.pkl")

print("\nModel trained successfully!")

print("\nModel saved.")