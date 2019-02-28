import numpy as np
from module_arene import Arene
from module_robot import Robot
from module_robot import calcul
import time
import random
from tkinter import*

class AffichageTK(object):
    
    #rectangle_robot
    def __init__(self, arene, robot):
        self.arene=arene
        self.robot=robot
        self.dim=arene.taille
        self.root = Tk()							# root variable contenant la fenêtre
        self.root.title('Tuto')						# Nom de la fenêtre	
        self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='pink')			# création de la fenêtre 
        self.can.pack()	
        self.affiche_robot()								
        quitter = Button(self.root, text = 'quitter', command=self.root.destroy)				# bouton pour quitter la fenêtre
        quitter.pack(side=BOTTOM)							# emplacement des boutons
        self.root.mainloop()
    
    def affiche_obstacle(self):
        for i in self.arene.obstacles:
            self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='yellow')
    
    		
    def affiche_robot(self):
        #self.r = self.can.create_rectangle(self.robot.y, self.robot.x, self.robot.y+self.robot.longueur, self.robot.x+self.robot.largeur, fill="black")
        self.can.create_rectangle(self.robot.x-(self.robot.longueur/2), self.robot.y-(self.robot.longueur/2), self.robot.x+(self.robot.longueur/2), self.robot.y+(self.robot.longueur/2), fill="green")
        self.can.create_line(self.robot.x, self.robot.y, self.robot.ptv[0] , self.robot.ptv[1], arrow='last', fill='blue')

        
    def deleterobot(self,robot):
        self.can.delete(robot)
    
