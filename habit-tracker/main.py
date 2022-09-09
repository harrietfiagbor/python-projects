import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "Dede3The3Developer3"
USERNAME = "harriet"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN,
}

# # Create a Pixela user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# # Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ichou",
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)

# Post a pixel
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you meditate?: "),
}
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(pixel_response.text)

# Updating a pixel
pixel_config_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
pixel_config = {
    "quantity": "12"
}
# pixel_config_response = requests.put(url=pixel_config_endpoint, json=pixel_config, headers=headers)
# print(pixel_config_response.text)

# Deleting a pixel
# pixel_delete_response = requests.delete(url=pixel_config_endpoint, headers=headers)
# print(pixel_delete_response.text)




