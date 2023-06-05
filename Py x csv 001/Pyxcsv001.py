import csv
f=open("Py x csv 001\csv001.csv",'r')
reader=csv.reader(f)
row=list(reader)
print(row)
f.close()