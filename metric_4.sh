#!/bin/bash

WD="/Users/barboza/Projects/Python/curvature"

if [ ! -f "$WD/metric_4.py" ]; then
    touch "$WD"/metric_4.py
else
    mv "$WD"/metric_4.py "$WD"/metric_4.py_orig && touch "$WD"/metric_4.py
fi

n=4

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( "$n" ) ]

A = Function( 'A' )( x[ 0 ], x[ 1 ] )
B = Function( 'B' )( x[ "$((i-1))" ]" >> "$WD"/metric_4.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ "$((i-1))" ]" >> "$WD"/metric_4.py
    else
        echo -n ", x[ "$((i-1))" ] )" >> "$WD"/metric_4.py
    fi
done

for i in $(seq 3 "$n"); do
    if [ "$i" = "3" ]; then
        echo -n "
C = Function( 'C' )( x[ "$((i-1))" ]" >> "$WD"/metric_4.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ "$((i-1))" ]" >> "$WD"/metric_4.py
    else
        echo -n ", x[ "$((i-1))" ] )
" >> "$WD"/metric_4.py
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
      [   - A * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_4.py
    elif [ "$i" = "2" ]; then
        echo -n "
    , [ 1 / A * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_4.py
    elif [ "$i" -lt "$n" ]; then
        echo -n "
    , [ B * C * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_4.py
    else
        echo -n "
    , [ B * C * delta( "$((i-1))", j ) for j in range( "$n" ) ]
]
" >> "$WD"/metric_4.py
    fi
done
