import os
from art import logo


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_max(bidders):
    winner = max(bidders, key=lambda k: bidders[k])

    # this is how it will be done if you use a for loop
    # highest_bid = 0
    # winner = ""
    # for key in bidders:
    #     if bidders[key] > highest_bid:
    #         winner = key
    #         highest_bid = bidders[key]
    return winner

# main program starts here
print(logo)
print("Welcome to the secret auction program.")
bidders = {}

cont = 'yes'

while cont != 'no':
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    bidders[name] = bid
    
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear_console()

winner = find_max(bidders)

print(f"The winner is {winner} with a bid of{bidders[winner]: .2f}")