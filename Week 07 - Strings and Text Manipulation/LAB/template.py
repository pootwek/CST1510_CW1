"""
record check  -  my version
===========================

name  :
lane  : cyber security
date  :

run it from this lab folder: python template.py
"""

# ====================================================================== parse
# clean one raw login record and turn its values into useful types.
def parse_line(raw_line):
    """clean one messy login record and return its fields in a dict."""
    fields = {}
    for piece in raw_line.strip().split(","):
        key, value = piece.split("=", 1)
        key = key.strip().lower()
        value = value.strip().lower()

        if key == "attempts":
            fields[key] = int(value)
        else:
            fields[key] = value

    return fields


def status_of(record):
    """say whether a login record needs attention."""
    if record["result"] == "failed" or record["attempts"] >= 5:
        return "FLAGGED"
    return "OK"


# ======================================================================= input
# load the deliberately messy sample lines from a file beside this script.
raw_records = []
with open("cyber_records.txt") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


# =============================================================== process + output
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    if status == "FLAGGED":
        flagged_count += 1

    print(record, "-", status)

print(f"{len(raw_records)} records checked; {flagged_count} flagged.")
