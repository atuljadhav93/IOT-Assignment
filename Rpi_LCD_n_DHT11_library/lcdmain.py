#RASPBERRY PI CODE TO DEMO TEXT ON 16X2 LCD DISPLAY

import lcd #import lcd library in the same folder
import time #import time for sleep function
import RPi.GPIO as GPIO #to use gpio on raspberry pi

#setting pins and do the same gpio connections
D4=5
D5=6
D6=12
D7=13
RS=16
EN=17

#cleanup
GPIO.cleanup()

#setting object as mylcd and initialization
mylcd=lcd.lcd()
mylcd.begin(D4,D5,D6,D7,RS,EN)

if __name__ == '__main__':
    while True:
        try:
            mylcd.clear()
            time.sleep(1)
            mylcd.Print("I am RaspberryPi") 
            time.sleep(1)
            mylcd.setCursor(2,1)
            mylcd.Print("SmartLogic")
            time.sleep(1)
            
            mylcd.clear()
            mylcd.Print("**Welcome**")
            mylcd.setCursor(2,9)
            mylcd.shift(mylcd.right,5)
            mylcd.shift(mylcd.left,5)
            
            mylcd.blinkCursorOn()
            time.sleep(2)
            mylcd.blinkCursorOff()
            mylcd.clear()
            time.sleep(2)
            
        except KeyboardInterrupt:
                #clean up of GPIOs
            GPIO.cleanup()
    