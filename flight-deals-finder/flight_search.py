import os
import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
DEPARTURE_AIRPORT_CODE = "LON"
CURRENCY = "GBP"
HEADER = {
    "apikey": os.getenv("TEQUILA_API_KEY")
}


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_city_code(self, name_of_city):
        print("get destination codes triggered")
        location_parameters = {
            "term": name_of_city,
            "location_types": "city",
        }
        locations_response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=location_parameters,
                                          headers=HEADER)
        city_code = locations_response.json()["locations"][0]["code"]
        self.city_codes.append(city_code)
        return city_code

    def get_flight(self, origin_airport_code, destination_airport_code, from_time, to_time):
        print(f"Check flights triggered for {destination_airport_code}")
        header = {
            "apikey": os.getenv("TEQUILA_API_KEY"),
        }
        search_parameters = {
            "fly_from": origin_airport_code,
            "fly_to": destination_airport_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURRENCY,
        }

        search_response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=search_parameters, headers=HEADER)

        try:
            data = search_response.json()["data"][0]
        except IndexError:

            search_parameters["max_stopovers"] = 1

            search_response_again = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=search_parameters,
                                                 headers=HEADER)
            try:
                data = search_response_again.json()["data"][0]
                pprint(data)
            except IndexError:
                print("No stop overs. mmmm")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_airport=data["route"][0]["flyTo"],
                    origin_city=data["route"][0]["cityFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][0]["local_arrival"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_airport=data["route"][0]["flyTo"],
                origin_city=data["route"][0]["cityFrom"],
                destination_city=data["route"][0]["cityTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_arrival"].split("T")[0]
            )
            # print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data






