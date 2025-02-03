from turtle import Turtle
#Paddle setup (The white boxes that bounces the balls)
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
#Movement of the paddle in the 'up' direction
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
#Movement of the paddle in the 'down' direction
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

