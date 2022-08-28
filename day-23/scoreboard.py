from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
PLACEMENT = (-250, 250)


class Scoreboard(Turtle):
    def __init__(self):
        """Scoreboard with the level that the player is on."""
        super().__init__()
        self.hideturtle()
        self.level = 1

        self.penup()
        self.setposition(PLACEMENT)
        self.write(f"Level: {self.level}", True, "left", FONT)
        time.sleep(0.5)

    def update_score(self):
        """Updating the level and the scoreboard"""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", True, "left", FONT)

    def game_over(self):
        """Show the game over message"""
        self.setposition(0, 0)
        self.write(f"GAME OVER", True, "center", FONT)
