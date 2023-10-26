import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = '4ce62ad0273d45bcb66e14bb1af47343'
CLIENT_SECRET = '022524ff98bc40ff907eba3798736d0e'
SCOPES = 'user-read-playback-state','user-modify-playback-state'

token = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri='http://localhost:8080', scope=SCOPES)
sp = spotipy.Spotify(auth_manager=token)


def get_deviceId():
    devices = sp.devices()['devices']
    if len(devices) > 0:
        return devices[0]['id']

def get_current_album():
    data = sp.currently_playing()
    if data != None:
        album = data['item']['album']
        return album['uri']

def set_volume(val):
    sp.volume(val)

def control(val):
        if val == 'play':
            sp.start_playback(get_deviceId())
        elif val == 'pause':
            sp.pause_playback(get_deviceId())
        elif val =='next':
            sp.next_track(get_deviceId())
        elif val == 'previous':
            sp.previous_track(get_deviceId())

def play_album(uri):
    sp.start_playback(device_id=DEVICE_ID,context_uri=uri)

DEVICE_ID = get_deviceId()
albumy = {}

print(f'''{get_deviceId()}
{get_current_album()}''')