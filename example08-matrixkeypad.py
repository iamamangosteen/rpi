import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time
import passivebuzzer
import matrixkeypad

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

while True:
    if matrixkeypad.checkKeypress() != None:
        print(matrixkeypad.checkKeypress())
    time.sleep(0.5)
