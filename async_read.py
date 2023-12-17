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
fase_1 = gpiozero.OutputDevice(6)
fase_2 = gpiozero.OutputDevice(13)
fase_3 = gpiozero.OutputDevice(19)
fase_4 = gpiozero.OutputDevice(26)

async def handle_buttons():
    print('script working')
    while True:
        global data
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
        await asyncio.sleep(0.1)  # Adjust the sleep duration as needed

#async def steps():
#    while True:
#        if data is not None:
#            dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
#            if is_playing:
#                for x in range(4):
#                    if x == 0:
#                        fase_1.on()
#                        fase_2.off()
#                        fase_3.on()
#                        fase_4.off()
#                    if x == 1:
#                        fase_1.off()
#                        fase_2.on()
#                        fase_3.on()
#                        fase_4.off()
#                    if x == 2:
#                        fase_1.off()
#                        fase_2.off()
#                        fase_3.on()
#                        fase_4.off()
#                    if x == 3:
#                        fase_1.off()
#                        fase_2.off()
#                        fase_3.off()
#                        fase_4.on()
#                    await asyncio.sleep(0.01)  # Adjust the sleep duration as needed
#            else:
#                await asyncio.sleep(1)
#        else:
#            await asyncio.sleep(1)

async def read_nfc():
    reader = SimpleMFRC522()
    while True:
        if data is not None:
            dev_id, name, support_vol, volume, repeat, shuffle, is_playing, currently_playing_album = data
            id = str(reader.read_id_no_block())
            with open('save.json') as f:
                albumy = json.load(f)
            if id != 'None' and adder.is_active:
                albumy[id] = currently_playing_album
                print('przypisano')
                with open('save.json','w') as f:
                    json.dump(albumy,f)
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
            #steps(),
            read_nfc()
        )

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