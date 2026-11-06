# Catch the bad number so the program can explain the problem and continue.
raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=", 1)
    try:
        print(key, float(value))
    except ValueError:
        print("Could not convert", value, "for", key)
