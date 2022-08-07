import datetime as dt
import requests
from dotenv import load_dotenv
import os

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph01"

# Creating an account

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph

headers = {
    "X-USER-TOKEN": TOKEN,
}


# graph_config = {
#     "id": GRAPH_ID,
#     "name": "pomodoro time",
#     "unit": "min",
#     "type": "int",
#     "color": "momiji",
# }
#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Creating a pixel /v1/users/<username>/graphs/<graphID>
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.now()
today = today.strftime("%Y%m%d")

pixel_info = {
    "date": today,
    "quantity": input("How many minutes did you study today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_info, headers=headers)
# print(response.text)

# To update or delete a pixel, we use the specific date we want to change as the endpoint
pixel_graph_endpoint = f"{pixel_endpoint}/20220805"

update_pixel = {
    "quantity": "350"
}
#
# response = requests.put(url=pixel_graph_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# Update the graph
new_graph_config = {
    "color": "shibafu",
}

response = requests.put(url=pixel_endpoint, json=new_graph_config, headers=headers)
print(response.text)