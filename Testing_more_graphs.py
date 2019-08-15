from datetime import datetime
from matplotlib import pyplot


class Graph_Plotter:

    def __init__(self):        
        pyplot.ion()
        self.x_time, self.y_moisture, self.y_light, self.y_pump_status = [], [], [], []
        self.figure = pyplot.figure()                

    def show_graph(self, input_data):
        sensordata = (input_data[0][0], input_data[0][2], input_data[0][1])
        self.data_to_plot = [datetime.now(), *sensordata, input_data[1]]

        self.x_time.append(datetime.now())
        self.y_moisture.append   (self.data_to_plot[1])
        self.y_light.append      (self.data_to_plot[2])
        self.y_pump_status.append(self.data_to_plot[4] * 500)

        axMoisture = pyplot.subplot(211)
        pyplot.plot(self.x_time, self.y_moisture)
        pyplot.plot(self.x_time, self.y_pump_status)

        # Makes the labels invisible
        pyplot.setp(axMoisture.get_xticklabels(), visible=False)

        axLight = pyplot.subplot(212)
        pyplot.plot(self.x_time, self.y_light)        

        self.figure.canvas.draw()
