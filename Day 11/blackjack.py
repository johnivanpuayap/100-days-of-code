############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def display_cards(user_cards, cpu_cards):
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {cpu_cards[0]}")

# start
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':
    print(logo)

    # generate cards
    user_cards = [deal_card(), deal_card()]
    user_score = sum(user_cards)

    cpu_cards = [deal_card(), deal_card()]
    cpu_score = sum(cpu_cards)
    
    # display cards
    display_cards(user_cards, cpu_cards)

    # ask user if they get another card
    hit = True

    while hit:
        choice = input("\nType 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            new_card = deal_card()
            user_cards.append(new_card)
            user_score += new_card

            if user_score > 21 and (11 not in user_cards):
                display_cards(user_cards, cpu_cards)
                print("\nYou exceeded 21. You lose")
                hit = False
            elif user_score > 21 and (11 in user_cards):
                user_score -= 10
                display_cards(user_cards, cpu_cards)
            elif user_score == 21:
                display_cards(user_cards, cpu_cards)
                hit = False
            else:
                display_cards(user_cards, cpu_cards)
        elif choice == 'n':
            hit = False            
            print(f"\nYou're final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {cpu_cards},  final score: {cpu_score}")
        else:
            print("Invalid input. Please try again.")

    # compare the scores
    if user_score > cpu_score:
        print("\nYou win")
    elif user_score < cpu_score:
        print("\nYou lose")
    else:
        print("\nDraw")




