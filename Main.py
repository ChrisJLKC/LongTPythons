import PumpingTPythons

number_of_cycles = 8
cycle_time = 10800

min_moisture = 400
pump_time = 2

pump = PumpingTPythons.Schedule_Pumping

for _ in range(1,number_of_cycles):
    pump.pump_water(pump_time, min_moisture)
    between_pumping(cycle_time)
    
    