import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

player_1 = Paddle((-SCREEN_WIDTH / 2 + 20, 0))
player_2 = Paddle((SCREEN_WIDTH / 2 - 20, 0))

ball = Ball()

screen.listen()
# Paddle controls
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
screen.onkey(player_2.up, "i")
screen.onkey(player_2.down, "k")

game_is_on = True

while game_is_on:
    # For the ball to go slower, use sleep. We could alternatively lower the amount by which the ball moves in each step
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Collision with up or down wall, meaning the ball should bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle (distance is not enough because of the paddle shape)

    if (ball.distance(player_2) < 50 and ball.xcor() > 320) or (ball.distance(player_1) < 50 and ball.xcor() < -320):
        ball.bounce_x()
screen.exitonclick()
