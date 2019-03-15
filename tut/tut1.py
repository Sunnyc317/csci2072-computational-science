# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def phi(x, a):
    return (x+a/x)/2

def iterate(x, a, k, eps):
    for i in range (k):
        x_kp1 = phi(x, a)
        print(x_kp1)
        if abs(x_kp1-x) < eps:
            return x_kp1
        x = x_kp1
    return x_kp1



def bigF(x, a):
    return x**2-a
'''
def bisection(F,m, a, b, k, err_x, err_y):
    c = 0
    for i in range(k):
        c = (a+b)/2
        print(c," is the middle point")
        #print(a," is the upper boundary")
        #print(b," is the lower boundary")
        
        f_c = F(c,m)
        f_a = F(a,m)
        if f_c*f_a < 0:
            b = c
        else:
            a = c
        if abs(f_c-f_a) < err_y or abs(a-b) < err_x:
            return c
    return c
'''
def bisection(F,m, a, b, k, err_x, err_y):
    c = 0
    result = np.zeros((k,3))
    for i in range(k):
        c = (a+b)/2
        print(c," is the middle point")
        print(a," is the left boundary")
        print(b," is the right boundary")
        f_c = F(c,m)
        f_a = F(a,m) 
        print(abs(f_c-f_a), " is the residual")
        result[i] = i,abs(b-a), abs(F(c,m))
        if f_c*f_a < 0:
            b = c
        else:
            a = c
        if abs(f_c-f_a) < err_y or abs(a-b) < err_x:
            print("bisaection converged")
            return c, result
    print("bisaection not converged")
    return c,result

iterate(3.0,19,4,0.1)
    
bisection(bigF,19.0,0.0,20.0,10, 10**(-3), 10**(-3))
