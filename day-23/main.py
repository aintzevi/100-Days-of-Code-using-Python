import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

game_is_on = True

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "p")

while game_is_on:

    # Cars continuously generated in every step
    car_manager.create(WIDTH, HEIGHT)
    car_manager.move(scoreboard.level)

    if player.ycor() > HEIGHT / 2 - 5:
        player.return_to_start()
        scoreboard.update_score()

    for car in car_manager.active_cars:
        if player.distance(car) < 25:
            print("Squish")
            scoreboard.game_over()
            game_is_on = False
            break

    time.sleep(0.1)
    screen.update()

screen.exitonclick()


