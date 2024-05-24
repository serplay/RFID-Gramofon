import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

class Spotify:
    CLIENT_ID = 'PUT YOUR ID HERE'
    CLIENT_SECRET = 'PUT YOUR SECRET HERE'
    SCOPES = 'user-read-playback-state','user-modify-playback-state','user-read-currently-playing'

    token = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uri='http://localhost:8080', scope=SCOPES, open_browser=False)
    sp = spotipy.Spotify(auth_manager=token)


    def get_data(self):
        data = self.sp.current_playback()
        if data != None:
            dev_id = data['device']['id']
            name = data['device']['name']
            support_vol=data['device']['supports_volume']
            volume=data['device']['volume_percent']
            repeat=data['repeat_state']
            shuffle=data['shuffle_state']
            is_playing=data['is_playing']
            currently_playing_album = data['item']['album']['uri']
            return dev_id,name,support_vol,volume,repeat,shuffle,is_playing,currently_playing_album
        return None
    
    def set_volume(self, val):
        self.sp.volume(val)

    def control(self, val, dev_id):
            if val == 'play':
                print(f'playing audio')
                self.sp.start_playback(dev_id)
            elif val == 'pause':
                print(f'audio paused')
                self.sp.pause_playback(dev_id)
            elif val =='next':
                print(f'playing next track')
                self.sp.next_track(dev_id)
            elif val == 'previous':
                print(f'playing previous track')
                self.sp.previous_track(dev_id)
            elif val == "shuffle_on":
                self.sp.shuffle(True,dev_id)
            elif val == "shuffle_off":
                self.sp.shuffle(False)
            elif val == "loop_song":
                self.sp.repeat("track")
            elif val == "loop":
                self.sp.repeat("context")

    def play_album(self, uri,dev_id):
        self.sp.start_playback(device_id=dev_id,context_uri=uri)
