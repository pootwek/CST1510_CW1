"""Collect bids privately and announce the highest bidder."""

bids = {}
keep_bidding = True

while keep_bidding:
    name = input("What is your name? ").strip()
    bid = int(input("What is your bid in pounds? "))
    bids[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if other_bidders == "yes":
        # clear the previous bid from view before the next person enters theirs
        print("\n" * 100)
    else:
        keep_bidding = False

highest_bid = 0
winner = ""

for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of £{highest_bid}.")
