
from bs4 import BeautifulSoup
import requests
import smtplib
from datetime import datetime 


my_email = "sagaciousdo2@gmail.com"
password = "ghmdstnzgftfbgxb"
#collected header info from https://myhttpheader.com/
header = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,ko;q=0.8",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = requests.get("https://www.amazon.com/dp/B07Q5BZFLB/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B07Q5BZFLB&pd_rd_w=rovDM&content-id=amzn1.sym.eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_p=eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_r=G63QMZ2AT84A9CH32232&pd_rd_wg=nnFSA&pd_rd_r=00751a18-2da9-4199-863e-f4ef557cdbe3&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw",headers=header)
response.raise_for_status()
web_page = response.text
#print(web_page)
#soup = BeautifulSoup(web_page,"html.parser")
soup = BeautifulSoup(web_page,"lxml")
#title = soup.select("div h1 span")
title = soup.find(id = "title")
song_names_spans = soup.find(name="span", class_="a-price-whole")
price= int(song_names_spans.text.replace('.',''))
print(price)
mytitle = title.getText().encode('utf-8').strip()

#titles = [val.getText().strip() for val in song_names_spans]
#article_tag = soup.find_all("h3", {"id": "title-of-a-story"})
today = datetime.now()
DATE= today.strftime("%Y%m%d")
letter_body = f"{mytitle} is {price} on {DATE}\n"
with open("./WebScraping/Amazon Tracker/History.txt", "a",encoding='utf-8') as myfile:
     myfile.write(letter_body)

if(price<100):
    with smtplib.SMTP("smtp.gmail.com", 587, timeout= 120) as connection:
            connection.starttls() #encrypt content
            connection.login(user =  my_email, password = password )
            myMessage = f"Subject:Price Lower!\n\n {letter_body}"
            connection.sendmail(from_addr=my_email, to_addrs="sagaciousdo@gmail.com", msg= myMessage)

