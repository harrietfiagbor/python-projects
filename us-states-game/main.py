import turtle
import pandas

FONT = ("Arial", 8, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
correct_guess = []


while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                              prompt="What's another state name").title()
    print(answer)

    if answer == "Exit":
        missing_state = [state for state in all_states if state not in correct_guess]
        # for state in all_states:
        #     if state not in correct_guess:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        correct_answer = data[data.state == answer]
        x_coord = int(correct_answer.x)
        y_coord = int(correct_answer.y)
        t.goto(x_coord, y_coord)
        t.write(correct_answer.state.item())
        correct_guess.append(answer)
