import csv
class CsvWriter:

    #  Initialisierung
    def __init__(self):
        with open('written_CSVs/mycsv.txt', 'w', newline='') as a:
            feldnamen= ['sensorId','timestamp','distance','unit']
            self.writer=csv.writer(a)
            self.writer.writerow(feldnamen)

    #  line: ist die bereits formatierte Zeile, die nur noch geschrieben wird.
    def write_line (self, line):
        with open('written_CSVs/mycsv.txt', 'a', newline='') as a:
            print("datei offen")
            self.writer.writerow(line)

    def format_line(self, dictionary):
        line =[dictionary["sensorId"],dictionary["timestamp"],dictionary["distance"],dictionary["unit"]]
        with open('written_CSVs/mycsv.txt', 'a', newline='') as a:
            self.writer=csv.writer(a)
            self.writer.writerow(line)
        return line
    
