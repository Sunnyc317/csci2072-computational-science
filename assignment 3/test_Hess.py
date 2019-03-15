# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 02:04:33 2019

@author: snnch

Computational Science assignment 3 Question 1d

Name:       Yiqing Cao
Student #:  100661688

This script is written to test Hess_LUP.py

"""
import scipy
from Hess_LUP import LUP 
from PLU import PLU
import time
import matplotlib.pyplot as plt

times = []
for i in range(8):
    n = 2**(i+4)
    A = scipy.random.rand(n,n);
    for i in range(2,n):
        for j in range(i-2):
            A[i,j] = 0;
    start = time.time()
    L,U,P,ok = LUP(A)
    end= time.time()
    times.append([n,end-start])
    #print('Matrix is\n')
    #print(A)
    
times = scipy.asarray(times)
plt.plot(times[:,0], times[:,1], '-b', label = "wall time")
plt.plot(times[:,0],1e-4*3*(times[:,0]-1),'r-', label = "flops")

'''
plt.loglog(times[:,0], times[:,1], '-b', label = "wall time")
plt.loglog(times[:,0],1e-4*3*(times[:,0]-1),'r-', label = "flops")
'''
plt.xlabel("square matrix size n")
plt.ylabel("wall time of Hess_LUP")
plt.legend()
plt.show()





'''
A = scipy.random.rand(4,4);
for i in range(2,4):
    for j in range(i-1):
        A[i,j] = 0
L,U,P,ok = LUP(A)
L2, U2, P2, ok2 = PLU(A)
print('Matrix is\n')
print(A)
print('\nL is \n')
print(L)
print('\nU is \n')
print(U)
print('\nP is \n')
print(P)

print("\nThis is PLU\n")

print('\nL2 is \n')
print(L2)
print('\nU2 is \n')
print(U2)
print('\nP2 is \n')
print(P2)
'''