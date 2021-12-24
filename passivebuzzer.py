#PASSIVE BUZZER LIBRARY
import RPi.GPIO as GPIO
import time

#playnote function takes in:
#   pin (the pin the buzzer is connected to)
#   pitch (the requency of the note to play)
#   duration (how long to play the note, in seconds)
def playnote(pin, pitch, duration):
    delay = (1.0/pitch) * 1/2
    cycles = int(duration * pitch)
    for _ in range(cycles):
        GPIO.output(pin,1)
        time.sleep(delay)
        GPIO.output(pin,0)
        time.sleep(delay)