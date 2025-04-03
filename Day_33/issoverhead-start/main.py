import requests
from datetime import datetime
import smtplib
import time

# Email credentials and location coordinates
MY_EMAIL = "test621094268@gmail.com"
MY_PASSWORD = "eaurquahylwrwobh"
MY_LAT = 34.083672
MY_LONG = 74.797279


def is_iss_overhead():
    """Check if the ISS is within ±5 degrees of the user's location."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is near the user's location
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
    """Check if it is currently nighttime at the user's location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    # Nighttime if current hour is after sunset or before sunrise
    return time_now >= sunset or time_now <= sunrise


# Main loop: Check ISS position and nighttime status every 60 seconds
while True:
    time.sleep(60)  # Wait for 1 minute before checking again
    if is_iss_overhead() and is_night():
        # Send an email alert if ISS is overhead at night
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="test62109@yahoo.com",
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
