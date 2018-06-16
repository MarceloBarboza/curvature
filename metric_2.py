#!/usr/bin/env python3

from sympy import *

x = [ var( 'x_%d' %i ) for i in range( 4 ) ]

zeta_0 = -1
zeta_1 = Function( 'zeta_1' )( x[0], x[1] )
zeta_2 = Function( 'zeta_2' )( x[0], x[2] )
zeta_3 = Function( 'zeta_3' )( x[0], x[3] )

def delta( i, j ):
    if i in range( 4 ) and j in range( 4 ):
        if i == j:
            return 1
        else:
            return 0

GG = [
      [ zeta_0 * delta( 0, j ) for j in range( 4 ) ] 
    , [ zeta_1 * delta( 1, j ) for j in range( 4 ) ]
    , [ zeta_2 * delta( 2, j ) for j in range( 4 ) ]
    , [ zeta_3 * delta( 3, j ) for j in range( 4 ) ]
]
