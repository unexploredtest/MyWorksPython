import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

x = [2,4,6,8,10]

y1 = [12,5,7,9,3]

y2 = [1,8,7,7,2]

y3 = [3,7,11,4,2]

sizer = np.arange(len(x))

plt.bar(sizer - 0.25, y1, width=0.25, label="lol1", color="red")
plt.bar(sizer , y2, width=0.25, label="lol2", color="orange")
plt.bar(sizer + 0.25, y3, width=0.25, label="lol3", color="yellow")

plt.xticks(ticks=sizer, labels=x)

plt.title("CHECK MY BAR!")
plt.legend()
plt.show()
