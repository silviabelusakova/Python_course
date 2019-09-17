#!/usr/bin/env python

from pathlib import Path
from shutil import copyfile

source = Path('words.txt')
destination = Path.home() / Path('words_bck.txt')

print(source)
print(source.absolute())
print(destination)

#copyfile(source, destination)