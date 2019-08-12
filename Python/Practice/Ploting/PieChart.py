import matplotlib.pyplot as plt

CPU_amount = [6, 9, 2, 3]
companies = ['AMD', 'Intel', 'Microsoft', 'SnapDragon']

cols = ["k", "b", "g", "r"]
plt.pie(CPU_amount, labels = companies, colors = cols, autopct = "%1.2f%%")

plt.show()
