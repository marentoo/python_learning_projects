import random
from hangman_auxilary import logo, stages, word_list
import os

chosen_word = random.choice(word_list)
print(logo)
# print(f"testing: {chosen_word}");print("")
lives = 6

hidden_list = []
for _ in chosen_word:
    hidden_list += ("_")
print(hidden_list)


end_of_game = False
while not end_of_game:
    guess = input("Guess the letter:\n").lower()
    os.system('cls')

    if guess in hidden_list:
        print(f"You have already guessed: {guess}")

    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            hidden_list[position] = letter
            print("Correct. Bravo!")
    print(hidden_list)

    if guess not in chosen_word:
        print(f'You guessed {guess} that is not in the word. You lose a life')
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was: {chosen_word}")
    
    print(stages[lives])

    if "_" not in hidden_list:
        end_of_game = True
        print("You Win")

