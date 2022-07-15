from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.turtlesize(0.5, 5)
        self.setheading(90)
        self.shape("square")
        self.speed("fastest")

    def up(self):
        self.setheading(90)
        self.forward(10)

    def down(self):
        self.setheading(270)
        self.forward(10)
