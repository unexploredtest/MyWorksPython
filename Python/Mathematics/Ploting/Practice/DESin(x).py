# Graphing sin(x) with Deferential equations
# dy/dx = cos(x) using Euler's method with inital (0,6).
import numpy as np
import matplotlib.pyplot as plt

dx = 0.001
x = np.arange(0, 6.0000001, dx)
y = [1]
n = int(6//dx)
for i in range(1, n//2 + 2):
    g = int(y[i-1])
    r = int(x[i-1])
    ydif = (g) + (r)**2
    z = y[i-1] + (ydif*dx)
    y = y + [z]
plt.figure(1, (27, 17))
plt.plot(x, y, "b-")
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.show()
