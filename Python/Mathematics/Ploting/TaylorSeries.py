import numpy as np
import matplotlib.pyplot as plt

x =  np.linspace(-8, 8, 200000)
sinx = np.sin(x)

T1sinx = x
T2sinx = x - x**3/6
T3sinx = x - x**3/6 + x**5/120
T4sinx = x - x**3/6 + x**5/120 - x**7/5040

plt.subplot(2, 2, 1)
plt.plot(x, sinx, "g-", label="sin(x)")
plt.plot(x, T1sinx, "r-", label="x")
plt.ylim(-3,3)
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper right", title='Taylor Series')

plt.subplot(2, 2, 2)
plt.plot(x, sinx, "g-", label="sin(x)")
plt.plot(x, T2sinx, "r-", label="x - x^3/6")
plt.ylim(-3,3)
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper right", title='Taylor Series')

plt.subplot(2, 2, 3)
plt.plot(x, sinx, "g-", label="sin(x)")
plt.plot(x, T3sinx, "r-", label="x - x^3/6 + x^5/120")
plt.ylim(-3,3)
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper right", title='Taylor Series')

plt.subplot(2, 2, 4)
plt.plot(x, sinx, "g-", label="sin(x)")
plt.plot(x, T4sinx, "r-", label="x - x^3/6 + x^5/120 - x^7/5040")
plt.ylim(-3,3)
plt.axhline(y=0, zorder=-1)
plt.axvline(x=0, zorder=-1)
plt.legend(loc="upper right", title='Taylor Series')

# plt.savefig("sin(x).png")

plt.show()
