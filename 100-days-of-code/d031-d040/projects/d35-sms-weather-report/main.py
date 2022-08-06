import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

MY_LAT = float(os.getenv("my_lat"))
MY_LONG = float(os.getenv("my_long"))

# Twilio API config
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Weather API
weather_api_key = os.getenv("WEATHER_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": weather_api_key,
    "units": "metric"
}

response = requests.get(weather_endpoint, params=parameters)
response.raise_for_status()

print(f"HTTP status: {response.status_code}")

weather_data = response.json()

hourly = weather_data["hourly"]  # 0 - 48h, 0 = current time

next_12 = hourly[:12]

# Cheking only if it's going to rain at any point in next 48 hours
will_rain = False

for hour in next_12:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                body="It's going to rain today. Bring an ☔.",
                from_=os.getenv("TWILIO_NUMBER"),
                to=os.getenv("my_number")
            )

    print(message.status)
