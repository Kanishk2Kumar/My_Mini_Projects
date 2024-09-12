import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
twilio_verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")

weather_params = {
    "lat": 18.520760,
    "lon": 73.855408,
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella today.",
        from_=twilio_virtual_number,
        to=twilio_verified_number
    )
    print(message.sid)
