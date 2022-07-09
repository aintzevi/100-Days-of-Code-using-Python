import random
from turtle import Turtle, Screen

screen = Screen()
colours = ["purple", "blue", "green", "yellow", "orange", "red"]

# Since the start and finish of the window matter for the race, we specifically set it

# Additionally, since 500 and 400 hundred could be either width or height, it is best to use keyword arguments
# instead of positional arguments so that one can instantly know which one is which
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour:")

is_race_on = False

all_turtles = []

for index in range(len(colours)):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    # (0, 0) is in the center of the window, where our turtle first appears
    # We could also create a list of the y_positions and call based on the turtle index
    new_turtle.goto(-230, -70 + index * 30)
    new_turtle.color(colours[index])
    all_turtles.append(new_turtle)

# Check if the user has given a bet
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle finished first!")
            else:
                print(f"You lose! {winner} won the race.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
