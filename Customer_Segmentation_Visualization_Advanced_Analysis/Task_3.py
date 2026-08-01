import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_telco_customer_churn.csv")

print(df.head())
print("\nDataset shape:", df.shape)

# Select numerical columns
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

print("\nNumerical Columns:")
print(numerical_columns)

# Mean
print("\nMean:")
print(df[numerical_columns].mean())

# Median
print("\nMedian:")
print(df[numerical_columns].median())

# Mode
print("\nMode:")
print(df[numerical_columns].mode().iloc[0])

# Histograms for numerical columns
for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
# Box plots for numerical columns
for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Box Plot of {column}")
    plt.xlabel(column)
    plt.show()

# Analyze churn vs non-churn proportions
churn_counts = df["churn"].value_counts()

print("\nChurn Counts:")
print(churn_counts)

churn_percentage = df["churn"].value_counts(normalize=True) * 100

print("\nChurn Percentage:")
print(churn_percentage)

# Visualize churn distribution
plt.figure(figsize=(6, 5))
sns.countplot(x="churn", data=df)
plt.title("Churn vs Non-Churn Customers")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()