import csv
data=[['Student','Year'],['Ajay','III'],['Bose','II'],['Syed','III']]
f=open("Py x csv 007\csv007.csv",'w')
writer=csv.writer(f)
writer.writerows(data)
f.close()
dis=open("Py x csv 007\csv007.csv",'r')
reader=csv.reader(dis)
for row in reader:
    print(row)
dis.close()
Adddata=[['Abisha','III'],['Akshaya','III']]
f=open("Py x csv 007\csv007.csv",'a')
writer=csv.writer(f)
writer.writerows(Adddata)
f.close()
dis=open("Py x csv 007\csv007.csv",'r')
reader=csv.reader(dis)
for row in reader:
    print(row)
dis.close()