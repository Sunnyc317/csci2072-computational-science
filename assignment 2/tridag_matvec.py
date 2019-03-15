# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:40:13 2019

@author: snnch

Functionality: 
    gety(): my algorithm of calculating the multiplication of a n by n
    triple diagonal matrix and a n by 1 matrix
    
    builtingety(): a method that use scipy.dot to get the result of the 
    mutiplication. Argument A, B and C are put in a matrix first to create a 
    triple diagonal matrix. 

Name: Yiqing Cao
Student number: 100661688
"""

import scipy


def gety(A,B,C,X):
    n = A.shape[0]
    # Getting the row number of A
    y = scipy.zeros(n)
    # Declaring a 1 by n zero matrix y
    
    for i in range(0,n-2):
        y[i] = A[i]*X[i] + B[i]*X[i+1]+ C[i]*X[i+2]
        # Assigning computed numbers to according index of y 
        # (for up to index n-2)
    y[n-2] = A[n-2]*X[n-2] + B[n-2]*X[n-1]
    y[n-1] = A[n-1]*X[n-1]
    # assgin the last 2 entries of Y
    
    return y

def builtingety(A,B,C,X):
    n = A.shape[0]
    # Getting the row number of A
    M = scipy.zeros((n,n))
    # Declaring a n by n zero matrix M
    
    for i in range(0,n-2):
        # Put A, B and C into M so that M is a triple diagonal matrix
        M[i,i] = A[i]
        M[i,i+1] = B[i]
        M[i,i+2] = C[i]
    M[n-2,n-2] = A[n-2]
    M[n-1,n-1] = A[n-1]
    M[n-2,n-1] = B[n-2]
    return scipy.dot(M,X)
    # Get the multiplication of M and X using built-in method scipy.dot
        
        
        