# Findings: 10.0.0.5 and 10.0.0.12 both had eight failed logins in total.
# I would escalate 10.0.0.12 first because all eight failures happened in one session.

import pandas as pd
import matplotlib.pyplot as plt

# Run this script from the DEMO folder.
df = pd.read_csv("../login_attempts.csv")
print(df.head())
print(df.dtypes)
print("Sessions:", len(df))

print("Sessions with at least 3 failed attempts:")
print(df[df["failed"] >= 3])

failed_by_ip = df.groupby("ip")["failed"].sum().sort_values(ascending=False)
print("Failed attempts per IP:")
print(failed_by_ip)
print("Most failures:")
print(failed_by_ip.head(1))

df["suspicious"] = df["failed"].apply(lambda failed: failed >= 3)
failed_by_ip.plot(kind="bar", title="Failed attempts per IP")
plt.tight_layout()
plt.savefig("failed_attempts_per_ip.png")
df[df["suspicious"]].to_csv("flagged_ips.csv", index=False)
print("Saved failed_attempts_per_ip.png and flagged_ips.csv")
