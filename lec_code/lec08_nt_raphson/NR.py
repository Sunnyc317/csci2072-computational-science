# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:39:59 2019

@author: snnch
for lec08.py
"""

import math
import scipy
import scipy.linalg

def NR(f,Df,x0,epsx,epsf,kmax):
    conv = 0
    x = scipy.matrix(x0)
    for k in range(0,kmax):
        r = -f(x)
        J = Df(x)
        
    