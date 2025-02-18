from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
start = True

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    t_label.config(text = 'Timer')
    check_label.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        t_label.config(text = "Break", fg = RED)
        count_down(long_break_sec)
    if reps % 2 == 0:
        t_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        t_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text = marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 100, bg = YELLOW)

#Creates canvas to put images on

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
t_image = PhotoImage(file = "tomato.png")
canvas.create_image(102, 112, image = t_image)
timer_text = canvas.create_text(102, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold") )
canvas.grid(row = 1, column = 1)

#Text label on the window
t_label= Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50, "normal"))
t_label.grid(row = 0, column = 1)

#Label that displays checkmarks

check_label = Label(text = "✔", bg = YELLOW, fg = GREEN)
check_label.grid(row = 3, column = 1)


#The Start button

start_button = Button(text="Start" , command=start_timer)
start_button.grid(row = 2, column = 0)

#The Reset button

reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)




window.mainloop()