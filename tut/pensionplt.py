# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:10:47 2019

@author: snnch
"""

import math
import scipy
import matplotlib.pyplot as plt
from UIRP import *
from Newton_method import Newton

# Set parameters
n = 12.0
TbyP = 10.0

# Plot to estimate where the solution is 
xs = scipy.linspace(0,0.1,100)
ys = F(xs, n, TbyP) #putting array in the first parameter
plt.plot(xs, ys)
plt.plot([0.,0.1],[0.,0.])
plt.show()

#set initial point
x0 = 0.019
#x0 = x

#Set Newton parameters
#the error bound goes from 0.1 to 10**-2, 10**-4, 10**-8, 10**-16...
#We only have 14 digits after the point, so no point to go further
kmax = 6
tolx = 1e-14
tolf = 1e-14

#Re-define the function and its derivative to have a single input
def f(x):
    return F(x,n,TbyP)
def df(x):
    return DF(x,n,TbyP)

#Call Newton
x,err, res = Newton(f,df,x0,tolx,tolf,kmax)








#