from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Consolas', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.color("#A3DDCB")
        self.penup()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    def read_high_score(self):
        with open("data.txt") as data:
            high_score = int(data.read())
            return high_score

    def write_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("#E6B566")
    #     self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)



