import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import *
import asyncio
import sys

reader = SimpleMFRC522()
is_reading = True

id = None

GPIO.setwarnings(False)

#def read(reader):
#        global id
#            await asyncio.sleep(0.5) # we only read every 0.5 seconds to give other coroutines time to do theri thing

#async def main():
    #await asyncio.create_task(read(reader))
    

while True:
    id = reader.read_id_no_block()
    if id != None:
        wejscie = input()
    if (id not in albumy[id]) and id != None and wejscie == '1':
        albumy[id] = get_current_album()
    elif id in albumy and id != None and wejscie == '0':
        print(get_current_album, albumy[id])