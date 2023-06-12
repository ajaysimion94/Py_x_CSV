import csv,operator
data=open("Py x csv 005\csv005.csv",'r')
next(data)
sortedlist=sorted(data,key=operator.itemgetter(1))
for row in sortedlist:
    print(row)
data.close()