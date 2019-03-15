# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:38:38 2019

@author: snnch

Yiqing Cao
100661688

These functions are written to calculate Px and Py -- the 
parameterized polynomials that describe the interpolated 
points
"""

from tut6 import Inter
from tut6 import PolyEval
from set_t_values import set_t_values
import scipy

def Lagrangian(ts, xy):
    t = set_t_values(xy[:,0], xy[:,1])
    ax = Inter(t, xy[:,0])
    ay = Inter(t, xy[:,1])
    
    Px = PolyEval(ax, ts)
    Py = PolyEval(ay, ts)
    
    return Px, Py

def piecewise_linear(ts, xy):
    t = set_t_values(xy[:,0], xy[:,1])
    Px = scipy.interpolate.interp1d(t, xy[:,0], kind = 'linear')
    Py = scipy.interpolate.interp1d(t, xy[:,1], kind = 'linear')
    
    return Px(ts), Py(ts)

def piecewise_cubic(ts, xy):
    t = set_t_values(xy[:,0], xy[:,1])
    Px = scipy.interpolate.interp1d(t, xy[:,0], kind = 'cubic')
    Py = scipy.interpolate.interp1d(t, xy[:,1], kind = 'cubic')
    
    return Px(ts), Py(ts)

