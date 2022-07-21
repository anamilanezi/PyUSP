from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.segments = 3
        self.create_body(self.segments)
        self.head = self.body[0]
        self.tail = self.body[:-1]
        self.last_direction = self.head.heading()

    def create_body(self, segments):
        xpos = 0
        ypos = 0
        for _ in range(segments):
            self.add_segment(xpos, ypos)

    def add_segment(self, xpos, ypos):
        body_segment = Turtle(shape="square")
        body_segment.color("#E04DB0")
        body_segment.penup()
        body_segment.goto(x=xpos, y=ypos)
        self.body.append(body_segment)
        xpos -= 20.0

    def extend(self):
        last_xy_position = self.body[-1].position()
        xpos = last_xy_position[0]
        ypos = last_xy_position[1]
        self.add_segment(xpos, ypos)

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_direction = self.head.heading()

    def up(self):
        if self.last_direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_direction != LEFT:
            self.head.setheading(RIGHT)
