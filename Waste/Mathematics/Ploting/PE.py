# Graphing e^x in interval [0,3] using two different methods:

# First method(using the normal method):

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("grayscale")

a = np.linspace(0, 3, 30001)
b = np.exp(a)

plt.subplot(1, 2, 1)
plt.figure(1, figsize=(30, 20))
plt.plot(a, b, "b-", label="Exponential1")
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper left", title="Exponential")
plt.title("e^x by numpy function.")

plt.grid(True, linestyle="--")

# Second method(using the dy/dx = y, y(0)=1):

dx = 0.001
x = np.arange(0, 3.00000001, dx)
x = list(x)
y = [1.0]

for i in range(0, len(x)-1):
    div = float(y[i])
    p = y[i]
    y += [p + (div * dx)]

plt.subplot(1, 2, 2)
plt.figure(1, figsize=(30, 20))
plt.plot(x, y, "r-", label="Exponential2")
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper left", title="Exponential")
plt.title("e^x by difinetion.")

plt.grid(True, linestyle="--")

plt.savefig("ComperingExponentials.png")

plt.show()

print(f"The e^3 by numpy function is {(np.exp(3)):.7f}... and the estimated one is {(y[len(x)-1]):.7f}... ." )
