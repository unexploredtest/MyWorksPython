import matplotlib.pyplot as plt

Cpu_Strengh = [1, 2, 3, 4, 5]

Microsoft =  [100, 1050, 20000, 5060, 60]
Intel =      [30, 305, 25000, 60000, 5200]
AMD =        [1000, 200300, 50000, 20030, 700]
SnapDragon = [150, 1100, 20050, 5110, 110]

plt.plot([], [], color = "k", label="Microsoft", linewidth=5)
plt.plot([], [], color = "b", label="Intel", linewidth=5)
plt.plot([], [], color = "m", label="AMD", linewidth=5)
plt.plot([], [], color = "g", label="SnapDragon", linewidth=5)

plt.stackplot(Cpu_Strengh, Microsoft, Intel, AMD, SnapDragon, colors = ["k", "b", "m", "g"])

plt.legend()
plt.show()
