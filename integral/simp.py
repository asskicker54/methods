import numpy as np
import sympy as sp

a, b = 0, 1
x0 = a

f = lambda x: [1] * len(x) #x**3 * np.exp(2 * x)


def diff4(i):
    x = sp.symbols('x')
    #func = x**3 * sp.exp(2 * x)
    func = 1
    yprime = sp.diff(func, x, 4)
    yprime = yprime.subs({x: i})
    return abs(yprime.evalf())

n = int(input("n: "))
if n % 2 != 0:
    print("Шаг нечётный!")
    exit(0)

h = (b - a) / n
x = np.arange(a, b + 0.1, h)
y = f(x)

y_diff4 = []
for i in x:
    y_diff4.append(diff4(i))

M4 = max(y_diff4)
print(f"M4 = {M4}")

r = (-(b - a) / 180) * M4 * h ** 4
print(f"R(h) = {r}")

s = y[0] + y[-1]
t = 1
for i in range(1, len(y) - 1):
    if i % 2 == 0:
        t = 2
    else:
        t = 4
    s += y[i] * t
print(s)

I = (h / 3) * s + r
print(f"I = {I}")