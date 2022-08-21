import time
from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"
FONT_SIZE = 44

class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score_left = 0
        self.score_right = 0

        self.penup()
        self.hideturtle()
        self.goto(0, screen_height/2)
        self.color("white")
        self.write(f"{self.score_left} \t {self.score_right}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
        time.sleep(0.5)

    def score_point_left(self):
        self.score_left += 1
        self.refresh()

    def score_point_right(self):
        self.score_right += 1
        self.refresh()

    def refresh(self):
        # TODO Update score values here
        self.clear()
        self.write(f"{self.score_left} \t {self.score_right}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
