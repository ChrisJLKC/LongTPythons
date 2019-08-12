from gpiozero import Motor
from time import sleep

class Pump_Control:

    def __init__(self):
        self.pump = Motor(17, 18)
    
    def start_pump(self):
        self.pump.forward()

    def stop_pump(self):
        self.pump.stop()
