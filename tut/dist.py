#Author: Lennaert van Veen
#Date: 1/17/2019
# Python function that computes the distance travelled by a cannon ball with air friction.
# In: theta, angle of the shot; c, coefficient of air friction;
# g, accelleration of gravity; V0, initial speed. See lecture 2.
# A solution of dist=R is the angle at which to tilt the canon for given c, g and V0.

#This is tutorial 2

import numpy as np
import matplotlib.pyplot as plt
from tut1 import bisection

def dist(theta,param):
    c = param[0]
    g = param[1]
    V0 = param[2]
    R = param[3]
    return (1/c) * np.log((c * V0 * np.cos(theta) / np.sqrt(c * g)) *                    \
                       (np.arctan(np.sqrt(c/g) * V0 * np.sin(theta)) +                 \
                        np.arccosh(np.sqrt((g + c * V0**2 * np.sin(theta)**2)/g))) + 1.0) - R
'''
def bisection(F,m, a, b, k, err_x, err_y):
    c = 0
    result = np.zeros((k,3))
    for i in range(k):
        c = (a+b)/2
        #print(c," is the middle point")
        #print(a," is the upper boundary")
        #print(b," is the lower boundary")
        f_c = F(c,m)
        f_a = F(a,m) 
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
'''

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


theta_c,result = bisection(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)
theta_c, result2 = secant(dist, [10**-3,9.81,40,100],1.0,1.4,30,10**-6, 10**-6)

plt.plot(result[:,0],result[:,1], label = "biseation")
plt.plot(result2[:,0],result2[:,1], label = "secant")
plt.legend()
plt.show()



#bisection(m, a, b, k, err_x, err_y)
print(theta_c)

