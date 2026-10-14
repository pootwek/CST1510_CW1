# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]

print(labels[2])

#the error is because labels only has 3 items,
#  so the last index is 2. Trying to access index 3 will cause an IndexError.
