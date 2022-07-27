import tkinter as tk

n = 0


def button_clicks():
    global n
    n += 1
    my_label.config(text=f"Button Got Clicked {n} times")


def input_entry():
    new_text = input.get()
    my_label.config(text=f"{new_text}")


# Create a window/screen object
window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)     # Add padding (space) on window margin

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")    # my_label["text"] = "New Text"
my_label.grid(column=0, row=0)      # Grid are relative to other elements and can't be used with .pack(
# my_label.pack(side="right")       # ordered from top to bottom or left to righ
# my_label.place(x=100, y=100)      # specific position
my_label.config(padx=50, pady=50)


# Button
button = tk.Button(text="Button", command=button_clicks)
button.grid(column=1, row=1)

button_input = tk.Button(text="New Button", command=input_entry)
button_input.grid(column=2, row=0)


# Entry
input = tk.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# Keep screen open, always at the bottom of code
window.mainloop()
