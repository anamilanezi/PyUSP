from turtle import Turtle
import random

HEADINGS = [*range(0, 360, 45)]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("#FFFA4D")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.setheading(random.choice(HEADINGS))
        self.goto(random_x, random_y)
