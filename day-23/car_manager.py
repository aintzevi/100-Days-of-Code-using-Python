from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        """Car constructor where all the active cars are kept"""
        super().__init__()
        self.hideturtle()
        self.active_cars = []

    def create(self, width, height):
        """Creates a car in every run, in a random height position inside the window limits."""

        # Add extra random option of 1 in 3 creation of a car
        randomizer = random.randint(0, 2)
        if randomizer == 0:
            car = Turtle("square")
            # Stretch horizontally to appear as rectangle
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))

            # Adjust bottom limit, for the turtle to not immediately die when leveling up
            initial_y_pos = random.randint(-height / 2 + 50, height / 2 - 20)
            car_initial_position = (width / 2, initial_y_pos)
            car.setposition(car_initial_position)
            car.setheading(180)

            self.active_cars.append(car)

        time.sleep(0.08)

    def move(self, level):
        """Every car in the window moves forward by a specific increment that increases overtime"""
        for car in self.active_cars:
            car.forward(MOVE_INCREMENT * level)
