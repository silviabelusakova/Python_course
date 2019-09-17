#!/usr/bin/python3

# read_csv3.py

import csv

f = open('values.csv', 'r')

with f:

    reader = csv.DictReader(f)
    
    f1, f2, f3 = reader.fieldnames
    print(f1, f2, f3)

    for row in reader:
        print(row[f1], row[f2], row[f3])

    # for col in reader:
    #     print(col[f1], col[f2], col[f3])