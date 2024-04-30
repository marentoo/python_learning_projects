print('''
*******************************************************************************
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************
''')
gold='''                    ________
                 .##@@&&&@@##.
              ,##@&::%&&%%::&@##.
             #@&:%%000000000%%:&@#
           #@&:%00'         '00%:&@#
          #@&:%0'             '0%:&@#
         #@&:%0                 0%:&@#
        #@&:%0                   0%:&@#
        #@&:%0                   0%:&@#
        "" ' "                   " ' ""
      _oOoOoOo_                   .-.-.
     (oOoOoOoOo)                 (  :  )
      )`"""""`(                .-.`. .'.-.
     /         \              (_  '.Y.'  _)
    |           |             (   .'|'.   )
    \           /              '-'  |  '-'
     `=========`
'''
print("Welcome to tresure island.\nYour Mission is to find the treasure. But you have to make choices...")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swimm across.\n').lower()
    if  choice2 =="wait":
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which door do you choose?\n').lower()
        if choice3 == "red":
            print("There is no floor. You fell into the hole. Game Over!")
        elif choice3 =="yellow":
            print(""); print("You found the treasure! You win!\n"); print(gold)
        elif choice3 == "blue":
            print("You enter room full of beasts! Game Over!")
        else:
            print("You have to chose. Game over!")
    else:
        print('You got attacked by a shark. Game Over.')
else:
    print("You fell into a hole, Game Over.")

    