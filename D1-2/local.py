#!/usr/bin/env python

# local_variable.py

name = "Jack"


def f():
    name = "Robert"
    print("Within function", name)


print("Outside function", name)
f()