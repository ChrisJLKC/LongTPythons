from gpiozero import LED #Imports the LED library
from time import sleep # Imports the sleep library

led = LED(17) #Defines the pin the LED will be using (17)

led.on() #Turns the LED on
sleep(1) #Pause the process for 1 second
led.off() #Turn the LED off