from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from users import Users
from pprint import pprint
from datetime import datetime, timedelta

DEPARTURE_AIRPORT_CODE = "LON"

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data_manager = DataManager()
data_manager.get_destination_data()
sheet_data = data_manager.destination_data
# pprint(sheet_data)

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_months_from_now = today + timedelta(days=6 * 30)

for city_data in sheet_data:
    search_flight = FlightSearch()
    # # populate sheet with city code
    # print(search_flight.get_city_code(city_data["city"]))
    # if city_data["iataCode"] == "":
    #     city_data["iataCode"] = search_flight.get_city_code(city_data["city"])

    # # updating the sheets with the city data
    # data_manager.update_destination_data()

    # getting flight price
    flight = search_flight.get_flight(
        origin_airport_code=DEPARTURE_AIRPORT_CODE,
        destination_airport_code=city_data["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now
    )

    if flight is None:
        continue

    message = None
    if city_data["lowestPrice"] > flight.price:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        ######################
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        print(message)
        #######################

    users = data_manager.get_customer_emails()
    emails = [row["eMail"] for row in users]
    names = [row["firstName"] for row in users]
    link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}" \
           f".{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date} "

    notification_manager = NotificationManager()
    notification_manager.send_emails(emails=emails, message=message, google_flight_link=link)
