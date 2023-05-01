import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "AC70942087a9e08736121bcde71f2615b0"
auth_token = "17609fb9b1700ccbc5920558d154f405"
alpha_api_key = "YLJNPLNFSLX71B9B"
newsapi_key = "e59251795737440288f730e4486d2907"
## STEP 1: Use https://www.alphavantage.co
alpha_parameters= {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "YLJNPLNFSLX71B9B"
}
def get_news():
    news_parameters = {
        "q": COMPANY_NAME,
        "from": "2023-04-01",
        "sortBy": "publishedAt",
        "apiKey":  newsapi_key
    }
    news_response = requests.get(url=f"https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    new_message = ""
    for value in news_data["articles"][4:5]:
        my_title = value["title"]
        description = value["description"]
        new_message += f"{my_title} and {description}\n\n"
        
    return new_message

def send_message(mssg):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"ALERT: {STOCK} changed by {round(percentage_increase,2)}%. NEWS = {mssg} ",
        from_="+18446540666",
        to="+12149091212"
    )

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=f"https://www.alphavantage.co/query", params=alpha_parameters)
response.raise_for_status()
data = response.json()
first_2_days = list(data["Time Series (Daily)"].keys())[0:2]
today_close = float(data["Time Series (Daily)"][first_2_days[0]]["4. close"])
yesterday_close = float(data["Time Series (Daily)"][first_2_days[1]]["4. close"])
percentage_increase = (today_close-yesterday_close)/yesterday_close * 100
print(percentage_increase)
if percentage_increase >= -4:
    print("Get News")
    mssg = get_news()
    send_message(mssg)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 



    #print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

