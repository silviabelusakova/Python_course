#!/usr/bin/env python

# arbitrary_args.py


def do_sum(*args):                                # hviezdicka, lubovolne mnozstvo argumentov zoradenych v n-tici (tuple)
    """Function returns the sum
of all values"""

    r = 0

    for i in args:
        r += i

    return r


print(do_sum.__doc__)                              # __doc__ documentation 
# print(do_sum.__name__)
print(do_sum(1, 2, 3))
print(do_sum(1, 2, 3, 4, 5))