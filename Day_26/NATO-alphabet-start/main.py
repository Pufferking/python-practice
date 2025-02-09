student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
name =input("Enter a name:")
import pandas
student_data_frame = pandas.DataFrame(student_dict)
nato = pandas.read_csv("nato_phonetic_alphabet.csv")


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dict = {word.letter:word.code for (letter,word) in nato.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_list = [nato_dict[letter.upper()] for letter in name]
print(nato_list)
