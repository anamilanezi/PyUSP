import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

x = random.randrange(0,150)
y = random.randrange(0,150)

for i in range(x):
    andy.down()
    lance.down()
    andy.forward(i)# your code goes here
    lance.forward(i)

wn.exitonclick()
