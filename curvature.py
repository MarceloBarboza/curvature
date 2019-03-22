#!/usr/bin/env python3

import sys
import sympy

def print_conformal_metric(dimension):
    orig_stdout = sys.stdout
    metric = open( 'metric.py', 'w' )
    sys.stdout = metric
    print("")
    print("#!/usr/bin/env python3")
    print("")
    print("import sympy")
    print("")
    for i in range(dimension):
        if i == 0:
            print("x = (sympy.Symbol('x_%d')" %i, end='')
        elif i < dimension - 1:
            print(", sympy.Symbol('x_%d')" %i, end='')
        else:
            print(", sympy.Symbol('x_%d'))" %i)
    print("")
    for i in range(dimension):
        if i == 0:
            print("sigma = sympy.Function('sigma')(x[0]", end='')
        elif i < dimension - 1:
            print(", x[%d]" %i, end='')
        else:
            print(", x[%d])" %i)
    print("")
    print("r = 0")
    print("for i in range(%d):" %dimension)
    print("\tr += x[i]**2")
    print("")
    print("def delta(i, j):")
    print("\tif i in range(%d) and j in range(%d):" %(dimension, dimension))
    print("\t\tif i == j:")
    print("\t\t\treturn 1")
    print("\t\telse:")
    print("\t\t\treturn 0")
    print("")
    print("G = [")
    print("\t[")
    print("\t\t((1+r)*sigma/2)**-2*delta(i, j) for j in range(%d)" %dimension)
    print("\t] for i in range(%d)" %dimension)
    print("]")
    print("")
    sys.stdout = orig_stdout
    metric.close()

import metric

g = sympy.Matrix(metric.G)

def main():
    if len(sys.argv) == 2:
        dimension = int(sys.argv[1])
        print_conformal_metric(dimension)
    else:
        print('You must inform a manifold dimension first.')

if __name__ == '__main__':
    main()
