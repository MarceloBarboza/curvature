#!/usr/bin/env python3

import sympy

x_0 = sympy.Symbol('x_0')
x_1 = sympy.Symbol('x_1')
x_2 = sympy.Symbol('x_2')

def r(x_0, x_1, x_2):
	return x_0 ** 2 + x_1 ** 2 + x_2 ** 2

def xi(x_0, x_1, x_2):
	return -1 + 2 / (1 + r(x_0, x_1, x_2))

def sigma(x_0, x_1, x_2):
	return sympy.cos(xi(x_0, x_1, x_2))

def delta(i, j):
	if i in range(3) and j in range(3):
		if i == j:
			return 1
		else:
			return 0

def G(x_0, x_1, x_2, i, j):
	return (1 + r(x_0, x_1, x_2) * sigma(x_0, x_1, x_2) / 2) ** 2 * delta(i, j)

def g(x_0, x_1, x_2):
	return sympy.Matrix(
		[
			[
				G(x_0, x_1, x_2, i, j) for j in range(3)
			] for i in range(3)
		]
	)

def h(x_0, x_1, x_2):
	return g(x_0, x_1, x_2) ** -1

# Christoffel Symbols
def Gamma(x_0, x_1, x_2, i, j, k):
	gamma = 0
	for l in range(3):
		gamma += 1/2 * (
			+ sympy.diff(g(x_0, x_1, x_2)[j, l], x_i):
			+ sympy.diff(g(x_0, x_1, x_2)[l, i], x_j):
			+ sympy.diff(g(x_0, x_1, x_2)[i, j], x_l) * h(x_0, x_1, x_2)[l, k]
	return sympy.simplify(gamma)

# Rm_{i, j, k}^l
def Rm1(x_0, x_1, x_2, i, j, k, l):
	rm1 = (
		+ sympy.diff(Gamma(x_0, x_1, x_2, i, k, l), x_j)
		- sympy.diff(Gamma(x_0, x_1, x_2, j, k, l), x_i)
	)
	for m in range(3):
	rm1 += (
		+ Gamma(x_0, x_1, x_2, i, k, m) * Gamma(x_0, x_1, x_2, m, j, l)
		- Gamma(x_0, x_1, x_2, j, k, m) * Gamma(x_0, x_1, x_2, m, i, l)
	)
	return sympy.simplify(rm1)

# Rm_{i, j, k, l}
def Rm2(x_0, x_1, x_2, i, j, k, l):
	rm2 = 0
	for m in range(3):
		rm2 += Rm1(x_0, x_1, x_2, i, j, k, l) * g(x_0, x_1, x_2, m, l)
	return sympy.simplify(rm2)

