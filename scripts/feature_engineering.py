from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_DATA = (
    PROJECT_ROOT
    / "data"
    / "intermediate"
    / "cleaned_churn.csv"
)

OUTPUT_DATA = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "churn_features.csv"
)

# --------------------------------------------------
# Load Clean Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_DATA)

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

print(f"\nInput Shape: {df.shape}")

# --------------------------------------------------
# Tenure Band
# --------------------------------------------------

df["tenure_band"] = pd.cut(
    df["Tenure Months"],
    bins=[-1, 12, 24, 48, np.inf],
    labels=[
        "New",
        "Growing",
        "Established",
        "Loyal"
    ]
)

# --------------------------------------------------
# Service Count
# --------------------------------------------------

service_columns = [
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies"
]

df["service_count"] = (
    df[service_columns]
    .eq("Yes")
    .sum(axis=1)
)

print("\nTenure Band Distribution")
print(df["tenure_band"].value_counts())

print("\nService Count Distribution")
print(df["service_count"].value_counts().sort_index())

# --------------------------------------------------
# Auto Payment
# --------------------------------------------------

df["auto_payment"] = df["Payment Method"].isin([
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

# --------------------------------------------------
# High Value Customer
# --------------------------------------------------

median_charge = df["Monthly Charges"].median()

df["high_value_customer"] = (
    df["Monthly Charges"] >= median_charge
)

# --------------------------------------------------
# Security Bundle
# --------------------------------------------------

df["security_bundle"] = (
    (df["Online Security"] == "Yes")
    &
    (df["Tech Support"] == "Yes")
)

# --------------------------------------------------
# Streaming Bundle
# --------------------------------------------------

df["streaming_bundle"] = (
    (df["Streaming TV"] == "Yes")
    &
    (df["Streaming Movies"] == "Yes")
)

# --------------------------------------------------
# Internet Customer
# --------------------------------------------------

df["internet_customer"] = (
    df["Internet Service"] != "No"
)

# --------------------------------------------------
# Customer Lifecycle
# --------------------------------------------------

conditions = [

    (df["Tenure Months"] <= 12),

    (df["Tenure Months"] > 12)
    &
    (df["Contract"] == "Month-to-month"),

    (df["Contract"] == "One year"),

    (df["Contract"] == "Two year")

]

choices = [

    "New Customer",

    "Growing Customer",

    "Committed Customer",

    "Loyal Customer"

]

df["customer_lifecycle"] = np.select(
    conditions,
    choices,
    default="Other"
)

print("\nNew Features Created")

print(df[
    [
        "auto_payment",
        "high_value_customer",
        "security_bundle",
        "streaming_bundle",
        "internet_customer",
        "customer_lifecycle"
    ]
].head())

# --------------------------------------------------
# Save Feature Dataset
# --------------------------------------------------

OUTPUT_DATA.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_DATA,
    index=False
)

print("\nFeature dataset saved successfully!")

print(f"\nFinal Shape: {df.shape}")