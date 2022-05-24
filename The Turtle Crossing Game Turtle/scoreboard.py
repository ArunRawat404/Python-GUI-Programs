from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"LEVEL: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
