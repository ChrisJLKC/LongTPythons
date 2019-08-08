import PumpingTPythons

number_of_cycles = 8
cycle_time = 10800
thirsty_time = 600 

min_moisture = 400
pump_time = 2

pump = PumpingTPythons.Schedule_Pumping

for _ in range(1,number_of_cycles):
    if pump.pump_water(pump_time, min_moisture) == True:
        between_pumping(cycle_time)
    elif pump.pump_water(pump_time, min_moisture) == False:
        between_pumping(thirsty_time)
    
    #placeholder :)
    else:
        pass
    