from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Motor
from time import sleep

Device.pin_factory = MockFactory()

pump = Motor(17, 18)
pump.forward()
sleep(5)
pump.stop()