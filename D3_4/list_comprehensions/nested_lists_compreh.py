#!/usr/bin/python3


# vytvorenie transponovanej matice 

M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M1_tr = [[row[i] for row in M1] for i in range(3)]
print(M1_tr)