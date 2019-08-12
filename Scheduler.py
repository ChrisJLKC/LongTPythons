from datetime import datetime, timedelta


def Pump():
    return "pump"    

def LED():
    return "LED"

def Sensor():
    return "Sensor"

class Scheduler:
    
    def __init__(self):
        self.Schedule = []
    
    def add(self, event):
        self.Schedule.append(event)
        self.Schedule.sort(key=lambda x: x[1])


    def run(self):        
        while len(self.Schedule) > 0:
            if self.Schedule[0][1] <= datetime.now():
                self.Schedule[0][0]()
                print(self.Schedule[0][1])
                self.Schedule.pop(0)

schedule = Scheduler()
schedule.add( (Sensor, datetime.now() + timedelta(seconds=3)) )
schedule.add( (Pump, datetime.now() + timedelta(seconds=1)) )
schedule.add( (LED, datetime.now() + timedelta(seconds=2)) )
schedule.run()
schedule.run()