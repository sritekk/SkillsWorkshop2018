# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:20:52 2018

@author: Srinivas
"""

import numpy as np

X = np.arange(1, 1000)

Y = X[(X % 3 == 0) | (X % 5 == 0)]

Z = sum(Y)

print(Z)

