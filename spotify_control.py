import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '4ce62ad0273d45bcb66e14bb1af47343'
CLIENT_SECRET = '022524ff98bc40ff907eba3798736d0e'
SCOPES = 'user-read-playback-state'

token = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http://localhost:8080',scope=SCOPES)
sp = spotipy.Spotify(auth_manager=token)
print(sp.devices())
print(sp.user_playlists(user='serplay'))