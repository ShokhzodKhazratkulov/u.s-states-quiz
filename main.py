import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Name Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_data = pandas.read_csv("50_states.csv")
all_states = all_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                  prompt="What's the state name?").title()
    if user_input in all_states:
        guessed_states.append(user_input)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_cors = all_data[all_data.state == user_input]
        timmy.goto(int(state_cors.x), int(state_cors.y))
        timmy.write(user_input)

    if user_input == "Exit":
        missed_states = []
        for i in all_states:
            if i not in guessed_states:
                missed_states.append(i)
        data_missed = pandas.DataFrame(missed_states)
        data_missed.to_csv("states to learn.csv")
        break
