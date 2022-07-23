from turtle import Turtle

FONT = ("Consolas", 21, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, -280)
        self.level = 1
        self.color("#184A8C")
        self.write_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    def write_level(self):
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
