from turtle import Turtle

FONT = ("Press Start 2P", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(f"LEVEL : {self.score}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
