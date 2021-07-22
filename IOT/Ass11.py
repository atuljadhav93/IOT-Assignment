#Program to demonstrate DC Motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)#EN1
GPIO.setup(20,GPIO.OUT)#IN1
GPIO.setup(21,GPIO.OUT)#IN2

GPIO.cleanup()

while True:
    try:
        btn1 = GPIO.input(20)
        btn2 = GPIO.input(21)
        btn3 = GPIO.input(22)
        if btn3==True:
            GPIO.output(20,True)
            GPIO.output(21,False)
            GPIO.output(22,True)
    
    except KeyboardInterrupt:
        GPIO.cleanup()