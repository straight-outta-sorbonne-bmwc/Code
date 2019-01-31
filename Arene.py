#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:23:51 2019

@author:  3670527
"""
import numpy as np
import random
class Arene:
    def __init__(self):
        self.Matrice=np.zeros((10,10))
        for i in range(15):
            u=random.randint(0,9)
            v=random.randint(0,9)
            self.Matrice[u][v]=1
    

arene = Arene()
print(arene.Matrice)