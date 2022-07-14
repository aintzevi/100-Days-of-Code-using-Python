import random
from turtle import Turtle


class Food(Turtle):
    """Models a new piece of food for the snake to eat in the game. Is positioned in a random place in the canvas"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.place_food()

    def place_food(self):
        # -1 and +1 added to not put foods on the walls
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)





