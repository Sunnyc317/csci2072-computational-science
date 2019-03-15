# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:29:54 2019

@author: snnch

# Lecture 5 code
# LU decomposition
# input: n X n matrix A
# Output: n X n matrices L and U such that LU = A and L and U are 
# triangular matrix
"""
    



import math
import scipy
import copy

def PLU(A):
    # throw warning flag when the number is too small
    # (close to 0)
    ok = 1
    small = 1e-12
    
    n = scipy.shape(A)[0]
    U = copy.copy(A)
    L = scipy.identity(n)
    P = scipy.identity(n)
    for j in range(1,n):
        print(j," operation")
        print("This is U")
        print(U)
        print("This is L")
        print(L)
        print("This is P")
        print(P)
        print()
        s = scipy.argmax(abs(U[j-1:n,j-1])) + j-1 
        # argmax returs the index of that number
        if s != j-1:
            U = swap(U,s,j-1,n)
            P = swap(P,s,j-1,n)
            if j > 1:
                L = swap(L,s,j-1,j-1)
                
        for i in range (j+1,n+1):
            if abs(U[j-1,j-1]) < small:
                print("Near-zero pivot!")
                ok = 0
                break
            L[i-1,j-1] = float(U[i-1,j-1])/float(U[j-1,j-1])
            for k in range(j,n+1):
                U[i-1,k-1] = float(U[i-1,k-1]) - L[i-1,j-1] * U[j-1,k-1]
    return L,U,P,ok

def swap(M,i,k,n):
    dum = copy.copy(M[i,0:n])
    M[i,0:n] = copy.copy(M[k,0:n])
    M[k,0:n] = copy.copy(dum)
    return M
