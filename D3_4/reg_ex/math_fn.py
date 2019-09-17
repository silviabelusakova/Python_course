#!/usr/bin/python3

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')   # r stands for a raw strings / lomitka a spatne lomitka nefunguje na odlis od spec znakov ale su vnimane ako ciste symboly  \) napr "uncle\'s dog\n\t"

for word in words:
    if re.match(pattern, word):
        print('The {} matches '.format(word))


print('***********************')

for word in words:
    if re.search(pattern, word):
        print('The {} is there'.format(word))