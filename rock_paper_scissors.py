##ASCII codes

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

hand_shape = [rock, paper, scissors]
player = input("Enter player's name:\n")
is_playing = input(f'Hello {player}! Down for a round? ("Y" or "N")\n')
draws=0;wins=0;losses=0

while is_playing == "Y" or is_playing == "y":
    
    ##player logic
    players_choice = input('Rock, paper or Scissors? (Type: "rock" or "1", "paper" or "2", "scissors" or "3")\n').lower()
    if players_choice == "rock" or players_choice == "1": players_choice = 1
    elif players_choice == "paper" or players_choice =="2": players_choice = 2
    elif players_choice == "scissors" or players_choice =="3": players_choice = 3
    else: raise SyntaxError
    print(f'{player}:\n{hand_shape[players_choice-1]}')

    ##computer logic
    computer_choice = random.randint(1,3)
    print(f'Machine:\n{hand_shape[computer_choice-1]}')

    ##who wins logic!? (remind: 1 is rock, 2 is paper, 3 is scissors)
    if players_choice == computer_choice:
        print("DRAW")
        draws +=1
    elif (players_choice == 1 and computer_choice == 2) or (players_choice == 2 and computer_choice == 3) or (players_choice == 3 and computer_choice == 1):
        print(f"{player} LOSE and Machine WINS")
        losses+=1
    else:
        print(f"{player} WINS and Machine LOSE")
        wins +=1
        
    is_playing = input(f'Hey {player}, down for another round?("Y" or "N")\n')

print(f"Summarization:\n {player} wins:{wins} | Draws: {draws} | Machine wins: {losses}")
print("Okay bye, bye!")
