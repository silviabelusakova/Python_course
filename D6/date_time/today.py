#!/usr/bin/env python

from datetime import date

today = date.today() 

print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)
print("Weekday: ", today.weekday())

print(today)
# print(today.isocalendar())