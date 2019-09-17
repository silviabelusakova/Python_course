#!/usr/bin/env python

# methods.py

class Obdlzik():

    def __init__(self, a=1,b=2):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b 

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b


O = Obdlzik()

print(O.area())

O.set_a(3)
O.set_b(6)

print(O.get_a())
print(O.get_b())
print(O.area())