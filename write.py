import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    text = input('Podaj dane na karte')
    print("Dotknij czytnik TAGiem RFID")
    reader.write(text)
    print(f'{text} zapisano na karte')
finally:
    GPIO.cleanup()