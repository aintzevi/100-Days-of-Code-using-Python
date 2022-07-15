from turtle import Turtle, Screen
from paddle import Paddle
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

screen = Screen()
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")


screen.tracer(0)
paddle = Paddle()

screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    screen.onkey(paddle.up, "Up")
    screen.onkey(paddle.down, "Down")

screen.exitonclick()
