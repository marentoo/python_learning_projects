#TODO: Create a letter using starting_letter.txt 

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as letter:
    starting_letter = letter.read()

with open("Input/Names/invited_names.txt","r") as names_files:
    names = names_files.readlines()

    for name in names:
        name = name.strip()
        with open(f"Output/ReadyToSend/letter_to_{name}.docx ", "w") as f:
            updated_letter = starting_letter.replace("[name]", name)
            f.write(updated_letter)

