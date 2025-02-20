from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password generator from Day 5 of "100 Days of Python"
def generate_password():
    e_password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
        , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Used List comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    e_password.insert(0, password)
    #Copies the generated password onto the clipboard
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
#Creates a text file and saves the name of website,email and the password
def add_p():
    website = e_website.get()
    email = e_email.get()
    password1= e_password.get()
    #Creates a dialogue box to determine any entries left empty or to confirm the details entered
    if len(password1) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title = "Oops", message = "Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the detaIls entered: \nEmail:"
                                                              f"{email}\nPassword: {password1}")

        if is_ok:
            with open("mypass.txt", "a") as text_f:
                text_f.write(f"{website} | {email} | {password1} \n")
            e_password.delete(0, END)
            e_website.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

#Window

window = Tk()
window.title("MY PASS")
window.config(padx = 50, pady = 50)

#Canvas

canvas = Canvas(height=200, width=200, )
logo = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

#Labels

l_website = Label(text = "Website:", )
l_website.grid(row = 1, column = 0)

l_email = Label(text = "Email/Username:")
l_email.grid(row = 2, column = 0)

l_password = Label(text = "Password:")
l_password.grid(row = 3, column = 0)

e_website = Entry(width = 52)
e_website.grid(row = 1, column = 1, columnspan = 2)
e_website.focus()

#Entries

e_email = Entry(width = 52)
e_email.grid(row = 2, column = 1, columnspan = 2)
e_email.insert(0, "adil@gmail.com")

e_password = Entry(width = 33)
e_password.grid(row = 3, column = 1)

#Buttons

gen_button = Button(text = "Generate Password", command=generate_password)
gen_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 44, command = add_p)
add_button.grid(row = 4, column = 1, columnspan = 2)



window.mainloop()
