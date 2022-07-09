from turtle import Turtle, Screen


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def move_clockwise():
    pen.right(10)
    pen.fd(10)


def move_counter_clockwise():
    pen.left(10)
    pen.fd(10)


def clear_screen():
    pen.reset()


pen = Turtle()
screen = Screen()

pen.speed("fastest")
screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
