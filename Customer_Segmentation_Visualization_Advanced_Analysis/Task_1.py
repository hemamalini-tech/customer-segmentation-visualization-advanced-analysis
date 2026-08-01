import pandas as pd
# Load the dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")
# Display first 10 rows
print(df.head(10))
# Identify data types of each column
print(df.dtypes)
# Check for missing values
print(df.isnull().sum())



