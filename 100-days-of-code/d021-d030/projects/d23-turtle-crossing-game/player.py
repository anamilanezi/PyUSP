from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.starting_position()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color("#547327")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)




