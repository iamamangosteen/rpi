import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(D3, GPIO.OUT)
p = GPIO.PWM(D3, 50) #pin=D3 frequency=50Hz
p.start(0)

while True:
	for dc in range(0, 101, 5):
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)
	for dc in range(100, -1, -5):
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)

