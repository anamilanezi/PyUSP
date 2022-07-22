from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.shape('square')
        self.color('#F4EEA9')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == 'left':
            self.xpos = -370
        elif side == 'right':
            self.xpos = 370
        self.ypos = 0
        self.goto(self.xpos, self.ypos)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xpos, new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xpos, new_y)


