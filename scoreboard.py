from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.score = 0

        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.upgrade_scoreboard()


    def upgrade_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.upgrade_scoreboard()


    def increase_point(self):
        self.score += 1

    def game_over(self):
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 0)

    def play_again(self):
        self.write("Play Again?", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 0)