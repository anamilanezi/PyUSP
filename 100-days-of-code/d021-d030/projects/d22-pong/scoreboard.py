from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 50, 'bold')

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("#A3DDCB")
        self.penup()
        if position == 'left':
            self.goto(-100, 200)
        if position == 'right':
            self.goto(100, 200)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()
