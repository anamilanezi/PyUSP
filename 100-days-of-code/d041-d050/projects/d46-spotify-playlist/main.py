import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, 'html.parser')

raw_playlist = soup.find_all(name="li", class_="o-chart-results-list__item")

songs = []
for song in raw_playlist:
    title = song.find(name="h3", class_="c-title", id="title-of-a-story")
    if title is None:
        continue
    else:
        songs.append(title.getText().replace("\n", "").replace("\t", ""))

print(songs)

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False, description=f'Billboard 100 songs from {date}')
playlist_id = playlist['id']

sp.user_playlist_change_details(user_id, playlist_id, public=False,)

sp.user_playlist_add_tracks(user_id, playlist_id, song_uris, position=None)

