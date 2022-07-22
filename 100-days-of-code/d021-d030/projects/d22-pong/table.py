from turtle import Turtle

class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-380, 280)
        self.pendown()
        self.forward(760)
        self.right(90)
        self.forward(560)
        self.right(90)
        self.forward(760)
        self.right(90)
        self.forward(560)
        self.goto(0, 280)
        self.setheading(270)
        for i in range(18):
            self.forward(16)
            self.penup()
            self.forward(16)
            self.pendown()
