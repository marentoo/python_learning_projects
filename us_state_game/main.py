import turtle
import pandas as pd

FONT = ('Arial', 12, 'bold')


screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


df = pd.read_csv("50_states.csv")

#get cordinates of guess state
def get_cor(input_state):
    filtered_row = df[df["state"] == answer_state]
    x_cor = filtered_row['x'].values[0]
    y_cor = filtered_row['y'].values[0]
    return x_cor, y_cor

#put writing of state on the map
def put_writing():
    writing = turtle.Turtle()
    writing.penup()
    writing.hideturtle()
    writing.goto(x_cor, y_cor)
    writing.write(answer_state, font = FONT)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 Correct States",
    prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]

        new_df = pd.DataFrame(states_to_learn)
        new_df.to_csv("states_to_learn.csv")

        break
    states_list = df["state"].to_list()
    if answer_state in states_list:
        guessed_states.append(answer_state)
        x_cor, y_cor = get_cor(answer_state)
        put_writing()


screen.exitonclick()

