import math
import requests
from BeautifulSoup import BeautifulSoup

print("hello")
#testing
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"
response = request(target_url)
print(response.content)
    