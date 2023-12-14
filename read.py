import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import Spotify
import gpiozero
import json
import asyncio
from time import sleep
GPIO.setwarnings(False)

back = gpiozero.Button(14)
play = gpiozero.Button(15)
skip = gpiozero.Button(18)
fase_1 = gpiozero.OutputDevice(6)
fase_2 = gpiozero.OutputDevice(13)
fase_3 = gpiozero.OutputDevice(19)
fase_4 = gpiozero.OutputDevice(26)

async def steps():
    for x in range(4):
        if x == 0:
            fase_1.on()
            fase_2.off()
            fase_3.off()
            fase_4.off()
        if x == 1:
            fase_1.off()
            fase_2.on()
            fase_3.off()
            fase_4.off()
        if x == 2:
            fase_1.off()
            fase_2.off()
            fase_3.on()
            fase_4.off()
        if x == 3:
            fase_1.off()
            fase_2.off()
            fase_3.off()
            fase_4.on()

reader = SimpleMFRC522()
is_reading = True
spoti = Spotify()
id = 'None'

with open('save.json') as f:
    albumy = json.load(f)
albumy_start = dict.copy(albumy)
step = 0
while True:
    loop = asyncio.get_event_loop()
    data=spoti.get_data()
    if data != None:
        dev_id,name,support_vol,volume,repeat,shuffle,is_playing,currently_playing_album = data
    back.when_activated = spoti.control('previous',dev_id)
    skip.when_activated = spoti.control('next',dev_id)
    if is_playing:
        play.when_activated = spoti.control('pause',dev_id)
    else:
        play.when_activated = spoti.control('play',dev_id)
    id = str(reader.read_id_no_block())
    wejscie = 'asd'

    if id != 'None' and wejscie == '1':
        albumy[id] = currently_playing_album
    elif (id in albumy) and wejscie == '0':
        print(currently_playing_album, albumy[id])
    elif (id in albumy) and wejscie == '2':
        spoti.play_album(albumy[id])
        
    if albumy != albumy_start:
        with open('save.json','w') as f:
            json.dump(albumy,f)
    
