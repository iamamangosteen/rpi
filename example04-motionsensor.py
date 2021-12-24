import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time
import passivebuzzer

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
GPIO.setup(D2, GPIO.IN)

while True:
    mylist = []
    for _ in range(5):
        mylist.append(GPIO.input(D2))
    if 1 in mylist:
        print("activated")
    else:
        print("not activated")
