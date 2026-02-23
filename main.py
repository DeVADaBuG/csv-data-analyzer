import csv
from io import StringIO

data = "name,age\nAlice,30\nBob,25"
f = StringIO(data)
reader = csv.reader(f)
next(reader)
ages = [int(row[1]) for row in reader]
print(f"Average age: {sum(ages)/len(ages)}")
