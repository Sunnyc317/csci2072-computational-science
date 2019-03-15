# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:09:44 2019

@author: snnch

Yiqing Cao
100661688

Script for Assignment 4 question (c) & (d)
It contains 4 graphs that demonstrate question c and d

question d:
The curve looks smoother when cubic splines piecewise interpolation is used. 
Cubic splines is better than linear splines because the curve is differentiable 
at each knot and the first derivatives are the same at every knot when 
approaching from both side. 
The curve looks nicer when using cupic splines than the one using Lagrangian 
interpolation since it computes a polynomial between two knots instead of 
computing a single polynomial that goes through all knots. 

"""
import matplotlib.pyplot as plt
from set_t_values import set_t_values
from construct_pols import Lagrangian
from construct_pols import piecewise_cubic
from construct_pols import piecewise_linear
import numpy as np

xy1 = np.array([[0,2], [0.5,2.5], [1.1,2.7],        #first set of data
                [1,2], [0.2,2.1]])

N = 200                                             #set t values for the first
t1 = set_t_values(xy1[:,0], xy1[:,1])               #set of data
ts1 = np.linspace(t1[0], t1[-1], N)

xy2 = np.array([[0,2], [0.5,2.5], [1.1,2.7],        #second set of data
                [1,2], [0.2,2.1], [0,2.15], 
                [-0.3,2.15]])

t2 = set_t_values(xy2[:,0], xy2[:,1])               #set t values for the
ts2 = np.linspace(t2[0], t2[-1], N)                 #second set of data

print("Lagrangian interpolation using the first set of data")
Px, Py = Lagrangian(ts1, xy1)                       #Interpolating with new 
plt.plot(xy1[:,0], xy1[:,1], 'ro', Px, Py)          #added points using 
plt.show()                                          #lagrangian interpolation
                                                    #(interpolating through all
                                                    #points to create a 
                                                    #higher-order polynomial curve)

print("\nLagrangian interpolation using the second set of data")
Px2, Py2 = Lagrangian(ts2, xy2)                     #Interpolating with new 
plt.plot(xy2[:,0], xy2[:,1], 'ro', Px2, Py2)        #added points using 
plt.show()                                          #lagrangian interpolation

print("\nLinear piecewise interpolation using the second set of data")
Px3, Py3 = piecewise_linear(ts2, xy2)     
plt.plot(xy2[:,0], xy2[:,1], 'ro',Px3, Py3)         #Interpolating with new
plt.show()                                          #added points using 
                                                    #piecewise interpolation
print("\nCubic piecewise interpolation using the second set of data")
Px4, Py4 = piecewise_cubic(ts2, xy2)     
plt.plot(xy2[:,0], xy2[:,1], 'ro',Px4, Py4)         #Interpolating with new
plt.show()                                          #added points using 
                                                    #piecewise interpolation
