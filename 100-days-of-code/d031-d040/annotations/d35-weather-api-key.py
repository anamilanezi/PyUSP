import requests
import statistics
from math import floor

MY_LAT = -11 # -28.637039
MY_LONG = -66 #-49.498371
WEATHER_KEY = "key"

URL = "https://api.openweathermap.org/data/2.5/onecall"

conditions_id = {
    "thunderstorm": range(200, 233),
    "drizzle": range(300, 322),
    "rain": range(500, 532),
    "snow": range(600, 623),
    "clear": [800],
    "clouds": range(801, 805)
}

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": WEATHER_KEY,
    "units": "metric"
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

print(f"HTTP status: {response.status_code}")

weather_data = response.json()
# print(weather_data)

# ----- Check if it will rain in the next 12 hours ----- #

hourly = weather_data["hourly"]         # 0 - 48h, 0 = current time

next_12 = hourly[:12]
id_for_next_12 = []

# Some alternatives for the same problem:

# Cheking only if it's going to rain at any point in next 48 hours
will_rain = False

for hour in next_12:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")

# Get the weather condition for each hour using an id dictionary
for hour in next_12:
    weather_id = hour['weather'][0]['id']
    id_for_next_12.append(weather_id)

if min(id_for_next_12) < 700:
    print("Bring an umbrella!")

median_id = statistics.median(id_for_next_12)
print(median_id)

for condition in conditions_id:
    if floor(median_id) in conditions_id[condition]:
        print(f"The most prevalent weather condition for the next 12 hours is: {condition.title()}")


# for condition in conditions_id:
#     if min(id_for_next_12) in conditions_id[condition]:
#         print(condition)

# for id in id_for_next_12:
#     for condition in conditions_id:
#         if id in conditions_id[condition]:
#             # print(condition)


# Without excluding daily data for a week:
# week_daily = weather_data["daily"]
# for day in data["daily"]:
#     min = day["temp"]["min"]
#     max = day["temp"]["max"]
#     print(f"Min: {min}\nMax: {max}")


