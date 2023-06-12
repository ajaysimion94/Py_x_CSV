import csv
csv.register_dialect("Readdialect",delimiter=",",skipinitialspace=True)
f=open("Py x csv 004\csv004.csv","r")
reader=csv.reader(f,dialect="Readdialect")
infolist=[]
for row in reader:
    infolist.append(row[2])
    print(row)
print(infolist)
f.close()