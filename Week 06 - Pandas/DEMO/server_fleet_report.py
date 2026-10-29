# Findings: North has the highest average usage at about 88.7%.
# srv-03 is highest at 120%, and three servers are over the limit.

import pandas as pd
import matplotlib.pyplot as plt

# Run this script from the DEMO folder.
df = pd.read_csv("../02 - Selecting and Filtering/examples/servers.csv")

print(df.head())
print(df.dtypes)
print("Servers:", len(df), "Columns:", len(df.columns))

df["percent"] = (df["used"] / df["total"]) * 100

at_risk = df[df["percent"] >= 90]
print("At or above 90%:", len(at_risk))
print(df.groupby("region")["percent"].mean())

most_at_risk = df.sort_values("percent", ascending=False).head(1)
print("Most at risk:")
print(most_at_risk)

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
df["region"].value_counts().plot(kind="bar", title="Servers per region")
plt.tight_layout()
plt.savefig("servers_per_region.png")

df[df["status"] == "OVER LIMIT"].to_csv("servers_at_risk.csv", index=False)
print("Saved servers_per_region.png and servers_at_risk.csv")

