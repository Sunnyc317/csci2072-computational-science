# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:14:50 2019

@author: sunny cao
"""
import math


def m(x_init, k, eps_x, eps_y):
    x = x_init
    print('0 iteration: x = %f' % (x))
    for i in range(1,k+1):
        x_init = x
        x = G(x_init)
        print('%d iteration: x = %f' % (i, x))
        print('\testimate error: %f, residual: %f' %(abs(x-x_init),abs(F(x))))
        if abs(x-x_init) <= eps_x and abs(F(x)) <= eps_y:
            print('converged')
            return x
    
    print('no convergence')
    return x
    
def G(x):
    return (math.sin(math.pi*x)-x**2)/(2*math.pi)+x

def F(x):
    return math.sin(math.pi*x)-x**2

m(1.4,40,1e-6,1e-6)