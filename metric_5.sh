#!/bin/bash

WD="/Users/barboza/Projects/Python/curvature"

if [ ! -f "$WD/metric_5.py" ]; then
    touch "$WD"/metric_5.py
else
    mv "$WD"/metric_5.py "$WD"/metric_5.py_orig && touch "$WD"/metric_5.py
fi

# Dimensao da base de um espaco-tempo estatico
n=3

echo "#!/usr/bin/env python3

from sympy import *

x = [ Symbol( 'x_%d' %i ) for i in range( "$n" ) ]
" >> "$WD"/metric_5.py

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "zeta = [ Function( 'zeta_%d' %i )( x[ "$((i-1))" ]" >> "$WD"/metric_5.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ "$((i-1))" ]" >> "$WD"/metric_5.py
    else
        echo ", x[ "$((i-1))" ] ) for i in range( "$n" ) ]" >> "$WD"/metric_5.py
    fi
done

echo -n "
def delta( i, j ):
    if i in range( "$n" ) and j in range( "$n" ):
        if i == j:
            return 1
        else:
            return 0
" >> "$WD"/metric_5.py

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "
GG = [
      [ zeta[ "$((i-1))" ] ** 2 * delta( "$((i-1))", j ) for j in range( "$n" ) ] " >> "$WD"/metric_5.py
    elif [ "$i" -lt "$n" ]; then
        echo -n "
    , [ zeta[ "$((i-1))" ] ** 2 * delta( "$((i-1))", j ) for j in range( "$n" ) ]" >> "$WD"/metric_5.py
    else
        echo "
    , [ zeta[ "$((i-1))" ] ** 2 * delta( "$((i-1))", j ) for j in range( "$n" ) ]
]
" >> "$WD"/metric_5.py
    fi
done

for i in $(seq "$n"); do
    if [ "$i" = "1" ]; then
        echo -n "h = Function( 'h' )( x[ "$((i-1))" ]" >> "$WD"/metric_5.py
    elif [ "$i" -lt "$n" ]; then
        echo -n ", x[ "$((i-1))" ]" >> "$WD"/metric_5.py
    else
        echo ", x[ "$((i-1))" ] )" >> "$WD"/metric_5.py
    fi
done