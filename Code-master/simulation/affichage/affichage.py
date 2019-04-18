import numpy as np
import time
import random
from tkinter import*

class AffichageTK(object):
    
    #rectangle_robot
    def __init__(self,arene,robot):
        self.robot=robot
        self.arene=arene
        self.dim=arene.taille
        self.l,self.r = None,None
    
    def affiche_obstacle(self):
        for i in self.arene.obstacles:
            self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='#000fff000')

    

    def start_affichage(self):
        self.root = Tk()                            # root variable contenant la fenÃªtre
        self.root.title('Tuto')                     # Nom de la fenÃªtre    
        
        self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='white')            # crÃ©ation de la fenÃªtre 
        self.can.pack()
        
        quitter = Button(self.root, text = 'quitter', command=self.deleteMe)                # bouton pour quitter la fenÃªtre
        quitter.pack(side=BOTTOM)
        if not self.arene.stop:
            self.root.after(5,self.updateA)

        self.root.mainloop()
        
    def updateA(self):
        self.deleterobot()
        self.affiche_robot()
        self.root.after(5,self.updateA)


    def deleteMe(self):
        self.arene.stop = True
        time.sleep(1)
        self.root.destroy()
    
    def affiche_robot(self):
        
        self.r=self.can.create_polygon(self.robot.a[0],self.robot.a[1],self.robot.b[0],self.robot.b[1],self.robot.c[0],self.robot.c[1],self.robot.d[0],self.robot.d[1],fill="black")
        self.l=self.can.create_line(self.robot.x, self.robot.y, self.robot.ptv[0] , self.robot.ptv[1], arrow='last', fill='red')
        self.t=self.can.create_line(self.robot.ptv[0] , self.robot.ptv[1], self.robot.ptv[0]+1 , self.robot.ptv[1]+1, fill='green')
        for i in self.arene.obstacles:
            self.can.create_rectangle(i.x-i.taille/2, i.y-i.taille/2, i.x+i.taille/2, i.y+i.taille/2,fill='maroon2')
           
        self.can.update()
    def deleterobot(self):
        if self.l:
            self.can.delete(self.l)
        if self.r: 
            self.can.delete(self.r)
        
