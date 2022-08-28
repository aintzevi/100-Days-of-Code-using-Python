from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Car constructor where all the active cars are kept"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.active_cars = []

    def create(self, width, height):
        """Creates a car in every run, in a random height position inside the window limits."""

        # A car is consisted of two square back to back blocks
        car = []

        car1 = Turtle()
        car2 = Turtle()
        car1.penup()
        car2.penup()

        car_color = random.choice(COLORS)
        car1.color(car_color)
        car2.color(car_color)
        car1.shape("square")
        car2.shape("square")

        initial_y_pos = random.randint(-height / 2 + 20, height / 2 - 20)
        car1_initial_position = (width / 2 - 20, initial_y_pos)
        car2_initial_position = (width / 2, initial_y_pos)
        car1.setposition(car1_initial_position)
        car2.setposition(car2_initial_position)

        car1.setheading(180)
        car2.setheading(180)

        car.append(car1)
        car.append(car2)

        self.active_cars.append(car)

        time.sleep(0.1)

    def move(self, level):
        """Every car in the window moves forward by a specific increment that increases overtime"""
        for car in self.active_cars:
            car[0].forward(MOVE_INCREMENT * level)
            car[1].forward(MOVE_INCREMENT * level)


