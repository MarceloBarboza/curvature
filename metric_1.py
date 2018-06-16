#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( 4 ) ]

A = Function( 'A' )( x[ 0 ] )
B = Function( 'B' )( x[ 1 ], x[ 2 ], x[ 3 ] )

zeta = exp( A + B )

def delta( i, j ):
    if i in range( 4 ) and j in range( 4 ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [   -1 * delta( i, 0 ) for i in range( 4 ) ]
    , [ zeta * delta( i, 1 ) for i in range( 4 ) ]
    , [ zeta * delta( i, 2 ) for i in range( 4 ) ]
    , [ zeta * delta( i, 3 ) for i in range( 4 ) ]
]

