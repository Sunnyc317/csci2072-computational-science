# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:14:49 2019

@author: snnch
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def Make_V(n):
    V = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            V[i,j] = (-1)**(i+j) / (i+2*j+3.0)
    return V

results = np.zeros((9,3))

print(Make_V(4))

for i in range(9):
    V = Make_V(i+2)
    
    r = V[:,0]
    e1 = np.zeros(i+2)
    e1[0] = 1
    
    x = la.solve(V,r)
    
    results[i] = la.norm(x - e1) / la.norm(e1) , la.norm(np.dot(V,x) - r) / la.norm(r), la.cond(V)
    
n = np.arange(2,11)
plt.semilogy(n,results[:,2],label = 'Condition Number')
plt.legend()
plt.show()

plt.figure(2)
plt.semilogy(n,results[:,0], label = 'Relative Error')
plt.semilogy(n,results[:,1], label = 'Relative Residual')
plt.semilogy(n,results[:,2] * results[:,1], label = 'Maximum Error')
plt.legend()
plt.show()