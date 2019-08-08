import PumpingTPythons

max_run_time = 24
max_run_time = max_run_time * 60 * 60
cycle_time = 10800
thirsty_time = 600

min_moisture = 400
pump_time = 2

pump = PumpingTPythons.Schedule_Pumping()

time_run = 0
while time_run < max_run_time:
    if pump.pump_water(pump_time, min_moisture) == True:
        print("run1")
        pump.between_pumping(cycle_time)
        time_run += 10800
    elif pump.pump_water(pump_time, min_moisture) == False:
        print("run2")
        pump.between_pumping(thirsty_time)
        time_run += 600
        
    #placeholder :)
    else:
        pass

    