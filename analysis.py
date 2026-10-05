import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Training_data")

# Inspection
print(df.shape)
print(df.head())
print(df.info())

# Check missing values
print(df.isnull().sum())

# Risk distribution
risk_distribution = df["Risk_Flag"].value_counts()

print("\nRisk Distribution:")
print(risk_distribution)

# Risk rate
overall_risk_rate = df["Risk_Flag"].mean()

print("\nOverall observed risk rate:")
print(overall_risk_rate)

# Risk by income
income_summary = (
    df.groupby(pd.cut(df["Income"], bins=10))["Risk_Flag"]
    .agg(["count", "mean"])
    .reset_index()
)

print("\nRisk by Income:")
print(income_summary)

# Risk by state
state_summary = (
    df.groupby("STATE")["Risk_Flag"]
    .agg(["count", "mean"])
    .sort_values("mean", ascending=False)
)

print("\nRisk by State:")
print(state_summary.head(10))

# Risk by profession
profession_summary = (
    df.groupby("Profession")["Risk_Flag"]
    .agg(["count", "mean"])
    .sort_values("mean", ascending=False)
)

print("\nRisk by Profession:")
print(profession_summary.head(10))

# Visualization
risk_distribution.plot(kind="bar")

plt.title("Observed Risk Distribution")
plt.xlabel("Risk Flag")
plt.ylabel("Number of Applicants")
plt.tight_layout()
plt.show()
