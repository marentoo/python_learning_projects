student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(row.student)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_df = {row.letter:row.code for (index, row) in df.iterrows()}
# print(dict_df)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



def generate_phonetic():
    given_word = input("Give a word: ").upper()

    try:
        list_of_phonetic_code_words = [dict_df[letter] for letter in given_word]
    except KeyError:
        print("Only letters")
        generate_phonetic()
    else:
        print(list_of_phonetic_code_words)

generate_phonetic()
