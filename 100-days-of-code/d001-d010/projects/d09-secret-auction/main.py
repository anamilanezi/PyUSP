# Using a dictionary nested in list prevents overwriting from possible duplicated names

import art
import os

bids = []
bid_again = True


# Creates a function to add new bids into the list
def new_bid(person_name, bid_value):
    new_entry = {
        person_name: bid_value
    }
    bids.append(new_entry)

def bidder_winner(bids_list):
    higher_bid = 0
    winner = ''
    # Loop through the bids list
    for bid_record in bids_list:
        # Each item of the list is a dictionary so we loop through using the keys and obtain all the info needed
        for bidder in bid_record:
            bid_amount = bid_record[bidder]
            if bid_amount > higher_bid:
                higher_bid = bid_amount
                winner = bidder
    print(art.win)
    print(f"The winner is {winner.title()} with a bid of ${higher_bid:.2f}.")


print(art.logo)
print("Welcome to the secret auction program!")

# Program runs until the user types no and change the value of the flag 
while bid_again:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    new_bid(name, bid)

    start_new_bid = input("Are there any other bidders? Type 'yes' or 'no:\n").lower()

    if start_new_bid == 'no':
        bid_again = False

    # The next line clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

bidder_winner(bids)

