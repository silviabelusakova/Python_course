#!/usr/bin/python3

import csv

f = open('numbers.csv', 'r')

_sum = 0 

with f:

    reader = csv.reader(f, delimiter='|')
    
    for row in reader:
        for e in row:
            _sum += int(e)
print(_sum)