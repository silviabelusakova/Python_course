#!/usr/bin/env python

# basics.py

basket = { 'oranges': 12, 'pears': 5, 'apples': 4 }

basket['bananas'] = 5

print(basket)
print("There are {0} various items in the basket".format(len(basket)))

print(basket['apples'])
basket['apples'] = 8
print(basket['apples'])

#print(basket['plums'])

print(basket.get('oranges', 'undefined'))
print(basket.get('cherries', 'not found'))