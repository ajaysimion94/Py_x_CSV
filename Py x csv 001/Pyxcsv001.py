import csv
f=open("Py x csv 001\csv001.csv",'r')
reader=csv.reader(f)
for row in reader:
    print(row)
f.close()