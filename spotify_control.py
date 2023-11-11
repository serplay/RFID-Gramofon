import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class Spotify:
    CLIENT_ID = '4ce62ad0273d45bcb66e14bb1af47343'
    CLIENT_SECRET = '022524ff98bc40ff907eba3798736d0e'
    SCOPES = 'user-read-playback-state','user-modify-playback-state','user-read-currently-playing'

    token = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uri='http://localhost:8080', scope=SCOPES, open_browser=False)
    sp = spotipy.Spotify(auth_manager=token)
    global data
    data = sp.current_playback()
    class Device:
        if data != None:
            id = data['device']['id']
            name = data['device']['name']
            support_vol=data['device']['supports_volume']
            volume=data['device']['volume_percent']
            repeat=data['repeat_state']
            shuffle=data['shuffle_state']
            is_playing=data['is_playing']
            if is_playing:
                currently_playing_album = data['item']['album']['uri']

    def set_volume(self, val):
        self.sp.volume(val)

    def control(self, val):
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

    def play_album(self, uri):
        album = self.Device.currently_playing_album
        print(f'playing {album["name"]} on device {self.Device.name}')
        #sp.start_playback(device_id=DEVICE_ID,context_uri=uri)



