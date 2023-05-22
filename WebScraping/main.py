from bs4 import BeautifulSoup
import requests
#import lxml


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
article_tag = soup.find_all(name = "span", class_ = "titleline")

article_text = []
article_link = []
for key, item in enumerate(article_tag):
    text = item.text
    link = item.find('a').get("href")
    article_text.append(text)
    article_link.append(link)
    #print(f"Name: {text} and Link: {link}")

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]
#print(article_text)
#print(article_link)
#print(article_upvote)
largest_number = max(article_upvote)
location_largest = article_upvote.index(largest_number)
print(article_text[location_largest])
print(article_link[location_largest])
print(largest_number)

'''
with open("WebScraping/website.html",encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())

print(soup.find_all(name="a"))

'''

movie_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = movie_response.text
mvsoup = BeautifulSoup(movie_web_page,"html.parser")
mv_article_tag = mvsoup.find_all(name = "h3", class_ = "title")
mv_array = []
for key, value in enumerate(mv_article_tag): 
        #print(value.text)
        mv_array.append(value.getText())

movies = mv_array[::-1] #reversing order

#for n in range(len(mv_array)-1,-1,-1):
 #     print(mv_array[n])

with open("./WebScraping/test.txt", "a",encoding='utf-8') as myfile:
        for movie in movies:
              myfile.write(f"{movie}\n")

print(movies)

        
