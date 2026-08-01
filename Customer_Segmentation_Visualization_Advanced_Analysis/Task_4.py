import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_telco_customer_churn.csv")

# Create tenure categories
df["tenure_category"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 36, float("inf")],
    labels=["0-12 months", "13-36 months", "37+ months"],
    include_lowest=True
)

# Display number of customers in each category
print("Customers by Tenure Category:")
print(df["tenure_category"].value_counts().sort_index())
# Count customers in each tenure category
tenure_counts = df["tenure_category"].value_counts().sort_index()

# Create donut chart
plt.figure(figsize=(7, 7))

plt.pie(
    tenure_counts,
    labels=tenure_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4}
)

plt.title("Customer Distribution by Tenure Category")
plt.show()

# Calculate average monthly charges by tenure category
avg_charges = df.groupby(
    "tenure_category",
    observed=True
)["monthlycharges"].mean()

print("\nAverage Monthly Charges by Tenure Category:")
print(avg_charges)

# Create bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    avg_charges.index,
    avg_charges.values
)

plt.title("Average Monthly Charges by Tenure Category")
plt.xlabel("Tenure Category")
plt.ylabel("Average Monthly Charges")

# Add value annotations on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.show()