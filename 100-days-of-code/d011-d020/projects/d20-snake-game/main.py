from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings

snake = Snake()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.08)
    snake.move()

# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

# Create the snake body:
# snake_body = []
# xpos = 0
#
# for i in range(3):
#     body_segment = Turtle(shape="square")
#     body_segment.color("white")
#     body_segment.penup()
#     body_segment.goto(x=xpos, y=0)
#     snake_body.append(body_segment)
#     xpos -= 20.0

# Move the snake:
# while game_is_on:
#     # Screen update and sleep make the movement of segments happen all at once, so they don't appear separeted
#     screen.update()
#     sleep(0.1)
# for seg_num in range(len(snake_body) - 1, 0, -1):
#     # Start from last segment to first, make last segment assume position of previous segment (will follow the head)
#     new_x = snake_body[seg_num - 1].xcor()
#     new_y = snake_body[seg_num - 1].ycor()
#     snake_body[seg_num].goto(new_x, new_y)
# Now if we move or turn the first segment (head), others will follow
# snake_body[0].forward(20)
# snake_body[0].left(90)
#
#  Angela's solution:

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)


screen.exitonclick()