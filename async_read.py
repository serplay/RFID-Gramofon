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
adder = gpiozero.Button(16)
shuffle = gpiozero.Button(23)
loop = gpiozero.Button(24)
stepper = gpiozero.DigitalOutputDevice(21)
indicator = gpiozero.LED(12)

async def handle_buttons():
    print('script working')
    while True:
        #try:
            data = spoti.get_data()
            if data is not None:
                dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
                if back.is_active:
                    spoti.control('previous', dev_id)
                if skip.is_active:
                    spoti.control('next', dev_id)
                if play.is_active:
                    if is_playing:
                        spoti.control('pause', dev_id)
                    else:
                        spoti.control('play', dev_id)
                if shuffle.is_active:
                    if shuffle:
                        spoti.control("shuffle_off",dev_id)
                    else:
                        spoti.control("shuffle_on",dev_id)
                if loop.is_active:
                    if repeat == "context":
                        spoti.control("loop_song")
                    else:
                        spoti.control("loop")
        #except Exception as e:
        #    print(e)
        #    pass
        #finally:
            await asyncio.sleep(0.01)  # Adjust the sleep duration as needed

async def steps():
    while True:
        if data is not None:
            dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
            if is_playing and not stepper.value:
                stepper.on()
            elif not is_playing and stepper.value:
                stepper.off()
        await asyncio.sleep(1)
            
async def read_nfc():
    reader = SimpleMFRC522()
    while True:
        if data is not None:
            dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
            id = str(reader.read_id_no_block())
            with open('save.json') as f:
                albumy = json.load(f)
            if adder.is_active:
                indicator.on()
                id = str(reader.read_id())
                albumy[id] = currently_playing_album
                print('przypisano')
                with open('save.json','w') as f:
                    json.dump(albumy,f)
                indicator.off()
            elif id in albumy:
                if currently_playing_album != albumy[id]:
                    spoti.play_album(albumy[id],dev_id)
                else:
                    pass
        await asyncio.sleep(1)  # Adjust the sleep duration as needed

async def main():
    while True:
        await asyncio.gather(
            handle_buttons(),
            steps(),
            read_nfc()
        )

if __name__ == "__main__":
    albumy = {}
    albumy_start = dict.copy(albumy)
    spoti = Spotify()
    indicator.blink(0.5,0.5,5)
    data = spoti.get_data()
    while data is None:
        data = spoti.get_data()
        if data is not None:
            dev_id, name, support_vol, volume, repeat, shuffle_sp, is_playing, currently_playing_album = data
    dev_id, name, support_vol, volume, repeat, shuffle_sp, is_playing, currently_playing_album = spoti.get_data()
    if shuffle_sp:
        spoti.control("shuffle_off",dev_id)
    if repeat != "context":
        spoti.control("loop",dev_id)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()