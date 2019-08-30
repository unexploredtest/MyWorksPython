import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import style

style.use("fivethirtyeight")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def live_graph(options):

    data = open("data.txt", "r").read()
    lines = data.split("\n")

    xs = []
    ys = []

    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(int(x))
            ys.append(int(y))

    ax1.clear()
    ax1.set_xticks(list(range(0, max(xs), 2)))
    ax1.set_yticks(list(range(0, max(ys), 3)))
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, live_graph, interval=2000)

plt.tight_layout()
plt.show()
