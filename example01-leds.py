import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

#pin map
D2 = 17
D3 = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
D8 = 25
D9 = 4
D10 = 8
A3 = 7

#setup pins
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)

#interact with pins
while True:
    GPIO.output(D2, 1)
    GPIO.output(D3, 0)
    time.sleep(1)
    GPIO.output(D2, 0)
    GPIO.output(D3, 1)
    time.sleep(1)
