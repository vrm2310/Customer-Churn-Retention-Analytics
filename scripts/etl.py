from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# --------------------------------------------------
# Create PostgreSQL Connection
# --------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME
)

engine = create_engine(DATABASE_URL)


# --------------------------------------------------
# Read Dataset
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

file_path = PROJECT_ROOT / "data" / "raw" / "Telco_customer_churn.xlsx"

df = pd.read_excel(file_path)


# --------------------------------------------------
# Quick Validation
# --------------------------------------------------

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 rows:\n")
print(df.head())

print("\nDatabase Connection Successful")

# --------------------------------------------------
# Standardize Column Names
# --------------------------------------------------

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("-", "_")
)

df.rename(
    columns={
        "customerid": "customer_id"
    },
    inplace=True
)

print("\nColumns standardized successfully.\n")
print(df.columns.tolist())

# --------------------------------------------------
# Load Data into Staging Table
# --------------------------------------------------

print("\nLoading data into staging table...")

df.to_sql(
    name="staging_telco_churn",
    con=engine,
    if_exists="append",
    index=False,
    method="multi"
)

print("Data loaded successfully into staging_telco_churn!")