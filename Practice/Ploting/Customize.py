import matplotlib.pyplot as plt

x = list(range(101))
y = [i**2 for i in x]

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(-40)
for label in ax1.yaxis.get_ticklabels():
    label.set_rotation(40)

ax1.xaxis.label.set_color("orange")
ax1.yaxis.label.set_color("blue")



ax1.spines["left"].set_color("blue")
ax1.spines["bottom"].set_color("orange")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax1.spines["left"].set_linewidth(2)
ax1.spines["bottom"].set_linewidth(2)

plt.set_xticks([1,2,3,4,5,6,7,8,9])

ax1.plot(x, y, color="green", label="x^2", linewidth=2.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("A porabebla")
plt.legend()
ax1.grid(True, color="black", linestyle="--", linewidth=0.5)
ax1.fill_between(x, y, 1000, alpha=1, facecolor="red")

ax1.tick_params(axis="x", color="yellow")

plt.subplots_adjust(right=0.9, left=0.15, bottom=0.15, top=0.9, wspace=0.1, hspace=0.1)
plt.show()
