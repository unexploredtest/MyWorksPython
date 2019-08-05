# A simple differential Equations y'=y+x^2 waiting te be graphed
# With starting x=1, y=3 with on interval [0,10]
import numpy as np
import matplotlib.pyplot as plt
dx = 0.001
x = np.arange(1, 2.00000001, dx)
y = [3]
n = int(2//dx)
for i in range(1,n//2 + 2):
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
