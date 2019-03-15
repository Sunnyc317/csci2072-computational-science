# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 03:29:59 2019

@author: snnch
"""

from midterm1 import bisection 
from midterm1 import Newton
from midterm1 import PLU
import math
import numpy as np
import scipy.linalg
#from dist import dist

# condition number: numpy.linalg.cond(M,p) p is usually 2 for 2 norm
# norm: scipy.linalg.norm(M, p)
A = scipy.matrix([[1,-3,1],[-2,-1.5,3],[2.5,6,1.5]])
x = scipy.matrix([[0.99960385],[-1.99996435],[-1.0000192]])
b = scipy.matrix([[6],[-11.8],[-11]])
print(np.linalg.cond(A) * scipy.linalg.norm(np.dot(A,x)-b) / scipy.linalg.norm(b))
print(scipy.linalg.norm(np.dot(A,x)-b))
print(scipy.linalg.norm(b))

'''
A = scipy.matrix([[1,-3,1],[-2,-1.5,3],[2.5,6,1.5]])
#A = scipy.matrix([[3,-1,1],[1,-1.5,3],[2.5,6,1.5]])

L,U,P,ok = PLU(A)

print('Matrix is\n')
print(A)
print('L is \n')
print(L)
print('U is \n')
print(U)
print('P is \n')
print(P)
'''
'''

def F(x,a=0):
    return x*math.sin(x) - 1

def df(x,a=0):
    return math.sin(x) + x * math.cos(x)

bisection(F,1,2,3,10,1e-10,0.05)
Newton(F,df,3,1e-5, 1e-5,4)
'''

'''

theta_c,result = bisection(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)
theta_c, result2 = secant(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)

plt.plot(result[:,0],result[:,1], label = "biseation")
plt.plot(result2[:,0],result2[:,1], label = "secant")
plt.legend()
plt.show()
'''

'''
xs = scipy.linspace(0,0.1,100)
ys = F(xs, n, TbyP) #putting array in the first parameter
plt.plot(xs, ys)
plt.plot([0.,0.1],[0.,0.])
plt.show()
#graphing a function to find initial point
'''

