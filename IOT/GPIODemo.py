import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
try:
    while True:
            GPIO.output(5,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(5,GPIO.LOW)
            time.sleep(1)
            GPIO.output(6,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(6,GPIO.LOW)
            time.sleep(1)
            GPIO.output(12,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(12,GPIO.LOW)
            time.sleep(1)
            GPIO.output(13,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(13,GPIO.LOW)
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()