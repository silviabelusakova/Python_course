#!/usr/bin/python3

import re
import requests

resp = requests.get('http://webcode.me')

content = str(resp.content, 'utf8')


pattern = re.compile(r'(</?.*>)')

found = re.findall(pattern, content)

# print(found)

for tag in found:
    print(tag)
