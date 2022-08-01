import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


# --------------------------------------- DATA --------------------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    words_to_learn = df.to_dict(orient="records") # Orient creates a list of dictionaries
random_word = {}

print(len(words_to_learn))


# ------------------------------------ FUNCTIONS ------------------------------------- #

def known_word():

    words_to_learn.remove(random_word)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def change_word():

    global random_word, flip_timer

    window.after_cancel(flip_timer)

    random_word = random.choice(words_to_learn)
    fr_word = random_word['French']

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=fr_word, fill="black")

    flip_timer = window.after(3500, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word['English'], fill="white")
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
right_button = tk.Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_word)
right_button.grid(column=1, row=1)

# Calling the function to pick a random word to start
flip_timer = window.after(3500, flip_card)
change_word()

window.mainloop()
