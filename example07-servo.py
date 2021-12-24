import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time
import passivebuzzer
import Adafruit_DHT
import RPi_I2C_LCD

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

#this function converts a degree from 0-180 to a value between 2.5-12.5 for the servo
def deg(x):
    y = (x*10)/180 + 2.5
    return y

#setup pins
GPIO.setup(D4, GPIO.OUT)
servo = GPIO.PWM(D4, 50) #frequency=50
servo.start(deg(90))
    
#interact with pins
while True:
    servo.ChangeDutyCycle(deg(90)) #90 degrees
    time.sleep(1)
    servo.ChangeDutyCycle(deg(160)) #160 degrees
    time.sleep(1)
    servo.ChangeDutyCycle(deg(20)) #20 degrees
    time.sleep(1)
