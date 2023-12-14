import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import Spotify
import gpiozero
import json
from time import sleep
GPIO.setwarnings(False)
back = gpiozero.Button(14)
play = gpiozero.Button(15)
skip = gpiozero.Button(18)
reader = SimpleMFRC522()
is_reading = True

id = 'None'

with open('save.json') as f:
    albumy = json.load(f)
albumy_start = dict.copy(albumy)

while True:
    id = str(reader.read_id_no_block())
    wejscie = 'asd'

    if id != 'None' and wejscie == '1':
        albumy[id] = Spotify.Device.currently_playing_album
    elif (id in albumy) and wejscie == '0':
        print(Spotify.currently_playing_album, albumy[id])
    elif (id in albumy) and wejscie == '2':
        Spotify.play_album(albumy[id])
    if back.is_active:
        Spotify.control('previous')
        sleep(.2)
    if play.is_active:
        if Spotify.is_playing:
            Spotify.control('play')
            sleep(.2)
        else:
            Spotify.control('pause')
            sleep(.2)
    if skip.is_active:
        Spotify.control('next')
        sleep(.2)
        
    if albumy != albumy_start:
        with open('save.json','w') as f:
            json.dump(albumy,f)
