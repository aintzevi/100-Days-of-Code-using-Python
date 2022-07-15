from turtle import Turtle, Screen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")


screen.tracer(0)
player_1 = Paddle()
player_2 = Paddle()

player_1.goto(-SCREEN_WIDTH / 2 + 20, 0)
player_2.goto(SCREEN_WIDTH / 2 - 20, 0)

screen.listen()

game_is_on = True

while game_is_on:
    screen.update()

    screen.onkey(player_1.up, "w")
    screen.onkey(player_1.down, "s")

    screen.onkey(player_2.up, "i")
    screen.onkey(player_2.down, "k")

    screen.update()


screen.exitonclick()
