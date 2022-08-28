from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
PLACEMENT = (-250, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.penup()
        self.setposition(PLACEMENT)
        self.hideturtle()
        self.write(f"Level: {self.level}", True, "left", FONT)
        time.sleep(0.5)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", True, "left", FONT)
