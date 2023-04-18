import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day

my_email = "sagaciousdo2@gmail.com"
password = "ghmdstnzgftfbgxb"
data = pandas.read_csv("./BirthdayWisher/birthdays.csv")

foundBdayPerson=data.loc[(data['month']==today_month) & (data['day'] ==today_day)]
if not foundBdayPerson.empty:
    bday_email = foundBdayPerson["email"].to_string(index=False)
    bday_name = foundBdayPerson["name"].to_string(index=False)
    print(bday_name)
    choice = random.randint(1,3)
    filename = f"./BirthdayWisher/letter_templates/letter_{choice}.txt"
    with open(filename) as file:
        temp= file.read()
        #global letter_body
        letter_body  = temp.replace("[NAME]",bday_name)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout= 120) as connection:
        connection.starttls() #encrypt content
        connection.login(user =  my_email, password = password )
        myMessage = f"Subject:Happy Birthday!\n\n {letter_body}"
        connection.sendmail(from_addr=my_email, to_addrs=bday_email, msg= myMessage)
        





#print(f"Hello {bday_email} and {bday_name}")






