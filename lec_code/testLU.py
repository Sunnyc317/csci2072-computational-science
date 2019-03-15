# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:02:47 2019

@author: snnch
"""

import scipy
import math
from PLU import PLU

A = scipy.matrix([[3,-1,1,2],[1,4,-2,3],[0,-3,5,-5],
                  [0,0,3,1]])

L,U,P,ok = PLU(A)

print('Matrix is\n')
print(A)
print('L is \n')
print(L)
print('U is \n')
print(U)
print('P is \n')
print(P)