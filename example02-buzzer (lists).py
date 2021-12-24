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
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)

#setup notes
C = 523
D = 587
E = 659
G = 784
notelist = [E,D,C,D,E,E,E,D,D,D,E,G,G,E,D,C,D,E,E,E,E,D,D,E,D,C] #mary had a little lamb

#interact with pins
while True:
    GPIO.output(D2, 1)
    GPIO.output(D3, 0)
    time.sleep(1)
    GPIO.output(D2, 0)
    GPIO.output(D3, 1)
    time.sleep(1)
    for note in notelist:
        passivebuzzer.playnote(D4, note, .5)
