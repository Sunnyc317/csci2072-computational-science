# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:53:52 2019

@author: snnch
Functionality:
    Test program for tridag_matvec.py, 
    the program test tridg_matvec.py with matrix of sizes from 
    10**2 to 10**4. (instead of 10**2 to 10**7)
    scipy.dot would used up my laptop's RAM 
    if the number goes up to 10**5

Name: Yiqing Cao
Student number: 100661688
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg
import scipy
import random
import time
import tridag_matvec

times = []
times2 = []
dottimes = []
xaxis = []
xaxis2 = []
# Anything bigger than 5 would crash my laptop
for k in range(2,5):
    n = 10**k
    xaxis.append(n)
    print("n = ",n)
    
    A = scipy.zeros(n)
    B = scipy.zeros(n-1)
    C = scipy.zeros(n-2)
    X = scipy.zeros(n)
    # Declaring matrixes A, B, C (the vectors that define 
    # matrix A in the question) and multiplier matrix X of size 1*n

    for i in range(0,n):
        x = random.random()
        A[i] = x
        
    for i in range(0,n-1):
        y = random.random()
        B[i] = y
    
    for i in range(0,n-2):
        z = random.random()
        C[i] = z
        
    for i in range(0,n):
        q = random.random()
        X[i] = q
    # put random numbers in matrix A, B, C and X
        
    start = time.time()
    Y1 = tridag_matvec.gety(A,B,C,X)
    end = time.time()
    times.append(end-start)
    # Getting the time it takes to get the multiplication of 
    # the triple diagonal matrix and X and put the time in a list. 
    
    start = time.time()
    Y2 = tridag_matvec.builtingety(A,B,C,X)
    end = time.time()
    dottimes.append(end-start)
    
    print("built-in method time cost: ", dottimes[k-2])
    print("my algorithm time cost: ",times[k-2])
    # print the time it took for different methods to get the result
    print()

plt.semilogx(xaxis, times, label = "my algorithm")
plt.semilogx(xaxis, dottimes, label = "scipy.dot")
'''
plt.semilogx(xaxis, times, xaxis, dottimes)
plt.xlabel("matrix row/column number")
'''
plt.ylabel("time")
plt.legend()
plt.show()


for k in range(2,8):
    n = 10**k
    xaxis2.append(n)
    
    A = scipy.zeros(n)
    B = scipy.zeros(n-1)
    C = scipy.zeros(n-2)
    X = scipy.zeros(n)
    # Declaring matrixes A, B, C (the vectors that define 
    # matrix A in the question) and multiplier matrix X of size 1*n

    for i in range(0,n):
        x = random.random()
        A[i] = x
        
    for i in range(0,n-1):
        y = random.random()
        B[i] = y
    
    for i in range(0,n-2):
        z = random.random()
        C[i] = z
        
    for i in range(0,n):
        q = random.random()
        X[i] = q
    # put random numbers in matrix A, B, C and X
        
    start = time.time()
    Y1 = tridag_matvec.gety(A,B,C,X)
    end = time.time()
    times2.append(end-start)

print("time plot of my algorithm: ")
plt.loglog(xaxis2, times2)
plt.show()
