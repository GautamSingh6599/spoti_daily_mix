import os
import json
import spotipy
import subprocess
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-private"

os.environ["SPOTIPY_CLIENT_ID"] = "557a384134f142b89cd0bf556f930ab0"
os.environ["SPOTIPY_CLIENT_SECRET"] = "383cb991b60b45ccb51a2213d66a7fed"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        "557a384134f142b89cd0bf556f930ab0",
        "383cb991b60b45ccb51a2213d66a7fed",
        "http://127.0.0.1:8384/",
        scope=scope,
    )
)

results = sp.current_user_playlists(limit=50)
links_list = []
for keys in results["items"]:
    links_list.append(keys["external_urls"]["spotify"])

for link in links_list:
    subprocess.run(["spotify_dl", "-l", link, "-o", "~/Music/"])
