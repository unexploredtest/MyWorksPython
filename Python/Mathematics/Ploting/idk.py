import numpy as np
import matplotlib.pyplot as plt
time, counts, unc = np.loadtxt('semilogDemo.txt', unpack=True)
t_half = 14
tau = t_half/np.log(2)
N0 = 8200
t = np.linspace(0, 180, 128)
N = N0* np.exp(-t/tau)
plt.figure(1, figsize=(9.5, 4))
plt.subplot(1, 2, 1)
plt.plot(t, N, color='C0', label="theory")
plt.plot(time, counts, 'oC1', label="data")
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')
plt.subplot(1, 2, 2) 
plt.semilogy(t, N, color='C0', label="theory")
plt.semilogy(time, counts, 'oC1', label="data")
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figures/semilogDemo.pdf')
plt.show()