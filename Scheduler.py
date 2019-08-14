import Sensor
import Pump
import Data
import LED
from datetime import datetime, timedelta


class Scheduler:

    def __init__(self):
        self.Schedule = []

        self.sensor = Sensor.Sensor_Control()
        self.get_moisture = self.sensor.moisture_check
        self.tank_button = self.sensor.float_switch

        self.pump = Pump.Pump_Control()
        self.start_pump = self.pump.start_pump
        self.stop_pump = self.pump.stop_pump

        self.data = Data.Data_Handling()
        self.write = self.data.write_to_csv

        self.led = LED.LED_Control()
        self.green_led = self.led.green_LED
        self.red_led = self.led.red_LED

        self.pump_running = 0
        self.min_moisture = 500

    def add(self, event):
        self.Schedule.append(event)
        self.Schedule.sort(key=lambda x: x[1])

    def Check_tank_level(self):
        if self.tank_button:
            self.green_led
        else:
            self.red_led
        self.add((Schedule.Check_tank_level, datetime.now()
                  + timedelta(seconds=2)))

    def Check_need_Pump(self):
        moisture = self.get_moisture()
        if moisture < self.min_moisture and self.pump_running = 0:
            self.add((self.Pump, datetime.now() + timedelta(seconds=1)))
            self.add((self.Check_need_Pump, datetime.now()
                      + timedelta(seconds=1)))

        elif moisture < self.min_moisture and self.pump_running == 1:
            self.add((self.Check_need_Pump, datetime.now()
                      + timedelta(seconds=0.25)))

        elif moisture > self.min_moisture and self.pump_running == 1:
            self.add((self.Pump, datetime.now() + timedelta(seconds=2)))
            self.add((self.Check_need_Pump, datetime.now()
                      + timedelta(seconds=20)))
        else:
            self.add((self.Check_need_Pump, datetime.now()
                      + timedelta(seconds=10)))

    def Pump(self):
        if self.pump_running == 1:
            self.stop_pump()
            self.pump_running = 0
        else:
            self.start_pump()
            self.pump_running = 1

    def Write(self):
        self.write(datetime.now(), self.get_moisture())
        self.add((self.Write, datetime.now() + timedelta(seconds=10)))

    def run(self):
        while len(self.Schedule) > 0:
            if self.Schedule[0][1] <= datetime.now():
                print(self.Schedule[0][0])
                self.Schedule[0][0]()
                print(self.Schedule[0][1])
                self.Schedule.pop(0)
                print(self.get_moisture())
                print(self.pump_running)


if __name__ == '__main__':
    Schedule = Scheduler()
    Schedule.add((Schedule.Check_need_Pump, datetime.now()
                  + timedelta(seconds=1)))

    Schedule.add((Schedule.Write, datetime.now()))
    Schedule.add((Schedule.Check_tank_level, datetime.now()))
    Schedule.run()
