'''
Welcome to password generator!
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | ____ |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!!!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_num = int(input("How many numbers?\n"))

password_list = []
for i in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for i in range(1, nr_num+1):
    password_list.append(random.choice(numbers))
for i in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

password_not_randomized_order = password_list
print(f'not randomly ordered passowrd {password_not_randomized_order}')
random.shuffle(password_not_randomized_order)
password_random_ordered = password_not_randomized_order
print(password_random_ordered)
password = str()
for element in password_random_ordered:
    password+=element
print(f'Your generated password is: {password}')