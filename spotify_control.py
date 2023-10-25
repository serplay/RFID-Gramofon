import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '4ce62ad0273d45bcb66e14bb1af47343'
CLIENT_SECRET = '022524ff98bc40ff907eba3798736d0e'
SCOPES = 'user-read-playback-state'

token = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri='http://localhost:8080', scope=SCOPES)
sp = spotipy.Spotify(auth_manager=token)


def get_device():
    return sp.devices()['devices'][0]['id'], sp.devices()['devices'][0]['name']


def get_current_album():
    data = sp.currently_playing()['item']
    album = data['album']
    track = data['name']
    return album['name'], album['uri'], track

print(f'''{get_device()}
{get_current_album()}''')