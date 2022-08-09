from dotenv import load_dotenv
import requests
import os
import datetime as dt
from pprint import pprint

load_dotenv("D:/Usuarios/Usuario/ENV/.env")


class FlightSearch:

    def __init__(self):

        self.header = {
            "apikey": os.getenv("FLIGHT_API_KEY")
        }

    def find_code(self, city):
        URL = "https://tequila-api.kiwi.com/locations/query"

        params = {
            "term": city,
            "location_types": "airport"
        }

        response = requests.get(url=URL, params=params, headers=self.header)
        data = response.json()
        code = data['locations'][0]['id']

        return code

    def find_price(self, fly_from, fly_to):

        today = dt.datetime.now()
        tomorrow = (today + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (today + dt.timedelta(days=180)).strftime("%d/%m/%Y")

        URL = "https://tequila-api.kiwi.com/v2/search"

        params = {
            "fly_from": self.find_code(fly_from),
            "fly_to": self.find_code(fly_to),
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 2,
            "flight_type": "round",
            "curr": "BRL",
        }

        response = requests.get(url=URL, params=params, headers=self.header)
        try:
            return response.json()["data"][0]
        except IndexError:
            return None

