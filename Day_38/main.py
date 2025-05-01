# This script logs exercise data using Nutritionix API and stores it in a Sheety spreadsheet.

# --- Import required modules ---
import requests
import os
from datetime import datetime

# --- Get today's date and time in required format ---
today_date = datetime.now()
today_reformatted = today_date.strftime(f"%d/%m/%Y")
today_time = today_date.strftime("%I:%M:%S")

# --- API credentials (stored as environment variables) ---
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

# --- API endpoints ---
exercise_info = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_end_point = "https://api.sheety.co/4c1877c3d6e21e69434f38eb7df206d3/workoutTracking/workouts"

# --- Ask user what exercises they did ---
user_query = input("Tell me which exercises you did ")

# --- Payload and headers for Nutritionix API ---
parameters = {
    "query": user_query
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# --- Send request to Nutritionix to get workout data ---
response = requests.post(url=exercise_info, json=parameters, headers=headers)
workout = response.json()

# --- Extract relevant exercise data from response ---
exercise = workout["exercises"][0]
exercise_name = exercise["name"]
exercise_duration = exercise["duration_min"]
exercise_burned_cal = exercise["nf_calories"]

# --- Prepare data for Sheety (Google Sheet) ---
sheety_parameters = {
    "workout": {
        "date": today_reformatted,
        "time": today_time,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_burned_cal
    }
}

# --- Auth header for Sheety API ---
headers = {
    "Authorization": f"Bearer randomtoken"
}

# --- Send data to Sheety to log the workout ---
response1 = requests.post(url=sheety_end_point, json=sheety_parameters, headers=headers)

# --- Print response status and text ---
print(response1.status_code)
print(response1.text)
