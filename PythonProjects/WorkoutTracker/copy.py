import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"
AGE = "50"

API_ID = os.getenv("NUTRITIONIX_API_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)
