from turtle import Turtle, Screen


def move_forwards():
    tim.fd(10)


tim = Turtle()
screen = Screen()

screen.listen()

# Passing a function into another function is done without the parenthesis
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

# A higher order function works using other functions. Very common in Python, not possible at all in some languages.
