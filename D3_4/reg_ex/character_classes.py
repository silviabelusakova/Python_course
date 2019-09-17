#!/usr/bin/python3

import re

# words = ('a gray bird', 'grey hair', 'great look')
words = ('deep', 'leak','look', 'meet', 'seen','seed', 'good')

pattern = re.compile(r'[^oe]{2}') # [^xy] neobsahuje, negacia hladaneho kriteria 

for word in words:
    if re.search(pattern, word):
        print('{} matches'.format(word))   