import csv
class CsvWriter:

    #  Initialisierung, Festlegung des Speicherorts der CSV-Datei sowie schreiben des Headers
    def __init__(self):
        self.filename='written_CSVs/mycsv.csv'
        with open(self.filename, 'w', newline='') as a:
            feldnamen= ['sensorId','timestamp','distance','unit']
            self.writer=csv.writer(a)
            self.writer.writerow(feldnamen)

    #  line: ist die bereits formatierte Zeile, die nur noch geschrieben wird.
    def write_line (self, line):
        with open(self.filename, 'a', newline='') as a:
            self.writer=csv.writer(a)
            self.writer.writerow(line)

    #  in dieser Funktion wird das übergebene Dictionary als line für die CSV-Datei formatiert
    def format_line(self, dictionary):
        line =[dictionary["sensorId"],dictionary["timestamp"],dictionary["distance"],dictionary["unit"]]
        self.write_line(line)
        return line
    
