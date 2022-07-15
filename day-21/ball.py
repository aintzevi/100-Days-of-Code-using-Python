from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(40)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10

        self.goto(new_x, new_y)
