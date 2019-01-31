#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 08:36:59 2019

@author:  3670527
"""

class Roue:
    def __init__(self):
        self.orientationRoue=[0,0]
        
    def TournerRoue(self, posRobot, posArrivee):
        vecteurRoue=[]
        vecteurRoue[0]=posArrivee[0]-posRobot[0]
        vecteurRoue[1]=posArrivee[1]-posRobot[1]
        return vecteurRoue
