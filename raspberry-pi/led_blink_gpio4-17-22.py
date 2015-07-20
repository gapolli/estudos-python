import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red = 4
yellow = 17
green = 22
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red, 1)
time.sleep(5)
GPIO.output(red, 0)
GPIO.output(yellow, 1)
time.sleep(5)
GPIO.output(yellow, 0)
GPIO.output(green, 1)
time.sleep(5)
GPIO.output(green, 0)
