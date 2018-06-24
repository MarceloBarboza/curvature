#!/usr/bin/env python3

from curvature import *

def T( i, j ):
    if i in range( n ) and j in range( n ):
        if i != j:
            return 0
        else:
            if i == 0:
                return simplify(
                    (
                        ( mu + rho ) / sqrt( e[ 0 ] * G[ 0, 0 ] )
                    ) + rho * G[ 0, 0 ]
                )
            else:
                return rho * G[ i, i ]

def semi_divT( i ):
    if i in range( n ):
        semi_div = diff( T( i, i ), x[ i ] ) / ( e[ i ] * G[ i, i ] )
        for j in range( n ):
            semi_div -= (
                e[ j ] * G[ j, j ]
            ) ** -1 * (
                + T( i, i ) * Gamma( j, j, i )
                + T( j, j ) * Gamma( i, j, j )
            )
        return simplify( semi_div )

import sys

orig_stdout = sys.stdout
f = open('divergence_2.tex', 'w')
sys.stdout = f

for i in range( n ):
    print(
        "\\frac{(\mbox{div}_g\mathbb{T})(E_"'%d' %i,")}{\eta_"'%d' %i
        ,"} & ="
        , latex( semi_divT( i ) )
        , "\\\\"
    )

sys.stdout = orig_stdout
f.close()