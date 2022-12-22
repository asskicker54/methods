import numpy as np

a, b = 0, 1
x0 = a
eps = 10** -3

f = lambda x: [1] * len(x) #x**3 * np.exp(2 * x)
y_diff2 = lambda x: [0] * len(x) #2 * x * (2 * x**2 + 6 * x + 3 ) * np.exp(2 * x)

n = 1

I1 = 1
I2 = 100
s = 0

while abs(I2 - I1) >= eps:
    n += 1
    s += 1
    n2 = n * 2
    h = (b - a) / n
    h2 = (b - a) / n2
    x = np.arange(a, b + 0.1, h)
    x2 = np.arange(a, b + 0.1, h2)
    y = f(x)
    y2 = f(x2)
    M = max(y_diff2(x))
    M2 = max(y_diff2(x2))
    r = (-(b - a) / 12) * M * h**2
    r2 = (-(b - a) / 12) * M2 * h2**2
    I1 = h * (((y[0] + y[-1]) / 2) + sum(y[1:-1])) + r
    I2 = h2 * (((y2[0] + y2[-1]) / 2) + sum(y2[1:-1])) + r2

print(f'n = {n}\t2n = {n * 2}\nrepeats: {s}\n\nIn = {I1}\tI2n = {I2}\n|I2n - In| = {abs(I2 - I1)}')