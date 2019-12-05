
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(0, 10, 1000)
y = x
z = x*y

for 
    ax.plot(x, y, z, color="blue")

plt.show()
