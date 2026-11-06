# Split only on the first equals sign, so the rest stays in the value.
piece = "note=server=east"
key, value = piece.split("=", 1)

print(key, value)
