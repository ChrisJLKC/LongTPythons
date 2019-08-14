import spidev
from gpiozero import Button


class Sensor_Control:

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 5000
        self.spi.mode = 0b01

        self.button = Button(16)

    def moisture_check(self):
        moisture_level_p = self.spi.xfer([0b01100000, 0b00000000])
        moisture_level = (moisture_level_p[0] * 256) + moisture_level_p[1]
        return moisture_level

    def float_switch(self):
        if self.button.when_pressed:
            return True
        else:
            return False
