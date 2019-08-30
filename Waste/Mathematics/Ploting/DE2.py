import numpy as np
import matplotlib.pyplot as plt
import time as t

dx = 0.000001
x = np.arange(0, 3.00000001, dx)
x = list(x)
y = [1.0]

time1 = t.process_time()
for i in range(0, len(x)-1):
    div = float(y[i])
    p = y[i]
    y += [p + (div * dx) + (p/2)*(dx**2)]
time2 = t.process_time()

dx2 = 0.0001

x2 = np.arange(0, 3.00000001, dx)
x2 = list(x2)
y2 = [1.0]

time3 = t.process_time()
for i in range(0, len(x2)-1):
    div2 = float(y2[i])
    p = y2[i]
    y2 += [p + (div2 * dx2)]
time4 = t.process_time()
t1 = time2 - time1
t2 = time4 - time3
print(np.exp(3))
print(y[-1], t1)
print(y2[-1], t2)
