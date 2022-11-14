import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 0.025, 0.025)
y = np.sin(np.sin(x))

S1 = []

for i in range(10, len(x), 10):
    for j in range(10):
        S1.append(y[i] + (x[i] - x[j + (i - 10)]) * (y[i-10] - y[i]) / (x[10] - x[0]))

S1.append(y[80] + (x[80] - x[80]) * (y[70] - y[80]) / (x[10] - x[0]))

S1 = np.array(S1)
#print(f"S1: {S1}")

R_pract = np.abs(S1 - y)
#print(f"R_pract: {R_pract}")

fig = plt.figure(figsize=(15, 15))
plt.subplot(2, 1, 1)
plt.plot(y)
plt.plot(S1)
plt.legend(['y', 'S1'])

plt.subplot(2, 1, 2)
plt.plot(R_pract)
plt.legend(['R_pract'])

plt.savefig('./linear.png')
