import csv

path= "/home/pi/IOT_SSH/assignment2/assignment2/src/written_CSVs/hallo.csv"
file= open(path, 'w')
#reader= csv.reader(file)


data=[]

#data.append([hallo, ich, bins, da, Maurice])

writer= csv.writer(file)

writer.writerow('hallo')
