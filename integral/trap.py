import numpy as np
import sympy as sp

a, b = 0, 1
x0 = a

f = lambda x: [1] * len(x) #x**3 * np.exp(2 * x)

n = int(input("n: "))

h = (b - a) / n
x = np.arange(a, b + 0.1, h)
y = f(x)

#y_diff2 = lambda x: 2 * x * (2 * x**2 + 6 * x + 3 ) * np.exp(2 * x)
def diff2(i):
    x = sp.symbols('x')
    #func = x**3 * sp.exp(x * 2)
    func = 1
    yprime = sp.diff(func, x, 2)
    yprime = yprime.subs({x: i})
    return abs(yprime.evalf())

y_diff = []
for i in y:
    y_diff.append(diff2(i))

M2 = max(y_diff)
print(f"M2 = {M2}")

r = (-(b - a) / 12) * M2 * h**2
print(f"R(h) = {r}")

I = h * (((y[0] + y[-1]) / 2) + sum(y[1:-1])) + r
print(f"I = {I}")