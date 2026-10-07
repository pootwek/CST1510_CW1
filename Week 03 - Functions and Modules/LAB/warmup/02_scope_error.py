# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"

status=check(87, 100)

print(status)


#status only exists inside the function so it cant print it outside return status
#sends the answerr back so i can save it and print it