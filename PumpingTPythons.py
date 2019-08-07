from gpiozero import Motor
from time import sleep
import spidev

class Schedule_Pumping:

    def __init__(self, number_of_cycles = 8, cycle_time = 10800, pump_time = 2, min_moisture = 100):
        
        bus = 19
        device = 21
        spi = spidev.SpiDev()
        spi.open(0, 0)
        spi.max_speed_hz = 5000
        spi.mode = 0b01
        
        pump = Motor(17, 18)        
        
        moisture_level_p = spi.xfer([0b01100000, 0b00000000])
        moisture_level = (moisture_level_p[0] * 256) + moisture_level_p[1]

        for _ in range(1,number_of_cycles):
            if moisture_level < min_moisture:
                pump.forward()
                sleep(pump_time)
                pump.stop()
            sleep(cycle_time)