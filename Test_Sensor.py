import Sensor


def test_moisture_sensor_returns_int():
    moist = Sensor.Sensor_Control()
    assert type(moist.moisture_check()) is int
