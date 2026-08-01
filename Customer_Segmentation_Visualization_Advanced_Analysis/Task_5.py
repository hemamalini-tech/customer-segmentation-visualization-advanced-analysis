import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_telco_customer_churn.csv")

# Create tenure categories
df["tenure_category"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 36, float("inf")],
    labels=["0-12 Months", "13-36 Months", "37+ Months"],
    include_lowest=True
)

df["churn_numeric"] = df["churn"].map({
    "Yes": 1,
    "No": 0
})

tenure_analysis = df.groupby(
    "tenure_category",
    observed=True
).agg(
    customer_count=("customerid", "count"),
    average_monthly_charges=("monthlycharges", "mean"),
    average_total_charges=("totalcharges", "mean"),
    churn_rate=("churn_numeric", "mean")
)

# Convert churn rate into percentage
tenure_analysis["churn_rate"] *= 100

print("\nTenure Analysis")
print(tenure_analysis.round(2))

# Churn by Gender
gender_churn = pd.crosstab(
    df["gender"],
    df["churn"],
    normalize="index"
) * 100

print("\nChurn Rate by Gender:")
print(gender_churn.round(2))

# Visualization
plt.figure(figsize=(7,5))
sns.countplot(x="gender", hue="churn", data=df)

plt.title("Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Customer Count")

plt.show()

# Churn by Senior Citizen
senior_churn = pd.crosstab(
    df["seniorcitizen"],
    df["churn"],
    normalize="index"
) * 100

print("\nChurn Rate by Senior Citizen:")
print(senior_churn.round(2))

# Visualization
plt.figure(figsize=(7,5))

sns.countplot(
    x="seniorcitizen",
    hue="churn",
    data=df
)

plt.title("Churn by Senior Citizen")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Customer Count")

plt.show()

# Churn by Payment Method
payment_churn = pd.crosstab(
    df["paymentmethod"],
    df["churn"],
    normalize="index"
) * 100

print("\nChurn Rate by Payment Method:")
print(payment_churn.round(2))

# Visualization
plt.figure(figsize=(10, 6))

sns.countplot(
    x="paymentmethod",
    hue="churn",
    data=df
)

plt.title("Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Customer Count")
plt.xticks(rotation=20)

plt.show()

# Churn by Contract Type
contract_churn = pd.crosstab(
    df["contract"],
    df["churn"],
    normalize="index"
) * 100

print("\nChurn Rate by Contract Type:")
print(contract_churn.round(2))

# Visualization
plt.figure(figsize=(8, 5))

sns.countplot(
    x="contract",
    hue="churn",
    data=df
)

plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Customer Count")

plt.show()
