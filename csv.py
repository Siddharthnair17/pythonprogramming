import csv
with open('emp.csv',newline=' ')as csvfile:
 data=csv.reader(csvfile,delimeter=' ',quotechar='|')
 for row in data:
    print(','.join(row))
