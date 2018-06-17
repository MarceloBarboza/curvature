#!/bin/bash

WD="/Users/barboza/Projects/Python/curvature"

if [ ! -f "$WD/metric_3.py" ]; then
    touch "$WD"/metric_3.py
else
    mv "$WD"/metric_3.py "$WD"/metric_3.py_orig && touch "$WD"/metric_3.py
fi

n=4

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo "#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( "$n" ) ]

def sigma( i ):
    if i in range( 1, "$n" ):
        if i < "$((n - 1))":
            return i + 1
        else:
            return 1

zeta_"$((i-1))" = -1" >> "$WD"/metric_3.py
    else
        echo "zeta_"$((i-1))" = Function( 'zeta_"$((i-1))"' )( x[ 0 ], x[ sigma( "$((i-1))" ) ] )" >> "$WD"/metric_3.py
    fi
done

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "
def delta( i, j ):
    if i in range( "$n" ) and j in range( "$n" ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [ zeta_"$((i-1))" * delta( "$((i-1))", j ) for j in range( "$n" ) ] " >> "$WD"/metric_3.py
    elif [ "$i" -lt "$n" ]; then
        echo -n "
    , [ zeta_"$((i-1))" * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_3.py
    else
        echo -n "
    , [ zeta_"$((i-1))" * delta( "$((i-1))", j ) for j in range( "$n" ) ]
]
" >> "$WD"/metric_3.py
    fi
done