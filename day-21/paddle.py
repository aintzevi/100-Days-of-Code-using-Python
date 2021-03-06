from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.speed("fastest")
        self.goto(initial_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
