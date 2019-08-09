from gpiozero import Motor
from time import sleep

class Pump_Control:

    def __init__(self):
        self.pump = Motor(17, 18)
    
    def pump_water(self, pump_time, pump_height):
        '''
        pump_time how long the plant needs to be watered for
        pump_height the height difference between the plant and the water tank
        '''
        self.pump.forward()
        sleep(pump_time + pump_height * 10)
        self.pump.stop()
