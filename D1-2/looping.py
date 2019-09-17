#!/usr/bin/env python

# looping.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway" }

for key in domains:
    print(key)
print('*******************************')
for val in domains.values():
    print(val)
print('*******************************')
for key, value in domains.items():
    # print(": ".join((k, v)))
    # print(key, value)
    print(f'{key}: {value}')