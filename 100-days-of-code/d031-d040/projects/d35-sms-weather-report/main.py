import requests
from twilio.rest import Client
import os

MY_LAT = -10
MY_LONG = -66

weather_api_key = os.environ.get("WEATHER_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("WEATHER_API_KEY"),
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
                from_='+1',
                to='+5'
            )

    print(message.status)