# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:19:32 2019

@author: snnch

Computational Science assignment 3 Question 2c

Name:       Yiqing Cao
Student #:  100661688

This script compute a polynomial interpolant
by getting coefficient a. 
A figure is drawn to show that the points provided
fits in the polynomial function.
"""
import scipy
import numpy as np
import matplotlib.pyplot as plt

k = [0,1,2,3,4]
n = len(k)
x = [0,1,2,3,4]
y = [0,1,5,14,35]
M = scipy.zeros([n,n])

# putting the according x to the vandermone matrix
for i in range(n):
    for j in range(n):
        M[i,j] = x[i]**j
            
a = np.linalg.solve(M, y)

print(M)
print(a)

# This line is used to varify that 
# a * M is equal to y
print(np.allclose(np.dot(M,a),y))

# To plot the interpolant, I created a list of x first
# and then calculate y using x and a that we just got
# y = aa sumof(a_k * x**k)
x_func = np.linspace(0,5,50)
y_func = []
for i in range(50):
    sum = 0
    for j in range(n):
        sum += a[j] * x_func[i]**j
    y_func.append(sum)
print(y_func)

#plot the points according to the provided x and y 
plt.plot(x, y, 'ro')
#plot the interpolant
plt.plot(x_func, y_func)

plt.show()
