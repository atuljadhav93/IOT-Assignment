import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def blink(led):
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)
    
def destroy():
    GPIO.cleanup()

if __name__=='__main__':
    try:
        while True:
            blink(5)
            blink(6)
    except KeyboardInterrupt:
        destroy()