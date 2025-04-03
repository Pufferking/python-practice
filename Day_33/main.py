import requests
from datetime import datetime

MY_LAT = 34.083672
MY_LONG =74.797279

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0

}

response = requests.get(url="https://api.sunrise-sunset.org/json",params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)
print(data)