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
while True:
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.output(green, 0)
