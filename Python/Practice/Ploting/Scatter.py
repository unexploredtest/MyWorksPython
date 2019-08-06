import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [5,3,6,7,9,4,2,7,3]

plt.scatter(x, y, label="Help!", color="r", marker="x", s=50)

plt.xlabel("I have no idea what are these.")
plt.ylabel("I have no idea what are these.")
plt.title("You must check it!")
plt.legend()
plt.show()
