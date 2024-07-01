import os
from pprint import pprint

import requests

# AUTHORIZATION = os.getenv("AUTHORIZATION")
POST_SHEETY = os.getenv("POST_SHEETY")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def print_spreadsheet_data(self):
        # Authorization = {
        #     "Authorization": str(AUTHORIZATION),
        #     "username": os.getenv("username"),
        #     "password": os.getenv("password")
        # }
        response = requests.get(POST_SHEETY)
        # response.raise_for_status()
        print(response.text)
        pprint(response.text)

    def get_prices(self):
        response = requests.get(POST_SHEETY)
        return response.json()["prices"]

    def put_iata_code(self, iata_code, row_id):
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }
        response = requests.put(url=f"{POST_SHEETY}/{row_id}", json=params)
        print(response.text)
