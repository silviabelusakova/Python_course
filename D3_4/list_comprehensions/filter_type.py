#!/usr/bin/python3

a = ['a', 2, 'c', 12, 3, 'd']

b = [e for e in a if type(e) == int]
c = [e for e in a if type(e) == str]

print(b)
print(c)
