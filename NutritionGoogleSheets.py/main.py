import requests
from datetime import datetime
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID="891a31fb"
API_KEY="977bfb1c8c14880c988726bbfe331ade"

sheetyapi_endpoint = "https://api.sheety.co/3b61a62c05058c0f8b42eb5daa62493b/workoutTracking/sheet1"
query = input("what did you do today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id": "0"
}
myparams= {
    "query":query, #"ran 3 miles and walked 4 miles",
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":154,
    "age":30
}

sheety_header = {
    "Authorization" : "Bearer lalalalalalaeihgeiruoqw54354522easdfde"

}


#myendpoint = f"{nutritionix_endpoint}/{USERNAME}/graphs/{GRAPHID}"
response = requests.post(url=nutritionix_endpoint, json= myparams,headers=headers)
response.raise_for_status()
data = response.json()
#print(data)
exercise_array = data["exercises"]
#print(exercise_array[1])
today = datetime.now()
DATE= today.strftime("%Y%m%d")
TIME = today.strftime("%H:%M:%S")

for val in exercise_array:
    print(val["user_input"])
    google_params= {
        "sheet1": {
            "date":DATE,
            "time":TIME,
            "exercise":val["user_input"],
            "duration":val["duration_min"],
            "calories":val["nf_calories"]
        
        }
    
    } 
    google_response = requests.post(url=sheetyapi_endpoint, json= google_params , headers=sheety_header)
    google_response.raise_for_status()
    print(google_response.status_code)

