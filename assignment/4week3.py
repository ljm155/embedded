import RPi.GPIO as GPIO # GPIO module use
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # setup 4 led pins
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
pins = [16,20,21,26]

for i in range(10): # repeat 10 times
    try:
        randPin = random.sample(pins,1) # randomly pick 1 led pin 
        print(randPin)
        GPIO.output(randPin,GPIO.HIGH) # blink led pin
        time.sleep(0.5)
        GPIO.output(randPin,GPIO.LOW)
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(16,GPIO.LOW) # turn off led pins
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.cleanup() # GPIO reset

