from turtle import Turtle
import random

GREEN = ["#4F732D", "#72A641", "#7AA638"]
TREE_SIZE = 13


class Landscape(Turtle):

    def __init__(self):
        super(Landscape, self).__init__()
        self.penup()
        self.hideturtle()
        self.draw_road()
        self.draw_side_line()
        self.draw_lake()
        self.draw_tree_lines(-250, 220)
        self.draw_tree_lines(70, 220)
        self.crossing_lines()

    def draw_rec(self, color, x, y, len, wid):
        self.fillcolor(color)
        self.goto(x, y)
        self.begin_fill()
        for _ in range(2):
            self.forward(len)
            self.right(90)
            self.forward(wid)
            self.right(90)
        self.end_fill()

    def draw_road(self):
        self.draw_rec("#E8EBED", x=-300, y=220, len=600, wid=440)

    def draw_side_line(self):
        self.draw_rec("#34434D", x=-300, y=220, len=600, wid=10)
        self.draw_rec("#34434D", x=-300, y=-220, len=600, wid=10)

    def crossing_lines(self):
        y = 225
        for i in range(12):
            self.draw_rec("white", x=-30, y=y, len=60, wid=20)
            y -= 40

    def draw_circle(self, color):

        self.color(color)
        self.begin_fill()
        self.circle(TREE_SIZE)
        self.end_fill()

    def draw_tree(self, xpos, ypos):
        color = random.choice(GREEN)
        self.goto(xpos, ypos + TREE_SIZE)
        self.draw_circle(color)
        self.goto(xpos - TREE_SIZE, ypos)
        self.draw_circle(color)
        self.goto(xpos, ypos - TREE_SIZE)
        self.draw_circle(color)
        self.goto(xpos + TREE_SIZE, ypos)
        self.draw_circle(color)

    def draw_tree_lines(self, start_x, ypos):
        y = ypos
        for i in range(4):
            self.draw_tree(start_x, y)
            start_x += 60
            y += 30
            if i == 1:
                y = ypos

    def draw_lake(self):
        self.color("#72A9F2")
        x = -50
        y = 270
        for i in range(2):
            self.goto(x, y)
            self.begin_fill()
            self.circle(200)
            self.end_fill()
            x += 100
            y += 10

