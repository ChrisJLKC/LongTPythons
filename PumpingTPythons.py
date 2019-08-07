from gpiozero import Motor
from time import sleep

class Schedule_Pumping:

    def __init__(self, number_of_cycles = 8, cycle_time = 10800, pump_time = 2):
        pump_time = 2
        cycle_time = 10800
        number_of_cycles = 8
        pump = Motor(17, 18)

        for _ in range(1,number_of_cycles):
            pump.forward()
            sleep(pump_time)
            pump.stop()
            sleep(cycle_time)