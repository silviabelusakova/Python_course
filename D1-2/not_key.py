#!/usr/bin/python3

# not_kwd.py

grades = ["A", "B", "C", "D", "E", "F"]

grade = (input('insert grade: '))

if grade in grades:
   print(f"{grade} grade ")

if grade not in grades:
   print("unknown grade")