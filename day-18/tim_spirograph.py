from turtle import Turtle, Screen
from random import uniform, choice

def random_colour():
    r = uniform(0, 1)
    g = uniform(0, 1)
    b = uniform(0, 1)

    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


directions = [0, 90, 180, 270]
tim = Turtle()

tim.speed("fastest")

draw_spirograph(5)

# This needs to be done after all else in the code - documentation
screen = Screen()
screen.exitonclick()
