from pathlib import Path

import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data" / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

TRAINED_MODELS_DIR = MODEL_DIR / "trained_models"

EVALUATION_DIR = MODEL_DIR / "evaluation"

TRAINED_MODELS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EVALUATION_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

X_train = pd.read_csv(
    DATA_DIR / "X_train_scaled.csv"
)

X_test = pd.read_csv(
    DATA_DIR / "X_test_scaled.csv"
)

y_train = pd.read_csv(
    DATA_DIR / "y_train.csv"
).squeeze()

y_test = pd.read_csv(
    DATA_DIR / "y_test.csv"
).squeeze()

print("=" * 60)
print("LOGISTIC REGRESSION")
print("=" * 60)

print(f"\nTraining Shape: {X_train.shape}")
print(f"Testing Shape : {X_test.shape}")

model = LogisticRegression(max_iter=1000, random_state=42)

model.fit(X_train, y_train)

print("\nModel trained successfully!")

joblib.dump(model, TRAINED_MODELS_DIR / "logistic_model.pkl")

print("\nModel saved successfully!")

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

print("\n" + "=" * 60)

print("MODEL PERFORMANCE")

print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall   : {recall:.4f}")

print(f"F1 Score : {f1:.4f}")

print(f"ROC-AUC  : {roc_auc:.4f}")

print("\nConfusion Matrix")

print(confusion_matrix(
    y_test,
    y_pred
))

print("\nClassification Report")

print(classification_report(
    y_test,
    y_pred
))

metrics_df = pd.DataFrame({

    "Metric": [

        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"

    ],

    "Value": [

        accuracy,
        precision,
        recall,
        f1,
        roc_auc

    ]

})

metrics_df.to_csv(EVALUATION_DIR / "logistic_metrics.csv", index=False)

print("\nEvaluation metrics saved successfully!")

coefficients = pd.DataFrame({"Feature": X_train.columns, "Coefficient": model.coef_[0]})

coefficients = coefficients.sort_values(by="Coefficient", ascending=False)

coefficients.to_csv(EVALUATION_DIR / "logistic_coefficients.csv", index=False)

print("Coefficient report saved successfully!")

print("\nTop 10 Churn Drivers")

print(coefficients.head(10))

print("\nTop 10 Retention Drivers")

print(coefficients.tail(10))

print("\nLogistic Regression pipeline completed successfully!")