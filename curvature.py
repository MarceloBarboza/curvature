#!/usr/bin/env python3

import sys

#
def print_conformal_metric(dimension):
    orig_stdout = sys.stdout
    metric = open( 'metric.py', 'w' )
    sys.stdout = metric
    print("#!/usr/bin/env python3")
    print("")
    print("import sympy")
    print("")
    for i in range(dimension):
        print("x_%d = sympy.Symbol('x_%d')" %(i, i))
    print("")
    for i in range(dimension):
        if i == 0:
            print("def r(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn x_%d ** 2" %i, end='')
        elif i < dimension - 1:
            print(" + x_%d ** 2" %i, end='')
        else:
            print(" + x_%d ** 2" %i)
    print("")
    for i in range(dimension):
        if i == 0:
            print("def xi(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn -1 + 2 / (1 + r(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d))" %i)
    print("")
    for i in range(dimension):
        if i == 0:
            print("def sigma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn sympy.cos(xi(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d))" %i)
    print("")
    print("def delta(i, j):")
    print("\tif i in range(%d) and j in range(%d):" %(dimension, dimension))
    print("\t\tif i == j:")
    print("\t\t\treturn 1")
    print("\t\telse:")
    print("\t\t\treturn 0")
    print("")
    for i in range(dimension):
        if i == 0:
            print("def G(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn (1 + r(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d) * sigma(x_0" %i, end='')
    for i in range(1, dimension):
        if i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d) / 2) ** 2 * delta(i, j)" %i)
    print("")
    for i in range(dimension):
        if i == 0:
            print("def g(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn sympy.Matrix(\n\t\t[\n\t\t\t[\n\t\t\t\tG(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j) for j in range(%d)\n\t\t\t] for i in range(%d)\n\t\t]\n\t)" %(i, dimension, dimension))
    print("")
    for i in range(dimension):
        if i == 0:
            print("def h(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d):" %i)
    for i in range(dimension):
        if i == 0:
            print("\treturn g(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d) ** -1" %i)
    print("")
    print("# Christoffel")
    for i in range(dimension):
        if i == 0:
            print("def Gamma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j, k):" %i)
    print("\tgamma = 0")
    print("\tfor l in range(%d):" %dimension)
    print("\t\tgamma += 1/2 * (")
    for i in range(dimension):
        if i == 0:
            print("\t\t\t+ sympy.diff(g(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d)[j, l], x_i):" %i)
    for i in range(dimension):
        if i == 0:
            print("\t\t\t+ sympy.diff(g(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d)[l, i], x_j):" %i)
    for i in range(dimension):
        if i == 0:
            print("\t\t\t+ sympy.diff(g(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d)[i, j], x_l) * h(x_0" %i, end='')
    for i in range(1, dimension):
        if i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d)[l, k]" %i)
    print("\treturn sympy.simplify(gamma)")
    print("")
    print("# Rm_{i, j, k}^l")
    for i in range(dimension):
        if i == 0:
            print("def Rm1(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j, k, l):" %i)
    for i in range(dimension):
        if i == 0:
            print("\trm1 = (\n\t\t+ sympy.diff(Gamma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, k, l), x_j)" %i)
    for i in range(dimension):
        if i == 0:
            print("\t\t- sympy.diff(Gamma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, j, k, l), x_i)\n\t)" %i)
    print("\tfor m in range(%d):" %dimension)
    print("\trm1 += (")
    for i in range(dimension):
        if i == 0:
            print("\t\t+ Gamma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, k, m) * Gamma(x_0" %i, end='')
    for i in range(1, dimension):
        if i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, m, j, l)" %i)
    for i in range(dimension):
        if i == 0:
            print("\t\t- Gamma(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, j, k, m) * Gamma(x_0" %i, end='')
    for i in range(1, dimension):
        if i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, m, i, l)\n\t)" %i)
    print("\treturn sympy.simplify(rm1)")
    print("")
    print("# Rm_{i, j, k, l}")
    for i in range(dimension):
        if i == 0:
            print("def Rm2(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j, k, l):" %i)
    print("\trm2 = 0")
    print("\tfor m in range(%d):" %dimension)
    for i in range(dimension):
        if i == 0:
            print("\t\trm2 += Rm1(x_0", end='')
        elif i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, i, j, k, l) * g(x_0" %i, end='')
    for i in range(1, dimension):
        if i < dimension - 1:
            print(", x_%d" %i, end='')
        else:
            print(", x_%d, m, l)" %i)
    print("\treturn sympy.simplify(rm2)")
    print("")
    sys.stdout = orig_stdout
    metric.close()

# Sectional Curvature
def K(i, j):
    if i in range(dimension) and j in range(dimension):
        if i != j:
            return simpy.simplify(
                Rm2(i, j, i, j) * (
                    metric.g[i, i] * metric.g[j, j] - metric.g[i, j]**2
                )**-1
            )

# Ricci
def Rc(i, j):
    rc = 0
    for k in range(dimension):
        rc += Rm1(i, k, j, k)
    return sympy.simplify(rc)

#
def main():
    if len(sys.argv) == 2:
        dimension = int(sys.argv[1])
        print_conformal_metric(dimension)
    else:
        print("Tente isto: ./curvature.py num_int.")

#
if __name__ == '__main__':
    main()
