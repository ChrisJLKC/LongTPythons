from gpiozero import Device, Motor
from time import sleep
import spidev

bus = 0
device = 1
pump = Motor(17, 18)

pump_time = 2
cycle_time = 10800
number_of_cycles = 8

spi = spidev.SpiDev()
spi.open(bus, device)

# Settings (for example)
spi.max_speed_hz = 5000
spi.mode = 0b01

print(spi)

for i in range(1,number_of_cycles):
        pump.forward()
        sleep(pump_time)
        pump.stop()
        sleep(cycle_time)

