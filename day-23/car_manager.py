from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.active_cars = []

    def create(self, width, height):
        # Call car creation that creates cars of random colours in random intervals of time, in random spaces.
        # Each car then moves towards the negative x
        # Create a car
        car = []

        car1 = Turtle()
        car2 = Turtle()
        car1.hideturtle()
        car2.hideturtle()
        car1.penup()
        car2.penup()

        car_color = random.choice(COLORS)
        car1.color(car_color)
        car2.color(car_color)
        car1.shape("square")
        car2.shape("square")

        initial_y_pos = random.randint(-height / 2 + 20, height / 2 - 20)
        car1_initial_position = (width / 2 - 40, initial_y_pos)
        car2_initial_position = (width / 2 - 20, initial_y_pos)
        car1.setposition(car1_initial_position)
        car2.setposition(car2_initial_position)

        car1.setheading(180)
        car2.setheading(180)

        car.append(car1)
        car.append(car2)

        self.active_cars.append(car)

        time.sleep(0.1)

    def move(self):
        for car in self.active_cars:
            car[0].forward(MOVE_INCREMENT)
            car[1].forward(MOVE_INCREMENT)

        # TODO Increase speed by level

