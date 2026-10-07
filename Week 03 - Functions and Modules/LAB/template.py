"""
RECORD CHECK - Cybersecurity

Checks failed login attempts for an IP address.
"""

def status_of(percent):
    """Choose a status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# Ask for the IP address and the login attempt numbers
label = input("Enter the IP address: ")
value = float(input("Enter the number of failed logins: "))
limit = float(input("Enter the allowed number of failed logins: "))

# Work out the difference, percentage and status
difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)

# Print the report
print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)
print(f"  Failed logins: {value}")
print(f"  Allowed logins: {limit}")
print(f"  Status: {status}")
print("=" * 34)