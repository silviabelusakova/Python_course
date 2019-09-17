#!/usr/bin/env python3

vals = "1@2@3@4@5@6@7"

### zadanie: rozdelit string na jednotl znaky a vypisat sucet cisel

splitted = vals.split("@")
print(splitted)
_sum = 0
for i in splitted:
    _sum += int(i)
print(_sum)

