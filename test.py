from bs4 import BeautifulSoup as bs
import requests
url = "https://www.stackoverflow.com/"

html_content = requests.get(url).text
soup = bs(html_content, "html.parser")

if soup.find('title').text is not None:
  print(soup.find('title').text)