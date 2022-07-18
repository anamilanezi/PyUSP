import random
import turtle as t

# How to pick colors from image using colorgram:
# import colorgram
# colors = colorgram.extract('image.png', 20)
#
# rgb_colors = []
#
# for color in colors:
#     rgb = color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     rgb_colors.append((red, green, blue))


def random_color():
    """Pick a random rgb color from list"""
    return random.choice(rgb_colors)


def random_color_dot(turtle, distance):
    """Make a dot of random color and size 20 and move to given distance"""
    turtle.dot(30, random_color())
    turtle.penup()
    turtle.fd(distance)


def turn_left(turtle, distance):
    """Turn the drawing direction to the left side of canvas"""
    turtle.left(90)
    turtle.fd(distance)
    turtle.left(90)
    turtle.fd(distance)


def turn_right(turtle, distance):
    """Turn the drawing direction to the right side of canvas"""
    turtle.right(90)
    turtle.fd(distance)
    turtle.right(90)
    turtle.fd(distance)


rgb_colors = [(50, 95, 133), (123, 185, 137), (244, 249, 246), (152, 66, 47), (214, 81, 115), (249, 150, 83),
              (250, 197, 77), (188, 46, 52), (38, 151, 72), (8, 19, 6), (66, 12, 56), (203, 197, 2), (198, 62, 61),
              (144, 187, 193), (1, 104, 124), (201, 133, 153), (167, 204, 184)]

tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setpos(-300, -300)


def hirst_painting(turtle, n_dots, distance):
    """Creates a hirst paint with 10 lines of n dots """
    for _ in range(5):
        for _ in range(n_dots):
            random_color_dot(turtle, distance)
        turn_left(turtle, distance)
        for _ in range(n_dots):
            random_color_dot(turtle, distance)
        turn_right(turtle, distance)


hirst_painting(turtle=tim, n_dots=10, distance=50)

# for _ in range(5):
#     for _ in range(10):
#
#         random_color_dot(tim, 50)
#     turn_left(tim, 50)
#     for _ in range(10):
#         random_color_dot(tim, 50)
#     turn_right(tim, 50)


screen = t.Screen()
screen.exitonclick()
