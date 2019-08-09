import spidev

class Sensor_Control:

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 5000
        self.spi.mode = 0b01
        
    def moisture_check(self):
        moisture_level_p = self.spi.xfer([0b01100000, 0b00000000])
        moisture_ level = moisture_level_p[0] * 256) + moisture_level_p[1]
        if moisture_level < 200:
            # Code to return error
            return (moisture_level)
        else:
            return (moisture_level)
    