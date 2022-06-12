import os

bids = {}

from art import logo
print(logo)

# It seems to be a tactic to have an extra true/false variable for the while loop, e.g. bidding_finished = False,
# then check that for the loop continuation
should_continue = "yes"
while should_continue == "yes":
    name = input("What is your name?: ")
    bid = input("What is your bid: $")

    bids[name] = int(bid)
    should_continue = input("Are there more bidders? ").lower()

    if should_continue == "no":
        break
    else:
        os.system('clear')

max_bid = 0
max_bidder_name = ""

for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        max_bidder_name = bidder


print (f"The winning bidder is {max_bidder_name} with a bid of $ {max_bid}")
