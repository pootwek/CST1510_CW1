"""Cyber Security login-attempt summary using pandas."""

import pandas as pd
import matplotlib.pyplot as plt

# Read the login data from the CSV file.
df = pd.read_csv("cyber_records.csv")

# Calculate the percentage of attempts that failed for each source IP.
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# Give each source IP a status based on its failed-login percentage.
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# Show the full table, then only the rows that need attention.
print(df)
print(df[df["status"] != "OK"])

# Count each status, save the report, and create a chart.
counts = df["status"].value_counts()
print(counts)
df.to_csv("cyber_records_report.csv", index=False)
counts.plot(kind="bar", title="Login records by status")
plt.tight_layout()
plt.savefig("cyber_status_counts.png")
plt.show()
