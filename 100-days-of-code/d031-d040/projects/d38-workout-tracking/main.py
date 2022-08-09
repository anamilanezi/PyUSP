import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

now = dt.datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

APP_ID = os.getenv("NUTRITIONIX_IDD")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
nutri_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_URL = os.getenv("SHEETY_ENDPOINT_WORKOUT")

exercise_text = input("Tell me which exercises you did: ")

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": exercise_text,
}

response = requests.post(url=nutri_URL, json=parameters, headers=nutri_headers)
result = response.json()
exercises = result["exercises"][0]

sheet_headers = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"}

sheet_row = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercises["user_input"].title(),
        "duration": exercises["duration_min"],
        "calories": exercises["nf_calories"]
    }
}

sheet_response = requests.post(url=sheet_URL, json=sheet_row, headers=sheet_headers)
print(sheet_response.status_code)
print(sheet_response.text)