import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [12,5,7,9,3]

x2 = [2,4,6,8,10]
y2 = [1,8,7,7,2]

plt.bar(x1, y1, label="lol1", color="red")
plt.bar(x2, y2, label="lol2", color="black")

plt.title("CHECK MY BAR!")
plt.legend()
plt.show()
