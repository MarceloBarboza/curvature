#!/usr/bin/env python3

import sympy

x_0 = sympy.Symbol('x_0')
x_1 = sympy.Symbol('x_1')

def r(x_0, x_1):
	return x_0 ** 2 + x_1 ** 2

def xi(x_0, x_1):
	return -1 + 2 / (1 + r(x_0, x_1))

def sigma(x_0, x_1):
	return sympy.cos(xi(x_0, x_1))

def delta(i, j):
	if i in range(2) and j in range(2):
		if i == j:
			return 1
		else:
			return 0

def G(x_0, x_1, i, j):
	return (1 + r(x_0, x_1) * sigma(x_0, x_1) / 2) ** 2 * delta(i, j)

def g(x_0, x_1):
	return sympy.Matrix(
		[
			[
				G(x_0, x_1, i, j) for j in range(2)
			] for i in range(2)
		]
	)

def h(x_0, x_1):
	return g(x_0, x_1) ** -1

# Christoffel
def Gamma(x_0, x_1, i, j, k):
	gamma = 0
	for l in range(2):
		gamma += 1/2 * (
			+ sympy.diff(g(x_0, x_1)[j, l], x_i)
			+ sympy.diff(g(x_0, x_1)[l, i], x_j)
			+ sympy.diff(g(x_0, x_1)[i, j], x_l) * h(x_0, x_1)[l, k]
	)
	return sympy.simplify(gamma)

# Rm_{i, j, k}^l
def Rm1(x_0, x_1, i, j, k, l):
	rm1 = (
		+ sympy.diff(Gamma(x_0, x_1, i, k, l), x_j)
		- sympy.diff(Gamma(x_0, x_1, j, k, l), x_i)
	)
	for m in range(2):
		rm1 += (
			+ Gamma(x_0, x_1, i, k, m) * Gamma(x_0, x_1, m, j, l)
		- Gamma(x_0, x_1, j, k, m) * Gamma(x_0, x_1, m, i, l)
		)
	return sympy.simplify(rm1)

# Rm_{i, j, k, l}
def Rm2(x_0, x_1, i, j, k, l):
	rm2 = 0
	for m in range(2):
		rm2 += Rm1(x_0, x_1, i, j, k, l) * g(x_0, x_1, m, l)
	return sympy.simplify(rm2)

# Sectional
def K(x_0, x_1, i, j):
	if i != j:
		k = Rm2(x_0, x_1, i, j, i, j) * (
				g(x_0, x_1, i, i) * g(x_0, x_1, j, j) - g(x_0, x_1, i, j) ** 2
			) ** -1
		return sympy.simplify(k)

# Ricci
def Rc(x_0, x_1, i, j):
	rc = 0
	for k in range(2):
		rc += Rm(x_0, x_1, i, k, j, k)
	return sympy.simplify(rc)

# Scalar
def scal(x_0, x_1):
	scal = 0
	for i in range(2):
		for j in range(2):
			scal += h(x_0, x_1)[i, j] * Rc(x_0, x_1, i, j)
	return sympy.simplify(scal)

