import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json

# https://getsongbpm.com/api

load_dotenv()

URI = "https://localhost:8888"
SCOPE = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=URI,
    scope=SCOPE
))

# kendrick_uri = "spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg"
# results = sp.artist_albums(kendrick_uri, album_type='album')
# albums = results["items"]
# for album in albums:
#     print(album['name'])

results = sp.current_user_saved_tracks(limit=1)
liked_songs = []
for idx, item in enumerate(results['items']):
    song = {}

    track = item['track']
    song['artists'] = [artist['name'] for artist in track['artists']]
    song['title'] = track['name']
    song['album'] = track['album']['name']
    song['uri'] = track['uri'].split(':')[-1]
    
    liked_songs.append(song)