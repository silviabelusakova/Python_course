#!/usr/bin/env python 

# list all the .py files while the directory 

import sys 

import os 

if len(sys.argv) !=2:
    print('Usage: list_files.py , dir_name')
    sys.exit(1)

dir_name = sys.argv[1]

gfiles =os.walk(dir_name)

for (root, dir, files) in gfiles:

    for file in files:
        if file.endswith('py'):
            print(file)
