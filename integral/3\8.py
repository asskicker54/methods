"""
Отрезок [0, 1]

"""



import numpy as np
import sympy as sp

a, b = 0, 1
x0 = a

f = lambda x:[1] * len(x) #x**3 * np.exp(x * 2)

def diff4(i):
    x = sp.symbols('x')
    func = x**3 * sp.exp(x * 2)
    #func = 1
    yprime = sp.diff(func, x, 4)
    yprime = yprime.subs({x: i})
    
    return abs(yprime.evalf())

n = int(input("n: "))
if n % 3 !=0:
    print("Шаг не кратен 3")
    exit(0)

h = (b - a) / n
x = np.arange(a, b + 0.1, h)
y = f(x)


y_p = []
for i in x:
    y_p.append(diff4(i))
    
M4 = max(y_p)
print(f"M4 = {M4}")

r = (-(b - a) / 80) * M4 * h ** 4
print(f"R(h) = {r}")

s1 = 0
s2 = 0
t = 1
for i in range(len(y) - 2):
    if (i + 1) % 3 == 0:
        s1 += y[i + 1]
    else:
        s2 += y[i + 1]
s = (y[0] + y[-1]) + 3 * s2 + 2 * s1
print(s)

I = 3 * (h / 8) * s + r
print(f"J = {I}")