import matplotlib.pyplot as plt

x = list(range(101))
y = [i**2 for i in x]

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(-40)
for label in ax1.yaxis.get_ticklabels():
    label.set_rotation(40)

ax1.plot(x, y, color="b", label="x^2", linewidth=1.5)

plt.xlabel("x")
plt.ylabel("y")
plt.title("A porabebla")
plt.legend()
ax1.grid(True, color="black", linestyle="--", linewidth=0.5)

plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9, wspace=0, hspace=0)
plt.show()
