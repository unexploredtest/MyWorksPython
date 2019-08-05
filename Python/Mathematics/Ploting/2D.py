# How to solve 2 degree polymiol
# x^2 - 5x + 6 = 0

import numpy as np

i = 0

dx = 1

while np.abs(i**2 - 5*i + 6) > 0.000001:
    d = i**2 - 5*i + 6
    if d > 0:
        dx = -(np.abs(dx))
        dx = dx/2
        i = dx + i
        print(i)
    elif d < 0:
        dx = (np.abs(dx))
        i =  i + dx
        dx = dx/2
        print(i)
print(i)
