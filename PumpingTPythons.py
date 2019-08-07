from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Motor
from time import sleep

Device.pin_factory = MockFactory()

pump_time = 2
cycle_time = 10800
number_of_cycles = 8

for i in range(1,number_of_cycles):
        pump = Motor(17, 18)
        pump.forward()
        sleep(pump_time)
        pump.stop()
        sleep(cycle_time)
