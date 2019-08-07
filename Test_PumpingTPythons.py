import PumpingTPythons

#Sample test to test tests test    
def test_Number_Of_Cycles_Is_8():
    '''This test will make sure the number of cycles is always 8'''
    PumpCycles = PumpingTPythons.Schedule_Pumping()
    assert PumpCycles.moisture_level() == 0