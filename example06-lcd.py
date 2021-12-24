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

#setup the LCD screen
lcd = RPi_I2C_LCD.LCD()
lcd.set_backlight(True)
lcd.clear()

#print to the screen
lcd.set_cursor(row=0)
lcd.message("LCD test")
lcd.set_cursor(row=1)
lcd.message("line 2")
