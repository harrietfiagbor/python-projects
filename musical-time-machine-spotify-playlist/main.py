from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "fd00cc4ce14b42da95623b3c3cc2ffa6"
SPOTIFY_CLIENT_SECRET = "1ad53bb83c7f4c0f96899ad11ed06a27"

time_travel_date = input("Which year do you want to travel to? Type the date in this format: "
                         "YYYYMMDD\n")
billboard_song = requests.get(f"https://www.officialcharts.com/charts/singles-chart/{time_travel_date}/7501/").text
soup = BeautifulSoup(billboard_song, "html.parser")
song_titles = [song.getText().lower() for song in soup.select("div .title a")]
# print(song_titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://mysite.com/callback/",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

year = time_travel_date[:-4]
song_uris = []
for song in song_titles:
    results = sp.search(q=f"track:{song} year:{year}", type='track')
    # print(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{time_travel_date} Billboard 100", public=False)
# print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)