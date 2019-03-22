
#!/usr/bin/env python3

import sympy

x = (sympy.Symbol('x_0'), sympy.Symbol('x_1'), sympy.Symbol('x_2'))

sigma = sympy.Function('sigma')(x[0], x[1], x[2])

r = 0
for i in range(3):
	r += x[i]**2

def delta(i, j):
	if i in range(3) and j in range(3):
		if i == j:
			return 1
		else:
			return 0

G = [
	[
		((1+r)*sigma/2)**-2*delta(i, j) for j in range(3)
	] for i in range(3)
]

