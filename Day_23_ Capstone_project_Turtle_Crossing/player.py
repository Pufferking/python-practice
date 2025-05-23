from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.reset_pos()

#Player control
    def go_up(self):
        self.forward(MOVE_DISTANCE)

#reset position of the player to beginning
    def reset_pos(self):
        self.goto(STARTING_POSITION)

