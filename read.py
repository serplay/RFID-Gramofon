import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys

reader = SimpleMFRC522()
is_reading = True

GPIO.setwarnings(False)

while is_reading:
    try:
        id, text = reader.read()
        print(f'ID :: {id}')
        print(f'TEXT :: {text}')

    except:
        GPIO.cleanup()
        sys.exit()