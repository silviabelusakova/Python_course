#!/usr/bin/env python

# defining.py


class Some():

    @staticmethod
    def f():
        print("f() method")


def f():
    print("f() function")


def g():
    def f():
        print("f() inner function")
    #     return 5
    # x = f()
    # return x


Some.f()
f()
# val = g()
# print(val)
g()