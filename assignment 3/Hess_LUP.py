# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:02:08 2019

@author: snnch

Computational Science assignment 3 Question 1d

Name:       Yiqing Cao
Student #:  100661688

This function calculate the LUP matrices
for Hessenberg matrix 
(almost triangular matrix)

INPUT:  n by n Hessenberg matrix A
OUTPUT: L, U, P matrices and integer ok to show 
        if the matrix has near-zero pivot


"""
import math
import scipy
import copy

def LUP(A):
    # throw warning flag when the number is too small
    # (close to 0)
    ok = 1
    small = 1e-12
    
    n = scipy.shape(A)[0]
    U = copy.copy(A)
    L = scipy.identity(n)
    P = scipy.identity(n)
    for j in range(1,n):
        s = scipy.argmax(abs(U[j-1:n,j-1])) + j-1 
        # argmax returs the index of that number
        if s != j-1:
            U = swap(U,s,j-1,n)
            P = swap(P,s,j-1,n)
            if j > 1:
                L = swap(L,s,j-1,j-1)
        # Since the multiplier is zero after the
        # second row after the pivot row, we only
        # need to calculate one row for U and L, which is the
        # row under the pivot row
        i = j+1
        if abs(U[j-1,j-1]) < small:
            print("Near-zero pivot!")
            ok = 0
            break
        L[i-1,j-1] = float(U[i-1,j-1])/U[j-1,j-1]
        for k in range(j,n+1):
            U[i-1,k-1] = U[i-1,k-1] - L[i-1,j-1] * U[j-1,k-1]
    return L,U,P,ok

def swap(M,i,k,n):
    dum = copy.copy(M[i,0:n])
    M[i,0:n] = copy.copy(M[k,0:n])
    M[k,0:n] = copy.copy(dum)
    return M

