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
    time.sleep(0.1)
    screen.update()

    # Cars continuously generated in every step
    car_manager.create(WIDTH, HEIGHT)
    car_manager.move()
    # Detect car collision
    # Detect finish line passing

screen.exitonclick()


