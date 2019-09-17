#!/usr/bin/env python

"""
A module containing the fibonacci
function.
"""

def fib(n):

    a, b = 0, 1
    
    while b < n:
    
        print(b, end=" ")
        (a, b) = (b, a + b)


# testing

def main():   #plati iba ak je priamo spusteny tento subor, nie ak je modul importovany a spusteny v inom subore 

    fib(500)

if __name__ == '__main__':
    main()