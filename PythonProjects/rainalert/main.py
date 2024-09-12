# import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "8b21d1d14cc49ac1043e74c9d2ff1844"

account_sid = "AC6e554281b2d2814bd12f585860df3a79"
auth_token = "6d1ed50f944f4d2810250c246ca7fe7d"

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
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"http": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token)  # , http_client=proxy_client
    message = client.messages \
                    .create(
                        body="Bring an umbrella today.",
                        from_='+12565791915',
                        to='+919359323128'
                    )
    print(message.sid)
