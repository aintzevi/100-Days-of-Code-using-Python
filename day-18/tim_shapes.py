from turtle import Turtle, Screen
from random import uniform


def draw_shape(num_of_edges):
    angle = 360 / num_of_edges
    for _ in range(num_of_edges):
        tim.fd(100)
        tim.right(angle)


tim = Turtle("turtle")

for i in range(3, 11):
    tim.color(uniform(0, 1), uniform(0, 1), uniform(0, 1))
    draw_shape(i)

# Dashed-line, could also be produced by changing colour between white and black every 10 steps
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# This needs to be done after all else in the code - documentation
screen = Screen()
screen.exitonclick()
