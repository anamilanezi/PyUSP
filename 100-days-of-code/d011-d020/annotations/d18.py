import turtle as t
from py_colors import selected_colors, angela_colors
import random as r


def random_color_list(list):
    return r.choice(list)


def random_color_rgb():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return (red, green, blue)


def dashed_line(turtle, dash_size, repetitions, color="red"):
    """Draw a dashed line """
    turtle.color(color)
    for _ in range(repetitions):
        turtle.pendown()
        turtle.forward(dash_size)
        turtle.penup()
        turtle.forward(dash_size)


def square(turtle, size):
    """Draw a square """
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_shape(turtle, side_size, n_sides):
    """Draw a shape of given number of sides and side size"""
    for _ in range(n_sides):
        turtle.forward(side_size)
        turtle.left(360/n_sides)


def random_walk(turtle, n):
    """Make a turtle object to walk n steps in random direction"""
    angles = [0, 90, 180, 270]
    turtle.forward(n)
    turtle.setheading(r.choice(angles))


def random_dot(turtle, n):
    angles = [0, 90, 180, 270]
    turtle.penup()
    turtle.forward(n)
    turtle.pendown()
    turtle.dot()
    turtle.setheading(r.choice(angles))


def spirograph(turtle, circle_radius, circle_distance):
    """Draw a spirograph shape with given radius and distance from each circle"""
    for i in range(0, 360, circle_distance):
        turtle.circle(circle_radius)
        turtle.setheading(i)
        turtle.color(random_color_rgb())


tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
# tim.pensize(15)
tim.speed(0)
tim.color(random_color_list(selected_colors))

# spirograph(tim, 100, 5)

# square(tim, 100)
# dashed_line(tim, 10, 5, "cyan4")

# for i in range(3, 11):
#     draw_shape(tim, 100, i)
#     tim.color(random_color(selected_colors))

# for _ in range(200):
#     random_walk(tim, 30)
#     tim.color(random_color_list(selected_colors))

for _ in range(200):
    random_dot(tim, 30)
    tim.color(random_color_list(selected_colors))

screen = t.Screen()
screen.exitonclick()
