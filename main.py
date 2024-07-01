#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_search
import data_manager

data_manager = data_manager.DataManager()

#sheet_data = data_manager.get_prices()
# Hardcoding response from Sheety's API for the time being for testing purposes

sheet_data = [
    {
      "city": "Paris",
      "iataCode": "",
      "lowestPrice": 54,
      "id": 2
    },
    {
      "city": "Frankfurt",
      "iataCode": "",
      "lowestPrice": 42,
      "id": 3
    },
    {
      "city": "Tokyo",
      "iataCode": "",
      "lowestPrice": 485,
      "id": 4
    },
    {
      "city": "Hong Kong",
      "iataCode": "",
      "lowestPrice": 551,
      "id": 5
    },
    {
      "city": "Istanbul",
      "iataCode": "",
      "lowestPrice": 95,
      "id": 6
    },
    {
      "city": "Kuala Lumpur",
      "iataCode": "",
      "lowestPrice": 414,
      "id": 7
    },
    {
      "city": "New York",
      "iataCode": "",
      "lowestPrice": 240,
      "id": 8
    },
    {
      "city": "San Francisco",
      "iataCode": "",
      "lowestPrice": 260,
      "id": 9
    },
    {
      "city": "Dublin",
      "iataCode": "",
      "lowestPrice": 378,
      "id": 10
    }
  ]
row_id = 2
for dict in sheet_data:
    if dict["iataCode"] is None or dict["iataCode"] == "":
        dict["iataCode"] = flight_search.get_iata_code(dict["city"])
        data_manager.put_iata_code("Test", row_id)
    row_id += 1


#print(sheet_data)

