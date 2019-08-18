import matplotlib.pyplot as plt
import csv
import numpy as np

# First method
x1 = []
y1 = []

with open("Numbers.txt", "r") as nums:
    numbers = csv.reader(nums, delimiter=",")
    for row in numbers:
        x1.append(row[0])
        y1.append(row[1])

plt.plot(x1, y1, color = "red", label = "Numbers")
plt.xlabel("Numbers")
plt.ylabel("Numbers")
plt.title("idk by csv")
plt.legend()
plt.show()

# Second method
x2, y2 = np.loadtxt("Numbers.txt", delimiter=",", unpack=True)

plt.plot(x2, y2, color = "b", label = "Numbers")
plt.xlabel("Numbers")
plt.ylabel("Numbers")
plt.title("idk by numpy")
plt.legend()
plt.show()
