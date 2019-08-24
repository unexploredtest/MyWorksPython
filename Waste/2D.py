# How to solve 2 degree polymiol
# x^2 - 5x + 6 = 0

import numpy as np

i = 0.0
dx = 1.0

iss = [0.0]

while abs(i**2 - i + 1) > 0.000001:
    d = i**2 - 10*i + 1
    if d > 0:
        if len(iss) > 1:
            if iss[i] == iss[i-2]:
                dx = (abs(dx) / 2
            else:
                dx = (abs(dx))

    i = dx + i
    iss.append(i)

        # print(dx)
    print(i)

    elif d < 0:
        dx = -(abs(dx))
        i =  i + dx
        print(i)
print("The answer is:", i)
