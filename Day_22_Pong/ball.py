from turtle import Turtle
#Setup of the ball that bounces around in pong
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_cor = 10
        self.y_cor = 10
        self.speed = 0.1

#movement of the ball
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)
#changing coordinates to perform "bounce" in the y direction
    def bounce_y(self):
        self.y_cor *= -1

# changing coordinates to perform "bounce" in the x direction
    def bounce_x(self):
        self.x_cor *= -1
        self.speed *= 0.9

#resets the ball position after a player scores a point
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 0.1