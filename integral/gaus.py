import numpy as np

a, b = 0, 1

f = lambda x: [1] * len(x) #x**3 * np.exp(2 * x)


n = 7

t = np.zeros(n)
t[0] = -0.94910791
t[6] = 0.94910791
t[1] = -0.74153119
t[5] = 0.74153119
t[2] = -0.40584515
t[4] = 0.40584515
t[3] = 0

A = np.zeros(n)
A[0] = A[6] = 0.12948496
A[1] = A[5] = 0.27970540
A[2] = A[4] = 0.38183006
A[3] = 0.41795918

x_i = (((b + a) / 2) + ((b - a) / 2) * t)

I = ((b - a) / 2) * np.sum(A * f(x_i))

print(f'I = {I}')

