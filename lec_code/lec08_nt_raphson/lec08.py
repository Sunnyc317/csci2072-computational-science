# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:26:48 2019

@author: snnch

lecture 8
"""

import scipy
import math
from functions import f, Df
import matplotlib.pyplot as plt
import NR


#initialize th eNR parameters
epsf = 1e-13
epsx = 1e-13
kmax = 10
#initialize x
x0 = scipy.ones([2,1])

x, err, res, conv = NR.NR(f,Df,x0,epsx,epsf,kmax)