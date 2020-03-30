import sensor.distance_sensor
import csv_123.csv_writer

instanz= sensor.distance_sensor.DistanceSensor()
p=instanz.read_value()
#print(p)

#writer= csv_123.csv_writer.CsvWriter()
#writer.format_line(p)

