#!/usr/bin/env python3

from sympy import *

x = [ Symbol( 'x_%d' %i ) for i in range( 4 ) ]
e = [ Symbol( 'e_%d' %i ) for i in range( 4 ) ]

for i in range( 4 ):
    if i == 0:
        e[ i ] = - 1
    else:
        e[ i ] = + 1

A = Function( 'A' )( x[ 0 ] )
B = Function( 'B' )( x[ 1 ], x[ 2 ], x[ 3 ] )

def delta( i, j ):
    if i in range( 4 ) and j in range( 4 ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [ e[ 0 ] * exp( 0 + 0 ) * delta( 0, j ) for j in range( 4 ) ]
    , [ e[ 1 ] * exp( A + B ) * delta( 1, j ) for j in range( 4 ) ]
    , [ e[ 2 ] * exp( A + B ) * delta( 2, j ) for j in range( 4 ) ]
    , [ e[ 3 ] * exp( A + B ) * delta( 3, j ) for j in range( 4 ) ]
]

