from time import sleep
import spidev

bus = 0
device = 1

spi = spidev.SpiDev()
spi.open(bus, device)

# Settings (for example)
spi.max_speed_hz = 5000
spi.mode = 0b01

print(spi)