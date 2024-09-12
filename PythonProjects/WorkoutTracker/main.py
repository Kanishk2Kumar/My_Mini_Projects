import requests
import json

API_ID = "51fba839"
API_KEY = "c61ab23acde44449f82f3bf82fbb6196	—"

end_point_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "content-type": "application/json"
}
user_params = {
                 "query": "ran 3 miles",
                 "gender": "female",
                 "weight_kg": 72.5,
                 "height_cm": 167.64,
                 "age": 30
              }
response = requests.post(url=end_point_url, json=user_params, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
