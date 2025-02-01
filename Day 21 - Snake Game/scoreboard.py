from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#Scoreboard class to keep track of the game's score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    #updates the score everytime the snake eats food
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    #initiates game over screen everytime the snake collide
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    #increment score variable by 1
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



