import matplotlib.pyplot as plt

Population_Age = [12, 34, 32, 23, 12, 54, 78, 1, 54, 3,
33, 5, 14, 43, 32, 6, 8, 68, 3, 43, 43, 3, 5, 54, 34, 42, 60]
Age_Range = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(Population_Age, Age_Range, histtype = "bar", rwidth = 0.8, label="Population Age" , color="red")
plt.xlabel("Age Range")
plt.ylabel("Age Numbers")
plt.title("Population Age of the city of idk")
plt.legend()
plt.show()
