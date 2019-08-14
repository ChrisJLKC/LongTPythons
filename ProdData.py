import csv
from datetime import datetime


class Data_Handling:

    def write_to_csv(self, data):
        row = [datetime.now(), *data[0], data[1]]
        with open('data.csv', 'a') as data_file:
            csv_writer = csv.writer(data_file)
            csv_writer.writerow(row)
