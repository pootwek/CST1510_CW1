"""
RECORD CHECK  -  my version
===========================

Name  :patryk
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit for one record."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value compared with the limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read records from a file and return them as Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

from pathlib import Path

records = load_records(Path(__file__).with_name("records_sample.txt"))


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Failed logins: {record.value}")
    print(f"  Allowed limit: {record.limit}")
    print(f"  Status:        {record.status()}")

    print("=" * 34)

over_limit_count = 0
for record in records:
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} records were OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
