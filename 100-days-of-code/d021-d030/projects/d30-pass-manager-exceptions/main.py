import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Consolas', 10, "bold")

# ---------------------------- FIND GENERATOR ------------------------------- #

def find_password():
    user_entry = website_entry.get()

    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No Data File Found!")
    else:
        for item in data:
            if item.lower() == user_entry.lower():
                messagebox.showinfo(title=f"{item}", message=f"Username/Email: {data[item]['username']}\n"
                                                             f"Password: {data[item]['password']}")
                pyperclip.copy(data[item]['password'])
            elif user_entry not in data:
                messagebox.showwarning(title="Oops", message=f"No details for {user_entry.title()} exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
            website: {
                    'username': username,
                    'password': password,
                    }
            }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")

    else:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


# ----- Canvas and Img ------ #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = tk.Canvas(width=200, height=200)
pass_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=0, row=0, columnspan=3)

# -------- Labels ---------- #
website_label = tk.Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, sticky='E')

username_label = tk.Label(text="Email/Username:", font=FONT)
username_label.grid(column=0, row=2, sticky='W')

password_label = tk.Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky='E')

# -------- Entries --------- #
website_entry = tk.Entry(font=('Consolas', 10), fg='#3c3d37')
website_entry.grid(column=1, row=1, sticky='EW')
website_entry.focus()

username_entry = tk.Entry(font=('Consolas', 10), fg='#3c3d37')
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

password_entry = tk.Entry(font=('Consolas', 10), fg='#3c3d37')
password_entry.grid(column=1, row=3, sticky='EW')

# -------- Buttons --------- #
search = tk.Button(text="Search", font=('Consolas', 10), command=find_password)
search.grid(column=2, row=1, sticky='EW')

generate = tk.Button(text="Generate", font=('Consolas', 10), command=generate_password)
generate.grid(column=2, row=3, sticky='EW', columnspan=2)

add = tk.Button(text="Add", width=40, font=('Consolas', 10), command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky='EW')
window.mainloop()
