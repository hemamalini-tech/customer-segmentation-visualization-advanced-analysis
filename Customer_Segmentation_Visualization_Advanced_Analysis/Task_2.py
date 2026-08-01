import pandas as pd
# Load the dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")
# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
# Check missing values in TotalCharges
print("Missing values in TotalCharges:",
      df["TotalCharges"].isnull().sum())
# Handle missing values
df.dropna(subset=["TotalCharges"], inplace=True)
# Check duplicate records
print("Duplicate rows:", df.duplicated().sum())
# Remove duplicate records if any
df.drop_duplicates(inplace=True)
# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
# Verify cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nNumber of rows after cleaning:", len(df))
print("\nColumn names after standardization:")
print(df.columns)
# Save cleaned dataset
df.to_csv("cleaned_telco_customer_churn.csv", index=False)
print("\nCleaned dataset saved successfully.")