from Primes1000000 import *
import matplotlib.pyplot as plt
from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

style.use("fivethirtyeight")

range = list(range(0, 1000001, 100000))
primes = [i for i in a if i <= 1000000]

ax1.hist(primes, range, histtype="bar", rwidth=0.8, color="red")

plt.show()
