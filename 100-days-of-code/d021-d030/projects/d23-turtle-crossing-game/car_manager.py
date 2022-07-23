from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super(CarManager, self).__init__()
        self.all_cars = []
        self.add_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle()
        car.shape('square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randrange(-200, 200, 30)
        car.goto(320, random_y)
        car.color(random.choice(COLORS))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def stop(self):
        self.move_distance = 0

    def restart(self):
        self.all_cars = []
