#!/usr/bin/env python3

number = 0
text = 0
space = 0
other = 0

with open ('data.txt') as f:

    lines = f.readlines()
    print(lines)

for line in lines:

    for char in line:

        if char.isalpha():
            text +=1
        elif char.isdigit():
            number +=1
        elif char.isspace():
             space +=1
        else:
             other +=1
print(f'There are {text} alphanumerical characters, {number} numbers {space} space characters and {other} other characters ')