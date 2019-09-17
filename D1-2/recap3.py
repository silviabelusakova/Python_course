#!/usr/bin/env python3
#zadanie: min,max, pocet prvkov, suma, prvy a posledny prvok vektorov

value = (7, 1, 2, 87, 6)
# value2 = (5, 7, 99, 101)

# minimum = min(value)
# maximum = max(value)
suma = sum(value)

#maximum 
maximum = value[0]

for i in value:
    if i > maximum:
        maximum = i
    
print(f'maximum je: {maximum}')

#minimum 
minimum = value[0]

for i in value:
    if i < minimum:
        minimum = i
    
print(f'minimum je: {minimum}')

print(sorted(value))
print(sorted(value, reverse=True))

# print(f'minimum je: {minimum}')
# print(f'maximum je: {maximum}')
# print(f'suma je: {suma}')
# print(f'pocet prvkov vektora je: {len(value)}')
# print(f'prvy prvok vektora je: {value[0]}')
# print(f'posledny prvok vektora je: {value[-1]}')