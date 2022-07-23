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

screen.listen()
screen.onkey(player.move_up, "Up")

counter = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 10 == 0:
        cars.add_car()
    cars.move()
    if player.ycor() > 280:
        player.starting_position()
        print("point")
        # Score +1
        # Car speed
    for car in cars.all_cars:
        if player.distance(car) < 15:
            print('colision')
    counter += 1

