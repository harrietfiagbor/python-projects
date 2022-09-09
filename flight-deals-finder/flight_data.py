
# This class is responsible for structuring the flight data.
class FlightData:

    def __init__(self, price, out_date, return_date, origin_airport, origin_city, destination_city, destination_airport,
                 stop_overs=0, via_city=""):
        self.price = price
        self.out_date = out_date
        self.return_date = return_date
        self.origin_airport = origin_airport
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.destination_airport = destination_airport

        self.stop_overs = stop_overs
        self.via_city = via_city


