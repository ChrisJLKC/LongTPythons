import csv

class Data_Handling:
    
    def write_to_csv(self, time, moisture_level):
        row = [time, moisture_level]
        with open('data.csv', 'wt') as data_file:
           csv_writer = csv.writer(data_file)
           csv_writer.writerow(row)
        