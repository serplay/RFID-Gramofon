import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import *
import asyncio
import sys

reader = SimpleMFRC522()
is_reading = True

id = None

GPIO.setwarnings(False)
async def read(reader):
        global id
        while True:
            id = reader.read_id_no_block()
            await asyncio.sleep(0.5) # we only read every 0.5 seconds to give other coroutines time to do theri thing

async def main():
    await asyncio.create_task(read(reader))
    

asyncio.run(main())