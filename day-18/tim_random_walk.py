from turtle import Turtle, Screen
from random import uniform, choice

def random_colour():
    r = uniform(0, 1)
    g = uniform(0, 1)
    b = uniform(0, 1)

    return r, g, b


directions = [0, 90, 180, 270]
tim = Turtle()
# tim.speed(10)
tim.speed("fastest")
tim.pensize(5)

for _ in range(200):
    tim.color(random_colour())
    tim.fd(30)
    tim.setheading(choice(directions))

# This needs to be done after all else in the code - documentation
screen = Screen()
screen.exitonclick()
