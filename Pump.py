from gpiozero import Motor
from time import sleep
import Sensor

class Pump_Control:

    def __init__(self):
        self.pump = Motor(17, 18)
        sensor = Sensor.Sensor_Control()
    
    def pump_water(self, pump_time):
        '''
        pump_time how long the plant needs to be watered for
        '''
        self.pump.forward()
        while sensor.moisture_check() < min_moisture:
            sleep(0.25)
        sleep(pump_time)
        self.pump.stop()
