from tkinter import *

def button_clicked():
    print("i got clicked")
    new_text = entry.get()
    my_label.config(text = "new_text")


#window
window = Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 300)
#Creates padding around the contents in window
window.config(padx = 20, pady = 20)


#Label
my_label = Label(text = "I Am a Label", font = ("Arial", 24, "bold"))
my_label.config(text = "New text")
#grid allows positioning of widgets in a column row fashion
my_label.grid(column = 0, row = 0)

#Button

button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 1, row = 1)

new_button = Button(text = "new button", command = button_clicked)
new_button.grid(column = 2, row = 0)

#Entry

entry = Entry(width = 10)
print(entry.get())
entry.grid(column = 3, row = 2)

#keeps the window open
window.mainloop()