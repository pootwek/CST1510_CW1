# strip the extra spaces while the value is still text, then convert it.
value_text = " 87 "
cleaned = value_text.strip()
value = float(cleaned)

print(value)
