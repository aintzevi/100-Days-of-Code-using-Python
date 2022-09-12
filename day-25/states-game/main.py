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
guessed_states = []
states_not_found = []

while len(guessed_states) < 50:
    # .title capitalizes each first word. Careful with quote marks and punctuation though
    answer_state = screen.textinput(title=f"Guess the state: {len(guessed_states)}/50 correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                states_not_found.append(state)
        df = pandas.DataFrame(states_not_found)
        df.to_csv("data/leftover_states.csv")
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
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



