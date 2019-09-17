#!/usr/bin/python3

import re

words = ('dog', 'Dog', 'DOG', 'Doggy', 'puppy')

pattern = re.compile(r'[dog]', re.IGNORECASE)   # add ^ mark into bracket to list other than selected strings 

for word in words:
    if re.match(pattern, word):
        print('{} matches'.format(word))