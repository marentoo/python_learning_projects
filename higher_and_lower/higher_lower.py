from game_data import data
from art import logo, vs
import random
import os

clean = lambda: os.system('cls')

def get_follower_info(acount):
    name = acount["name"]
    description = acount["description"]
    country = acount["country"]
    follower_count = acount["follower_count"]
    return name, description, country, follower_count

win_streak = True
final_score=0
acount_B = random.choice(data)

while win_streak:
    print(logo)
    acount_A = acount_B
    acount_B = random.choice(data)

    while acount_A == acount_B:
        acount_B = random.choice(data)

    name, description, country, follower_countA = get_follower_info(acount_A)
    print(f"Compare A: {name}, a {description}, from {country}")
    print(vs)
    name, description, country, follower_countB = get_follower_info(acount_B)
    print(f"Against B: {name}, a {description}, from {country}")
    
    guess = input("Who has more followers. Type 'A' or 'B': ")
    if (follower_countA > follower_countB and guess == 'A') or (follower_countB > follower_countA and guess == 'B'):
        clean()
        print("correct")
        final_score +=1
        print(f"You are right. Current score: {final_score}")
    else:
        clean()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
        win_streak = False
