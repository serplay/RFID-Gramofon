import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import *
import json
GPIO.setwarnings(False)

reader = SimpleMFRC522()
is_reading = True

id = 'None'

with open('save.json') as f:
    albumy = json.load(f)
albumy_start = dict.copy(albumy)

while True:
    id = str(reader.read_id_no_block())
    
    if id != 'None':
        wejscie = input('awaiting input: ')
    if id != 'None' and wejscie == '1':
        albumy[id] = get_current_album()
    elif (id in albumy) and wejscie == '0':
        print(get_current_album(), albumy[id])
    
    if albumy != albumy_start:
        with open('save.json','w') as f:
            json.dump(albumy,f)
