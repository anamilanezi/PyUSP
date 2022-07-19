from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [100, 60, 20, -20, -60, -100]
turtles = []

# Creates six instances of turtle
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=y_pos[i])

# Race only starts after user enter the bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        n = random.randint(0, 30)
        turtle.forward(n)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            print(f"{winner_color.title()} is the winner!")

if user_bet.lower() == winner_color.lower():
    print("Congratulations, you've won the bet!")
else:
    print("You've lost the bet.")

screen.exitonclick()