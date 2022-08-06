import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen, Request

root = tk.Tk()

imageURL = Request("https://cdn.shibe.online/shibes/108256a873b601241c80a1d33cc469dae6927b90.jpg", headers={'User-Agent': 'Mozilla/5.0'})
u = urlopen(imageURL)
raw_data = u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = tk.Label(image=photo)

label.image = photo
label.pack()

root.mainloop()