"""Pick a friend to pay the bill using two random methods."""

import random

friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

# pick a name directly from the list
payer = random.choice(friends)
print(f"{payer} is paying the bill today!")

# pick a random list position, then use it to get a name
num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]
print(f"{payer} is paying the bill today!")
