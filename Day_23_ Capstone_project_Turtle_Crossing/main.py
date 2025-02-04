import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Screen Setup and class initialisation
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Player input key to move turtle
screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

#Determines if car hits the turtle
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

#Determines if the turtle reaches end of level

    if player.ycor() > 290:
        player.reset_pos()
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()