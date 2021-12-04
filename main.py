import pandas
import turtle
#import pyinstaller

screen = turtle.Screen()
screen.title("U.S States game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.screensize()
status = True
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessedStates = []
while len(guessedStates)<50:
    answer_states =screen.textinput(title=f"Guessed states: {len(guessedStates)}/50", prompt="What's another state's name?").title()
    if answer_states == "Exit":
        missing_states =[]
        for state in states:
            if state not in guessedStates:
                missing_states.append(state)
        dp = pandas.Series(missing_states)
        dp.to_csv("missed_states.csv")

        break
    if answer_states in states:
        guessedStates.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state == answer_states]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_states)
