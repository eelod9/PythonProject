import requests
from datetime import datetime
MY_LAT = 36.164717
MY_LONG =-115.360225
#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()
#data = response.json()["iss_position"]['longitude']
#print(data)
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0


}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#print(sunset.split("T")[1].split(":")[0])
time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)

'''
httpstatuses.com

Response codes:

1xx hold on
2xx here you go
3xx go away
4xx you screwed up
5xx I screwed up
'''