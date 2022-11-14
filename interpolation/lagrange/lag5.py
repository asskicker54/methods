import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 2.1, 0.1)
y = np.sin(np.sin(x))

res = y[0] * (x - x[10]) * (x - x[20]) * (x - x[30]) * (x - x[40]) * (x - x[50])/((x[0] - x[10]) * (x[0] - x[20]) * (x[0] - x[30]) * (x[0] - x[40]) * (x[0] - x[50])) +\
y[10] * (x - x[0]) * (x - x[20]) * (x - x[30]) * (x - x[40]) * (x - x[50]) / ((x[10] - x[0]) * (x[10] - x[20]) * (x[10] - x[30]) * (x[10] - x[40]) * (x[10] - x[50])) +\
y[20] * (x - x[10]) * (x - x[0]) * (x - x[30]) * (x - x[40]) * (x - x[50]) / ((x[20] - x[10]) * (x[20] - x[0]) * (x[20] - x[30]) * (x[20] - x[40]) * (x[20] - x[50])) +\
y[30] * (x - x[10]) * (x - x[20]) * (x - x[0]) * (x - x[40]) * (x - x[50]) / ((x[30] - x[10]) * (x[30] - x[20]) * (x[30] - x[0]) * (x[30] - x[40]) * (x[30] - x[50])) +\
y[40] * (x - x[10]) * (x - x[20]) * (x - x[30]) * (x - x[0]) * (x - x[50]) / ((x[40] - x[10]) * (x[40] - x[20]) * (x[40] - x[30]) * (x[40] - x[0]) * (x[40] - x[50])) +\
y[50] * (x - x[10]) * (x - x[20]) * (x - x[30]) * (x - x[40]) * (x - x[0]) / ((x[50] - x[10]) * (x[50] - x[20]) * (x[50] - x[30]) * (x[50] - x[40]) * (x[50] - x[0])) 

R_pract = np.abs(res - y)

fig = plt.figure(figsize=(12, 7))

plt.subplot(2, 1, 1)
plt.plot(y)
plt.plot(res)
plt.legend(['y', 'L5'])

plt.subplot(2, 1, 2)
plt.plot(R_pract)
plt.legend(["R_pract"])

plt.savefig('./l5.png')