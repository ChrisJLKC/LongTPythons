import Pump
import Sensor
from time import time, sleep

watering_time = 2
min_moisture = 800

time_between_water = 180

pump = Pump.Pump_Control()
sensor = Sensor.Sensor_Control()

water_needed = True
while water_needed:
    start = time()
    moisture = sensor.moisture_check()
    if moisture < 200:
        print("Moisture sensor may have failed")
        break
    elif moisture < min_moisture:
        pump.pump_water(pump_time)
    else:
        continue
    
    # if water_level:
    # Write moisture level to file here
    sleep(60 - (time()-start))
    