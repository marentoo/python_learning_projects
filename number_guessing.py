logo = """
  _   _                       _                                                          _                 
 | \ | |                     | |                                                        (_)                
 |  \| |  _   _   _ __ ___   | |__     ___   _ __      __ _   _   _    ___   ___   ___   _   _ __     __ _ 
 | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|    / _` | | | | |  / _ \ / __| / __| | | | '_ \   / _` |
 | |\  | | |_| | | | | | | | | |_) | |  __/ | |      | (_| | | |_| | |  __/ \__ \ \__ \ | | | | | | | (_| |
 |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|       \__, |  \__,_|  \___| |___/ |___/ |_| |_| |_|  \__, |
                                                       __/ |                                          __/ |
                                                      |___/                                          |___/ 
"""

import random
import os
clean = lambda: os.system('cls')
end_game = False


def guess_checker(number, guess, attempts):
    global end_game
    if attempts > 0:
        if number == guess:
            print("Yes. It is correct guess! You win!🤗")
            end_game  = True
        elif number > guess:
            attempts -=1
            print("Too low.")
        elif number < guess:
            attempts -=1
            print("Too high.")
    return attempts

def play():
    # print("PSSSSSSSSST, answer is :{number}".format(number=number))
    difficulty = input("Chose difficulty. Type 'easy' or 'hard':\n")
    if difficulty == "easy":
        attempts = 10
    elif difficulty=="hard":
        attempts = 5

    while not end_game:
        guess = int(input("You have {attempts} attempts to guess the number\n Guess:\t".format(attempts = attempts)))
        attempts = guess_checker(number, guess, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return


while not end_game:
    number = random.randint(1, 101)
    clean()
    print(logo)
    print("Welcome to Number Guessing!\nI'm thinking of a number between 1 and 100.")
    play()
    if input("You want to play again? Type 'y' or 'n'.") == 'y':
        end_game = False
    else:
        print("Bye Bye")
        break

