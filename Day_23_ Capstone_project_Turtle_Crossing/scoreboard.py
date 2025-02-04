from turtle import Turtle

FONT = ("Courier", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 250)
        self.update_scoreboard()

#update scoreboard everytime player completes a level
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level} ", align="center", font=FONT)

#increasing the level counter in the game
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

#Prompts the Game Over screen when the player gets hit by a car
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = "center", font = FONT)


