# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:53:46 2019

@author: snnch
"""
import numpy
import scipy
import matplotlib.pyplot as plt

def m(x_init, k, eps_x, eps_y, n = 1):
    x = G(x_init)
    print('%d iteration: x = %f' %(n,x))
    print('\testimate error: %f, residual: %f' %(abs(x-x_init),abs(F(x))))
    if abs(x-x_init) <= eps_x and abs(F(x)) <= eps_y:
        print('converged')
        return x
    elif k == 0:
        print('no convergance')
        return x
    else:
        n += 1
        m(x, k-1, eps_x, eps_y, n)
        
def G(x):
    return (numpy.sin(numpy.pi*x)-x**2)/(2*numpy.pi)+x

def F(x):
    return numpy.sin(numpy.pi*x)-x**2

m(1.4,40,1e-6,1e-6)


'''
xs = scipy.linspace(-2.0,2.0,100)
ys = F(xs)
plt.plot(xs, ys)
plt.plot([-2.0,2.0],[0.,0.])
plt.show()


When x_init < 0: 
    The result would be too large after some iteration
    because ...
    
When x_init = 0:
    It would always converge at the first iteration 
    since the residual is 0

'''