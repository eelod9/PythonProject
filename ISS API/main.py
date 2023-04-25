import requests
from datetime import datetime
import smtplib
import time

my_email = "sagaciousdo2@gmail.com"
password = "ghmdstnzgftfbgxb"

MY_LAT = 36.164717
MY_LONG =-115.360225
#MY_LAT = 50
#MY_LONG =-179

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset and time_now.hour < sunrise :
          return True
    else: return False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



def checkWithinRange():
      if (MY_LAT-5 <= iss_latitude <= MY_LAT +5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5):
            return True
      else: return False
print(f"my_lat = {MY_LAT}, my_long = {MY_LONG}, \n iss_lat = { iss_latitude}, iss_long = {iss_longitude}")
while True:
    time.sleep(60)
    if (checkWithinRange() and is_night()):
            letter_body = "check the sky!!!"
            with smtplib.SMTP("smtp.gmail.com", 587, timeout= 120) as connection:
                connection.starttls() #encrypt content
                connection.login(user =  my_email, password = password )
                myMessage = f"Subject:Happy Birthday!\n\n {letter_body}"
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg= myMessage)
    else: print("Not overhead")
    