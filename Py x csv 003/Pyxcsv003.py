import csv
csv.register_dialect('myDialect',delimiter='|',skipinitialspace=True)
f=open("Py x csv 003\csv003.csv","r")
reader=csv.reader(f,dialect="myDialect")
for row in reader:
    print (row[0],row[1])
f.close()