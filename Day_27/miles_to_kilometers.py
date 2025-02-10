from tkinter import *
#This code creates a simple GUI to convert miles to kilometer

#window setup
window = Tk()
window.title("Miles to Km Converter")
window.config(padx = 20, pady = 20)


#function to convert the mile to kilometer from entry

def miles_to_km():
    text = float(entry.get())
    km = round(text * 1.6)
    label2.config(text=f"{km}")




#Entry box setup (input box)
entry = Entry(width = 7)
entry.grid(column = 1, row = 0)

#Labels to display various text in the window
mile_label = Label(text = "Miles")
mile_label.grid(row = 0, column = 2)

label1 = Label(text = "is equal to")
label1.grid(column = 0, row = 1)

label2 = Label(text = "0")
label2.grid(column = 1, row = 1)

km_label = Label(text = "Km")
km_label.grid(column = 2, row = 1)

#Calculate button which on click displays the converted km
button = Button(text = "Calculate", command=miles_to_km)
button.grid(column = 1, row =2)












window.mainloop()



