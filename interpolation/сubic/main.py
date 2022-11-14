import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 0.025, 0.025)
y = np.sin(np.sin(x))

h = 0.25
A = G = h
B = h * 4

p = [0, 0]
for i in range(2, 9):
    p.append(-G / (B + A * p[i - 1]))

a = y[::10]

fi = [0]
for i in range(2, 9):
    fi.append(6 * ((a[i] - a[i - 1]) / h - (a[i - 1] - a[i - 2]) / h))

q = [0, 0]
for i in range(1, 8):
    q.append((fi[i] - A * q[i]) / (B + A * p[i]))

c = np.zeros(9)
for i in range(8, 1, -1):
    c[i - 1] = (p[i] * c[i] + q[i])

d = [0]
for i in range(1, 9):
    d.append((c[i - 1] - c[i]) / h)

b = [0]
for i in range(1, 9):
    b.append((a[i - 1] - a[i]) / h - c[i] * h / 2 - (c[i - 1] - c[i]) * h / 6)

S3 = []

for i in range(10, 81, 10):
    for j in range(10):
        S3.append(a[i // 10] + b[i // 10] * (x[i] - x[(i - 10) + j]) +
                   (c[i // 10] * (x[i] - x[(i - 10) + j])**2) / 2 +
                   (d[i // 10] * (x[i] - x[(i - 10) + j])**3) / 6)

S3.append(a[8] + b[8] * (x[80] - x[80]) + (c[8] * (x[80] - x[80])**2) / 2 +
           (d[8] * (x[80] - x[80])**3) / 6)

S3 = np.array(S3)
R_pract = np.abs(S3 - y)

fig = plt.figure(figsize=(15, 15))

plt.subplot(2, 1, 1)
plt.plot(y)
plt.plot(S3)
plt.legend(['y', 'S3'])

plt.subplot(2, 1, 2)
plt.plot(R_pract)
plt.legend(['R_pract'])

plt.savefig('./cubic.png')


