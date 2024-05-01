"""
assumption in this project is infinity deck and
each card has same probability of occuring and 
cards are not removed from the deck as they are drawn.
"""

from art import logo
import random
import os

clear = lambda: os.system('cls')

def deal():
    """
    return random card from a deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    it calculates score (sum) of cards inside list (hand)
    """
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player_score, computer_score):
    """
    return comparing of the results
    """
    if player_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose, computer has blackjack"
    elif player_score == 0:
        return "You win. You have a blackjack"
    elif player_score>21:
        return "you went over, You lose"
    elif computer_score>21:
        return "computer went over, you win"
    elif player_score>computer_score:
        return "you win"
    else:
        return "you lose"
    

def play():
    computer_hand = []; player_hand = []
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal())
        computer_hand.append(deal())

    while not is_game_over:
        computer_score = calculate_score(computer_hand)
        player_score = calculate_score(player_hand)
        print(f"Your's cards are {player_hand}", f"Players score is: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        
        if computer_score == 0 or player_score > 21 or player_score==0:
            is_game_over = True
        else:
            if input("Do you want to have another card? Type 'y' or 'n'.") == 'y':
                player_hand.append(deal())
                player_score = calculate_score(player_hand)
            else:
                is_game_over = True
    print(f"Your final cards are:{player_hand} with result of {player_score}")

    while computer_score!= 0 and computer_score <17:
        computer_hand.append(deal())
        computer_score = sum(computer_hand)

    print(f"Computer final cards are:{computer_hand} with result of {computer_score}")

    print(compare_scores(player_score, computer_score))


while input("You want to play a game of blackjack? Type 'y' or 'n'.") == 'y':
    clear()
    print(logo)
    play()
