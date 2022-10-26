import RPi.GPIO as GPIO # GPIO module use
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # setup 4 led pins
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

while True:
    try:
        GPIO.output(16,GPIO.HIGH) # blink 4 led pins for each 1 sec
        time.sleep(1.0)
        GPIO.output(16,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(21,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(20,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(20,GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(26,GPIO.LOW)
        time.sleep(1.0)
    except KeyboardInterrupt:
        GPIO.output(16,GPIO.LOW) # turn off led pins
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.cleanup() # GPIO reset
