#!/bin/bash

WD="/Users/barboza/Projects/Python/curvature"

if [ ! -f "$WD/metric_1.py" ]; then
    touch "$WD"/metric_1.py
else
    mv "$WD"/metric_1.py "$WD"/metric_1.py_orig && touch "$WD"/metric_1.py
fi

n=4

for i in $(seq "$((n-1))"); do
    if [ "$i" = "1" ]; then
        echo -n "#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( "$n" ) ]
e = [ var( 'e_%d' %i ) for i in range( "$n" ) ]

for i in range( "$n" ):
    if i == 0:
        e[ i ] = - 1
    else:
        e[ i ] = + 1

A = Function( 'A' )( x[ 0 ] )
B = Function( 'B' )( x[ "$i" ]" >> "$WD"/metric_1.py
    elif [ "$i" -lt "$((n-1))" ]; then
        echo -n ", x[ "$i" ]" >> "$WD"/metric_1.py
    else
        echo -n ", x[ "$i" ] )
" >> "$WD"/metric_1.py
    fi
done

echo "
def delta( i, j ):
    if i in range( "$n" ) and j in range( "$n" ):
        if i == j:
            return 1
        else:
            return 0" >> "$WD"/metric_1.py

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "
GG = [
      [ e[ 0 ] * exp( 0 + 0 ) * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_1.py
    elif [ "$i" -lt "$n" ]; then
        echo -n "
    , [ e[ "$((i-1))" ] * exp( A + B ) * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_1.py
    else
        echo "
    , [ e[ "$((i-1))" ] * exp( A + B ) * delta( "$((i-1))", j ) for j in range( "$n" ) ]
]
" >> "$WD"/metric_1.py
    fi
done

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "mu  = Function( 'mu' )( x[ "$((i-1))" ]" >> "$WD"/metric_1.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ $((i-1)) ]" >> "$WD"/metric_1.py
    else
        echo ", x[ "$((i-1))" ] )" >> "$WD"/metric_1.py
    fi
done

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "rho = Function( 'mu' )( x[ "$((i-1))" ]" >> "$WD"/metric_1.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ $((i-1)) ]" >> "$WD"/metric_1.py
    else
        echo ", x[ "$((i-1))" ] )" >> "$WD"/metric_1.py
    fi
done
