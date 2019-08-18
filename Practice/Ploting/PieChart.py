import matplotlib.pyplot as plt

CPU_amount = [6, 9, 2, 3]
companies = ['AMD', 'Intel', 'Microsoft', 'SnapDragon']

cols = ["r", "lightblue", "yellow", "g"]
plt.pie(CPU_amount, labels = companies, colors = cols, startangle = 90,
        autopct = "%1.1f%%", shadow = True, explode=[0, 0, 0.1, 0]
        )

plt.show()
