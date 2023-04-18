import smtplib
import datetime as dt
import random


my_email = "sagaciousdo2@gmail.com"
password = "ghmdstnzgftfbgxb"
with open("./Email/quotes.txt",'r') as file:
    contents = file.readlines()
    quote = random.choice(contents)
    print(quote)
now = dt.datetime.now()

if now.weekday() == 1: 
    print("hello")
    with smtplib.SMTP("smtp.gmail.com", 587, timeout= 120) as connection:
        connection.starttls() #encrypt content
        connection.login(user =  my_email, password = password )
        myMessage = f"Subject:Quote of the day!\n\n {quote}"
        connection.sendmail(from_addr=my_email, to_addrs="sagaciousdo3@gmail.com", msg= myMessage)




