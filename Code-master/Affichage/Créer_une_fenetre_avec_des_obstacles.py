#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:41:19 2019

@author: 3671243
"""
from tkinter import *
import random 

tabx=[]
taby=[]
tabdx=[]
tabdy=[]
largeurObs=30 #longueur de l'obstacle
longueurObs=30 #largeur de l'obstacle
#Position du robot
posxRobot=250 
posyRobot=250
#Dimension du robot
largeurRobot=30
longueurRobot=20
#On ajoute les donnés ds le tableau
tabx.append(posxRobot)
taby.append(posyRobot)
tabdx.append(posxRobot+largeurRobot)
tabdy.append(posxRobot+longueurRobot)

def verif(x,y): #vérifie si on empiete pas sur un autre obstacle ou sur le robot
    i=0
    while i<len(tabx):
        if(x>=tabx[i] and x<=tabdx[i]):
            return 1
        if((y>=tabx[i] and y<=tabdx[i])):
            return 1
        if(y+largeurObs>dim or x+largeurObs>dim):
            return 1
        if(x+largeurObs>=tabx[i] and x+largeurObs<=tabdx[i]):
            return 1
        if(y+longueurObs>=tabx[i] and y+longueurObs<=tabdx[i]):
            return 1
        if((y>=tabx[i] and y<=tabdx[i])):
            return 1
        i=i+1
    return 0


#on crée notre fenêtre
tk = Tk()
dim =500
canvas = Canvas(tk,width = dim, height = dim , bd=0, bg="black")
canvas.pack(padx=10,pady=10)
 
#fonction qui crée les obstacle
def creeObstacle():
    x=random.randint(0,dim)
    y=random.randint(0,dim)
    if(verif(x,y)==0):
        tabx.append(x)
        taby.append(y)
        tabdx.append(x+longueurObs)
        tabdy.append(y+largeurObs)
        canvas.create_rectangle(x,y,x+largeurObs,y+longueurObs,fill='red')
    else:
        creeObstacle()

#On crée notre robot
canvas.create_rectangle(posxRobot,posyRobot,posxRobot+largeurRobot,posyRobot+longueurRobot,fill='green')

#création du bouton obstacle
cree_obstacle = Button(tk, text='obstacle', command=creeObstacle)
cree_obstacle.pack(side=RIGHT)

#création du bouton quitter
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
Bouton_Quitter.pack(side=BOTTOM)
tk.mainloop()