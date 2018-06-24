#!/usr/bin/env python3

from sympy import *

x = [ Symbol( 'x_%d' %i ) for i in range( 3 ) ]

zeta_0 = Function( 'zeta_0' )( x[ 1 ], x[ 2 ] )
zeta_1 = Function( 'zeta_1' )( x[ 0 ], x[ 2 ] )
zeta_2 = Function( 'zeta_2' )( x[ 0 ], x[ 1 ] )

def delta( i, j ):
    if i in range( 3 ) and j in range( 3 ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [ zeta_0 * delta( 0, j ) for j in range( 3 ) ] 
    , [ zeta_1 * delta( 1, j ) for j in range( 3 ) ]
    , [ zeta_2 * delta( 2, j ) for j in range( 3 ) ]
]

h = Function( 'h' )( x[ 0 ], x[ 1 ], x[ 2 ] )
