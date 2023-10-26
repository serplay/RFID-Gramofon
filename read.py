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
    if get_current_album() != albumy[id] and id != None:
        print(get_current_album())