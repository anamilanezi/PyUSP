import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ('Consolas', 10, "bold")


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

    if len(website) > 0 and len(username) > 0 and len(password) > 0:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered:\n\nEmail/Username: {username}'
                                               f'\nPassword: {password}\n\nIs it ok to save?')

        if is_ok:
            with open('data.csv', mode='a') as file:
                if file.tell() == 0:
                    file.write(f"website;username;password\n")
                file.write(f"{website};{username};{password}\n")

            website_entry.delete(0, 'end')
            website_entry.insert(0, 'Website')
            username_entry.delete(0, 'end')
            username_entry.insert(0, 'Email/Username')
            password_entry.delete(0, 'end')
            password_entry.insert(0, 'Password')

    else:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")


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
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')
website_entry.focus()

username_entry = tk.Entry(font=('Consolas', 10), fg='#3c3d37')
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

password_entry = tk.Entry(font=('Consolas', 10), fg='#3c3d37')
password_entry.grid(column=1, row=3, sticky='EW')

# -------- Buttons --------- #
generate = tk.Button(text="Generate", font=('Consolas', 10), command=generate_password)
generate.grid(column=2, row=3, sticky='EW', columnspan=2)

add = tk.Button(text="Add", width=40, font=('Consolas', 10), command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky='EW')
window.mainloop()
