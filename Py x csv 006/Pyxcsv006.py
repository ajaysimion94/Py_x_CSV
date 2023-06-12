import csv
csv.register_dialect("read",delimiter=",",skipinitialspace=True)
f=open("Py x csv 006\csv006.csv","r")
reader=csv.DictReader(f, dialect="read")
for row in reader:
    print(row)
f.close()