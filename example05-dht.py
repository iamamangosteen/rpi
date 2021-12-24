import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time
import passivebuzzer
import Adafruit_DHT

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

#interact with pins
while True:
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, D2)
    print("temp =", temp)
    print("humidity =", humidity)
    time.sleep(1)
