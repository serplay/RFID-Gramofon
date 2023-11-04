import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = '4ce62ad0273d45bcb66e14bb1af47343'
CLIENT_SECRET = '022524ff98bc40ff907eba3798736d0e'
SCOPES = 'user-read-playback-state','user-modify-playback-state'

token = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri='http://localhost:8080', scope=SCOPES, open_browser=False)
sp = spotipy.Spotify(auth_manager=token)



def get_deviceId() -> str :
    devices = sp.devices()['devices']
    if len(devices) > 0:
        return devices[0]['id']

def get_current_album() -> str:
    data = sp.currently_playing()
    if data != None:
        album = data['item']['album']
        return album['uri']

#def set_volume(val):
    #sp.volume(val)

def control(val):
        if val == 'play':
            print(f'playing audio')
            #sp.start_playback(get_deviceId())
        elif val == 'pause':
            print(f'audio paused')
            #sp.pause_playback(get_deviceId())
        elif val =='next':
            print(f'playing next track')
            #sp.next_track(get_deviceId())
        elif val == 'previous':
            print(f'playing previous track')
            #sp.previous_track(get_deviceId())

def play_album(uri):
    album = sp.album(uri)
    print(f'playing {album["name"]} on device {DEVICE_ID}')
    #sp.start_playback(device_id=DEVICE_ID,context_uri=uri)

DEVICE_ID = get_deviceId()

