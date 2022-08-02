import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Consolas', 10, "bold")
BACKGROUND_COLOR = "#DCD7FD"
PURPLE = "#3b319e"
BLUE = "#2B216B"


# ---------------------------- FIND GENERATOR ------------------------------- #

def find_password():
    user_entry = website_entry.get().lower()
    if len(user_entry) == 0:
        messagebox.showinfo(title="Campo vazio", message=f"Por favor, digite alguma coisa para utilizar a busca.")
        return

    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Nenhum arquivo de dados encontrado. "
                                                     "Adicione uma senha para iniciar.")
    else:
        if user_entry in data:
            username = data[user_entry]["username"]
            password = data[user_entry]["password"]
            messagebox.showinfo(title=user_entry.title(), message=f"Email:   {username}\nSenha: {password}"
                                                                  f"\n\nSenha copiada para área de transferência.")
            pyperclip.copy(data[user_entry]['password'])
        else:
            messagebox.showinfo(title="Not found", message=f"No details for {user_entry.title()} exists.")


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
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Por favor, verifique se nenhum campo está vazio antes de adicionar!")

    else:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)

                if website in data:
                    update = messagebox.askyesno("Atenção!", f"Você já possui uma senha salva para o site"
                                                             f" {website.title()}.\nGostaria de sobrescrever?")

                    if update:
                        pass
                    else:
                        return

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
window.title("Gerenciador de Senhas")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
window.iconbitmap("favicon.ico")

canvas = tk.Canvas(width=250, height=255, bg=BACKGROUND_COLOR, highlightthickness=0)
pass_img = tk.PhotoImage(file="logo-bird.png")
canvas.create_image(125, 127, image=pass_img)
canvas.grid(column=0, row=0, columnspan=3, pady=20)

# -------- Labels ---------- #
website_label = tk.Label(text="Site:", font=FONT, bg=BACKGROUND_COLOR, fg=BLUE)
website_label.grid(column=0, row=1, sticky='E')

username_label = tk.Label(text="Usuário:", font=FONT, bg=BACKGROUND_COLOR, fg=BLUE)
username_label.grid(column=0, row=2, sticky='W')

password_label = tk.Label(text="Senha:", font=FONT, bg=BACKGROUND_COLOR, fg=BLUE)
password_label.grid(column=0, row=3, sticky='E')

# -------- Entries --------- #
website_entry = tk.Entry(font=('Consolas', 10), fg=BLUE)
website_entry.grid(column=1, row=1, sticky='EW')
website_entry.focus()

username_entry = tk.Entry(font=('Consolas', 10), fg=PURPLE)
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')

password_entry = tk.Entry(font=('Consolas', 10), fg=PURPLE)
password_entry.grid(column=1, row=3, sticky='EW')

# -------- Buttons --------- #
search = tk.Button(text="Buscar",
                   font=('Consolas', 10),
                   bg=PURPLE,
                   fg='white',
                   borderwidth=1,
                   highlightthickness=0,
                   activebackground=BLUE,
                   activeforeground='white',
                   command=find_password)
search.grid(column=2, row=1, sticky='EW')

generate = tk.Button(text="Gerar senha",
                     font=('Consolas', 10),
                     bg=PURPLE,
                     fg='white',
                     borderwidth=1,
                     highlightthickness=0,
                     activebackground=BLUE,
                     activeforeground='white',
                     command=generate_password)
generate.grid(column=2, row=3, sticky='EW', columnspan=2)

add = tk.Button(text="A D I C I O N A R",
                width=40,
                bg="#988feb",
                fg='white',
                borderwidth=1,
                highlightthickness=0,
                activebackground=PURPLE,
                activeforeground='white',
                font=FONT,
                command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky='EW', pady=5)
window.mainloop()
