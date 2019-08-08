from gpiozero import Motor
from time import sleep
import spidev

class Schedule_Pumping:

    def __init__(self):
        #SPI SETUP
        self.spi = spidev.SpiDev()
        #MOTOR SETUP
        self.pump = Motor(17, 18)        
    
    def moisture_check(self):
        #Sets up the SPI values required to check moisture - returns the value as a positive integer
        spi.open(0, 0)
        spi.max_speed_hz = 5000
        spi.mode = 0b01
        moisture_level_p = spi.xfer([0b01100000, 0b00000000]) #This is the 16 bit binary number that is produced from the 8-bit chip 
        return (moisture_level_p[0] * 256) + moisture_level_p[1] #combines both 8 bit binary numbers into a 16 bit number
    
    def pump_water(self, pump_time, min_moisture):
        #Causes the device to stop/start pumping water based on the current moisture level
        if moisture_check() < min_moisture:
            pump.forward()
            sleep(pump_time)
            pump.stop()
            return True
        else:
            return False
        
    def between_pumping(self, cycle_time):
        #Begins processes which will take place between pumps
        sleep(cycle_time)
        