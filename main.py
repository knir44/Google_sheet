import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT = "74"
HEIGHT = "170"
AGE = "26"

exercise_text = input("Tell me which exercies you did today? ")

APP_ID = "81592854"
API_KEY ="7061d78859ac7ac1168ce018153835b7"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

EXERCISE_PARAMS = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}



response = requests.post(url=EXERCISE_ENDPOINT,json=EXERCISE_PARAMS, headers=HEADERS)
response.raise_for_status()
result = response.json()


SHEETY_ENDPOINT = "https://api.sheety.co/2bba7ac4649ccd844f50e10c0c973659/myWorkouts/workouts"


today = datetime.now()

today_date = today.strftime("%d/%m/%Y")
now_time = today.time().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
Authorization_Header = {
    "Authorization" : os.environ["Authorization"]
}


sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=Authorization_Header)
sheety_response.raise_for_status()
sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=Authorization_Header)
sheety_response.raise_for_status()
data = sheety_response.json()