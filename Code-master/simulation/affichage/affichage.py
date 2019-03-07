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
        self.root = Tk()                            # root variable contenant la fenÃªtre
        self.root.title('Tuto')                     # Nom de la fenÃªtre    
        
        self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='pink')            # crÃ©ation de la fenÃªtre 
        self.can.pack()
        
        quitter = Button(self.root, text = 'quitter', command=self.root.destroy)                # bouton pour quitter la fenÃªtre
        quitter.pack(side=BOTTOM)

        self.main()

        self.root.mainloop()
    
    def affiche_obstacle(self):
        for i in self.arene.obstacles:
            self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='yellow')
    
            
    def affiche_robot(self):
        #self.r = self.can.create_rectangle(self.robot.y, self.robot.x, self.robot.y+self.robot.longueur, self.robot.x+self.robot.largeur, fill="black")
        self.r=self.can.create_rectangle(self.robot.x-(self.robot.longueur/2), self.robot.y-(self.robot.longueur/2), self.robot.x+(self.robot.longueur/2), self.robot.y+(self.robot.longueur/2), fill="green")
        self.l=self.can.create_line(self.robot.x, self.robot.y, self.robot.ptv[0] , self.robot.ptv[1], arrow='last', fill='blue')
        
    def deleterobot(self):
        self.can.delete(self.l)
        self.can.delete(self.r)
        
    def main(self):
        angle=random.randint(0,180)
        #angle=90
        #print(angle)
        self.robot.rotationDroite(angle)
        while(True):
            time.sleep(0.02)
            self.affiche_robot()
            if (self.arene.collision(self.robot.x + self.robot.direction[0], self.robot.y + self.robot.direction[1])):
                self.robot.avance_vers()
            else :
                angle=random.randint(0,180)
                self.robot.rotationDroite(angle)
            self.can.update()
            self.deleterobot()