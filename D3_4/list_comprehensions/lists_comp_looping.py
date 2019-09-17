#!/usr/bin/python3

a = [1, 2, 3]
b = ['A', 'B', 'C']

c = [ str(i) + j for i in a for j in b]
print(c)




# ekvivalent k pristupu lists comprehensions (s funkcionalnym progr)

# k = []

# for i in a:
#     for j in b:
#         k.append(str(i)+j)

# print(k)