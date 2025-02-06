PH = "[name]"
#100_days_of_Python by Angela Yu (Day 24)

#Sending mail to different people with the same contents but the name changed


#The names in the invited_names.txt file saved in  a list
with open("./Input/Names/invited_names.txt") as names_file:
    n_list = names_file.readlines()

#new letter created to the individuals in the invited_names.txt

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_cont = letter.read()
    for name in n_list:
        stripped_name = name.strip()
        replaced = letter_cont.replace(PH, stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode = "w") as random:
            random.write(replaced)