# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}
record["status"] = "OK"

print(record["status"])

#the error is because python tried to print status but that key wasnt in
#the dictionary, adding the key first means python can find it and print its value
