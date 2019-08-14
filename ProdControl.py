import ProdPump
import ProdSensor
import ProdData
import ProdLED
import ProdScheduler


class Control:

    def __init__(self, min_moisture):
        self.Pump_Control = ProdPump.Pump_Control()
        self.Sensor_Control = ProdSensor.Sensor_Control()
        self.Data = ProdData.Data_Handling()
        self.LED = ProdLED.LED_Control()

        self.InternalData = []
        self.min_moisture = min_moisture

        self.Schedule = ProdScheduler.Scheduler()

    def Checkup(self):
        """
        Collect Diagnostics and current state of other objects.
        Write diagnostic data to Database.
        """
        # [Sensor, Pump]
        #  Sensor -> (Moisture_Level, Tank_Level)
        #  Pump -> Pumping State

        data = []

        data.append((self.Sensor_Control.moisture_check(),
                     self.Sensor_Control.float_switch()))

        data.append(self.Pump_Control.State)

        self.Data.write_to_csv(data[0][0])
        self.InternalData = data

    def UpdateSchedule(self):
        """
        Update the schedule based on what is already scheduled,
        state of other objects and collected Diagnostics
        """

        # Schedule Pump if not currently scheduled and moisture is too low
        if not self.Schedule.isScheduled(self.Pump_Control.start_pump,
                                         self.Pump_Control.stop_pump):

            if self.InternalData[0][0] < self.min_moisture:
                self.Schedule.add(self.Pump_Control.start_pump,
                                  None, (0, 0, 1))

                self.Schedule.add(self.Pump_Control.stop_pump,
                                  None, (0, 0, 3))
            else:
                pass

        # Schedule LED Update if not currently scheduled
        if not self.Schedule.isScheduled(self.LED.green_LED, self.LED.red_LED):
            if self.InternalData[0][1]:
                self.Schedule.add(self.LED.green_LED, None, (0, 0, 1))

            else:
                self.Schedule.add(self.LED.red_LED, None, (0, 0, 1))

    def ExecuteNextTask(self):
        """
        Encapsulated way to execute next task without
        needing to go through control
        to scheduler to execute.
        """

        task = self.Schedule.nextTask()

        print(task[0])
        if task is None:
            pass

        else:
            if task[1] is not None:
                task[0](task[1])
            else:
                task[0]()


if __name__ == "__main__":
    MainController = Control(200)

    while True:

        MainController.Checkup()
        MainController.UpdateSchedule()
        MainController.ExecuteNextTask()
