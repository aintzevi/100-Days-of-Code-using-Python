from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")

# This stops animating the screen immediately after a change. We need to update the screen xplicitly when we need to.
# This helps to make the snake appear as its components move smoothly and not "blinking"
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

food = Food()
scoreboard = Scoreboard(SCREEN_HEIGHT)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)

    snake.move()

    # Detect collision - we assume that if the snake head is about 15 steps far from the food, it is eating it
    if snake.head.distance(food) < 15:
        food.place_food()
        snake.extend()
        scoreboard.refresh()

    # Detect collision with walls
    if snake.head.xcor() > SCREEN_WIDTH/2 - 15 or snake.head.xcor() < -SCREEN_WIDTH/2 + 15 \
            or snake.head.ycor() > SCREEN_HEIGHT/2 - 15 or snake.head.ycor() < -SCREEN_HEIGHT/2 + 15:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for block in snake.snake_blocks[1:]:
        # The head anyway has less than 10 distance with itself, so we need to pass the head check
        if snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
