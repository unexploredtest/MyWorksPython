# A simple differential Equations y'=y+x^2 waiting te be graphed
# With starting x=1, y=3 with on interval [0,10]
import numpy as np
import matplotlib.pyplot as plt
dx = 0.0001
x = np.arange(0, 20.00000001, dx)
x = list(x)
y = [0]

for i in range(0, len(x)-1):
    div = float(np.cos(x[i]))
    p = y[i]
    y += [p + (div * dx)]

# plt.subplot(1, 2, 2)
plt.figure(1, figsize=(30, 20))
plt.plot(x, y, "r-", label="Exponential2")
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper left", title="Exponential")
plt.title("cos(x) by difinetion.")

plt.savefig("cos(x).png")

plt.show()
