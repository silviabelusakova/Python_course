#!/usr/bin/env python 

#vuypisat sekv cisel od 100 do 1000

import numpy

#1 sposob
# vals = numpy.linspace(100,1000,900,dtype=int)
# print(vals)

#2
# vals2 = []
# for i in range(100,1001):
#     vals2.append(i)

# print(vals2)

# #3

# start = 100
# step = 1
# end = 1000
# i = 0
# vals3 = []

# while start + i <= end:
#     vals3.append(start +i)
#     i += 1
# print(vals3)

#4

def seq():
    
    start = 100
    end = 1000

    while start <= end:
        yield start
        start += 1

vals4 = []

for i in seq():
    vals4.append(i)
print(vals4)


