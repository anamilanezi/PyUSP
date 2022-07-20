from turtle import Turtle
upda
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, segments=3):
        self.body = []
        self.create_body(segments)
        self.head = self.body[0]

    def create_body(self, segments=3):
        xpos = 0  # random.randint(-200, 200)
        ypos = 0  # random.randint(-200, 200)
        for i in range(segments):
            body_segment = Turtle(shape="square")
            body_segment.color("white")
            body_segment.penup()
            body_segment.goto(x=xpos, y=ypos)
            self.body.append(body_segment)
            xpos -= 20.0

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
