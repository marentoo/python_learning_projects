logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

print(logo)
clear = lambda: os.system('cls') ## call 'clear()' whenever needed
bids = {}
bidding_finished = False

def find_highest_bidding(bidding_record):
    highest_bid = 0; winner=""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner=bidder
    print(f'Highest bid is ${highest_bid} by {winner}')

while not bidding_finished:
    name = input("What is your Name?:\n")
    price = int(input("What is your bidding price?:\n$"))
    bids[name] = price

    other_users = input("Are there other users who want to bid? Type 'y' or 'n'!:\n")

    if other_users == "n":
        bidding_finished = True
    elif other_users == 'y':
        clear()

find_highest_bidding(bids)