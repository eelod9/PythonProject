
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENTID = ""
SEC = ""
URI= "http://example.com"
timeMachine = "2007-09-09"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{timeMachine}")
response.raise_for_status()
web_page = response.text
#print(web_page)
soup = BeautifulSoup(web_page,"html.parser")
song_names_spans = soup.select("li ul li h3")
titles = [val.getText().strip() for val in song_names_spans]
#article_tag = soup.find_all("h3", {"id": "title-of-a-story"})
print(titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENTID,
        client_secret=SEC,
        redirect_uri=URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
        )
    )
                                               
results = sp.current_user() #check if auth successful
#artist = "BTS"
#track = "dynamite"
year= timeMachine.split("-")[0]
#finding = sp.search(q='artist:' + artist + ' track:' + track + ' year:' + year, type='track')
song_uris= []
for song in titles[:10]:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(len(titles))
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(titles[:10])
uid = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user = uid,
    name = f"{timeMachine} Top 10",
    public = False,
    collaborative= False

)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)