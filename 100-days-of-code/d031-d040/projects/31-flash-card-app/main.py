import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

flip_timer = None

# --------------------------------------- DATA --------------------------------------- #
df = pd.read_csv("data/french_words.csv")
# Orient creates a list of dictionaries
words_to_learn = df.to_dict(orient="records")


# dictionary = {row.French: row.English for (index, row) in df_dictionary.iterrows()}

# fr_word, en_word = random.choice(list(dictionary.items()))
# print(fr_word)


# ------------------------------------ FUNCTIONS ------------------------------------- #

def change_word():

    global flip_timer
    try:
        window.after_cancel(flip_timer)
    except ValueError:
        pass

    random_word = random.choice(words_to_learn)
    fr_word = random_word['French']

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=fr_word, fill="black")

    en_word = random_word['English']
    flip_timer = window.after(4000, flip_card, en_word)


def flip_card(word):
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)



# ---------------------------------------- UI ---------------------------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -------------- Canvas -------------- #

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ------------- Buttons ------------- #

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=change_word)
wrong_button.grid(column=0, row=1)

right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, borderwidth=0, command=change_word)
right_button.grid(column=1, row=1)

# Calling the function to pick a random word to start
change_word()

window.mainloop()
