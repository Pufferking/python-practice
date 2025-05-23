import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# -------------------------------------
# Load environment variables from .env
# -------------------------------------
load_dotenv()

# -------------------------------------
# 1. Twilio credentials (for sending SMS)
# -------------------------------------
account_id = os.getenv("TWILIO_ACCOUNT_ID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# -------------------------------------
# 2. OpenWeatherMap API credentials and endpoint
# -------------------------------------
api_key = os.getenv("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# -------------------------------------
# 3. Location coordinates
# -------------------------------------
MY_LAT = 34.124601
MY_LONG = 74.838846

# -------------------------------------
# 4. Parameters for the API request (next 4 intervals = 12 hours)
# -------------------------------------
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,  # Get forecasts for the next 4 time intervals (3-hour steps)
}

# -------------------------------------
# 5. Send request to OpenWeatherMap
# -------------------------------------
response = requests.get(url=OWM_endpoint, params=weather_params)
weather_data = response.json()

# -------------------------------------
# 6. Check if rain is expected in any of the forecast intervals
# -------------------------------------
will_rain = False
for item in weather_data["list"]:
    weather_id = int(item["weather"][0]["id"])
    if weather_id < 700:
        will_rain = True

# -------------------------------------
# 7. If rain is expected, send SMS using Twilio
# -------------------------------------
if will_rain:
    client = Client(account_id, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Any clothes outside?",
        from_="+16672740765",  # Your Twilio phone number
        to="+918714323222",    # Recipient's phone number
    )

    print(message.status)  # Print the status of the message (e.g., queued, sent)
