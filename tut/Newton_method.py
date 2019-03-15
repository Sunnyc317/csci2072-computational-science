# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:35:20 2019
a method for pensionplt.py
@author: snnch
"""

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
    