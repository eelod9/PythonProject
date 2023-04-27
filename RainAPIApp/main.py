import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure


#this works --->
#[Environment]::SetEnvironmentVariable('Twilio_Account_SID', 'API Key Here', 'User')

#get-childitem -Path Env:

#after update, relaunch python for os environ to detect new env
for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
account_sid = os.environ.get("Twilio_Account_SID")
auth_token = os.environ.get("Twilio_Auth_Token")

myphone = os.environ.get("myphone")
#print(f"account sid : {account_sid}, account auth: {auth_token}, myphone: {myphone}")

api_key = os.environ.get("Openweathermap_API_key")
city_name = "las vegas"
#response =  requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
parameters = {
    "lat" :36.164717,
    "lon" :-115.360225,
    "appid" : api_key
}



response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather", params=parameters)
#response = requests.get(url= "https://api.openweathermap.org/data/3.0/onecall", params=parameters)
#https://api.openweathermap.org/data/2.5/weather?lat=36.164717&lon=-115.360225&appid=92d227726d96c56450ad2a181bab1b19
#https://api.openweathermap.org/data/2.5/weather?q=London&appid=92d227726d96c56450ad2a181bab1b19
response.raise_for_status()
data = response.json()
current_weather =data["weather"][0]['main']

client = Client(account_sid, auth_token)


message = client.messages.create(
  body=f"Hello It will be {current_weather} today woohoo",
  from_="+18446540666",
  to=myphone
)
print(message.status)

