import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 4, 4000)
y1 = (np.sin(x1)) * x1

x2 = np.linspace(4, 6, 2000)
y2 = (np.sin(x2)) * x2

x3 = np.linspace(6, 10, 4000)
y3 = (np.sin(x3)) * x3

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

ax1.axhline(y=0, color="black")

ax1.plot(x1, y1, color="green", label="x*sin(x)")
ax1.plot(x2, y2, color="green")
ax1.plot(x3, y3, color="green")

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(0)
for label in ax1.yaxis.get_ticklabels():
    label.set_rotation(90)

ax1.xaxis.label.set_color("red")
ax1.yaxis.label.set_color("blue")

ax1.spines["bottom"].set_color("red")
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_color("blue")
ax1.spines["bottom"].set_linewidth(2)
ax1.spines["left"].set_linewidth(2)

ax1.grid(True, linestyle="--", color="black", linewidth=0.5)

plt.fill_between(x1, y1, where=(y1 >= 0), facecolor="red", alpha=1)

ax1.set_xticks(list(range(11)))
ax1.set_yticks(list(range(-10,9)))

plt.ylim(-6,8)
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.title("The graph of x*sin(x) in interval [0,10]")
plt.legend()
plt.show()
