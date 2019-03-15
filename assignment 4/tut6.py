# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:26:44 2019

@author: snnch

Yiqing Cao
100661688

These functions use vandermonde matrix to calculate the coefficients of
the polynomials and calculate the corresponding y values with these 
coefficients
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def Vandermonde(x):
    n = len(x)
    V = np.ones((n,n))
    for i in np.arange(1,n):
        V[:,i] = V[:,i-1] * x
    #print('The condition number is ' + str(la.cond(V)))
    return(V)
    
def Inter(x,y):
    V = Vandermonde(x)
    return la.solve(V,y)

def PolyEval(a,x):
    y = np.zeros(len(x))
    #x = np.array(x)
    #y = np.array(y)
    for i in range(len(a)):
        y += a[i] * np.power(x,i)
    return y

'''
N = 12

x = np.array(range(N))
y = x**2

a = Inter(x,y)

x_test = np.linspace(0,N-1,num = 1000)
y_test = PolyEval(a,x_test)
'''
#plt.semilogy(x,y,'.', label = 'Data')
#plt.semilogy(x_test,y_test,label = 'Fit')
#plt.legend()
#plt.show()

#print(PolyEval(a, x))