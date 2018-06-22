#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( 4 ) ]
e = [ var( 'e_%d' %i ) for i in range( 4 ) ]

for i in range( 4 ):
    if i == 0:
        e[ i ] = - 1
    else:
        e[ i ] = + 1

A = Function( 'A' )( x[ 0 ], x[ 1 ] )
B = Function( 'B' )( x[ 0 ], x[ 1 ], x[ 2 ], x[ 3 ] )
C = Function( 'C' )( x[ 2 ], x[ 3 ] )

GG = [
      [   - A * delta( 0, j ) for j in range( 4 ) ]
    , [ 1 / A * delta( 1, j ) for j in range( 4 ) ]
    , [ B * C * delta( 2, j ) for j in range( 4 ) ]
    , [ B * C * delta( 3, j ) for j in range( 4 ) ]
]

mu  = Function( 'mu' )( x[ 0 ], x[ 1 ], x[ 2 ], x[ 3 ] )
rho = Function( 'mu' )( x[ 0 ], x[ 1 ], x[ 2 ], x[ 3 ] )
