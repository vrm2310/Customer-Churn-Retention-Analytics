from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "Telco_customer_churn.xlsx"

OUTPUT_DATA = (
    PROJECT_ROOT
    / "data"
    / "intermediate"
    / "cleaned_churn.csv"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_excel(RAW_DATA)

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

print(f"\nOriginal Shape: {df.shape}")

# --------------------------------------------------
# Clean Total Charges
# --------------------------------------------------

df["Total Charges"] = (
    pd.to_numeric(
        df["Total Charges"].astype(str).str.strip(),
        errors="coerce"
    )
)

print(
    "\nMissing Total Charges:",
    df["Total Charges"].isna().sum()
)

# --------------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------------

OUTPUT_DATA.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(
    OUTPUT_DATA,
    index=False
)

print("\nCleaned dataset saved successfully.")