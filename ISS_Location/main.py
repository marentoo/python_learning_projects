import requests
from datetime import datetime as dt

MY_LAT = 51.110550
MY_LONG = 17.025560

def is_iss_near():
    #iss code
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    iss_position = (iss_latitude, iss_longitude)
    my_pos = (MY_LAT, MY_LONG)

    #error margin +-5 to lat and long + #compare my position to iss position
    # print(f"Iss pos: {iss_position}")
    # print(f"My pos: {my_pos}")

    if -5 <= iss_latitude - MY_LAT <= 5 and -5 <= iss_longitude - MY_LONG <= 5:
        # print("jest w zasięgu")
        return True
    else:
        print("nie jest w zasięgu")

def is_night():
    #my position + sunset
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset  = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = dt.now().hour

    if time_now >=sunset or time_now <=sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_near() and is_night():
        print("look up")
    else:
        print("dont look up")