# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:52:15 2019

@author: snnch
"""

import math
import numpy as np
import scipy.linalg
import random

C = scipy.zeros((4,4))
A = scipy.zeros((4,4))
B = scipy.zeros((4,4))

for i in range(4):
    for j in range (i):
        x = random.random()
        A[i,j] = x
        
for i in range(4):
    for j in range (i):
        x = random.random()
        B[i,j] = x
        
for i in range(4):
    for j in range(4):
        for k in range(4):
            if j<i:
                C[i,j] = C[i,j] + A[i,k]*B[k,j]
                
print(C)