from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Player turtle class, starts from the bottom of the screen and can move only upward"""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        """Turtle moving one step upwards"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def return_to_start(self):
        """Repositions turtle to the bottom of the window"""
        self.goto(STARTING_POSITION)
