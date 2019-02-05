#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:04:24 2019

@author: 3671243
"""
from tkinter import *
import numpy as np
import Arene

tk = Tk()
dim = 10 #dimension de l' aréne
echelle = 25 #à l'échelle x25 sur la fenêtre tkinter

canvas = Canvas(tk,width = dim*echelle, height = dim*echelle , bd=0, bg="black")
canvas.pack(padx=10,pady=10)

"""Variable globale"""
tabx=[]
taby=[]
k=0
"""----------------"""

def coordObstacle(arene): #On récupére les coordonnées des obstacle
    for i in range(dim):
        for j in range(dim):
            if(arene.Matrice[i][j]==1):
                tabx.append(j)
                taby.append(i)
    

def afficheObstacle():
    global k
    canvas.create_rectangle(tabx[k]*echelle,taby[k]*echelle,tabx[k]*echelle+echelle,taby[k]*echelle+echelle,fill='red')
    k=k+1

#test----------------------------
arene=Arene.Arene(dim)
arene.ajouterObstacleAleatoire()
print(arene.Matrice)
coordObstacle(arene)
#---------------------------------

#On crée le bouton obstacle
afficheObstacle = Button(tk, text='obstacle', command=afficheObstacle)
afficheObstacle.pack(side=RIGHT)

#On crée le bouton quitter
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
Bouton_Quitter.pack(side=BOTTOM)
tk.mainloop()
    
