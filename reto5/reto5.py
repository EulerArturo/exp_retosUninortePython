import csv

archivo = "codigo python\data.csv"

with open('data.csv') as f:
    reader = csv.reader(f)
    for raw in reader:
        print(raw)