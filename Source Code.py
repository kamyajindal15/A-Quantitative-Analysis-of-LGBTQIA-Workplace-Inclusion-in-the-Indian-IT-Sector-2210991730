# Quantitative Analysis of LGBTQIA+ Workplace Inclusion
# Indian IT Sector Study

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Table 1: Organisational Inclusion Metrics
# ----------------------------------------

data = {
    "Indicator": [
        "Productivity Increase",
        "Hiring Advantage",
        "Employee Performance",
        "Attrition Risk",
        "Attrition Reduction"
    ],
    "Value": [68, 79, 1.5, 1.4, 50]
}

df = pd.DataFrame(data)

print("=== Inclusion Metrics Dataset ===")
print(df)

# ----------------------------------------
# Basic Statistical Summary
# ----------------------------------------

print("\n=== Statistical Summary ===")
print(df.describe())

# ----------------------------------------
# Visualization
# ----------------------------------------

plt.figure(figsize=(10, 5))
plt.bar(df["Indicator"], df["Value"])

plt.title("Impact of Inclusive Workplace Practices")
plt.xlabel("Indicators")
plt.ylabel("Quantitative Values")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# ----------------------------------------
# Workforce Representation Analysis
# ----------------------------------------

representation = {
    "Category": ["Estimated LGBTQIA+ Population", "Openly Identified in IT Workforce"],
    "Percentage": [17, 3]
}

rep_df = pd.DataFrame(representation)

print("\n=== Representation Gap Analysis ===")
print(rep_df)

gap = 17 - 3
print(f"\nRepresentation Gap: {gap}%")

# ----------------------------------------
# India vs USA Comparison
# ----------------------------------------

comparison = {
    "Country": ["India", "USA"],
    "Open Workforce Disclosure (%)": [3, 3],
    "Estimated LGBTQ+ Population (%)": [17, 9.3]
}

comp_df = pd.DataFrame(comparison)

print("\n=== India vs USA Comparison ===")
print(comp_df)

# ----------------------------------------
# Correlation-style Interpretation
# ----------------------------------------

if 68 > 50:
    print("\nInclusive practices are associated with higher organisational productivity.")

if 1.4 > 1:
    print("Bias exposure increases employee attrition risk.")

if 50 >= 50:
    print("Improving BLISS scores significantly reduces attrition.")
