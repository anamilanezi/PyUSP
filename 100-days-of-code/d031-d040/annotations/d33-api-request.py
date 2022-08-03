import requests

MY_LAT = -25
MY_LONG = -45

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
#
#
# # If any error occurs, we can catch it using raise_for_status.
# response.raise_for_status()
#
# # Get data from json
# data = response.json()
# print(data)
#
# # Get specific key from json:
# longitude = response.json()["iss_position"]["longitude"]
# # or
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# API that takes parameters

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()