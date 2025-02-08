import turtle
import pandas

#Screen setup
screen = turtle.Screen()
screen.title("US states Game")
image = "blank_states_img.gif"
screen.addshape(image)
c_states = []
turtle.shape(image)

#All data from the 50_states.csv saved in 'data' variable
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

#Continuous loop to run the title box until all states found
while len(c_states) < 50:

    #Appearance of the Text input box
    answer_state = screen.textinput(title = f"{len(c_states)}/50 States Correct",
                                    prompt = "What's another state name").title()

    #exits the loop on typing 'exit' to the text input box
    if answer_state == "Exit":
        break
    #Check if the state given in the title box is valid if so create a turtle to display the
    #placement of state in the map
    if answer_state in all_states:
        c_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

#Adds states not guessed to a list and make a csv file listing all the states to learn
w_states = []
for state in all_states:
    if state not in c_states:
        w_states.append(state)

data = pandas.DataFrame(w_states)
data.to_csv("States to learn.csv")