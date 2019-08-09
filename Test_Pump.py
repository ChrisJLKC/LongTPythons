import PumpingTPythons

#Sample test to test tests test    
def test_moisture_level_is_positive_interger():
    pump = PumpingTPythons.Schedule_Pumping()
    result = pump.moisture_check()
    assert type(result) is int
    assert result >= 0
    
def test_pump_water_returns_boolean():
    pump = PumpingTPythons.Schedule_Pumping()
    assert type(pump.pump_water(2, 1)) is bool

    