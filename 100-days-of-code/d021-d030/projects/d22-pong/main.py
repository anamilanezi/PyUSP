from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from table import Table


screen = Screen()
screen.bgcolor("#064635")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

table = Table()
left_paddle = Paddle('left')
right_paddle = Paddle('right')
ball = Ball()
left_score = Scoreboard('left')
right_score = Scoreboard('right')

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 350) or (ball.distance(left_paddle) < 50 and ball.xcor() < - 350):
        ball.bounce_x()

    # Detect if right paddle miss the ball
    if ball.xcor() > 375:
        left_score.update_score()
        ball.reset_position()
    # Detect if right paddle miss the ball
    elif ball.xcor() < -375:
        right_score.update_score()
        ball.reset_position()


screen.exitonclick()
