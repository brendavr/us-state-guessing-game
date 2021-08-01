import turtle
import pandas

screen = turtle.Screen()
screen.title("U.s. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
num_correct = 0
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state?").title()

    if answer_state == "Exit":
        missed_states = []
        for states in state_list:
            if states not in guessed_states:
                missed_states.append(states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        num_correct += 1






