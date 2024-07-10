import os
import requests
from requests.auth import HTTPBasicAuth

POST_SHEETY = os.getenv("POST_SHEETY")


class DataManager:
    def __init__(self):
        self._user = os.getenv("username")
        self._password = os.getenv("password")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=POST_SHEETY)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    def get_prices(self):
        response = requests.get(POST_SHEETY)
        return response.json()["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{POST_SHEETY}/{city['id']}",
                json=new_data
            )
            print(response.text)


