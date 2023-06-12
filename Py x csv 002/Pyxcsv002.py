import csv
with open("Py x csv 002\csv002.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
f.close()