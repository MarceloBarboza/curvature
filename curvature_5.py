#!/usr/bin/env python3

from metric_5 import *

n = len( x )

G = Matrix( GG )
H = G ** -1

def Gamma( i, j, k ):
    gamma = 0
    for l in range( n ):
        gamma += 1/2 * (
                + diff( G[ j, l ], x[ i ] )
                + diff( G[ l, i ], x[ j ] )
                - diff( G[ i, j ], x[ l ] )
        ) * H[ l, k ]
    return simplify( gamma )

# Rm_{i, j, k}^l:
def Rm1( i, j, k, l ):
    rm1 = (
        + diff( Gamma( i, k, l ), x[ j ] )
        - diff( Gamma( j, k, l ), x[ i ] )
    )
    for m in range( n ):
        rm1 += (
                + Gamma( i, k, m ) * Gamma( m, j, l )
                - Gamma( j, k, m ) * Gamma( m, i, l )
        )
    return simplify( rm1 )

# Rm_{i, j, k, l}:
def Rm2( i, j, k, l ):
    rm2 = 0
    for m in range( n ):
        rm2 += Rm1( i, j, k, l ) * G[ m, l ]
    return simplify( rm2 )

def K( i, j ):
    if i != j:
        return simplify(
            Rm2( i, j, i, j ) * (
                + G[ i, i ] * G[ j, j ]
                - G[ i, j ] * G[ i, j ]
            ) ** -1
        )

def Rc( i, j ):
    rc = 0
    for k in range( n ):
        rc += Rm1( i, k, j, k )
    return simplify( rc )

r = 0
for i in range( n ):
    for j in range( n ):
        r += H[ i, j ] * Rc( i, j )
R = simplify( r )

def Rc0( i, j ):
    return simplify( Rc( i, j ) - R/n * G[ i, j ] )

def Hessh( i, j ):
    hessh = diff( h, x[ i ], x[ j ] )
    for k in range( n ):
        hessh -= Gamma( i, j, k ) * diff( h, x[ k ] )
    return simplify( hessh )

laph = 0
for i in range( n ):
    for j in range( n ):
        laph += H[ i, j ] * Hessh( i, j )
Laph = simplify( laph )

def Hessh0( i, j ):
    return simplify( Hessh( i, j ) - Laph/n * G[ i, j ] )

import sys

orig_stdout = sys.stdout
f = open('curvature_5.tex', 'w')
sys.stdout = f

for i in range( n ):
    for j in range( i, n ):
        print(
            "\ZZ{\partial_"'%d' %i
            ,"}{\partial_"'%d' %j
            ,"} & ="
            , latex( Rc0( i, j ) )
            , "\\\\"
        )

for i in range( n ):
    for j in range( i, n ):
        print(        
            "\WW{\partial_"'%d' %i
            ,"}{\partial_"'%d' %j
            ,"} & ="
            , latex( Hessh0( i, j ) )
            , "\\\\"
        )

sys.stdout = orig_stdout
f.close()