# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:48:56 2019

@author: snnch
"""
def iteration(f, fp, x, eps, n):
    for i in range (1,n+1):
        y1 = x
        y2 = y1-f(y1)/fp(y1)
        y3 = y2-f(y2)/fp(y2)
        
        x = y1 - (y2-y1)**2/(y3-2*y2+y1)
        
        fx = abs(f(x))
        print('%d iteration: x = %f' %(i,x))
        print('f(x) = %f' %(fx))
        if fx < eps:
            print("converged!")
            print("x* = %f" %(x))
            break

def ntiteration(f, fp, x, eps, n):
    for i in range (1,n+1):
        x = x - f(x)/fp(x)
        fx = abs(f(x))
        print('%d iteration: x = %f' %(i,x))
        print('f(x) = %f' %(fx))
        if fx < eps:
            print("converged!")
            print("x* = %f" %(x))
            break
        