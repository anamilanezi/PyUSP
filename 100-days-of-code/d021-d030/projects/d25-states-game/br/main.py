import turtle
import pandas

# Set the screen with img
screen = turtle.Screen()
screen.title("Estados do Brasil")
screen.setup(width=643, height=597)
img = "Brazil_Political_Map.gif"
screen.addshape(img)
turtle.shape(img)

# Create a writer turtle
writer = turtle.Turtle()
writer.hideturtle()


# Get xy coordinate of state
def get_xy(state):
    state_row = data[data.estado == state]
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
data = pandas.read_csv("estados_capitais_br.csv")
states_list = data.estado.to_list()


#Ask for states until complete the list:
while count_correct < 27:

    # Ask the user for an answer
    answer_state = screen.textinput(title=f"Guess the State {correct_answers}", prompt="What's another state's name?").title()

    if answer_state == "Sair":
        break

    # Checks if answer is in states list
    if answer_state in states_list:

        # Removes from list
        states_list.remove(answer_state)

        # Write state name on xy
        write_state_name()

        # Update correct answers count:
        count_correct += 1
        correct_answers = f"{count_correct}/27"


# Create a CSV file of missing states:
states_list_dict = {
    'estados': states_list
}

# Create a dataframe with missed states names and export to a csv file
# data = pandas.DataFrame(states_list_dict)
# data.to_csv("estados_para_aprender.csv")

screen.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()