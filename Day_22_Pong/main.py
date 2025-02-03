from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

#Screen and Paddle setup
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



#Moving paddles by detecting specific keys pressed on keyboard
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.down, "s")
game_is_on = True

#updating screen and the tick speed of the animation
while game_is_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

#Detect ball hitting top and bottom side
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


#Detect Ball hitting Paddles
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)) :
        ball.bounce_x()


# Detect Right paddle missing
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()
# Detect Right paddle missing
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()









screen.exitonclick()