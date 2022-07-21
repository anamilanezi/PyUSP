from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Consolas', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#A3DDCB")
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.write_score()
        self.all_scores = {}

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("#E6B566")
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)

    def record_score(self, name):
        self.all_scores[name] = self.score
        print(self.all_scores)
