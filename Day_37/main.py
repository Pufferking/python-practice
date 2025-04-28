# This script uses Pixela API to create a graph, add today's data, and update it.

# --- Importing necessary modules ---
import requests
from datetime import datetime

# --- User account setup ---
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "podffjvnjdjkriwosfe"
USERNAME = "adilmohammed"

# --- User registration data (for creating a new user) ---
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# --- Registering the user (only needs to be run once) ---
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# --- Graph creation setup ---
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",             # Unique graph ID
    "name": "Cycling Graph",     # Graph name
    "unit": "Km",                # Unit of measurement
    "type": "float",             # Data type
    "color": "ajisai"            # Graph color
}

headers = {
    "X-USER-TOKEN": TOKEN        # Authentication header
}

# --- Creating the graph (only needs to be run once) ---
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --- Pixel (data entry) setup ---
pixel_endpoint = f"{graph_endpoint}/graph1"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),  # Today's date in required format
    "quantity": "10",                  # Activity quantity for today
}

# --- Adding a pixel (new data for today) ---
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# --- Updating today's pixel data ---
pixel_update = {
    "quantity": "100"                  # New updated quantity
}

response = requests.put(
    url=f"{pixel_endpoint}/{today.strftime('%Y%m%d')}",
    json=pixel_update,
    headers=headers
)
print(response.text)
