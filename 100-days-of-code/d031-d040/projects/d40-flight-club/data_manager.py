from dotenv import load_dotenv
import requests
import os

load_dotenv("D:/Usuarios/Usuario/ENV/.env")


class DataManager:

    def __init__(self):
        self.headers = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"}
        self.URL_PRICE = os.getenv("SHEETY_ENDPOINT_FLIGHT_PRICES")
        self.URL_USER = os.getenv("SHEETY_ENDPOINT_FLIGHT_USERS")

    def get_data(self):
        response = requests.get(url=self.URL_PRICE, headers=self.headers)
        return response.json()["prices"]

    def get_city_id(self, city):
        prices = self.get_data()
        for price in prices:
            if price["city"] == city.title():
                return price["id"]
        return

    def post_data(self, city, iata, lowprice):
        new_row = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": lowprice,
            }
        }

        requests.post(url=self.URL_PRICE, json=new_row, headers=self.headers)

    def put_data(self, city, **kwargs):
        row_id = self.get_city_id(city)
        endpoint = f"{self.URL_PRICE}/{row_id}"

        if "lowprice" in kwargs:
            edit_row = {
                "price": {
                    "iataCode": kwargs["iata"],
                    "lowestPrice": kwargs["lowprice"],
                }
            }
        else:
            edit_row = {
                "price": {
                    "iataCode": kwargs["iata"],
                }
            }

        requests.put(url=endpoint, json=edit_row, headers=self.headers)

    def new_user(self, first, last, email):

        row = {
            "user": {
            "firstName": first,
            "lastName": last,
            "email": email
            }
        }

        response = requests.post(url=self.URL_USER, json=row, headers=self.headers)
        print(response.text)



#
