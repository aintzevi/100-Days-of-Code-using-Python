import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "images/blank_states_img.gif"

# Handle images in turtle
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data/50_states.csv")
states = data.state.to_list()

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the state: ", prompt="What's another state's name?").capitalize()
    if answer_state in states:
        # Specific row of answer state
        state_data = data[data.state == answer_state]
        city_name = turtle.Turtle()
        city_name.penup()
        city_name.hideturtle()
        city_name.goto(int(state_data.x), int(state_data.y))
        # We could also use state_data.state.item(), where item picks only the value of the data piece,
        # without the data type information etc.
        city_name.write(answer_state)

    print(answer_state)

screen.exitonclick()



