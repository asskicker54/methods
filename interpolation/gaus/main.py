import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 0.1, 0.1)
y = np.sin(np.sin(x))

del_y = np.array([y[10] - y[0], y[20] - y[10]])
del_2_y = del_y[1] - del_y[0]

t = (x - x[0]) / (x[10] - x[0])

#print(f"del_y: {del_y}")
#print(f"del_2_y: {del_2_y}")
#print(f"t: {t}")

G2 = y[0] + del_y[0] * t + del_2_y * t * (t - 1) / 2

#print(f"G2: {G2}")

R_pract = np.abs(G2 - y)

#print(f"R_pract: {R_pract}")

fig = plt.figure(figsize=(12, 7))

#plt.subplot(1, 2, 1)
plt.plot(y)
plt.plot(G2)
plt.legend(["y", "G2"])

#plt.subplot(1, 2, 2)
#plt.plot(R_pract)
#plt.legend(["R_pract"])

plt.savefig("./gaus.png")

