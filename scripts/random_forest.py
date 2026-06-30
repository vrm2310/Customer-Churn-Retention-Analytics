from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import RandomizedSearchCV

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
    DATA_DIR / "X_train_unscaled.csv"
)

X_test = pd.read_csv(
    DATA_DIR / "X_test_unscaled.csv"
)

y_train = pd.read_csv(
    DATA_DIR / "y_train.csv"
).squeeze()

y_test = pd.read_csv(
    DATA_DIR / "y_test.csv"
).squeeze()

print("=" * 60)
print("RANDOM FOREST")
print("=" * 60)

print(f"\nTraining Shape: {X_train.shape}")
print(f"Testing Shape : {X_test.shape}")

param_grid = {

    "n_estimators": [100, 200, 300],

    "max_depth": [5, 10, 20, None],

    "min_samples_split": [2, 5, 10],

    "min_samples_leaf": [1, 2, 4],

    "max_features": ["sqrt", "log2"]

}

rf = RandomForestClassifier(
    random_state=42
)

random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_grid,
    n_iter=15,
    cv=5,
    scoring="roc_auc",
    random_state=42,
    n_jobs=-1
)

print("\nTraining Random Forest...")

random_search.fit(
    X_train,
    y_train
)

model = random_search.best_estimator_

print("\nBest Parameters:")

print(random_search.best_params_)

joblib.dump(

    model,

    TRAINED_MODELS_DIR / "random_forest_model.pkl"

)

print("\nModel saved successfully!")

# --------------------------------------------------
# Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

# --------------------------------------------------
# Evaluation Metrics
# --------------------------------------------------

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

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred
    )
)

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

metrics_df.to_csv(

    EVALUATION_DIR /
    "random_forest_metrics.csv",

    index=False

)

print("\nEvaluation metrics saved successfully!")

feature_importance = pd.DataFrame({

    "Feature": X_train.columns,

    "Importance": model.feature_importances_

})

feature_importance = feature_importance.sort_values(

    by="Importance",

    ascending=False

)

feature_importance.to_csv(

    EVALUATION_DIR /
    "random_forest_feature_importance.csv",

    index=False

)

print("Feature importance report saved successfully!")

print("\nTop 15 Important Features")

print(feature_importance.head(15))

print("\nRandom Forest pipeline completed successfully!")