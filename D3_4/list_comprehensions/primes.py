#!/usr/bin/python3

no_primes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [e for e in range(2, 100) if e not in no_primes]
print (primes)