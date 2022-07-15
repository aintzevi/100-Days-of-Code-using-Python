import time
from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"
FONT_SIZE = 44

class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0

        self.penup()
        self.hideturtle()
        self.goto(0, screen_height/2)
        self.color("white")
        self.write(f"{self.score_1} \t {self.score_2}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
        time.sleep(0.5)

    def refresh(self):
        # TODO Update score values here
        self.clear()
        self.write(f"{self.score_1} \t {self.score_2}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
