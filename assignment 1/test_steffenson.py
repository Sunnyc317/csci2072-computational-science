# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:21:40 2019

@author: snnch
"""
import steffenson
import math

def function(x):
    return math.exp(-x**2+x) - x/2 - 1.0836

def functionprime(x):
    return ((-2) * x + 1) * math.exp(-x**2 + x) - 1/2

steffenson.iteration(function, functionprime, 1, 1e-12, 10)
print('\n\n')
steffenson.ntiteration(function, functionprime, 1, 1e-12, 10)