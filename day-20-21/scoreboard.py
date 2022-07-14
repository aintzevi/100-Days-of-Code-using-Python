from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_WEIGHT = "normal"


class Scoreboard(Turtle):
    """Models the scoreboard of the game, keeping track of the score and presenting to the user"""

    def __init__(self, height):
        self.score = 0
        super().__init__()

        # Position turtle to the top, so the text can bbe displayed there,
        # Additionally hide the turtle, we only need the text to so
        self.goto(x=0, y=height/2 - 30)
        self.hideturtle()
        self.color("white")

        display = "Score = " + str(self.score)
        self.write(arg=display, align=ALIGNMENT, font=(FONT_NAME, 20, FONT_WEIGHT))

    def refresh(self):
        self.score += 10
        self.clear()
        self.show_score()

    def show_score(self):
        display = "Score = " + str(self.score)
        self.write(arg=display, align=ALIGNMENT, font=(FONT_NAME, 20, FONT_WEIGHT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=(FONT_NAME, 20, FONT_WEIGHT))
