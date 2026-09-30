import pandas as pd
import numpy as np

# Load the sample dataset
input_file = "Week-2/data/agribusiness_sample.csv"
df = pd.read_csv(input_file)

print("========== BEFORE CLEANING ==========")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# --------------------------------------------------
# 1. Standardize text columns
# --------------------------------------------------

text_columns = ["District", "Crop", "Season"]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

df["District"] = df["District"].str.title()
df["Crop"] = df["Crop"].str.title()
df["Season"] = df["Season"].str.title()

# --------------------------------------------------
# 2. Convert numerical columns
# --------------------------------------------------

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Area_Ha"] = pd.to_numeric(df["Area_Ha"], errors="coerce")
df["Production_Tonnes"] = pd.to_numeric(
    df["Production_Tonnes"],
    errors="coerce"
)

# --------------------------------------------------
# 3. Detect invalid area values
# --------------------------------------------------

invalid_area = df["Area_Ha"] <= 0

print("\nInvalid area records:", invalid_area.sum())

df.loc[invalid_area, "Area_Ha"] = np.nan

# --------------------------------------------------
# 4. Remove complete duplicate records
# --------------------------------------------------

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

print("Duplicates removed:", duplicates_before)

# --------------------------------------------------
# 5. Handle missing numeric values
# --------------------------------------------------

# Fill missing Area_Ha with the median area
area_median = df["Area_Ha"].median()
df["Area_Ha"] = df["Area_Ha"].fillna(area_median)

# Fill missing Production_Tonnes with the median production
production_median = df["Production_Tonnes"].median()
df["Production_Tonnes"] = df["Production_Tonnes"].fillna(
    production_median
)

# --------------------------------------------------
# 6. Calculate yield
# --------------------------------------------------

df["Yield_Tonnes_per_Ha"] = (
    df["Production_Tonnes"] / df["Area_Ha"]
)

# --------------------------------------------------
# 7. Final validation
# --------------------------------------------------

print("\n========== AFTER CLEANING ==========")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nCleaned dataset:")
print(df)

# --------------------------------------------------
# 8. Save cleaned dataset
# --------------------------------------------------

output_file = "Week-2/data/agribusiness_cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved to:", output_file)

