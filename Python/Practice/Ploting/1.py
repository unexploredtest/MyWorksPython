import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [23,5,11,7,9]

x2 = [1,2,3,4,5]
y2 = [2,-3,1,12,9]

plt.plot(x1, y1, label="First")
plt.plot(x2, y2, label="Second")

plt.title("A very good graph\nCheck it")
plt.legend()

plt.show()
