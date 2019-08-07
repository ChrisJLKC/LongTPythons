from gpiozero import Device
from time import sleep
import spidev

bus = 19
device = 21

spi = spidev.SpiDev()
spi.open(0, 0)

# Settings (for example)
spi.max_speed_hz = 5000
spi.mode = 0b01

while True:
    sleep(1)
    number = spi.xfer([0b01100000, 0b00000000])
    number[0] = number[0] * 256
    print(number[0] + number[1])