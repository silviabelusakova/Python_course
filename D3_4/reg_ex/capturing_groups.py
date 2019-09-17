#!/usr/bin/python3

import re

content = '''<p>The <code>Pattern</code> is a compiled
representation of a regular expression.</p>'''             #trojite uvodzovky sluzia na oznac viacriadk stringov 

pattern = re.compile(r'(</?[a-z]*>)')

found = re.findall(pattern, content)

for tag in found:
    print(tag)