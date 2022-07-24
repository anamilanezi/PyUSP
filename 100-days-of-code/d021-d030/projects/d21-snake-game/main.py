from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#11052C")
screen.title("Snake Game")
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings

snake = Snake()
food = Food()
score = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    sleep(snake.speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()
        snake.speed -= 0.002

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        snake.speed = 0.1


    # Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            snake.speed = 0.1

    # if not game_is_on:
    #     play_again = screen.textinput(title="GAME OVER", prompt="Do you want to play again? (y/n)")
    #     if play_again is None:
    #         return False
    #     if play_again.lower() == 'y':
    #         screen.clear()
    #         return True
    #     else:
    #         return False

screen.exitonclick()

