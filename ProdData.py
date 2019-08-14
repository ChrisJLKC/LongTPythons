import csv
from datetime import datetime


class Data_Handling:

    def write_to_csv(self, moisture_level):
        row = [datetime.now(), moisture_level]
        with open('data.csv', 'a') as data_file:
            csv_writer = csv.writer(data_file)
            csv_writer.writerow(row)
