#Prime Checker
import numpy as np
b = 100
c = []
for h in range(b+1):
    c += [(10**h)+1]
for g in range(b):
    u = c[g]
    i = 2
    while u % i != 0:
        i += 1
    if u > i:
        print(f"{u} is composite and its smallest non-one factor is {i}.")
    else:
        print(f"{u} is prime.")
print("lol")
