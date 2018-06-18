#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( 4 ) ]

A = Function( 'A' )( x[ 0 ], x[ 1 ] )
B = Function( 'B' )( x[ 0 ], x[ 1 ], x[ 2 ], x[ 3 ] )
C = Function( 'C' )( x[ 2 ], x[ 3 ] )

def delta( i, j ):
    if i in range( 4 ) and j in range( 4 ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [   - A * delta( 0, j ) for j in range( 4 ) ]
    , [ 1 / A * delta( 1, j ) for j in range( 4 ) ]
    , [ B * C * delta( 2, j ) for j in range( 4 ) ]
    , [ B * C * delta( 3, j ) for j in range( 4 ) ]
]
