import requests
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
from random import choice

window = tk.Tk()

URL = "http://shibe.online/api/shibes"
parameters = {
    "count": 20,
}

response = requests.get(URL, params=parameters)
print(response.status_code)

images_list = response.json()


def pick_image(list):
    imageURL = Request(choice(list),
                       headers={'User-Agent': 'Mozilla/5.0'})
    u = urlopen(imageURL)
    raw_data = u.read()
    u.close()
    return raw_data



def change_photo():
    global photo
    doge = pick_image(images_list)
    photo = ImageTk.PhotoImage(data=doge)
    label.config(image=photo)


doge = pick_image(images_list)
photo = ImageTk.PhotoImage(data=doge)
label = tk.Label(image=photo)

# label.image = photo
label.pack()

button = tk.Button(text="Doge", command=change_photo)
button.pack()
window.mainloop()


