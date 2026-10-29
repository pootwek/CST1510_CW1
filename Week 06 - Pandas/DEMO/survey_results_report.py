# Findings: Category A has the strongest average score at 81.5.
# Three of the ten rows were unanswered, so 30% were removed before comparing scores.

import pandas as pd
import matplotlib.pyplot as plt

# Run this script from the DEMO folder.
df = pd.read_csv("../survey_results.csv")
print(df.head())
print(df.dtypes)
print("Rows:", len(df))

missing_percent = len(df[df["answered"] == 0]) / len(df) * 100
print("Unanswered rows (%):", missing_percent)

clean = df[df["answered"] == 1].copy()
averages = clean.groupby("category")["score"].mean().sort_values(ascending=False)
print("Average score by category:")
print(averages)

clean["result"] = clean["score"].apply(lambda score: "Pass" if score >= 60 else "Fail")
print(clean["result"].value_counts())
clean["result"].value_counts().plot(kind="bar", title="Survey results")
plt.tight_layout()
plt.savefig("survey_pass_fail.png")
clean.to_csv("survey_results_clean.csv", index=False)
print("Saved survey_pass_fail.png and survey_results_clean.csv")
