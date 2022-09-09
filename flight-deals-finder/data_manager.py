import requests
from users import Users

SHEETY_ENDPOINT = "https://api.sheety.co/d47a24e3e6d73ae30310267c44500504/flightDeals/prices"
AUTH_TOKEN_SHEETS = "THISISMYFLIGHTDEAL"
SHEETY_ENDPOINT_USERS = "https://api.sheety.co/d47a24e3e6d73ae30310267c44500504/flightDeals/users"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return response.text

    def update_destination_data(self):
        # print(self.destination_data)
        bearer_auth_header = {
            "Authorization": f"Bearer {AUTH_TOKEN_SHEETS}"
        }
        for destination in self.destination_data:
            parameters = {
                "price": {
                    "iataCode": destination["iataCode"],
                }
            }

            sheety_response = requests.put(f"{SHEETY_ENDPOINT}/{destination['id']}", json=parameters,
                                           headers=bearer_auth_header)
            print(sheety_response.text)

    def get_users(self):
        print(requests.get(SHEETY_ENDPOINT_USERS).text)

    def update_users_sheet(self):
        user = Users()
        first_name = user.first_name
        last_name = user.surname
        email = user.email

        user_parameters = {
            "user": {
                "firstName": first_name.title(),
                "lastName": last_name.title(),
                "eMail": email
            }
        }

        users_response = requests.post(f"{SHEETY_ENDPOINT_USERS}", json=user_parameters)
        print(users_response.text)

    def get_customer_emails(self):
        response = requests.get(SHEETY_ENDPOINT_USERS)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
