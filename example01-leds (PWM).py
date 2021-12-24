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
p = GPIO.PWM(D3, 50) #frequency = 50hz
p.start(50) #duty-cycle = 50

#interact with pins
while True:
    p.ChangeDutyCycle(10)
    time.sleep(.25)
    p.ChangeDutyCycle(20)
    time.sleep(.25)
    p.ChangeDutyCycle(30)
    time.sleep(.25)
    p.ChangeDutyCycle(40)
    time.sleep(.25)
    p.ChangeDutyCycle(60)
    time.sleep(.25)
    p.ChangeDutyCycle(80)
    time.sleep(.25)
    p.ChangeDutyCycle(100)
    time.sleep(.25)