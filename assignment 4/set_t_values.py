# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:58:58 2019

@author: snnch

Yiqing Cao
100661688

This is a function that set t values to interpolate
with the provided set of points (x, y)

"""
import numpy as np

def set_t_values(x, y):
    t = []
    n = len(x)
    t.append(0);
    for i in range(1, n):
        t.append(t[i-1] + np.linalg.norm([x[i]-x[i-1],y[i]-y[i-1]]))
    return t
