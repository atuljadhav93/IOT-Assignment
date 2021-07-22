#RAS[BERRY PI BASED PROGRAM TO MEASURE TEMPERATURE AND HUMIDITY USING DHT11

#we need to import the libraries
import dht11 #keep the dht11.py in same folder for the humidity and temperature sensor 
import lcd #lcd for 16x2 lcd
import time #to use sleep function
import RPi.GPIO as GPIO # GPIO object from the RPi.GPIO library


#set pins
instance = dht11.DHT11(pin=21)#pin 21 GPIO connection input for dht11 sensor on board
#lcd connections to GPIO pins
D4=5 
D5=6
D6=12
D7=13
RS=16
EN=17

#create mylcd object
mylcd=lcd.lcd()
#initilize lcd inputs
mylcd.begin(D4,D5,D6,D7,RS,EN)

#function to display on console
def display():
    print("Temperature")
    print(result.temperature)
    print("Humidity")
    print(result.humidity)

#function to diplay on 16x2 lcd on board
def lcddisplay():    
    mylcd.clear()
    mylcd.Print("Temp: %d C " % result.temperature) 
    mylcd.setCursor(2,1)
    mylcd.Print("Humidity: %d %% " % result.humidity)
    
#clear GPIOs
def destroy():
    GPIO.cleanup()
    
#main block
if __name__ == '__main__':
    while True:
        try:
            result = instance.read() #sense the values
            time.sleep(2)            # sleep for 2 seconds   
            display()                #display the sensor values 
            lcddisplay()
            
        except KeyboardInterrupt:    # If keyboard Interrupt (CTRL-C) is pressed
            destroy()
       

   
    