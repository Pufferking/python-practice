from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#Scoreboard class to keep track of the game's score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        #High Score taken from a txt file called data.txt
        with open("data.txt") as random:
            self.high_score = int(random.read())


        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    #updates the score everytime the snake eats food
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    #resets the score, changes the current high score and save it to the data.txt for furthur use
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as bla:
                bla.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    #increment score variable by 1
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



