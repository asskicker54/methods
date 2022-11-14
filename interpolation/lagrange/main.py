import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = np.arange(-2, 1.1, 0.1)
y = np.sin(np.sin(a))

res=y[0] * (a - a[10]) * (a - a[20]) * (a - a[30]) / ((a[0] - a[10]) * (a[0] - a[20]) * (a[0] - a[30])) +\
y[10] * (a - a[0]) * (a - a[20]) * (a - a[30]) / ((a[10] - a[0]) * (a[10] - a[20]) * (a[10] - a[30])) +\
y[20] * (a - a[10]) * (a - a[0]) * (a - a[30]) / ((a[20] - a[10]) * (a[20] - a[0]) * (a[20] - a[30])) +\
y[30] * (a - a[10]) * (a - a[20]) * (a - a[0]) / ((a[30] - a[10]) * (a[30] - a[20]) * (a[30] - a[0]))

print(res)

r_pract = abs(y - res)
print(r_pract)


def diff4(i):
    x = sp.symbols('x')
    func = sp.sin(sp.sin(x))
    yprime = sp.diff(func, x, 4)
    yprime = yprime.subs({x: i})
    return yprime.evalf()

r_teor = []

for x in a:
    r_teor.append(round((abs(diff4(x) / 24 * (x-a[0]) * (x - a[10]) * (x - a[20]) * (x - a[30]))), 9))

r_teor=np.array(r_teor)


figure = plt.figure(figsize=(15, 7))

plt.subplot(1, 2, 1)
plt.plot(a,y)
plt.plot(a,res)
plt.legend(["y","L3"])

plt.subplot(1, 2, 2)
plt.plot(r_pract)
plt.plot(r_teor)
plt.legend(["r_pract","r_teor"])

plt.subplots_adjust(top=0.9, bottom=0.2, wspace=0.25)
plt.savefig('./lagrange.png')