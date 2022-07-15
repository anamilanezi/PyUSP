# import turtle
#
# timmy = turtle.Turtle()
# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()                # Create an instance
# print(timmy)
# timmy.shape("turtle")           # Method
# timmy.color("aquamarine4")      # Method
# turtle.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)     # Attribute
# my_screen.exitonclick()         # Method

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])

print(table.align)
table.align = "l"

print(table)

# x = PrettyTable()
# x.add_column("City name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
# print(x)