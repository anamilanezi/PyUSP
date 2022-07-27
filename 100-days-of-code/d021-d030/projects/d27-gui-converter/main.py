import tkinter as tk

FONT = ('Consolas', 10)


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km:.2f}")


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

text_label = tk.Label(text="is equal to", font=FONT)
text_label.grid(column=0, row=1)

km_result_label = tk.Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

miles_input = tk.Entry(width=10)
miles_input.insert(1, string="0")
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = tk.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=convert, font=FONT)
button.grid(column=1, row=2)





window.mainloop()
