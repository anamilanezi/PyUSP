import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

counter = 1
limit = 10
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    if player.ycor() > 280:
        player.starting_position()
        score.update_level()
        print(cars.move_distance)
        cars.increase_speed()
        print("point")

    for car in cars.all_cars:
        if player.distance(car) < 20:
            cars.stop()
            score.game_over()

    if counter % limit == 0:
        cars.add_car()

    counter += 1

    if cars.move_distance >= 15:
        limit = 5
    elif cars.move_distance >= 25:
        limit = 3
    elif cars.move_distance >= 35:
        limit = 2

