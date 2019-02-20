# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:04:51 2019

@author: franc
"""

import numpy as np
import Robot
import Arene
from tkinter import*		
import calcul		
import time							
#test----------------------------
robot=Robot.Robot(500, 500, 50, 50)
arene=Arene.Arene(700, robot)
tk = Tk()
canvas = Canvas(tk, width = arene.taille, height = arene.taille , bd=0, bg="black")
canvas.pack(padx=10,pady=10)

def vers():
    print("Valeur de x")
    x=input()
    print("Valeur de y")
    y=input()
    coord=(float(x), float(y))
    pos=(robot.x, robot.y)
    while(calcul.distance(pos, coord)>3):
        print(calcul.distance(pos, coord))
        res=robot.avancevers(coord)
        pos=(robot.x, robot.y)
        print(robot.x, robot.y)
        time.sleep(0.025)
        canvas.move(r, res[0], res[1])
        canvas.update()
    print(robot.x, robot.y)


r=canvas.create_rectangle(robot.y, robot.x, robot.y+robot.longueur, robot.x+robot.largeur, fill="green")

avancer=Button(tk, text ='Avance', command = vers)
avancer.pack(side=RIGHT)

Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
Bouton_Quitter.pack(side=BOTTOM)
tk.mainloop()

