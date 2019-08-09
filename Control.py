import PumpingTPythons
import SensorTPythons
from time import time, sleep

watering_time = 2
plant_height = 0.10
min_moisture = 800

time_between_water = 180

pump = PumpingTPythons.Pump_Control()
sensor = SensorTPythons.Sensor_Control()

water_needed = True
while water_needed:
    start = time()
    moisture = sensor.moisture_check()
    if moisture < 200:
        print("Moisture sensor may have failed")
        break
    elif moisture < min_moisture:
        pump.pump_water(pump_time, pump_height)
    # Write moisture level to file here
    sleep(60 - (time()-start))
    