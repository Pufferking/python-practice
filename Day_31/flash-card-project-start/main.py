from tkinter import *  # Importing all functions from the Tkinter library for GUI development
import pandas  # Importing pandas for handling CSV data
from random import *  # Importing all functions from the random module for random selection

current_card = {}  # Dictionary to store the current flashcard's data
BACKGROUND_COLOR = "#B1DDC6"  # Background color for the application
words = {}  # Dictionary to store words from the CSV file

# Try to load words from "words_to_learn.csv", if not found, load from the original file
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # Reading the saved words-to-learn file
except FileNotFoundError:
    original_data = pandas.read_csv("data/Untitled spreadsheet - Sheet1.csv")  # Reading the original dataset
    words = original_data.to_dict(orient="records")  # Converting the data into a list of dictionaries
else:
    words = data.to_dict(orient="records")  # Converting the data into a list of dictionaries if file exists

# Creating the main window for the application
window = Tk()
window.title("Flash Cards")  # Setting the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Adding padding and background color

# Function to remove the known word from the list and save the remaining words

def is_known():
    words.remove(current_card)  # Removing the current card from the list
    data = pandas.DataFrame(words)  # Converting the updated list back into a DataFrame
    data.to_csv("data/words to learn.csv", index=False)  # Saving the updated list without index numbers
    next_card()  # Moving to the next card

# Function to display the next flashcard

def next_card():
    global current_card, flip_timer  # Using global variables
    window.after_cancel(flip_timer)  # Cancel the previous flip timer
    current_card = choice(words)  # Choosing a random word from the list
    word = current_card["Japanese"]  # Extracting the Japanese word
    canvas.itemconfig(w_text, text=word, fill="black")  # Updating the word text on the card
    canvas.itemconfig(title_text, text="Japanese", fill="black")  # Updating the title text
    canvas.itemconfig(card_background, image=fl_card_front)  # Changing to the front image
    flip_timer = window.after(3000, func=flip_card)  # Setting a timer to flip the card

# Function to flip the card and show the English translation

def flip_card():
    canvas.itemconfig(card_background, image=fl_card_back)  # Changing to the back image
    canvas.itemconfig(title_text, text="English", fill="white")  # Updating title to English
    canvas.itemconfig(w_text, text=current_card["English"], fill="white")  # Showing the English translation

flip_timer = window.after(3000, func=flip_card)  # Initial timer to flip the card after 3 seconds

# Creating the canvas to display the flashcards
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)  # Creating a canvas
fl_card_front = PhotoImage(file="images/card_front.png")  # Loading the front card image
fl_card_back = PhotoImage(file="images/card_back.png")  # Loading the back card image
card_background = canvas.create_image(400, 263, image=fl_card_front)  # Placing the card image on canvas

# Creating text elements for the flashcard
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))  # Title text placeholder
w_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))  # Word text placeholder
canvas.grid(row=0, column=0, columnspan=2)  # Placing the canvas in the grid

# Creating the 'Right' button (for known words)
image1 = PhotoImage(file="images/right.png")  # Loading the right button image
button1 = Button(image=image1, highlightthickness=0, command=is_known)  # Creating the button with an action
button1.grid(row=1, column=1)  # Placing the button in the grid

# Creating the 'Wrong' button (to move to the next card)
image2 = PhotoImage(file="images/wrong.png")  # Loading the wrong button image
button2 = Button(image=image2, highlightthickness=0, command=next_card)  # Creating the button with an action
button2.grid(row=1, column=0)  # Placing the button in the grid

next_card()  # Calling the next_card function to start the flashcards

window.mainloop()  # Running the application loop
