#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:25:01 2019

@author: 3671243
"""

from tkinter import *
import numpy as np
import math
import time

tk = Tk()

canvas = Canvas(tk,width = 700, height = 700 , bd=0, bg="black")
canvas.pack(padx=10,pady=10)

robot=[(500, 500), (600, 500), (600, 550), (500, 550)]
angle=0

r=canvas.create_polygon(robot, fill='red', width=2)

def dist(a,b):
    return round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 1)

def calculVecteur(a, b):
    u=b[0]-a[0]
    v=b[1]-a[1]
    return u,v

def normVecteur(a):
    return round(math.sqrt(a[0]*a[0]+a[1]*a[1]), 1)

def normalize(a):
    n=normVecteur(a)/4
    return round(a[0]/n,1), round(a[1]/n,1)
    
def angle2vect(a,b):
    in1=a[0]*b[0]+a[1]*b[1]
    in2=normVecteur(a)*normVecteur(b)
    return round(math.acos(in1/in2)*(180/math.pi),1)

    
def rotatePoint(M, O, angle) :
    angle *=math.pi / 180
    xM = M[0] - O[0]
    yM = M[1] - O[1]
    x = xM * math.cos(angle) + yM*math.sin(angle) + O[0]
    y =  -xM * math.sin (angle) + yM * math.cos (angle) + O[1]
    liste=[round(x,1),round(y,1)]
    return liste;

def rotateRobot():
    global r, robot
    canvas.delete(r)
    listeR=[]
    l=[]
    robotbis=[]
    for i in range (0, len(robot)-1):
        listeR=listeR+rotatePoint(robot[i], robot[len(robot)-1], angle)
        l=rotatePoint(robot[i], robot[len(robot)-1], angle)
        robotbis.append((l[0],l[1]))
        
    robotbis.append(robot[len(robot)-1])
    listeR.append(robot[len(robot)-1])
    r=canvas.create_polygon(listeR, fill='red', width=2)
    robot=robotbis[:]

def avancer():
    global r, angle, robot
    print('Position x')
    x=input()
    print('position y')
    y=input()
    pos=(int(x),int(y))
    vect1=calculVecteur(robot[len(robot)-1], pos)
    vect2=calculVecteur(robot[len(robot)-1], robot[len(robot)-2])
    norm=normalize(vect1)
    angle=angle2vect(vect1,vect2)
    rotateRobot()
    while dist(robot[len(robot)-1], pos)>10:
        l=[]
        for i in range(0, len(robot)):
            x=(round(robot[i][0]+norm[0],1), round(robot[i][1]+norm[1],1))
            l.append(x)
        robot=l[:]
        time.sleep(0.025)
        canvas.move(r, norm[0], norm[1])
        canvas.update()
        

avancer=Button(tk, text ='Avance', command = avancer)
avancer.pack(side=RIGHT)

Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
Bouton_Quitter.pack(side=BOTTOM)
tk.mainloop()
    