from gpiozero import Motor
from time import sleep


pump = Motor(17, 18)
pump.forward()

sleep(5)

pump.stop()