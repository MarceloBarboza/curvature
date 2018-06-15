#!/bin/bash

WD="/Users/barboza/Projects/Python"

if [ ! -f "$WD/metric.py" ]; then
    touch "$WD"/metric.py
else
    mv "$WD"/metric.py "$WD"/metric.py_orig && touch "$WD"/metric.py
fi

n=4

for i in $(seq "$((n-1))"); do
    if [ "$i" = "1" ]; then
        echo -n "#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( "$n" ) ]

A = Function( 'A' )( x[ 0 ] )
B = Function( 'B' )( x[ "$i" ]" >> metric.py
    elif [ "$i" -lt "$((n-1))" ]; then
        echo -n ", x[ "$i" ]" >> metric.py
    else
        echo -n ", x[ "$i" ] )

zeta = exp( A + B )

def delta( i, j ):
    if i in range( "$n" ) and j in range( "$n" ):
        if i == j:
            return 1
        else:
            return 0
" >> metric.py
        for j in $(seq "$n"); do
            if [ "$j" = "1" ]; then
                echo -n "
GG = [
      [   -1 * delta( i, "$((j-1))" ) for i in range( "$n" ) ]" >> metric.py
            elif [ "$j" -lt "$n" ]; then
                echo -n "
    , [ zeta * delta( i, "$((j-1))" ) for i in range( "$n" ) ]" >> metric.py
            else
                echo "
    , [ zeta * delta( i, "$((j-1))" ) for i in range( "$n" ) ]
]
" >> metric.py
            fi
        done
    fi
done
