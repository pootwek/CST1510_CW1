"""
RECORD CHECK  -  my version
===========================

Name  :patryk
Lane  :  Cyber      (delete two)
Date  :14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate the difference, percentage and status for a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print all the details for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Failed logins: {value}")
    print(f"  Allowed limit: {limit}")
    print(f"  Difference:    {difference:.2f}")
    print(f"  Percent:       {percent:.2f}%")
    print(f"  Status:        {status}")
    print("=" * 34)


# ====================================================================== STORE


records = []
records = [
    {"label": "10.0.0.5", "value": 87, "limit": 100},
    {"label": "10.0.0.9", "value": 120, "limit": 100},
    {"label": "10.0.0.12", "value": 45, "limit": 100}
]


# =============================================================== PROCESS + OUTPUT
for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )
    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
