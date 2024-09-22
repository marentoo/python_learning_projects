import requests
from sms_handler import send_msg
from config.py import OMN_Endpoint, api_key


weather_params = {
    "lat":51.621441,
    "lon":-3.943646,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OMN_Endpoint, params=weather_params)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    send_msg()