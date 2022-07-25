import turtle
import pandas

# Set the screen with img
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Create a writer turtle
writer = turtle.Turtle()
writer.hideturtle()


# Get xy coordinate of state
def get_xy(state):
    state_row = data[data.state == state]
    x = int(state_row.x)
    y = int(state_row.y)
    coordinates = (x, y)
    return coordinates


# Write the state name on map
def write_state_name():
    writer.penup()
    writer.goto(get_xy(answer_state))
    writer.write(answer_state, align='center', font=('Consolas', 8, 'bold'))


# Counter start
correct_answers = ""
count_correct = 0


# Get a list of states from csv file
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


# Ask for states until complete the list:
while count_correct < 50:

    # Ask the user for an answer
    answer_state = screen.textinput(title=f"Guess the State {correct_answers}", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # Checks if answer is in states list
    if answer_state in states_list:

        # Removes from list
        states_list.remove(answer_state)

        # Write state name on xy
        write_state_name()

        # Update correct answers count:
        count_correct += 1
        correct_answers = f"{count_correct}/50"

# Create a CSV file of missing states:
states_list_dict = {
    'States': states_list
}

# Create a dataframe with missed states names and export to a csv file
data = pandas.DataFrame(states_list_dict)
data.to_csv("states_to_learn.csv")
