# I heard a formula which
# says lim(x => infinity)[(The least common factor of 1 to n) ** 1/n] = e

import matplotlib.pyplot as plt
import numpy as np
from Simple.TLCM2 import list_past, TLCM2
import decimal as d

times = int(input("How many time would you like to compute e?"))
tlcm = 1
x = list(range(1, times))
y = []
for i in x:
    tlcm = TLCM2([tlcm, i])
    tlcml = d.Decimal(tlcm) ** d.Decimal(1/i)
    y.append(tlcml)

plt.plot(x, y, color="r", label="TLCM")
plt.scatter(x, y, marker="x", color="k", label="TLCM real values", s=5)
plt.axvline(x=0)
plt.axhline(y=0)
plt.axhline(y=np.exp(1), color="b", label="Number e")

plt.title("lim(n => infinity)[(The least common multipler of 1 to n) ** 1/n] = e")
plt.legend()
plt.show()
