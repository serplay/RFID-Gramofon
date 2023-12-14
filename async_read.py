import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotify_control import Spotify
import gpiozero
import json
import asyncio

GPIO.setwarnings(False)

back = gpiozero.Button(14)
play = gpiozero.Button(15)
skip = gpiozero.Button(18)
fase_1 = gpiozero.OutputDevice(6)
fase_2 = gpiozero.OutputDevice(13)
fase_3 = gpiozero.OutputDevice(19)
fase_4 = gpiozero.OutputDevice(26)
async def handle_buttons():
    while True:
        data = spoti.get_data()
        if data is not None:
            dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
            back.when_activated = spoti.control('previous', dev_id)
            skip.when_activated = spoti.control('next', dev_id)
            if is_playing:
                play.when_activated = spoti.control('pause', dev_id)
            else:
                play.when_activated = spoti.control('play', dev_id)
        await asyncio.sleep(0.1)  # Adjust the sleep duration as needed
        
async def steps():
    while True:
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
            await asyncio.sleep(0.5)  # Adjust the sleep duration as needed

async def read_nfc():
    reader = SimpleMFRC522()
    while True:
        id = str(reader.read_id_no_block())
        wejscie = 'asd'
        if id != 'None' and wejscie == '1':
            albumy[id] = currently_playing_album
        elif (id in albumy) and wejscie == '0':
            print(currently_playing_album, albumy[id])
        elif (id in albumy) and wejscie == '2':
            spoti.play_album(albumy[id])
        await asyncio.sleep(1)  # Adjust the sleep duration as needed



async def main():
    tasks = [
        asyncio.create_task(steps()),
        asyncio.create_task(read_nfc()),
        asyncio.create_task(handle_buttons())
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    albumy = {}
    albumy_start = dict.copy(albumy)
    spoti = Spotify()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()