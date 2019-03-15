# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 03:13:34 2019

@author: snnch
"""

import numpy as np
import matplotlib.pyplot as plt
#from dist import dist

'''
xs = scipy.linspace(0,0.1,100)
ys = F(xs, n, TbyP) #putting array in the first parameter
plt.plot(xs, ys)
plt.plot([0.,0.1],[0.,0.])
plt.show()
#graphing a function to find initial point
'''

def bisection(F,m, a, b, k, err_x, err_y):
    c = 0
    result = np.zeros((k,3))
    for i in range(k):
        c = (a+b)/2
        #print(c," is the middle point")
        print(a," is the left boundary")
        print(b," is the right boundary")
        f_c = F(c,m)
        f_a = F(a,m) 
        print(abs(a-b), " is the error")
        print(abs(f_c-f_a), " is the residual")
        result[i] = i,abs(b-a), abs(F(c,m))
        if f_c*f_a < 0:
            b = c
        else:
            a = c
        print()
        if abs(f_c-f_a) < err_y or abs(a-b) < err_x:
            print("bisaection converged")
            return c, result
    print("bisaection not converged")
    return c,result

def secant(F,m, x0, x1, k=10, err_x=10**-4, err_y=10**-4):
    results = np.zeros((k,3))
    xnew = 0
    
    for i in range(k):
        xnew = x1 - F(x1,m) * (x1 - x0) / (F(x1,m) - F(x0,m))
        results[i] = i, abs(xnew - x1), abs(F(xnew, m))
        if (abs(xnew - x1)<err_x) and (abs(F(xnew,m))<err_y):
            print("secant converged")
            return xnew,results[:i]
        x0 = x1
        x1 = xnew
    
    print('secant not converged')
    return xnew,results



# Testing secant and bisection
# dist imported from dist.py
'''
theta_c,result = bisection(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)
theta_c, result2 = secant(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)

plt.plot(result[:,0],result[:,1], label = "biseation")
plt.plot(result2[:,0],result2[:,1], label = "secant")
plt.legend()
plt.show()
'''


def Newton(f,df,x0,tolf,tolx,kmax):
    x = x0
    conv = 0
    for i in range(1,kmax+1):
        r = f(x)
        dx = - r/df(x)
        x = x + dx
        err = abs(dx)
        res = abs(r)
        print('it=%d x=%e err=%e res=%e' % (i,x,err,res))
        if err < tolx and res < tolf :
            conv = 1
            break
    if conv ==0:
        print('No convergance')
    return x,err,res


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
            L[i-1,j-1] = U[i-1,j-1]/U[j-1,j-1]
            for k in range(j,n+1):
                U[i-1,k-1] = U[i-1,k-1] - L[i-1,j-1] * U[j-1,k-1]
    return L,U,P,ok

def swap(M,i,k,n):
    dum = copy.copy(M[i,0:n])
    M[i,0:n] = copy.copy(M[k,0:n])
    M[k,0:n] = copy.copy(dum)
    return M
    